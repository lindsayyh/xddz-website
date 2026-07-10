document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-years-since]').forEach((el) => {
    const foundedYear = Number(el.dataset.yearsSince);
    if (Number.isFinite(foundedYear)) {
      el.textContent = String(new Date().getFullYear() - foundedYear);
    }
  });

  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav-main');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen);
    });
  }

  const literatureTabs = document.querySelectorAll('.literature-tab');
  const literatureItems = document.querySelectorAll('.literature-item');
  const literatureEmpty = document.getElementById('literature-empty');

  if (literatureTabs.length && literatureItems.length) {
    const applyLiteratureFilter = (filter) => {
      literatureTabs.forEach((t) => {
        const active = t.dataset.filter === filter;
        t.classList.toggle('active', active);
        t.setAttribute('aria-selected', active);
      });

      let visible = 0;
      literatureItems.forEach((item) => {
        const show = filter === 'all' || item.dataset.category === filter;
        item.toggleAttribute('hidden', !show);
        if (show) visible += 1;
      });

      if (literatureEmpty) {
        literatureEmpty.classList.toggle('hidden', visible > 0);
      }
    };

    literatureTabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        applyLiteratureFilter(tab.dataset.filter);
      });
    });

    const queryFilter = new URLSearchParams(window.location.search).get('cat');
    const hashFilter = window.location.hash.replace('#', '');
    const initialFilter = queryFilter || hashFilter;
    if (initialFilter && document.querySelector(`.literature-tab[data-filter="${initialFilter}"]`)) {
      applyLiteratureFilter(initialFilter);
    }
  }

  const tutorialTabs = document.querySelectorAll('.tutorial-type-tab');
  const tutorialCards = document.querySelectorAll('.tutorial-card[data-tutorial-type]');
  const tutorialEmpty = document.getElementById('tutorial-empty');

  if (tutorialTabs.length && tutorialCards.length) {
    tutorialTabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const filter = tab.dataset.tutorialFilter;

        tutorialTabs.forEach((t) => {
          const active = t === tab;
          t.classList.toggle('active', active);
          t.setAttribute('aria-selected', active);
        });

        let visible = 0;
        tutorialCards.forEach((card) => {
          const show = filter === 'all' || card.dataset.tutorialType === filter;
          card.toggleAttribute('hidden', !show);
          if (show) visible += 1;
        });

        if (tutorialEmpty) {
          tutorialEmpty.classList.toggle('hidden', visible > 0);
        }
      });
    });
  }

  // Product gallery + high-res lightbox
  let lbRoot = null;
  let lbCtx = null;

  const closeLightbox = () => {
    if (!lbRoot) return;
    lbRoot.hidden = true;
    document.body.classList.remove('product-lightbox-open');
    lbCtx = null;
  };

  const showLb = (index) => {
    if (!lbRoot || !lbCtx) return;
    const { sources } = lbCtx;
    if (!sources.length) return;
    const i = ((index % sources.length) + sources.length) % sources.length;
    lbCtx.index = i;
    const item = sources[i];
    const img = lbRoot.querySelector('.product-lightbox-img');
    const caption = lbRoot.querySelector('.product-lightbox-caption');
    img.src = item.src;
    img.alt = item.alt;
    caption.textContent = `${i + 1} / ${sources.length}`;
    const multi = sources.length > 1;
    lbRoot.querySelector('[data-lb-prev]').hidden = !multi;
    lbRoot.querySelector('[data-lb-next]').hidden = !multi;
  };

  const openLightbox = (sources, index) => {
    if (!lbRoot) {
      lbRoot = document.createElement('div');
      lbRoot.id = 'product-lightbox';
      lbRoot.className = 'product-lightbox';
      lbRoot.hidden = true;
      lbRoot.setAttribute('role', 'dialog');
      lbRoot.setAttribute('aria-modal', 'true');
      lbRoot.setAttribute('aria-label', '产品高清大图');
      lbRoot.innerHTML = `
        <div class="product-lightbox-backdrop" data-lb-close></div>
        <button type="button" class="product-lightbox-close" data-lb-close aria-label="关闭">×</button>
        <button type="button" class="product-lightbox-nav product-lightbox-prev" data-lb-prev aria-label="上一张">‹</button>
        <button type="button" class="product-lightbox-nav product-lightbox-next" data-lb-next aria-label="下一张">›</button>
        <figure class="product-lightbox-figure">
          <img class="product-lightbox-img" alt="" />
          <figcaption class="product-lightbox-caption"></figcaption>
        </figure>
      `;
      document.body.appendChild(lbRoot);

      lbRoot.addEventListener('click', (e) => {
        if (e.target.closest('[data-lb-close]')) {
          closeLightbox();
          return;
        }
        if (e.target.closest('[data-lb-prev]') && lbCtx) {
          showLb(lbCtx.index - 1);
          return;
        }
        if (e.target.closest('[data-lb-next]') && lbCtx) {
          showLb(lbCtx.index + 1);
        }
      });

      document.addEventListener('keydown', (e) => {
        if (!lbCtx || lbRoot.hidden) return;
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') showLb(lbCtx.index - 1);
        if (e.key === 'ArrowRight') showLb(lbCtx.index + 1);
      });
    }

    lbCtx = { sources, index: 0 };
    showLb(index);
    lbRoot.hidden = false;
    document.body.classList.add('product-lightbox-open');
  };

  document.querySelectorAll('[data-product-gallery]').forEach((gallery) => {
    const main = gallery.querySelector('.product-showcase-main');
    const stage = gallery.querySelector('.product-showcase-stage');
    const thumbs = [...gallery.querySelectorAll('.product-showcase-thumb')];
    if (!main || !thumbs.length) return;

    const sources = thumbs
      .map((thumb) => ({
        src: thumb.dataset.gallerySrc || '',
        alt: thumb.dataset.galleryAlt || main.alt || '',
      }))
      .filter((item) => item.src);
    if (!sources.length) return;

    let activeIndex = Math.max(0, thumbs.findIndex((t) => t.classList.contains('is-active')));

    const syncMain = (index) => {
      if (index < 0 || index >= sources.length) return;
      activeIndex = index;
      main.src = sources[index].src;
      main.alt = sources[index].alt;
      thumbs.forEach((t, i) => {
        const on = i === index;
        t.classList.toggle('is-active', on);
        t.setAttribute('aria-selected', on ? 'true' : 'false');
      });
    };

    thumbs.forEach((thumb, index) => {
      thumb.addEventListener('click', () => {
        syncMain(index);
      });
    });

    main.classList.add('product-showcase-main--zoomable');
    main.title = '点击查看高清大图';

    let suppressMainClick = false;

    main.addEventListener('click', () => {
      if (suppressMainClick) {
        suppressMainClick = false;
        return;
      }
      openLightbox(sources, activeIndex);
    });

    if (stage && sources.length > 1) {
      let touchStartX = 0;
      let touchStartY = 0;

      stage.addEventListener(
        'touchstart',
        (e) => {
          if (e.touches.length !== 1) return;
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
        },
        { passive: true }
      );

      stage.addEventListener(
        'touchend',
        (e) => {
          if (e.changedTouches.length !== 1) return;
          const dx = e.changedTouches[0].clientX - touchStartX;
          const dy = e.changedTouches[0].clientY - touchStartY;
          const threshold = 48;
          if (Math.abs(dx) < threshold || Math.abs(dx) <= Math.abs(dy) * 1.2) return;

          suppressMainClick = true;
          if (dx < 0) {
            syncMain((activeIndex + 1) % sources.length);
          } else {
            syncMain((activeIndex - 1 + sources.length) % sources.length);
          }
        },
        { passive: true }
      );
    }
  });
});
