self.addEventListener('install', function (e) {
  self.skipWaiting();
  e.waitUntil(
    caches.open('hangarin-cache-v2').then(function (cache) {
      return cache.add('/').catch(function () {});
    })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', function (e) {
  e.respondWith(
    caches.match(e.request).then(function (response) {
      return response || fetch(e.request);
    })
  );
});