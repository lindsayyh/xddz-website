#!/usr/bin/env python3
"""Resize and compress site images; convert large PNGs to WebP.

Rules
-----
- List thumbnails (images/列表缩略图/): max width 400
- Hero / product PNGs in images/: max width 800
- Product JPGs in images/: max width 1200
- Footer QR: max width 240
- literature/assets: max width 1000
- logo.png: max width 320, stay PNG
- PNG (except logo) → WebP when smaller; HTML paths updated
- JPG/JPEG recompressed in place at quality ~80
"""

from __future__ import annotations

import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".JPG", ".JPEG", ".PNG"}

JPEG_QUALITY = 80
WEBP_QUALITY = 78


def max_width_for(path: Path) -> int:
    rel = path.relative_to(ROOT).as_posix()
    name = path.name
    if name == "logo.png":
        return 320
    if "日出红似火微信" in name:
        return 240
    if "列表缩略图" in rel:
        return 400
    if rel.startswith("literature/assets/"):
        return 1000
    if path.suffix.lower() == ".png":
        return 800
    return 1200


def has_useful_alpha(im: Image.Image) -> bool:
    if im.mode in ("RGBA", "LA"):
        extrema = im.getchannel("A").getextrema()
        return extrema[0] < 255
    if im.mode == "P" and "transparency" in im.info:
        return True
    return False


def resize_if_needed(im: Image.Image, max_w: int) -> Image.Image:
    w, h = im.size
    if w <= max_w:
        return im
    new_h = max(1, round(h * (max_w / w)))
    return im.resize((max_w, new_h), Image.Resampling.LANCZOS)


def save_jpeg(im: Image.Image, dest: Path) -> None:
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGB")
    elif im.mode != "RGB":
        im = im.convert("RGB")
    im.save(dest, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)


def save_png(im: Image.Image, dest: Path) -> None:
    if im.mode not in ("RGB", "RGBA", "L", "LA", "P"):
        im = im.convert("RGBA" if has_useful_alpha(im) else "RGB")
    im.save(dest, format="PNG", optimize=True, compress_level=9)


def save_webp(im: Image.Image, dest: Path) -> None:
    if has_useful_alpha(im):
        if im.mode != "RGBA":
            im = im.convert("RGBA")
    else:
        if im.mode != "RGB":
            im = im.convert("RGB")
    im.save(dest, format="WEBP", quality=WEBP_QUALITY, method=6)


def process_file(path: Path) -> tuple[str, int, int, Path | None]:
    """Returns action, before bytes, after bytes, replacement path (if renamed)."""
    before = path.stat().st_size
    max_w = max_width_for(path)
    with Image.open(path) as src:
        im = src.convert("RGBA") if has_useful_alpha(src) else src.convert("RGB")
        im = resize_if_needed(im, max_w)
        ext = path.suffix.lower()

        if path.name == "logo.png" or ext in {".jpg", ".jpeg"}:
            # Keep original extension / logo as PNG
            if ext in {".jpg", ".jpeg"}:
                save_jpeg(im, path)
            else:
                save_png(im, path)
            after = path.stat().st_size
            return ("compress", before, after, None)

        # PNG (and odd casing): try WebP if smaller
        webp_path = path.with_suffix(".png")
        save_webp(im, webp_path)
        webp_size = webp_path.stat().st_size

        # Also write an optimized PNG candidate in memory comparison
        tmp_png = path.with_suffix(".png.__tmp__")
        save_png(im, tmp_png)
        png_size = tmp_png.stat().st_size

        if webp_size < png_size and webp_size < before:
            tmp_png.unlink(missing_ok=True)
            if path != webp_path and path.exists():
                path.unlink()
            after = webp_size
            return ("to-webp", before, after, webp_path)

        # Keep optimized PNG under original name
        webp_path.unlink(missing_ok=True)
        tmp_png.replace(path)
        after = path.stat().st_size
        return ("compress-png", before, after, None)


def update_html_refs(replacements: dict[str, str]) -> int:
    """Replace old relative image filenames with new ones across HTML."""
    if not replacements:
        return 0
    changed_files = 0
    for html in ROOT.rglob("*.html"):
        text = html.read_text(encoding="utf-8")
        new = text
        for old, new_name in replacements.items():
            # Replace path endings / basename occurrences carefully
            new = new.replace(old, new_name)
        if new != text:
            html.write_text(new, encoding="utf-8")
            changed_files += 1
    return changed_files


def add_lazy_loading() -> int:
    """Add loading=\"lazy\" to content images that lack it (not logo)."""
    changed = 0
    for html in ROOT.rglob("*.html"):
        text = html.read_text(encoding="utf-8")

        def repl(match: re.Match[str]) -> str:
            tag = match.group(0)
            if "loading=" in tag:
                return tag
            src = match.group(1)
            if "logo.png" in src or "logo." in src:
                return tag
            # hero flagship stays eager (first viewport)
            if "hero-flagship" in tag or "hero-flagship-img" in tag:
                return tag
            if tag.endswith("/>"):
                return tag[:-2] + ' loading="lazy" />'
            if tag.endswith(">"):
                return tag[:-1] + ' loading="lazy">'
            return tag

        new = re.sub(
            r"<img\b[^>]*\bsrc=\"([^\"]+)\"[^>]*>",
            repl,
            text,
            flags=re.IGNORECASE,
        )
        if new != text:
            html.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    roots = [ROOT / "images", ROOT / "literature" / "assets"]
    files: list[Path] = []
    for base in roots:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in IMAGE_EXTS and not p.name.endswith(".__tmp__"):
                files.append(p)

    replacements: dict[str, str] = {}
    total_before = 0
    total_after = 0
    print(f"Processing {len(files)} images…")

    for path in sorted(files):
        try:
            action, before, after, new_path = process_file(path)
        except Exception as exc:  # noqa: BLE001
            print(f"SKIP {path.relative_to(ROOT)}: {exc}")
            continue
        total_before += before
        total_after += after
        rel = (new_path or path).relative_to(ROOT)
        saved = before - after
        print(
            f"{action:12} {before/1024:7.1f}KB → {after/1024:7.1f}KB "
            f"({saved/1024:+.1f}KB)  {rel}"
        )
        if new_path is not None:
            old_name = path.name
            new_name = new_path.name
            replacements[old_name] = new_name

    html_n = update_html_refs(replacements)
    lazy_n = add_lazy_loading()
    print()
    print(
        f"Total: {total_before/1024:.0f}KB → {total_after/1024:.0f}KB "
        f"({(total_before-total_after)/1024:.0f}KB saved, "
        f"{(1-total_after/total_before)*100:.0f}% smaller)"
    )
    print(f"HTML files updated for WebP: {html_n}")
    print(f"HTML files updated for lazy-loading: {lazy_n}")
    print(f"Replacements: {len(replacements)}")


if __name__ == "__main__":
    main()
