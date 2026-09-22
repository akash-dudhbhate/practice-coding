# lesson-14-error-boundaries-suspense — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Error boundary catches what?
<details><summary>Answer</summary>
Errors in rendering, lifecycle methods, and constructors of child components. Does NOT catch: event handlers, async code, setTimeout, errors in the boundary itself.
</details>

## Check 02: getDerivedStateFromError
```jsx
static getDerivedStateFromError(error) {
  return { hasError: true };
}
```
<details><summary>Answer</summary>
Lifecycle method that catches render errors. Returns new state. Used to show fallback UI.
</details>

## Check 03: componentDidCatch
```jsx
componentDidCatch(error, info) {
  logError(error, info);
}
```
<details><summary>Answer</summary>
Called after error is caught. Used for side effects like logging. `info` contains component stack.
</details>

## Check 04: Suspense
```jsx
const LazyComponent = React.lazy(() => import("./Component"));
<Suspense fallback={<Spinner />}>
  <LazyComponent />
</Suspense>
```
<details><summary>Answer</summary>
Suspense shows fallback while lazy component loads. React.lazy dynamically imports the component.
</details>

## Check 05: Nested Suspense
```jsx
<Suspense fallback={<GlobalSpinner />}>
  <Header />
  <Suspense fallback={<ContentSpinner />}>
    <Content />
  </Suspense>
</Suspense>
```
<details><summary>Answer</summary>
Nested Suspense — each level has its own fallback. Content loads independently of Header.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Error Boundary Not Catching
```jsx
function MyComponent() {
  if (error) throw new Error("oops");
}
// No error boundary wraps it
```
<details><summary>Answer</summary>
**Bug:** Error in render crashes the whole app. No error boundary to catch it.
**Fix:** Wrap in `<ErrorBoundary><MyComponent /></ErrorBoundary>`.
</details>

## Debug 02 (Medium): Error Boundary as Hook
```jsx
function useErrorBoundary() {
  const [error, setError] = useState(null);
  // can't catch render errors with hooks
}
```
<details><summary>Answer</summary>
**Bug:** Error boundaries MUST be class components. Hooks can't catch render errors.
**Fix:** Use class component with `componentDidCatch` or `getDerivedStateFromError`.
</details>

## Debug 03 (Hard): Suspense Without Fallback
```jsx
<Suspense>
  <LazyComponent />
</Suspense>
```
<details><summary>Answer</summary>
**Bug:** No fallback prop — shows nothing while loading.
**Fix:** `<Suspense fallback={<Spinner />}>`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: No error boundary
```jsx
// WRONG — one error crashes entire app
<App />
// CORRECT — isolate errors
<ErrorBoundary><App /></ErrorBoundary>
```

## Mistake 02: Error boundary as function component
```jsx
// WRONG — can't catch errors
function ErrorBoundary() { ... }
// CORRECT — must be class
class ErrorBoundary extends React.Component { ... }
```

## Mistake 03: No fallback in Suspense
```jsx
// WRONG — blank screen while loading
<Suspense><Lazy /></Suspense>
// CORRECT
<Suspense fallback={<Spinner />}><Lazy /></Suspense>
```

## Mistake 04: Not logging errors
```jsx
componentDidCatch(error) {
  // silently ignored
}
// CORRECT
componentDidCatch(error, info) {
  logToService(error, info);
}
```

## Mistake 05: Catching event handler errors in boundary
```jsx
// Error boundaries DON'T catch event handler errors
// Use try/catch in the handler instead
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Error Boundary
### Before
```jsx
<App /> // crash takes down whole app
```
### After
```jsx
<ErrorBoundary fallback={<Error />}><App /></ErrorBoundary>
```

## Refactor 02 (Medium): No Suspense Fallback
### Before
```jsx
<Suspense><LazyComponent /></Suspense>
```
### After
```jsx
<Suspense fallback={<Spinner />}><LazyComponent /></Suspense>
```

## Refactor 03 (Hard): Error in Callback
### Before
```jsx
onClick={() => { throw new Error("oops"); }} // not caught by boundary
```
### After
```jsx
onClick={() => { try { riskyAction(); } catch (e) { setError(e.message); } }}
```

---

## Approach Comparison — different ways to solve it

## Problem: Handle Errors

### Approach 1: try/catch in render
```jsx
try { return <Component />; }
catch (e) { return <Error />; }
```
**Cons:** Can't catch render errors in children.

### Approach 2: Error boundary
```jsx
<ErrorBoundary><Component /></ErrorBoundary>
```

**Winner:** Approach 2 — catches errors in entire subtree.

---

## Problem: Code Splitting

### Approach 1: React.lazy + Suspense
```jsx
const Page = React.lazy(() => import("./Page"));
<Suspense fallback={<Spinner />}><Page /></Suspense>
```

### Approach 2: Manual dynamic import
```jsx
const [Page, setPage] = useState(null);
useEffect(() => { import("./Page").then(m => setPage(m.default)); }, []);
if (!Page) return <Spinner />;
return <Page />;
```

**Winner:** Approach 1 — declarative, cleaner.
