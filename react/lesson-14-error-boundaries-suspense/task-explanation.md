# Lesson 14 — Error Boundaries & Suspense

## What you'll learn
- Error boundaries (catching render errors)
- getDerivedStateFromError (state update on error)
- componentDidCatch (logging and side effects)
- Fallback UI (what to show on error)
- Resetting error boundaries (retry without reload)
- Suspense (waiting for async content)
- React.lazy and code splitting
- Combining Suspense with Error Boundaries

## Lesson

### Error boundary
```jsx
class ErrorBoundary extends Component {
    static getDerivedStateFromError(error) { return { hasError: true }; }
    render() {
        return this.state.hasError ? <Fallback /> : this.props.children;
    }
}
```

### Lazy + Suspense
```jsx
const Lazy = lazy(() => import('./Component'));
<Suspense fallback={<Loading />}><Lazy /></Suspense>
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create an `ErrorBoundary` class component that catches errors and shows a simple fallback message. Test it with a component that throws on render.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | Something went wrong.            |  <- <h2> fallback replaces
   +----------------------------------+     the crashed <BuggyComponent>
   (page stays alive — no white screen)
   ```
2. `easy/p02-solve.jsx` — Use `React.lazy` to lazy-load a component. Wrap it in `<Suspense>` with a loading fallback. Verify it loads on demand.

   WHAT IT SHOULD LOOK LIKE:
   ```
   WHILE CHUNK LOADS:       AFTER RESOLVE:
   Loading...               <the lazy component's content>
   ```
3. `easy/p03-solve.jsx` — Create a component that simulates an error (e.g., throws if a prop is missing). Wrap it in an `ErrorBoundary` and show a user-friendly fallback.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | Oops! Something broke.           |  <- red fallback when
   | Please refresh the page.         |     user prop is missing
   +----------------------------------+
   (with a user prop: "Alice" renders normally)
   ```

### Medium
4. `medium/p01-solve.jsx` — Create an `ErrorBoundary` with logging: use `componentDidCatch` to log errors to console with the component stack. Show the error message in the fallback UI.

   WHAT IT SHOULD LOOK LIKE:
   ```
   PAGE:                        CONSOLE:
   Error                        user prop is required
   user prop is required        + component stack trace
   ```
5. `medium/p02-solve.jsx` — Create an `ErrorBoundary` with a reset function. The fallback has a "Try Again" button that resets the error state. Test with a component that fails randomly.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | Error occurred                   |
   |              [ Try Again ]       |  <- resets hasError,
   +----------------------------------+     re-renders children
   ```
6. `medium/p03-solve.jsx` — Create a lazy-loaded route setup: 3 routes, each component is `lazy()`-loaded. Wrap in `Suspense` with a shared loading fallback. Add an `ErrorBoundary` outside Suspense.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Home | About | Contact              <- nav links
   ----------------------------------
   FIRST VISIT to /about:
   Loading page...   ->   About        <- lazy chunk + <h1>
   (broken import -> boundary fallback instead)
   ```

### Hard
7. `hard/p01-solve.jsx` — Build a reusable `ErrorBoundary` that accepts a `fallback` render prop: `fallback={(error, reset) => <CustomError error={error} onRetry={reset} />}`. Include logging to a mock error service.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | CUSTOM FALLBACK (from render     |
   |  prop, shows real error message) |
   | "user prop is required"          |
   |                    [ Retry ]     |  <- calls reset()
   +----------------------------------+
   ```
8. `hard/p02-solve.jsx` — Build a dashboard with multiple widgets, each wrapped in its own `ErrorBoundary`. If one widget crashes, others keep working. Each shows its own error fallback with retry.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----------+ +-----------+ +-----------+
   |  Stats    | |  CHART    | | Widget    |  <- only the buggy
   |  OK       | |  OK       | | crashed   |     widget shows the
   |           | |           | | [ Retry ] |     fallback
   +-----------+ +-----------+ +-----------+
   ```
9. `hard/p03-solve.jsx` — Build a code-split app: lazy-load 5 components (Home, About, Products, Contact, Admin). Each route has its own `Suspense` (with skeleton fallbacks) and `ErrorBoundary` (for failed imports). Include a shared loading bar at the top.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Home | About | Products | Contact | Admin
   ====================================== <- loading bar
   +----------------------------------+
   | skeleton Loading...              |  <- per-route skeleton,
   +----------------------------------+     fault-isolated per route
   ```

### How to work
- Write your complete React solution.
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
