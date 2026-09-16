/**
 * LESSON 18 — Quasar SSR
 * MEDIUM P03 — Custom SSR Middleware
 * ============================================
 * CONCEPT: Files in src-ssr/middleware/ run in filename order — prefix
 * them (01-, 02-, 99-). Each is a Connect-style (req, res, next)
 * function; call next() to continue or write/end the response to stop.
 *
 * PROBLEM: Write three middlewares: (1) logging — timestamp, method, URL,
 * user-agent; (2) headers — set X-App-Version; (3) a 404 handler (last!)
 * that skips asset paths and redirects unmatched requests to /404.
 * Document the order and why it matters in comments.
 *
 * TRY THIS: const loggingMiddleware = (req, res, next) => {
 *   console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`); next() }
 * res.writeHead(302, { Location: '/404' }); res.end()
 *
 * EXPECTED OUTPUT: Every request is logged, carries X-App-Version, and
 * unmatched routes land on the custom 404 page.
 *
 * CHECK: python3 check.py medium/p03
 */
// TODO: write your middleware here
