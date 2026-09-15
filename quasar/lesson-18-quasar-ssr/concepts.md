# Lesson 18 — Concepts Explained (Quasar SSR - Server-Side Rendering)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is SSR?

**What:** Server-Side Rendering — the server generates the HTML, not the browser.

```bash
# Add SSR mode
quasar mode add ssr

# Develop
quasar dev -m ssr

# Build
quasar build -m ssr
```

**Why it exists:** Without SSR (client-side rendering), the browser gets an empty HTML file + JS → JS runs → renders content → SEO crawlers see nothing → poor SEO. SSR → server sends full HTML → crawlers see content → better SEO → faster first paint.

**Where it's used:** Content-heavy sites — blogs, e-commerce, news, any site where SEO matters.

**What goes wrong without it:**
- Using SSR for an app that doesn't need SEO (admin dashboard) → unnecessary complexity. Use SPA.
- Not handling hydration → server and client render differently → hydration mismatch → console errors.
- Server doesn't have the same data as client → different HTML → mismatch. Use prefetch for data.

---

## SSR vs SPA vs SSG

**What:** Three rendering modes:

| SPA | SSR | SSG |
|-----|-----|-----|
| Client renders | Server renders per request | Pre-rendered at build time |
| Empty HTML → JS fills in | Full HTML per request | Full HTML, static files |
| Poor SEO | Good SEO | Best SEO |
| Fast after load | Fast first paint | Fastest (no server) |
| Simple | Complex | Simple (build-time) |
| Dashboard, admin | E-commerce, news | Blog, docs, marketing |

**Why it exists:** Different sites have different needs. SPA for apps, SSR for dynamic content with SEO, SSG for static content with SEO. Quasar supports all three.

**Where it's used:** Choose based on SEO needs and content dynamism.

**What goes wrong without it:**
- SSG for frequently updated content → stale pages → need rebuild on every change. Use SSR.
- SSR for a static blog → unnecessary server cost. Use SSG.
- SPA for an e-commerce site → products not indexed → lost traffic. Use SSR or SSG.

---

## Prefetch (Data Fetching on Server)

**What:** Fetch data on the server before rendering → HTML includes the data.

```js
// In a route component
export default {
    async preFetch({ store, currentRoute, redirect }) {
        // This runs on the SERVER before rendering
        const { id } = currentRoute.params
        const data = await fetch(`/api/products/${id}`).then(r => r.json())
        store.commit('setProduct', data)
    }
}
```

**Why it exists:** Without prefetch, the server renders empty HTML (no data) → client fetches data → renders → SEO crawler sees empty page. Prefetch → server fetches data → HTML includes it → crawler sees full content.

**Where it's used:** Every SSR page that displays data from an API.

**What goes wrong without it:**
- `preFetch` only works on route components (top-level). Not on child components.
- Not handling errors in preFetch → server crashes → 500 error. Use try/catch and redirect.
- Not using the store → data fetched on server but not available on client → refetch. Use Pinia/Vuex.

---

## SSR-Aware Components

**What:** Some code runs only on server, some only on client.

```js
// Check if running on server or client
import { process } from 'quasar'

if (process.env.SERVER) {
    // Runs only on server
    console.log('Server-side')
}

if (process.env.CLIENT) {
    // Runs only on client
    console.log('Client-side')
}

// In components:
mounted() {
    // mounted only runs on client (no mounted on server)
    window.addEventListener('resize', this.onResize)
}
```

**Why it exists:** Server has no `window`, `document`, `localStorage`. Client has no `fs`, `path`. Using the wrong API → crash. SSR-aware code → uses the right API on the right side.

**Where it's used:** Every SSR app — anywhere you use browser or Node.js APIs.

**What goes wrong without it:**
- Accessing `window` in `created()` → runs on server → `window is not defined` → crash. Use `mounted()`.
- Using `localStorage` during SSR → doesn't exist on server → error. Guard with `process.env.CLIENT`.
- `onMounted` (Composition API) → only runs on client → safe for browser APIs.

---

## SSR with Pinia

**What:** State management that works with SSR.

```js
// In preFetch, use Pinia store
import { useProductStore } from 'stores/product'

export default {
    async preFetch({ pinia }) {
        const store = useProductStore(pinia)
        await store.fetchProduct()
    }
}

// The store state is serialized and sent to the client
// Client hydrates with the same state → no refetch needed
```

**Why it exists:** Without SSR-compatible state, the server fetches data → renders → sends HTML → client re-initializes → fetches again → double work. Pinia SSR → server state is sent to client → client uses it → no refetch → efficient.

**Where it's used:** Every SSR app with Pinia.

**What goes wrong without it:**
- Not passing `pinia` to `preFetch` → store doesn't have the SSR context → state not transferred.
- Mutating state outside `preFetch` on server → state is lost (not serialized). Only mutate in preFetch.
- Client and server state mismatch → hydration error. Ensure same data on both sides.

---

## SEO Meta Tags

**What:** Set page title, description, and other meta tags for SEO.

```js
// Using @unhead/vue or vue-meta
import { useHead } from '@unhead/vue'

// In a component
useHead({
    title: 'Product Page',
    meta: [
        { name: 'description', content: 'Buy this amazing product' },
        { property: 'og:title', content: 'Product Page' },
        { property: 'og:image', content: 'https://example.com/image.jpg' },
    ]
})
```

**Why it exists:** Without meta tags, search engines and social media don't know what the page is about → poor SEO, ugly link previews. SSR + meta tags → crawlers see them → better ranking, nice previews.

**Where it's used:** Every SSR page — unique title and description per page.

**What goes wrong without it:**
- Same title on all pages → search engines think all pages are the same → poor ranking.
- Not setting Open Graph tags → social media links show generic preview → low click-through.
- Setting meta tags only on client → crawlers don't see them (they read server HTML). Set on server.

---

## SSR Configuration

**What:** Configure SSR settings in `quasar.config.js`.

```js
// quasar.config.js
return {
    ssr: {
        ssrPwa: false,  // combine SSR with PWA
        componentCache: {
            max: 1000,
            maxAge: 1000 * 60 * 15,  // 15 minutes
        },
        // Custom server middleware
        middlewares: [
            ctx.prod ? 'compression' : '',
            'render',  // keep this as last one
        ]
    }
}
```

**Why it exists:** SSR has performance considerations → caching, compression, middleware. Configuration lets you optimize → faster response → better UX and SEO.

**Where it's used:** SSR production setup.

**What goes wrong without it:**
- No compression → large HTML → slow transfer. Always enable compression in production.
- No component cache → server re-renders every request → slow. Enable for static components.
- `'render'` middleware not last → SSR doesn't render. Keep it as the last middleware.

---

## Hydration

**What:** The client "hydrates" the server-rendered HTML → makes it interactive.

```js
// Hydration happens automatically in Quasar SSR
// But mismatches cause errors:

// BAD: different output on server vs client
<template>
    <div>{{ Math.random() }}</div>  <!-- different on server and client -->
</template>

// GOOD: same output
<template>
    <div>{{ productId }}</div>  <!-- same if data is prefetched -->
</template>
```

**Why it exists:** The server sends static HTML → the client needs to make it interactive (event listeners, reactivity). Hydration → Vue attaches to the existing HTML → no re-render → fast.

**Where it's used:** Every SSR app — hydration is automatic but you must avoid mismatches.

**What goes wrong without it:**
- `Math.random()`, `Date.now()` → different on server and client → mismatch → Vue re-renders → warning.
- Using `window` in render → server has no window → error. Use `mounted()` for browser APIs.
- Different data on server vs client → mismatch. Ensure preFetch provides the same data.
