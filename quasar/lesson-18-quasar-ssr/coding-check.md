# Lesson 18 — Coding Check

## Easy

### p01-solve.js — SSR configuration
- [ ] SSR mode enabled in config
- [ ] Component cache configured (max, maxAge)
- [ ] Compression middleware added
- [ ] `render` middleware last
- [ ] Each setting documented

### p02-solve.vue — SSR-aware component
- [ ] `process.env.SERVER` used
- [ ] `process.env.CLIENT` used
- [ ] `window` accessed only in `mounted()`
- [ ] Message displayed based on environment
- [ ] No SSR crashes (no window on server)

### p03-solve.vue — SEO meta tags
- [ ] Title set
- [ ] Description meta tag set
- [ ] Open Graph tags set (og:title, og:description)
- [ ] Tags appear in page source
- [ ] Tags set on server (not just client)

## Medium

### p01-solve.vue — Product page with prefetch
- [ ] `preFetch` hook used
- [ ] API call simulated (promise)
- [ ] Data stored in Pinia
- [ ] Data rendered
- [ ] Data appears in server HTML (view source)
- [ ] No hydration mismatch

### p02-solve.vue — Blog post list
- [ ] `preFetch` fetches all posts
- [ ] Posts rendered in a list
- [ ] Links to individual posts
- [ ] Unique SEO title per page
- [ ] Unique SEO description per page
- [ ] Pinia used for state

### p03-solve.js — Custom middleware
- [ ] Request logging (URL, timestamp, UA)
- [ ] Custom header added (X-App-Version)
- [ ] 404 handling (redirect to 404 page)
- [ ] Middleware order documented
- [ ] `render` middleware kept last

## Hard

### p01-solve.vue — Complete SSR blog
- [ ] List page with prefetch
- [ ] Post detail page with prefetch
- [ ] SEO meta tags per page
- [ ] Breadcrumb navigation
- [ ] Related posts section
- [ ] Loading states
- [ ] 404 handling for missing posts
- [ ] No hydration mismatches

### p02-solve.vue — SSR e-commerce page
- [ ] Prefetch product data
- [ ] Prefetch reviews
- [ ] Prefetch related products
- [ ] Rich SEO meta tags (title, description, OG, Twitter)
- [ ] Product schema (structured data)
- [ ] 404 for missing products
- [ ] All data in server HTML

### p03-solve.js — SSR middleware stack
- [ ] Request logging middleware
- [ ] API proxy (/api/* → backend)
- [ ] Caching middleware (5 min for products)
- [ ] Compression middleware
- [ ] Custom error pages (400, 404, 500)
- [ ] Middleware order documented
- [ ] `render` middleware last
- [ ] Order explained (why it matters)
