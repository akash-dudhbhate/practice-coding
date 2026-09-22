/*
LESSON 14 — Error Boundaries & Suspense
EASY P02 — React.lazy + Suspense
============================================
CONCEPT: `lazy(() => import("./Comp"))` code-splits a component into a separate chunk fetched on first render. `Suspense` wraps it and shows `fallback` UI while the chunk downloads.
PROBLEM: Import `lazy` and `Suspense` from react. Define `const LazyComponent = lazy(() => import("./SomeComponent"))`. Build `App` rendering `<LazyComponent />` inside `<Suspense fallback={<p>Loading...</p>}>`.
TRY THIS: Render `<App />` with network throttling — the fallback appears first, then the component pops in.
EXPECTED OUTPUT: "Loading..." shows until the lazy chunk resolves, then the component renders.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
