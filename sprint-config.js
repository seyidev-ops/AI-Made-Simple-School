/* 30-Day Professional AI Sprint — one place to change price, payment link and WhatsApp number.
   Every element with data-sprint-pay gets the payment link; data-sprint-price gets the price. */
window.AMS_SPRINT_CFG = {
  price: 10000,
  priceText: '₦10,000',
  payUrl: 'https://paystack.shop/pay/47k86yk7f2',
  whatsapp: '2347033134979'
};
(function(){
  function apply(){
    var c = window.AMS_SPRINT_CFG;
    document.querySelectorAll('[data-sprint-pay]').forEach(function(a){ a.href = c.payUrl; a.target = '_blank'; a.rel = 'noopener'; });
    document.querySelectorAll('[data-sprint-price]').forEach(function(e){ e.textContent = c.priceText; });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply); else apply();
})();
