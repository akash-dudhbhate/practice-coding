# Lesson 14 — Intuition Checks

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
