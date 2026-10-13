/* AI Made Simple — shared site UI. Loaded last on every page. */
(function () {
  var ORDER = ['dark', 'light', 'system'];
  var LABEL = { dark: 'Dark mode', light: 'Light mode', system: 'Auto · follows your device' };
  var root = document.documentElement;

  function saved() { try { return localStorage.getItem('ams-theme') || 'dark'; } catch (e) { return 'dark'; } }
  function resolve(m) {
    var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    return m === 'system' ? (dark ? 'dark' : 'light') : m;
  }
  function paint(m) {
    root.setAttribute('data-theme-mode', m);
    var b = document.getElementById('themeCycle');
    if (b) { b.setAttribute('aria-label', 'Theme: ' + LABEL[m] + '. Tap to change.'); b.title = LABEL[m]; }
  }

  window.applyTheme = function (m) { root.setAttribute('data-theme', resolve(m)); root.setAttribute('data-theme-mode', m); };
  window.setTheme = function (m) {
    if (ORDER.indexOf(m) < 0) m = 'dark';
    try { localStorage.setItem('ams-theme', m); } catch (e) {}
    window.applyTheme(m); paint(m);
  };
  var toastTimer;
  function toast(msg) {
    var t = document.getElementById('tcToast');
    if (!t) { t = document.createElement('div'); t.id = 'tcToast'; t.className = 'tc-toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(function () { t.classList.remove('show'); }, 1600);
  }
  window.cycleTheme = function () {
    var next = ORDER[(ORDER.indexOf(saved()) + 1) % ORDER.length];
    window.setTheme(next); toast(LABEL[next]);
  };

  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function () { if (saved() === 'system') window.applyTheme('system'); };
    if (mq.addEventListener) mq.addEventListener('change', onChange); else if (mq.addListener) mq.addListener(onChange);
  }

  /* Mobile menu (shared; pages without their own get this one) */
  function els() { return { links: document.getElementById('navLinks'), ham: document.getElementById('navHam'), over: document.getElementById('navOverlay') }; }
  window.toggleMobileNav = function () {
    var e = els(); if (!e.links) return;
    var open = e.links.classList.toggle('open');
    if (e.ham) { e.ham.classList.toggle('open', open); e.ham.setAttribute('aria-expanded', String(open)); }
    if (e.over) e.over.classList.toggle('show', open);
    document.body.style.overflow = open ? 'hidden' : '';
  };
  window.closeMobileNav = function () {
    var e = els();
    if (e.links) e.links.classList.remove('open');
    if (e.ham) { e.ham.classList.remove('open'); e.ham.setAttribute('aria-expanded', 'false'); }
    if (e.over) e.over.classList.remove('show');
    document.body.style.overflow = '';
  };
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') window.closeMobileNav(); });
  window.addEventListener('resize', function () { if (window.innerWidth > 768) window.closeMobileNav(); });

  function boot() {
    paint(saved());
    document.querySelectorAll('#navLinks a').forEach(function (a) { a.addEventListener('click', function () { setTimeout(window.closeMobileNav, 50); }); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
