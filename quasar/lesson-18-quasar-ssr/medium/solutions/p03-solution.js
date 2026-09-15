// Custom SSR middleware for Quasar
// Place in src-ssr/middleware/ — runs in order defined by filename prefix.

// --- 1. Request logging middleware ---
// File: src-ssr/middleware/01-logging.js
const loggingMiddleware = (req, res, next) => {
  const timestamp = new Date().toISOString()
  const { url, headers } = req
  console.log(`[${timestamp}] ${req.method} ${url} — UA: ${headers['user-agent']}`)
  next()
}

// --- 2. Custom header middleware ---
// File: src-ssr/middleware/02-headers.js
const headerMiddleware = (req, res, next) => {
  res.setHeader('X-App-Version', '1.0.0')
  res.setHeader('X-Powered-By', 'Quasar SSR')
  next()
}

// --- 3. 404 handler middleware ---
// File: src-ssr/middleware/99-not-found.js
// Must be LAST — catches unmatched routes
const notFoundMiddleware = (req, res, next) => {
  // Only handle non-asset requests
  if (req.url.startsWith('/assets') || req.url.startsWith('/icons')) {
    return next()
  }
  // If no route matched, redirect to custom 404
  if (!res.headersSent) {
    res.writeHead(302, { Location: '/404' })
    res.end()
  }
}

// --- Middleware order documentation ---
/*
Middleware execution order (by filename prefix):
  01-logging.js     — Log every request FIRST
  02-headers.js     — Add custom headers before response
  03-auth.js        — (optional) Authentication checks
  04-rate-limit.js  — (optional) Rate limiting
  99-not-found.js   — 404 handler MUST be last

Why order matters:
  - Logging first: capture all requests even if later middleware fails
  - Headers early: ensure custom headers are set before any response
  - 404 last: only catch requests that weren't handled by routes
*/

export { loggingMiddleware, headerMiddleware, notFoundMiddleware }
