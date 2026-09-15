# Lesson 14 — Debug Exercises

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
