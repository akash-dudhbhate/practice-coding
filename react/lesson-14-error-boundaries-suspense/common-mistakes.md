# Lesson 14 — Common Mistakes

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
