# Lesson 14 — Refactoring Challenges

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
