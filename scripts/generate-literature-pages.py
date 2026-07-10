#!/usr/bin/env python3
"""Migrate literature articles from xddzjs.com and generate HTML pages."""

import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT = ROOT / "literature"
ASSETS = LIT / "assets"
OLD_CP = "http://www.xddzjs.com/cp/"
TMP = Path("/tmp")

ARTICLES = [
    {
        "num": "01",
        "file": "article-01.html",
        "category": "media",
        "category_label": "媒体报道",
        "title": "河南省质监局介入电信计量监管维护电信服务交易公平",
        "source": "媒体报道",
        "old": "wx1.htm",
    },
    {
        "num": "02",
        "file": "article-02.html",
        "category": "media",
        "category_label": "媒体报道",
        "title": "谁来监管电话计时这杆秤——甘肃白银市手机「计时风波」",
        "source": "新华社报道",
        "old": "wx2.htm",
    },
    {
        "num": "03",
        "file": "article-03.html",
        "category": "paper",
        "category_label": "科研论文",
        "title": "智能公话系统中同步计费终端的计时检测 中国计量 2007.3",
        "source": "中国计量 2007.3",
        "old": "wx3.htm",
    },
    {
        "num": "04",
        "file": "article-04.html",
        "category": "paper",
        "category_label": "科研论文",
        "title": "心电图机时间常数在不同规程中检定方法的分析",
        "source": "《中国计量》2015.2",
        "old": "wx4.htm",
    },
    {
        "num": "05",
        "file": "article-05.html",
        "category": "paper",
        "category_label": "科研论文",
        "title": "地感触发车牌识别停车计时装置的计时原理及检定方法",
        "source": "《大众标准化》2018.1",
        "old": "wx5.htm",
    },
    {
        "num": "06",
        "file": "article-06.html",
        "category": "paper",
        "category_label": "科研论文",
        "title": "视频触发车牌识别停车计时收费系统的计时检定方法",
        "source": "《中国计量》2019.05",
        "old": "wx6.htm",
    },
    {
        "num": "07",
        "file": "article-07.html",
        "category": "spec",
        "category_label": "计量规范",
        "title": "JJF 1900-2021 停车场电子计时装置检定仪校准规范",
        "source": "国家计量技术规范 · 参与起草",
        "old": "wx7.htm",
    },
    {
        "num": "08",
        "file": "article-08.html",
        "category": "paper",
        "category_label": "科研论文",
        "title": "地磁型电子停车计时收费平台的现场检定仪的设计及应用",
        "source": "《中国计量》2022.03",
        "old": "wx8.htm",
    },
    {
        "num": "09",
        "file": "article-09.html",
        "category": "news",
        "category_label": "公司动态",
        "title": "河南省计量协会举办 JJG 543-2026 心电图机检定规程宣贯",
        "source": "公司动态 · ECG-6 现场实操",
        "old": "wx9.htm",
    },
]

HEADER = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — 文献与资讯</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="logo">
        <img src="../images/logo.png" alt="先达技术 AdvancedTech" class="logo-img" />
        <span class="logo-company">郑州市先达电子技术有限公司</span>
      </a>
      <nav class="nav-main" aria-label="主导航">
        <a href="../index.html" class="nav-link">首页</a>
        <a href="../about.html" class="nav-link">公司简介</a>
        <a href="../products.html" class="nav-link">产品中心</a>
        <a href="../tutorials.html" class="nav-link">产品教程</a>
        <a href="../literature.html" class="nav-link active">文献与资讯</a>
        <a href="../contact.html" class="nav-link">联系我们</a>
      </nav>
      <div class="header-actions">
        <a href="tel:0371-63930606" class="header-phone">0371-63930606</a>
        <a href="../contact.html" class="btn btn-primary btn-sm">技术咨询</a>
        <button class="nav-toggle" aria-label="打开菜单" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main>
    <section class="section article-page">
      <div class="container">
        <a href="../literature.html" class="product-back">← 返回文献与资讯</a>
        <p class="article-page-meta">
          <span class="literature-tag literature-tag-{category}">{category_label}</span>
          <span class="article-page-source">{source}</span>
        </p>
        <h1 class="article-page-title">{title}</h1>
        <div class="article-body migrated-content">
{body}
        </div>
      </div>
    </section>
  </main>
"""

FOOTER = """
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <p>郑州市先达电子技术有限公司</p>
        <p class="footer-desc">医疗与停车计时检定设备研发生产厂家</p>
      </div>
      <div class="footer-links">
        <h4>快速链接</h4>
        <a href="../products.html">产品中心</a>
        <a href="../tutorials.html">产品教程</a>
        <a href="../literature.html">文献与资讯</a>
        <a href="../about.html">公司简介</a>
      </div>
      <div class="footer-contact">
        <h4>联系我们</h4>
        <p>地址：河南省郑州市俭学街 5 号</p>
        <p>电话：<a href="tel:0371-63930606">0371-63930606</a></p>
        <p>邮箱：<a href="mailto:xdzz001@126.com">xdzz001@126.com</a></p>
        <p>联系人：郜女士</p>
        <div class="footer-wechat">
          <p class="footer-wechat-label">微信</p>
          <img src="../images/日出红似火微信.jpg" alt="微信二维码" class="footer-wechat-qr" width="120" height="120" loading="lazy" />
        </div>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>Copyright © 2008-2026 郑州市先达电子技术有限公司</p>
      <p>
        <a href="https://beian.miit.gov.cn/#/Integrated/index" target="_blank" rel="noopener noreferrer">豫ICP备2020028709号-1</a>
        <a href="https://beian.mps.gov.cn/#/" target="_blank" rel="noopener noreferrer">豫公网安备41010502007492号</a>
      </p>
    </div>
  </footer>

  <a href="tel:0371-63930606" class="float-call" aria-label="拨打电话">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">
      <path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.56 1 1 0 01-.24 1.01l-2.2 2.2z"/>
    </svg>
  </a>

  <script src="../main.js"></script>
</body>
</html>
"""


def extract_body(html: str) -> str:
    m = re.search(
        r'<td vAlign="top" align="middle" width="81%" height="\d+">(.*?)</td>',
        html,
        re.S | re.I,
    )
    if not m:
        raise ValueError("Could not extract article body")
    return m.group(1)


def download_image(src: str, article_num: str) -> str:
    if src.startswith("../") or src.startswith("http"):
        return src
    filename = Path(src).name
    safe_name = re.sub(r"\s+", "_", filename)
    dest_name = f"a{article_num}_{safe_name}"
    dest = ASSETS / dest_name
    if not dest.exists():
        url = OLD_CP + urllib.parse.quote(src.lstrip("/"))
        try:
            urllib.request.urlretrieve(url, dest)
            print(f"  downloaded {dest_name}")
        except Exception as e:
            print(f"  WARN download failed {url}: {e}")
            return src
    return f"assets/{dest_name}"


def clean_body(html: str, article_num: str) -> str:
    html = re.sub(r"<br\s*/?>", "<br />", html, flags=re.I)

    def repl_img(m):
        src = m.group(1)
        if "right_a101" in src or "../images/" in src:
            return ""
        new_src = download_image(src, article_num)
        alt = m.group(2) if m.lastindex >= 2 else ""
        w = m.group(3) if m.lastindex >= 3 and m.group(3) else ""
        h = m.group(4) if m.lastindex >= 4 and m.group(4) else ""
        style = ""
        if w and h:
            style = f' style="max-width:100%;height:auto;"'
        return f'<img src="{new_src}" alt="{alt}" loading="lazy"{style} />'

    html = re.sub(
        r'<img[^>]+src="([^"]+)"[^>]*(?:alt="([^"]*)")?[^>]*(?:width="(\d+)"[^>]*height="(\d+)")?[^>]*/?>',
        repl_img,
        html,
        flags=re.I,
    )
    html = re.sub(r"<font[^>]*>", "", html, flags=re.I)
    html = re.sub(r"</font>", "", html, flags=re.I)
    html = re.sub(r"<span[^>]*>", "", html, flags=re.I)
    html = re.sub(r"</span>", "", html, flags=re.I)
    html = re.sub(r'class="MsoNormal"', 'class="article-p"', html, flags=re.I)
    html = re.sub(r'class="css"', 'class="article-p"', html, flags=re.I)
    html = re.sub(r'class="font"', 'class="article-p"', html, flags=re.I)
    html = re.sub(r"<p(?![^>]*class=)", "<p class=\"article-p\"", html, flags=re.I)
    html = re.sub(r"&nbsp;", " ", html)
    html = re.sub(r"&ldquo;", "\u201c", html)
    html = re.sub(r"&rdquo;", "\u201d", html)
    html = re.sub(r"&mdash;", "—", html)
    html = re.sub(r"&tau;", "τ", html)
    html = re.sub(r"&mu;", "μ", html)
    html = re.sub(r"&Omega;", "Ω", html)
    html = re.sub(r"<b>", "<strong>", html, flags=re.I)
    html = re.sub(r"</b>", "</strong>", html, flags=re.I)
    html = re.sub(r"<strong>\s*</strong>", "", html)
    html = re.sub(r"<p class=\"article-p\"\s*>\s*</p>", "", html)
    html = re.sub(r'\s*align="[^"]*"', "", html, flags=re.I)
    html = re.sub(r"\n{3,}", "\n\n", html)
    html = re.sub(r"制作人：李[^<《]+", "制作人：李旸", html)
    return html.strip()


def render_article_page(article: dict, body: str) -> str:
    return (
        HEADER.format(**article, body=body)
        + FOOTER
    )


def render_index_list(articles) -> str:
    items = []
    for a in articles:
        items.append(
            f"""          <article class="literature-item" data-category="{a['category']}">
            <span class="literature-item-num">{a['num']}</span>
            <div class="literature-item-main">
              <span class="literature-tag literature-tag-{a['category']}">{a['category_label']}</span>
              <h3 class="literature-item-title">
                <a href="literature/{a['file']}">{a['title']}</a>
              </h3>
              <p class="literature-item-source">{a['source']}</p>
            </div>
            <a href="literature/{a['file']}" class="literature-item-link">阅读全文 →</a>
          </article>"""
        )
    return "\n".join(items)


def main():
    LIT.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)

    for art in ARTICLES:
        wx_num = art["old"].replace("wx", "").replace(".htm", "")
        src_path = TMP / f"wx{wx_num}.htm"
        if not src_path.exists():
            urllib.request.urlretrieve(OLD_CP + art["old"], src_path)
        html = src_path.read_bytes().decode("gb2312", errors="replace")
        raw_body = extract_body(html)
        body = clean_body(raw_body, art["num"])
        page = render_article_page(art, body)
        (LIT / art["file"]).write_text(page, encoding="utf-8")
        print(f"wrote {art['file']}")


if __name__ == "__main__":
    main()
