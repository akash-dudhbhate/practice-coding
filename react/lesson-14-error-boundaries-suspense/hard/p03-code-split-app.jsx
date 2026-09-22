/*
LESSON 14 — Error Boundaries & Suspense
HARD P03 — Code-Split App (Per-Route Suspense + Boundary)
============================================
CONCEPT: The production pattern: every route gets its OWN `ErrorBoundary` + `Suspense` pair, so a slow chunk shows a route-local skeleton and a failed import only breaks that page — not the whole app.
PROBLEM: Define `ErrorBoundary` (hasError + `reset`, fallback "Failed to load." + Retry). `lazy()`-import FIVE components: Home, About, Products, Contact, Admin. `App` renders `BrowserRouter`, a nav with links to all five, and `Routes` where each `Route`'s `element` is `<ErrorBoundary><Suspense fallback={<div className="skeleton">Loading...</div>}><Page /></Suspense></ErrorBoundary>`.
TRY THIS: Render `<App />` and visit /admin — its skeleton shows, then Admin renders; other routes unaffected.
EXPECTED OUTPUT: Per-route skeleton fallbacks; each route independently fault-isolated.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
