/*
LESSON 20 — React Performance
MEDIUM P03 — Route-Level Code Splitting
============================================
CONCEPT: `lazy()` at the route level means each page ships as its own chunk — the initial bundle excludes them. Wrap `Routes` in `Suspense` (loading UI) and an `ErrorBoundary` (failed import UI). Document the bundle-size win in comments.
PROBLEM: Define an `ErrorBoundary` class (hasError + fallback "Failed to load route"). `lazy()`-import Home, About, Contact. `App` renders `BrowserRouter` + nav Links, then `<ErrorBoundary><Suspense fallback={<p>Loading route...</p>}><Routes>` with the 3 routes. Add comments comparing initial bundle size with vs. without splitting.
TRY THIS: Render `<App />` — each route chunk downloads only on first visit (check Network tab).
EXPECTED OUTPUT: Smaller initial bundle; per-route chunks load on demand with the shared fallback.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
