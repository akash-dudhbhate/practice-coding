/*
LESSON 14 — Error Boundaries & Suspense
MEDIUM P03 — Lazy-Loaded Routes
============================================
CONCEPT: Route-level code splitting means each page ships as its own chunk. Wrap the whole `Routes` block in one `Suspense` (shared fallback) and one `ErrorBoundary` (a failed dynamic import lands there).
PROBLEM: `lazy()`-import three page components (Home, About, Contact). Build `App` with `BrowserRouter`, a nav of `Link`s, then `<ErrorBoundary>` wrapping `<Suspense fallback={<p>Loading page...</p>}>` wrapping `Routes` with routes for "/", "/about", "/contact". (Import or define `ErrorBoundary` from a sibling file.)
TRY THIS: Render `<App />` and click About — the shared "Loading page..." fallback flashes while the chunk loads.
EXPECTED OUTPUT: Each route lazy-loads on first visit; a broken import shows the boundary fallback.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
