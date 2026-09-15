# Lesson 14 — Coding Check

## Easy

### p01-solve.jsx — Basic ErrorBoundary
- [ ] Class component with `getDerivedStateFromError`
- [ ] `hasError` state set to true on error
- [ ] Fallback UI shown when error occurs
- [ ] Children rendered normally when no error
- [ ] Test component that throws on render is included

### p02-solve.jsx — Lazy + Suspense
- [ ] `React.lazy()` used to import a component
- [ ] `<Suspense>` wraps the lazy component
- [ ] Loading fallback shown while loading
- [ ] Component renders after loading completes
- [ ] No errors in console

### p03-solve.jsx — Error boundary with missing prop
- [ ] Component throws if required prop is missing
- [ ] Wrapped in `ErrorBoundary`
- [ ] Fallback UI shown when error occurs
- [ ] User-friendly error message displayed
- [ ] App doesn't crash entirely

## Medium

### p01-solve.jsx — ErrorBoundary with logging
- [ ] `componentDidCatch` implemented
- [ ] Error logged to console
- [ ] Component stack logged (errorInfo.componentStack)
- [ ] Error message shown in fallback UI
- [ ] Both `getDerivedStateFromError` and `componentDidCatch` present

### p02-solve.jsx — ErrorBoundary with reset
- [ ] Reset function defined
- [ ] Reset clears `hasError` state
- [ ] Fallback has "Try Again" button
- [ ] Button calls reset function
- [ ] Component re-renders after reset
- [ ] Works with randomly failing component

### p03-solve.jsx — Lazy routes with Suspense
- [ ] 3 route components lazy-loaded
- [ ] Each uses `React.lazy()`
- [ ] Shared `Suspense` wrapper with loading fallback
- [ ] `ErrorBoundary` outside `Suspense`
- [ ] Routes work correctly
- [ ] Loading state visible on navigation

## Hard

### p01-solve.jsx — Reusable ErrorBoundary with render prop
- [ ] `fallback` accepts a function (render prop)
- [ ] Function receives `error` and `reset` arguments
- [ ] Custom error UI rendered via render prop
- [ ] Mock error service logging implemented
- [ ] Reset functionality works
- [ ] Reusable across different components

### p02-solve.jsx — Dashboard with isolated error boundaries
- [ ] Multiple widgets in a dashboard
- [ ] Each widget wrapped in its own `ErrorBoundary`
- [ ] One widget crashing doesn't affect others
- [ ] Each widget shows its own error fallback
- [ ] Each has its own retry button
- [ ] Working widgets continue to function

### p03-solve.jsx — Code-split app with 5 routes
- [ ] 5 components lazy-loaded (Home, About, Products, Contact, Admin)
- [ ] Each route has its own `Suspense` boundary
- [ ] Skeleton fallbacks for each route
- [ ] `ErrorBoundary` for failed imports
- [ ] Shared loading bar at the top
- [ ] Navigation between routes is smooth
- [ ] Failed imports show error fallback
