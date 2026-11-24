/* ═══════════════════════════════════════════════════
   AI Made Simple School — Service Worker v2
   Enables PWA install + offline support
═══════════════════════════════════════════════════ */
const CACHE = 'ams-v18';
const STATIC = [
  '/',
  '/index.html',
  '/programmes.html',
  '/about.html',
  '/access-firstuse.js',
  '/ams-config.js',
  '/terms.html',
  '/privacy.html',
  '/assets/ona-services-logo.png',
  '/login.html',
  '/register.html',
  '/dashboard.html',
  '/lessons-plus.js',
  '/sprint-content.js',
  '/sprint-config.js',
  '/sprint-day1.html',
  '/blog.html',
  '/day1.html',
  '/admin-login.html',
  '/assets/logo.svg',
  '/manifest.json'
];

/* Install: pre-cache all static files */
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => c.addAll(STATIC.map(u => new Request(u, {cache:'reload'}))))
      .then(() => self.skipWaiting())
  );
});

/* Activate: wipe old caches */
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

/* Fetch rules
   - Other sites (Google Apps Script, Paystack, fonts...) and anything with ?action= are never touched,
     so signups, unsubscribes and access-code checks always get a live answer.
   - Our own pages, scripts, styles and data: network-first (updates reach people straight away),
     falling back to the saved copy when offline.
   - Images and icons under /assets/: cache-first. */
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (!url.protocol.startsWith('http')) return;
  if (url.origin !== self.location.origin) return;
  if (url.searchParams.has('action')) return;
  if (url.pathname.startsWith('/videos/') || e.request.headers.has('range')) return;  // stream videos straight from the network

  const isAsset = url.pathname.startsWith('/assets/') && !url.pathname.endsWith('.html');
  if (!isAsset) {
    e.respondWith(
      fetch(e.request)
        .then(r => { if (r && r.ok) { const c = r.clone(); caches.open(CACHE).then(cache => cache.put(e.request, c)); } return r; })
        .catch(() => caches.match(e.request).then(m => m || caches.match('/index.html')))
    );
  } else {
    e.respondWith(
      caches.match(e.request)
        .then(cached => cached || fetch(e.request)
          .then(r => { if (r && r.ok) { const c = r.clone(); caches.open(CACHE).then(cache => cache.put(e.request, c)); } return r; })
          .catch(() => new Response('', {status:408}))
        )
    );
  }
});
