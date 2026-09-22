/*
LESSON 14 — Error Boundaries & Suspense
MEDIUM P01 — ErrorBoundary with Logging
============================================
CONCEPT: `componentDidCatch(error, errorInfo)` is the second half of a boundary — it runs after the fallback swap and is where you report errors (console, Sentry, …). `errorInfo.componentStack` tells you WHICH component threw.
PROBLEM: Write `ErrorBoundary` with `state = {hasError: false, error: null}`. `static getDerivedStateFromError(error)` stores the error. `componentDidCatch(error, errorInfo)` logs `error.message` and `errorInfo.componentStack` via `console.error`. `render()` shows an `<h2>Error</h2>` plus `this.state.error?.message` when `hasError`, else `this.props.children`. Export the boundary itself.
TRY THIS: Wrap a component that throws and open the console — you see both the message and the component stack.
EXPECTED OUTPUT: Fallback displays the error message; console shows the logged error + stack.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
