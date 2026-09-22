/**
 * LESSON 15 — Quasar PWA
 * MEDIUM P01 — Workbox Runtime Caching Config
 * ============================================
 * CONCEPT: Workbox's runtimeCaching routes each request to a strategy:
 * CacheFirst for static assets (fast, rarely change), NetworkFirst for API
 * calls (fresh preferred, cache as fallback), StaleWhileRevalidate for
 * images. Expiration caps keep the cache bounded.
 *
 * PROBLEM: Export a workbox config object (for quasar.config.js's pwa
 * section): workboxPluginMode 'GenerateSW', navigateFallback 'index.html',
 * and runtimeCaching rules for /css|/js (CacheFirst), /api (NetworkFirst
 * with networkTimeoutSeconds), and images (StaleWhileRevalidate) — each
 * with cacheName + expiration (maxEntries, maxAgeSeconds).
 *
 * TRY THIS: { urlPattern: ({ url }) => url.pathname.startsWith('/api'),
 *   handler: 'NetworkFirst', options: { cacheName: 'api-cache',
 *   networkTimeoutSeconds: 5, expiration: { maxEntries: 50, maxAgeSeconds: 86400 } } }
 *
 * EXPECTED OUTPUT: A config that keeps the app working offline — assets
 * instant, API cached after first hit, images always fast.
 *
 * CHECK: python3 check.py medium/p01
 */
// TODO: write your workbox config here
