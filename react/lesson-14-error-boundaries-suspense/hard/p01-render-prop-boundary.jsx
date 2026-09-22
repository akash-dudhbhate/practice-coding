/*
LESSON 14 — Error Boundaries & Suspense
HARD P01 — Reusable ErrorBoundary with Fallback Render Prop
============================================
CONCEPT: A hard-coded fallback makes the boundary single-purpose. Accepting `fallback` as a FUNCTION prop — `this.props.fallback(error, reset)` — lets every caller design its own error UI with retry.
PROBLEM: Write `ErrorBoundary` storing `{hasError, error}` in state via `getDerivedStateFromError`, logging `{error: error.message, stack: errorInfo.componentStack}` to a mock error service in `componentDidCatch`, and exposing `reset` (clears both fields). On error, `render()` returns `this.props.fallback(this.state.error, this.reset)`; else `this.props.children`. Add a usage comment showing `<ErrorBoundary fallback={(error, reset) => ...}>`.
TRY THIS: Use it with `fallback={(error, reset) => <div><p>{error.message}</p><button onClick={reset}>Retry</button></div>}` around a buggy child.
EXPECTED OUTPUT: Caller's custom fallback renders with the real message and a working Retry.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
