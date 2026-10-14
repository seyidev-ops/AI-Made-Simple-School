/* AI Made Simple — campaign tracking (static-site safe).
 *
 * 1. Reads utm_source / utm_medium / utm_campaign / utm_content from the URL
 *    and keeps them for the visit (sessionStorage, with a 30-day localStorage copy).
 * 2. Adds a short reference to every WhatsApp link's prefilled text,
 *    e.g. "(ref: biz1-a2-ig)", so a chat can be matched to the advert that sent it.
 * 3. Loads the Meta Pixel ONLY when PIXEL_ID below is filled in, and sends:
 *      PageView           every page
 *      ViewContent        pricing section seen (index.html)
 *      InitiateCheckout   any Paystack link clicked
 *      Contact            any WhatsApp link clicked
 *      PaystackReturn     thank-you page reached (custom event; a signal, NOT a confirmed sale)
 *
 * To switch the Pixel on: paste your Pixel ID between the quotes below and push.
 */
(function () {
  var PIXEL_ID = ''; // e.g. '123456789012345' from Meta Events Manager

  var KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
  var STORE = 'ams-utm';

  function read(store) { try { return JSON.parse(store.getItem(STORE) || 'null'); } catch (e) { return null; } }
  function write(store, v) { try { store.setItem(STORE, JSON.stringify(v)); } catch (e) {} }

  var params = new URLSearchParams(location.search);
  var fresh = {};
  var hasFresh = false;
  KEYS.forEach(function (k) { var v = params.get(k); if (v) { fresh[k] = v.slice(0, 40); hasFresh = true; } });

  var utm = null;
  if (hasFresh) {
    fresh.t = Date.now();
    utm = fresh;
    write(window.sessionStorage, utm);
    write(window.localStorage, utm);
  } else {
    utm = read(window.sessionStorage);
    if (!utm) {
      var old = read(window.localStorage);
      if (old && old.t && Date.now() - old.t < 30 * 864e5) utm = old;
    }
  }

  function refCode() {
    if (!utm) return '';
    var parts = [utm.utm_campaign, utm.utm_content, utm.utm_source].filter(Boolean);
    return parts.length ? parts.join('-').toLowerCase().replace(/[^a-z0-9_-]/g, '') : '';
  }
  window.AMS_REF = refCode();

  function tagWhatsApp(a) {
    var ref = window.AMS_REF;
    if (!ref || a.dataset.amsTagged) return;
    try {
      var u = new URL(a.href);
      var text = u.searchParams.get('text') || '';
      if (text.indexOf('(ref:') === -1) {
        var full = (text ? text + ' ' : '') + '(ref: ' + ref + ')';
        // encodeURIComponent keeps spaces as %20 (WhatsApp can show '+' literally)
        a.href = u.origin + u.pathname + '?text=' + encodeURIComponent(full);
      }
      a.dataset.amsTagged = '1';
    } catch (e) {}
  }

  /* ── Meta Pixel (only when configured) ── */
  function track(name, data, custom) {
    if (typeof window.fbq !== 'function') return;
    try { window.fbq(custom ? 'trackCustom' : 'track', name, data || {}); } catch (e) {}
  }
  window.amsTrack = track;

  if (PIXEL_ID) {
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', PIXEL_ID);
    window.fbq('track', 'PageView');
  }

  function boot() {
    document.querySelectorAll('a[href*="wa.me/"]').forEach(tagWhatsApp);

    document.addEventListener('click', function (ev) {
      var a = ev.target.closest && ev.target.closest('a[href]');
      if (!a) return;
      if (a.href.indexOf('wa.me/') > -1) { tagWhatsApp(a); track('Contact', { ref: window.AMS_REF || 'direct' }); }
      if (a.href.indexOf('paystack.shop/') > -1) track('InitiateCheckout', { content_name: a.dataset.programme || a.href.split('/').pop(), currency: 'NGN' });
    }, true);

    var pricing = document.getElementById('pricing');
    if (pricing && 'IntersectionObserver' in window) {
      var seen = false;
      new IntersectionObserver(function (entries, obs) {
        if (!seen && entries[0].isIntersecting) { seen = true; track('ViewContent', { content_name: 'pricing' }); obs.disconnect(); }
      }, { threshold: 0.35 }).observe(pricing);
    }

    if (document.body && document.body.dataset.page === 'thanks') track('PaystackReturn', { ref: window.AMS_REF || 'direct' }, true);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
