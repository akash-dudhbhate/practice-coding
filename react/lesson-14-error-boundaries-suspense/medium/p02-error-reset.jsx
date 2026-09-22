/*
LESSON 14 — Error Boundaries & Suspense
MEDIUM P02 — ErrorBoundary with Reset
============================================
CONCEPT: A fallback with no escape hatch traps the user. Giving the boundary a `reset` method (setState back to no-error) plus a "Try Again" button lets the children re-render after a transient failure.
PROBLEM: Write `ErrorBoundary` with `hasError` state and `getDerivedStateFromError`. Add a class-field `reset = () => this.setState({hasError: false})`. When `hasError`, render "Error occurred" and a `<button onClick={this.reset}>Try Again</button>`; otherwise render `this.props.children`. Export the boundary.
TRY THIS: Wrap a widget that throws, watch the fallback, then click Try Again (the child re-renders — it may throw again, which is expected).
EXPECTED OUTPUT: Fallback with a working Try Again button that attempts re-render.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
