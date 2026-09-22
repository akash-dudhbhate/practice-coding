/*
LESSON 14 — Error Boundaries & Suspense
EASY P01 — ErrorBoundary Class Component
============================================
CONCEPT: Error boundaries are the ONLY class components still needed: `static getDerivedStateFromError` flips an error flag so render can swap children for a fallback instead of crashing the whole tree.
PROBLEM: Write an `ErrorBoundary` class extending `Component` with `state = {hasError: false}` and `static getDerivedStateFromError()` returning `{hasError: true}`. `render()` returns an `<h2>Something went wrong.</h2>` when `hasError`, else `this.props.children`. Create `BuggyComponent` that throws on render, and `App` wrapping it in the boundary.
TRY THIS: Render `<App />` — instead of a white screen you get the fallback.
EXPECTED OUTPUT: "Something went wrong." renders; without the boundary the app would crash.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
