# Lesson 18 — Quasar SSR (Server-Side Rendering)

## What you'll learn
- What SSR is (server renders HTML)
- SSR vs SPA vs SSG (when to use which)
- Prefetch (data fetching on server)
- SSR-aware components (server vs client code)
- SSR with Pinia (state transfer)
- SEO meta tags (title, description, Open Graph)
- SSR configuration (caching, compression)
- Hydration (making server HTML interactive)

## Lesson

### Enable SSR
```bash
quasar mode add ssr
quasar dev -m ssr
quasar build -m ssr
```

### Prefetch
```js
async preFetch({ store, currentRoute }) {
    const data = await fetch(`/api/${currentRoute.params.id}`).then(r => r.json())
    store.commit('setData', data)
}
```

### SSR-aware
```js
if (process.env.SERVER) { /* server only */ }
if (process.env.CLIENT) { /* client only */ }
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Write SSR configuration for `quasar.config.js`: enable SSR, set component cache (max 1000, 15min maxAge), and add compression middleware for production. Document each setting.

   WHAT IT SHOULD LOOK LIKE:
   ```
   // quasar.config.js -> ssr: { pwa: false,
   //   prodPort: 3000, middlewares: [ ... ] }
   // component cache: max 1000, maxAge 15min
   // + gzip compression in production
   ```
2. `easy/p02-solve.vue` — Create an SSR-aware component: use `process.env.SERVER` and `process.env.CLIENT` to log where it's running. Access `window` only in `mounted()`. Display a message based on environment.

   WHAT IT SHOULD LOOK LIKE:
   ```
   PAGE SOURCE (server HTML):    AFTER HYDRATION (client):
   +----------------------+      +----------------------+
   | Rendered on SERVER   |      | Hydrated on CLIENT   |  <- card
   +----------------------+      +----------------------+
   (no "window is not defined" crash)
   ```
3. `easy/p03-solve.vue` — Create a component with SEO meta tags using `useHead` or document manipulation. Set title, description, and Open Graph tags. Verify they appear in the page source (not just after JS runs).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Ctrl+U page source:
   <title>My Page Title</title>
   <meta name="description" content="...">
   <meta property="og:title" content="...">
   <meta property="og:image" content="...">
   ```

### Medium
4. `medium/p01-solve.vue` — Create a product page with `preFetch`: fetch product data from an API (simulate with a promise), store it in Pinia, and render. Verify the data appears in the server-rendered HTML (view page source).

   WHAT IT SHOULD LOOK LIKE:
   ```
   view-source:/product/42 already contains:
   +----------------------------------+
   | Product 42                       |
   | $19.99                           |   <- name in initial HTML
   | Great product description...     |     (preFetch on server)
   +----------------------------------+
   ```
5. `medium/p02-solve.vue` — Create a blog post list page: use `preFetch` to fetch all posts. Render the list with links to individual posts. Set unique SEO meta tags per page (title, description). Use Pinia for state.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Server HTML:
   <title>Blog — My Site</title>
   * <a href="/post/first">First post</a>
   * <a href="/post/second">Second post</a>   <- real links in HTML
   * <a href="/post/third">Third post</a>
   ```
6. `medium/p03-solve.js` — Write a custom SSR middleware: log each request (URL, timestamp, user agent), add a custom header (`X-App-Version`), and handle 404s by redirecting to a custom 404 page. Document the middleware order.

   WHAT IT SHOULD LOOK LIKE:
   ```
   request -> [log URL+UA] -> [X-App-Version header]
           -> [route] -> [404? -> custom 404 page]
   ```

### Hard
7. `hard/p01-solve.vue` — Build a complete SSR blog: list page (prefetch all posts), post detail page (prefetch single post), SEO meta tags per page, breadcrumb navigation, and related posts. Include loading states and error handling (404 for missing posts).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Server HTML for /post/hello:
   Home > Blog > Hello World              <- breadcrumbs
   +----------------------------------+
   | Hello World                      |   <- post in initial HTML
   | Post body text...                |
   | Related: * Post A * Post B       |
   +----------------------------------+
   /post/bad-id -> custom 404 page
   ```
8. `hard/p02-solve.vue` — Build an SSR e-commerce product page: prefetch product data, reviews, and related products. Set rich SEO meta tags (title, description, OG, Twitter cards, product schema). Handle 404 for missing products. Include structured data for Google.

   WHAT IT SHOULD LOOK LIKE:
   ```
   view-source shows:
   Product 42 — $19.99
   * review one  * review two            <- reviews in HTML
   <script type="application/ld+json">
     { "@type": "Product", "name": ... }  <- parseable JSON-LD
   </script>
   ```
9. `hard/p03-solve.js` — Build an SSR server middleware stack: request logging, API proxy (forward /api/* to backend), caching (cache product pages for 5 minutes), compression, and custom error pages (400, 404, 500). Document the middleware order and why it matters.

   WHAT IT SHOULD LOOK LIKE:
   ```
   request -> logger -> /api/* proxy -> page cache (5min)
           -> compression -> render -> error pages (400/404/500)
   ```

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar SSR app.
