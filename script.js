document.addEventListener('DOMContentLoaded', () => {
  // ==========================================
  // 1. DYNAMIC PROFIT SIMULATOR
  // ==========================================
  const cupsSlider = document.getElementById('cupsSlider');
  const cupsLabel = document.getElementById('cupsLabel');
  const costNumber = document.getElementById('costNumber');
  const salesNumber = document.getElementById('salesNumber');
  const profitNumber = document.getElementById('profitNumber');

  const COST_PER_CUP = 0.60;  // USD
  const SALE_PRICE_PER_CUP = 2.50; // USD
  const DAYS_IN_MONTH = 30;

  function updateSimulator(cupsPerDay) {
    const totalCupsMonth = cupsPerDay * DAYS_IN_MONTH;
    const totalCost = Math.round(totalCupsMonth * COST_PER_CUP);
    const totalSales = Math.round(totalCupsMonth * SALE_PRICE_PER_CUP);
    const totalProfit = totalSales - totalCost;

    if (cupsLabel) cupsLabel.textContent = `${cupsPerDay} vasitos / día`;
    if (costNumber) costNumber.textContent = `$${totalCost.toLocaleString('en-US')} USD`;
    if (salesNumber) salesNumber.textContent = `$${totalSales.toLocaleString('en-US')} USD`;
    if (profitNumber) profitNumber.textContent = `$${totalProfit.toLocaleString('en-US')} USD`;
  }

  if (cupsSlider) {
    cupsSlider.addEventListener('input', (e) => {
      updateSimulator(parseInt(e.target.value, 10));
    });
    // Init with default
    updateSimulator(parseInt(cupsSlider.value, 10));
  }

  // ==========================================
  // 2. COUNTDOWN TIMER (14:59)
  // ==========================================
  const countdownEl = document.getElementById('countdown');
  let timeInSeconds = 14 * 60 + 59;

  function updateCountdown() {
    if (!countdownEl) return;
    const minutes = Math.floor(timeInSeconds / 60);
    const seconds = timeInSeconds % 60;
    countdownEl.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    
    if (timeInSeconds > 0) {
      timeInSeconds--;
    } else {
      timeInSeconds = 14 * 60 + 59; // Reset smoothly
    }
  }

  setInterval(updateCountdown, 1000);

  // ==========================================
  // 3. FAQ ACCORDION
  // ==========================================
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    const btn = item.querySelector('.faq-btn');
    if (btn) {
      btn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        // Close others
        faqItems.forEach((other) => {
          other.classList.remove('active');
          const otherBtn = other.querySelector('.faq-btn');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
        });

        if (!isActive) {
          item.classList.add('active');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    }
  });

  // Open first FAQ by default
  if (faqItems.length > 0) {
    faqItems[0].classList.add('active');
    const firstBtn = faqItems[0].querySelector('.faq-btn');
    if (firstBtn) firstBtn.setAttribute('aria-expanded', 'true');
  }

  // ==========================================
  // 4. LIVE SOCIAL PROOF TOASTS (LATAM)
  // ==========================================
  const toastNotification = document.getElementById('toastNotification');
  const toastUser = document.getElementById('toastUser');

  const buyers = [
    { name: 'María Elena', country: 'México 🇲🇽', minutes: '2' },
    { name: 'Carolina G.', country: 'Colombia 🇨🇴', minutes: '4' },
    { name: 'Rosa M.', country: 'Perú 🇵🇪', minutes: '6' },
    { name: 'Daniela S.', country: 'Chile 🇨🇱', minutes: '1' },
    { name: 'Gabriela T.', country: 'Ecuador 🇪🇨', minutes: '5' },
    { name: 'Patricia V.', country: 'Guatemala 🇬🇹', minutes: '3' }
  ];

  let buyerIndex = 0;

  function showNextToast() {
    if (!toastNotification || !toastUser) return;
    const buyer = buyers[buyerIndex];
    toastUser.textContent = `${buyer.name} de ${buyer.country}`;
    const textSpan = toastNotification.querySelector('.toast-text span');
    if (textSpan) {
      textSpan.textContent = `acaba de adquirir el manual hace ${buyer.minutes} minutos`;
    }

    toastNotification.classList.add('show');

    setTimeout(() => {
      toastNotification.classList.remove('show');
    }, 4500);

    buyerIndex = (buyerIndex + 1) % buyers.length;
  }

  // Initial delay then loop
  setTimeout(() => {
    showNextToast();
    setInterval(showNextToast, 12000);
  }, 3500);
});
