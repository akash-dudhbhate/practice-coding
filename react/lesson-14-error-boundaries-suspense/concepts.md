# Lesson 14 — Concepts Explained (Error Boundaries & Suspense)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Error Boundaries

**What:** Error boundaries are React components that catch errors in their child component tree. They prevent one component's error from crashing the entire app.

```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true, error };
    }

    componentDidCatch(error, errorInfo) {
        console.error("Error caught:", error, errorInfo);
        // log to error reporting service (Sentry, etc.)
    }

    render() {
        if (this.state.hasError) {
            return this.props.fallback || <h1>Something went wrong.</h1>;
        }
        return this.props.children;
    }
}

// Usage
function App() {
    return (
        <ErrorBoundary fallback={<ErrorPage />}>
            <MyComponent />
        </ErrorBoundary>
    );
}
```

**Why it exists:** Without error boundaries, a JavaScript error in any component unmounts the ENTIRE component tree → blank page → terrible UX. Error boundaries catch the error → show a fallback → rest of the app keeps working.

**Where it's used:** Around risky components (data fetching, third-party widgets, user-generated content), at the app root (last-resort catch), around route-level components.

**What goes wrong without it:**
- Error boundaries ONLY catch errors in rendering, lifecycle methods, and constructors. They do NOT catch: event handlers, async code, setTimeout. Wrap those in try/catch.
- Error boundary must be a CLASS component (no hook equivalent). This is one of the few cases where class components are still needed.
- Error in the error boundary's own `render` → not caught → propagates up. Keep the fallback simple.

---

## getDerivedStateFromError

**What:** A static lifecycle method that updates state when a child throws an error.

```jsx
static getDerivedStateFromError(error) {
    // Called during the "render" phase → must be pure
    // Can only return a new state object
    return { hasError: true, error };
}
```

**Why it exists:** This method runs during render → it must be pure (no side effects). It sets the state that triggers the fallback UI. Without it, the error boundary doesn't know an error occurred.

**Where it's used:** Inside every error boundary class component.

**What goes wrong without it:**
- Calling `setState` directly in `componentDidCatch` during render → error. Use `getDerivedStateFromError` for state update, `componentDidCatch` for side effects (logging).
- Returning `null` → state doesn't change → error boundary doesn't show fallback → error propagates.
- This method is `static` → can't access `this`. Only receives the `error` argument.

---

## componentDidCatch

**What:** A lifecycle method called AFTER the error is caught — for side effects like logging.

```jsx
componentDidCatch(error, errorInfo) {
    // Called after render → safe for side effects
    logErrorToService(error, errorInfo);
    console.error("Component error:", error);
    console.error("Component stack:", errorInfo.componentStack);
}
```

**Why it exists:** `getDerivedStateFromError` must be pure (no side effects). `componentDidCatch` runs after render → safe for logging, analytics, error reporting. Together they handle both state update and side effects.

**Where it's used:** Error reporting (Sentry, LogRocket, custom logging), analytics, development debugging.

**What goes wrong without it:**
- Logging in `getDerivedStateFromError` → side effects during render → React may call it multiple times → duplicate logs.
- `errorInfo.componentStack` → shows where in the component tree the error occurred → invaluable for debugging. Don't ignore it.
- Forgetting to log → errors are silently swallowed → can't debug production issues.

---

## Fallback UI

**What:** The UI shown when an error is caught — instead of the crashed component.

```jsx
<ErrorBoundary fallback={
    <div className="error-fallback">
        <h2>Oops! Something broke.</h2>
        <p>We're working on it.</p>
        <button onClick={() => window.location.reload()}>Reload</button>
    </div>
}>
    <RiskyComponent />
</ErrorBoundary>

// Or use a render prop for more control
<ErrorBoundary fallback={(error, reset) => (
    <div>
        <p>Error: {error.message}</p>
        <button onClick={reset}>Try Again</button>
    </div>
)}>
    <RiskyComponent />
</ErrorBoundary>
```

**Why it exists:** Without a fallback, the error boundary shows nothing → blank area → confusing. A good fallback explains what happened and offers recovery (reload, retry, go home).

**Where it's used:** Every error boundary — the fallback is what the user sees instead of the crashed component.

**What goes wrong without it:**
- Fallback that uses the same broken component → error again → infinite error loop. Keep the fallback simple and independent.
- No recovery action → user is stuck on the error page. Always provide a way to recover (reload, navigate, retry).
- Showing the raw error to users → confusing and potentially a security risk (stack traces). Show user-friendly messages.

---

## Resetting Error Boundaries

**What:** Allow the error boundary to recover without a full page reload.

```jsx
class ErrorBoundary extends Component {
    state = { hasError: false, error: null };

    static getDerivedStateFromError(error) {
        return { hasError: true, error };
    }

    reset = () => {
        this.setState({ hasError: false, error: null });
    };

    render() {
        if (this.state.hasError) {
            if (typeof this.props.fallback === 'function') {
                return this.props.fallback(this.state.error, this.reset);
            }
            return this.props.fallback || <h1>Something went wrong.</h1>;
        }
        return this.props.children;
    }
}

// Usage with reset
<ErrorBoundary fallback={(error, reset) => (
    <div>
        <p>Error: {error.message}</p>
        <button onClick={reset}>Try Again</button>
    </div>
)}>
    <RiskyComponent />
</ErrorBoundary>
```

**Why it exists:** Without reset, the only recovery is a full page reload → loses all app state. Reset clears the error state → children re-render → if the error was transient, it might work now.

**Where it's used:** Error boundaries with retry functionality — failed API calls, flaky components, user-initiated retries.

**What goes wrong without it:**
- Reset doesn't fix the underlying issue → same error immediately → error loop. Reset is useful for transient errors, not persistent ones.
- Reset clears the error state but doesn't re-mount children → if the child's state caused the error, it might still be broken. Use `key` to force remount: `<RiskyComponent key={Date.now()} />`.

---

## Suspense

**What:** `Suspense` lets components "wait" for something (data, lazy-loaded code) before rendering. Shows a fallback while waiting.

```jsx
import { Suspense, lazy } from 'react';

const LazyComponent = lazy(() => import('./HeavyComponent'));

function App() {
    return (
        <Suspense fallback={<div>Loading...</div>}>
            <LazyComponent />
        </Suspense>
    );
}
// While HeavyComponent loads, "Loading..." is shown
// Once loaded, HeavyComponent renders
```

**Why it exists:** Without Suspense, lazy-loaded components show nothing while loading → blank area → bad UX. Suspense shows a fallback (spinner, skeleton) → user knows something is loading.

**Where it's used:** Code splitting (lazy-loaded routes/components), data fetching (React 18+ with Suspense for Data Fetching), image loading.

**What goes wrong without it:**
- `lazy()` without `Suspense` → error: "React was unable to find the Suspense boundary." Always wrap lazy components in Suspense.
- Fallback that's too small → layout shift when the real component loads. Use a skeleton that matches the component's size.
- Nested Suspense → inner Suspense fallback shows for inner component, outer for outer. Useful for progressive loading.

---

## React.lazy and Code Splitting

**What:** `React.lazy` dynamically imports a component only when it's first rendered → reduces initial bundle size.

```jsx
import { lazy, Suspense } from 'react';

// Static import (always loaded)
import Home from './Home';

// Lazy import (loaded on demand)
const About = lazy(() => import('./About'));
const Dashboard = lazy(() => import('./Dashboard'));

function App() {
    return (
        <Suspense fallback={<Loading />}>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </Suspense>
    );
}
// Home loads immediately. About and Dashboard load when navigated to.
```

**Why it exists:** Without code splitting, the entire app is in one JS bundle → slow initial load. `lazy()` splits the bundle → user only downloads what they need → faster initial page load.

**Where it's used:** Route-level code splitting, heavy components (charts, editors), admin sections that most users don't visit.

**What goes wrong without it:**
- `lazy(() => import('./Component'))` → `import()` returns a promise. If the import fails (network error, missing file) → error. Wrap in an error boundary.
- Named exports: `lazy(() => import('./Module').then(m => m.NamedExport))` → `lazy` expects default export. For named exports, map it.
- Too many lazy components → many small chunks → many network requests. Find a balance.

---

## Suspense with Error Boundaries

**What:** Combine Suspense (loading) with Error Boundaries (errors) for complete async handling.

```jsx
function App() {
    return (
        <ErrorBoundary fallback={<ErrorPage />}>
            <Suspense fallback={<Loading />}>
                <LazyComponent />
            </Suspense>
        </ErrorBoundary>
    );
}

// Error boundary OUTSIDE Suspense → catches:
// 1. Render errors in LazyComponent
// 2. Errors from failed lazy import (network error, missing file)
```

**Why it exists:** Suspense handles the loading state. Error boundaries handle the error state. Together they cover both failure modes of async components → robust UX.

**Where it's used:** Every lazy-loaded component — wrap in both Suspense (for loading) and ErrorBoundary (for import failures).

**What goes wrong without it:**
- Error boundary INSIDE Suspense → can't catch import errors (Suspense catches the thrown promise first). Put error boundary OUTSIDE.
- No error boundary → failed import → blank page or crash. Always wrap lazy components in error boundaries.
- No Suspense → lazy component throws a promise → React error. Always wrap in Suspense.
