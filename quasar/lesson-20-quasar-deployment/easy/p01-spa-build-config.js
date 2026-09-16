/**
 * LESSON 20 — Quasar Deployment
 * EASY P01 — SPA Production Build Config
 * ============================================
 * CONCEPT: quasar.config.js' build section shapes the production bundle:
 * publicPath (base URL), sourcemap (off for prod), gzip (pre-compressed
 * assets), env (vars baked into process.env at build time).
 *
 * PROBLEM: Export a config with a build section: publicPath '/',
 * sourcemap false, gzip true, and env.API_URL switching between a dev
 * localhost URL and a prod https URL based on NODE_ENV. Comment each
 * setting.
 *
 * TRY THIS: build: { publicPath: '/', sourcemap: false, gzip: true,
 *   env: { API_URL: process.env.NODE_ENV === 'production'
 *     ? 'https://api.myapp.com' : 'http://localhost:3001' } }
 *
 * EXPECTED OUTPUT: `quasar build -m spa` produces a gzipped dist/spa with
 * the right API URL per environment.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your build config here
