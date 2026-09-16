/*
LESSON 14 — Error Boundaries & Suspense
EASY P03 — Boundary Catching a Missing Prop
============================================
CONCEPT: Throwing during render for invalid props is fine IF a boundary is above — the error becomes a controlled fallback instead of an app crash.
PROBLEM: Write `ErrorBoundary` (class, `getDerivedStateFromError` → `hasError`) rendering a friendly red fallback ("Oops! Something broke." + "Please refresh the page."). Write `UserCard({user})` that throws `new Error("user prop is required")` when `user` is missing, else renders `user.name`. `App` renders `<UserCard />` (NO prop) inside the boundary.
TRY THIS: Render `<App />` — the boundary catches the missing-prop throw.
EXPECTED OUTPUT: The friendly fallback renders; pass a `user` prop and the name shows instead.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
