// SSR server middleware stack for Quasar
// Place files in src-ssr/middleware/ with numeric prefixes for ordering.

// --- 1. Request logging (first — capture all requests) ---
// File: src-ssr/middleware/01-logging.js
const loggingMiddleware = (req, res, next) => {
  const start = Date.now()
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`)
  res.on('finish', () => {
    console.log(`  → ${res.statusCode} (${Date.now() - start}ms)`)
  })
  next()
}

// --- 2. Compression (early — compress all responses) ---
// File: src-ssr/middleware/02-compression.js
const compressionMiddleware = (req, res, next) => {
  // In production, use the 'compression' npm package
  // const compression = require('compression')
  // compression()(req, res, next)
  next()
}

// --- 3. API proxy (forward /api/* to backend) ---
// File: src-ssr/middleware/03-api-proxy.js
const apiProxyMiddleware = (req, res, next) => {
  if (req.url.startsWith('/api/')) {
    // Proxy to backend server
    // In production, use http-proxy-middleware
    // const { createProxyMiddleware } = require('http-proxy-middleware')
    // createProxyMiddleware({ target: 'http://localhost:3001' })(req, res, next)
    console.log(`[Proxy] Forwarding ${req.url} to backend`)
  } else {
    next()
  }
}

// --- 4. Caching (cache product pages for 5 minutes) ---
// File: src-ssr/middleware/04-caching.js
const cache = new Map()
const CACHE_TTL = 5 * 60 * 1000 // 5 minutes

const cachingMiddleware = (req, res, next) => {
  // Only cache GET requests for product pages
  if (req.method !== 'GET' || !req.url.startsWith('/shop/')) {
    return next()
  }

  const cached = cache.get(req.url)
  if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
    console.log(`[Cache] HIT: ${req.url}`)
    res.setHeader('X-Cache', 'HIT')
    res.end(cached.body)
    return
  }

  // Capture response to cache
  const originalEnd = res.end
  const chunks = []
  res.write = (chunk) => { chunks.push(chunk); return true }
  res.end = (chunk) => {
    if (chunk) chunks.push(chunk)
    const body = Buffer.concat(chunks)
    cache.set(req.url, { body, timestamp: Date.now() })
    res.setHeader('X-Cache', 'MISS')
    originalEnd.call(res, body)
  }
  next()
}

// --- 5. Custom error pages (last — catch errors) ---
// File: src-ssr/middleware/99-error-pages.js
const errorPagesMiddleware = (err, req, res, next) => {
  if (!err) return next()

  const status = err.status || 500
  const errorPages = {
    400: '/400',
    404: '/404',
    500: '/500',
  }

  if (errorPages[status]) {
    res.writeHead(302, { Location: errorPages[status] })
    res.end()
  } else {
    console.error(`[Error] ${status}:`, err.message)
    res.writeHead(500, { 'Content-Type': 'text/plain' })
    res.end('Internal Server Error')
  }
}

/*
=== Middleware Order and Why It Matters ===

1. Logging (01)     — Must be FIRST to capture every request, even if later
                       middleware throws errors.
2. Compression (02)  — Early so all responses are compressed, including
                       cached and proxied responses.
3. API Proxy (03)    — Before caching so API calls bypass the page cache.
                       API responses have their own caching strategy.
4. Caching (04)      — After proxy so only page requests are cached.
                       Product pages cached for 5 min for fast repeat loads.
5. Error Pages (99)  — Must be LAST to catch errors from all other middleware
                       and render appropriate error pages.

Wrong order examples:
  - Caching before logging: cache hits won't be logged
  - Error pages before proxy: proxy errors won't show custom pages
  - Compression after caching: cached content won't be compressed
*/

export {
  loggingMiddleware,
  compressionMiddleware,
  apiProxyMiddleware,
  cachingMiddleware,
  errorPagesMiddleware,
}
