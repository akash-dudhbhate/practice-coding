/**
 * LESSON 18 — Quasar SSR
 * EASY P01 — quasar.config.js SSR Configuration
 * ============================================
 * CONCEPT: The ssr section of quasar.config.js controls the SSR server:
 * componentCache (an LRU for rendered components — max entries + maxAge),
 * middlewares (ordered list; 'render' must be last), and pwa for hybrid
 * SSR+PWA builds.
 *
 * PROBLEM: Export a config function returning { ssr: { ssr: true,
 * componentCache: { max: 1000, maxAge: 15 min in ms }, middlewares:
 * ['compression', 'render'], pwa: false }, build: {...} }. Document each
 * setting in comments.
 *
 * TRY THIS: ssr: { ssr: true, componentCache: { max: 1000,
 *   maxAge: 1000 * 60 * 15 }, middlewares: ['compression', 'render'] }
 *
 * EXPECTED OUTPUT: A config that enables SSR with a bounded component
 * cache and gzipped responses in production.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your SSR config here
