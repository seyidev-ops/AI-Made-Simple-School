/* ═══════════════════════════════════════════════════
   AI Made Simple School — Service Worker v2
   Enables PWA install + offline support
═══════════════════════════════════════════════════ */
const CACHE = 'ams-v3';
const STATIC = [
  '/',
  '/index.html',
  '/login.html',
  '/register.html',
  '/dashboard.html',
  '/blog.html',
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

/* Fetch: cache-first for static assets, network-first for navigation */
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (!url.protocol.startsWith('http')) return;

  if (e.request.mode === 'navigate') {
    /* Network-first for HTML pages */
    e.respondWith(
      fetch(e.request)
        .then(r => { const c = r.clone(); caches.open(CACHE).then(cache => cache.put(e.request, c)); return r; })
        .catch(() => caches.match(e.request) || caches.match('/index.html'))
    );
  } else {
    /* Cache-first for assets */
    e.respondWith(
      caches.match(e.request)
        .then(cached => cached || fetch(e.request)
          .then(r => { const c = r.clone(); caches.open(CACHE).then(cache => cache.put(e.request, c)); return r; })
          .catch(() => new Response('', {status:408}))
        )
    );
  }
});
