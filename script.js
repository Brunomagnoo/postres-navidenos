/* ═══════════════════════════════════════════════
   POSTRES NAVIDEÑOS — INTERACTIVE JAVASCRIPT
   Focus: UX, Conversion, Engagement
═══════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ─────────────────────────────────────────────
     UTILITY: throttle
  ───────────────────────────────────────────── */
  function throttle(fn, wait) {
    let last = 0;
    return function (...args) {
      const now = Date.now();
      if (now - last >= wait) { last = now; fn.apply(this, args); }
    };
  }

  /* ─────────────────────────────────────────────
     1. COUNTDOWN TIMER (loops 14:59)
  ───────────────────────────────────────────── */
  const elH = document.getElementById('t-h');
  const elM = document.getElementById('t-m');
  const elS = document.getElementById('t-s');
  let totalSecs = 14 * 60 + 59;

  function tickTimer() {
    if (!elH || !elM || !elS) return;
    const h = Math.floor(totalSecs / 3600);
    const m = Math.floor((totalSecs % 3600) / 60);
    const s = totalSecs % 60;
    elH.textContent = String(h).padStart(2, '0');
    elM.textContent = String(m).padStart(2, '0');
    elS.textContent = String(s).padStart(2, '0');
    totalSecs = totalSecs > 0 ? totalSecs - 1 : 14 * 60 + 59;
  }

  tickTimer();
  setInterval(tickTimer, 1000);

  /* ─────────────────────────────────────────────
     2. SPOTS LEFT — random countdown
  ───────────────────────────────────────────── */
  const spotsEl = document.getElementById('spots-left');
  let spots = 11;

  function maybeLowerSpots() {
    if (!spotsEl || spots <= 4) return;
    const dropNow = Math.random() < 0.3; // 30% chance per interval
    if (dropNow) {
      spots = Math.max(4, spots - 1);
      spotsEl.textContent = spots;
      spotsEl.style.transition = 'color 0.3s';
      spotsEl.style.color = '#FF1744';
      setTimeout(() => { spotsEl.style.color = ''; }, 1200);
    }
  }

  setInterval(maybeLowerSpots, 25000);

  /* ─────────────────────────────────────────────
     3. STICKY HEADER — shadow on scroll
  ───────────────────────────────────────────── */
  const siteHeader = document.getElementById('siteHeader');

  window.addEventListener('scroll', throttle(function () {
    if (!siteHeader) return;
    if (window.scrollY > 60) {
      siteHeader.classList.add('scrolled');
    } else {
      siteHeader.classList.remove('scrolled');
    }
  }, 80));

  /* ─────────────────────────────────────────────
     4. PROFIT SIMULATOR
  ───────────────────────────────────────────── */
  const slider     = document.getElementById('simSlider');
  const sliderLive = document.getElementById('sliderLive');
  const rInvest    = document.getElementById('rInvest');
  const rSales     = document.getElementById('rSales');
  const rProfit    = document.getElementById('rProfit');

  const COST_PER   = 0.60;  // USD per cup
  const SALE_PRICE = 2.50;  // USD per cup
  const DAYS       = 30;

  function updateSliderFill(input) {
    const min = Number(input.min);
    const max = Number(input.max);
    const val = Number(input.value);
    const pct = ((val - min) / (max - min)) * 100;
    input.style.background =
      `linear-gradient(to right, var(--brand-crimson) 0%, var(--brand-crimson) ${pct}%, #DDD5CC ${pct}%, #DDD5CC 100%)`;
  }

  function formatUSD(n) {
    return '$' + n.toLocaleString('en-US');
  }

  function calcSimulator(cups) {
    const totalCups  = cups * DAYS;
    const invest     = Math.round(totalCups * COST_PER);
    const sales      = Math.round(totalCups * SALE_PRICE);
    const profit     = sales - invest;
    return { invest, sales, profit };
  }

  function renderSimulator(cups) {
    if (!slider) return;
    const { invest, sales, profit } = calcSimulator(cups);
    sliderLive.textContent = `${cups} vasitos/día`;
    rInvest.textContent = formatUSD(invest);
    rSales.textContent  = formatUSD(sales);
    rProfit.textContent = formatUSD(profit);
    updateSliderFill(slider);
  }

  if (slider) {
    renderSimulator(Number(slider.value));
    slider.addEventListener('input', function () {
      renderSimulator(Number(this.value));
    });
  }

  /* ─────────────────────────────────────────────
     5. FAQ ACCORDION
  ───────────────────────────────────────────── */
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(function (item) {
    const btn = item.querySelector('.faq-q');
    if (!btn) return;

    btn.addEventListener('click', function () {
      const isOpen = item.classList.contains('open');

      // Close all
      faqItems.forEach(function (other) {
        other.classList.remove('open');
        const ob = other.querySelector('.faq-q');
        if (ob) ob.setAttribute('aria-expanded', 'false');
      });

      // Open clicked if it was closed
      if (!isOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // Open first by default
  if (faqItems.length > 0) {
    faqItems[0].classList.add('open');
    const fb = faqItems[0].querySelector('.faq-q');
    if (fb) fb.setAttribute('aria-expanded', 'true');
  }

  /* ─────────────────────────────────────────────
     6. LIVE SOCIAL PROOF TOASTS
  ───────────────────────────────────────────── */
  const toast     = document.getElementById('liveToast');
  const toastName = document.getElementById('toastName');
  const toastMsg  = document.getElementById('toastMsg');

  const BUYERS = [
    { name: 'María Elena', city: 'México 🇲🇽', mins: '2', action: 'acaba de comprar el manual' },
    { name: 'Carolina G.', city: 'Colombia 🇨🇴', mins: '5', action: 'acaba de acceder al recetario' },
    { name: 'Rosa M.', city: 'Perú 🇵🇪', mins: '3', action: 'acaba de comprar el manual' },
    { name: 'Daniela S.', city: 'Chile 🇨🇱', mins: '1', action: 'acaba de acceder al recetario' },
    { name: 'Gabriela T.', city: 'Ecuador 🇪🇨', mins: '7', action: 'acaba de comprar el manual' },
    { name: 'Patricia V.', city: 'Guatemala 🇬🇹', mins: '4', action: 'acaba de comprar el manual' },
    { name: 'Mariana F.', city: 'Argentina 🇦🇷', mins: '6', action: 'acaba de acceder al recetario' },
    { name: 'Lucía P.', city: 'Venezuela 🇻🇪', mins: '2', action: 'acaba de comprar el manual' }
  ];

  let buyerIdx = Math.floor(Math.random() * BUYERS.length);

  function showToast() {
    if (!toast || !toastName || !toastMsg) return;
    const b = BUYERS[buyerIdx];
    toastName.textContent = `${b.name} de ${b.city}`;
    toastMsg.textContent = `${b.action} · hace ${b.mins} min`;
    toast.classList.add('visible');
    setTimeout(function () { toast.classList.remove('visible'); }, 5000);
    buyerIdx = (buyerIdx + 1) % BUYERS.length;
  }

  setTimeout(function () {
    showToast();
    setInterval(showToast, 14000);
  }, 4000);

  /* ─────────────────────────────────────────────
     7. SMOOTH ANCHOR SCROLL (fallback for older browsers)
  ───────────────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      const headerH = (document.getElementById('siteHeader') || { offsetHeight: 0 }).offsetHeight;
      const urgH    = (document.querySelector('.urgency-bar') || { offsetHeight: 0 }).offsetHeight;
      const offset  = target.getBoundingClientRect().top + window.scrollY - headerH - urgH - 10;
      window.scrollTo({ top: offset, behavior: 'smooth' });
    });
  });

  /* ─────────────────────────────────────────────
     8. CTA CLICK TRACKING (console + dataLayer)
  ───────────────────────────────────────────── */
  function trackCTA(label) {
    console.log('[CTA Click]', label);
    if (window.dataLayer) {
      window.dataLayer.push({ event: 'cta_click', cta_label: label });
    }
  }

  const ctaMap = {
    heroCta:   'hero_main_cta',
    offerCta:  'offer_checkout_cta'
  };

  Object.keys(ctaMap).forEach(function (id) {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener('click', function () { trackCTA(ctaMap[id]); });
    }
  });

})();
