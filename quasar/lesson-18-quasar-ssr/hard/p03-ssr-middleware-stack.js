/**
 * LESSON 18 — Quasar SSR
 * HARD P03 — SSR Middleware Stack
 * ============================================
 * CONCEPT: Compose a production middleware chain in src-ssr/middleware/:
 * logging first (see everything), compression early, API proxy before
 * page caching, a TTL cache for product pages, and a (err, req, res,
 * next) error handler last.
 *
 * PROBLEM: Write five middlewares: request logging (with response-time on
 * 'finish'); compression hook; an /api/* proxy stub; a Map-based cache
 * that stores GET /shop/* responses for 5 minutes (X-Cache HIT/MISS,
 * wrap res.end); and an error-pages handler redirecting 400/404/500 to
 * custom pages. Document order and failure modes in comments.
 *
 * TRY THIS: const cached = cache.get(req.url);
 * if (cached && Date.now() - cached.timestamp < TTL) { res.end(cached.body); return }
 * const errorPages = (err, req, res, next) => { ... res.writeHead(302, {Location:'/404'}) }
 *
 * EXPECTED OUTPUT: Requests are logged, API calls forwarded, product
 * pages served from cache for 5 min, errors show friendly pages.
 *
 * CHECK: python3 check.py hard/p03
 */
// TODO: write your middleware stack here
