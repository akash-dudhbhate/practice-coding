# Lesson 20 — React Performance Optimization

## What you'll learn
- The React render cycle (when components re-render)
- React.memo (preventing unnecessary re-renders)
- useMemo and useCallback (stable references)
- Virtualization (rendering large lists efficiently)
- Code splitting (lazy loading for smaller bundles)
- Bundle analysis (finding large dependencies)
- Profiling with React DevTools
- useTransition (non-urgent updates)
- useDeferredValue (deferring expensive computations)

## Lesson

### React.memo + useCallback
```jsx
const Child = React.memo(({ onClick }) => <button onClick={onClick}>X</button>);
const handle = useCallback(() => {}, []);
```

### Virtualization
```jsx
import { FixedSizeList as List } from 'react-window';
<List height={600} itemCount={items.length} itemSize={50}>{Row}</List>
```

### useTransition
```jsx
const [isPending, startTransition] = useTransition();
startTransition(() => setResults(filterHuge(query)));
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a parent with a counter and a `React.memo` child. The child should NOT re-render when the counter changes. Add a render counter (console.log) to verify.
2. `easy/p02-solve.jsx` — Create a component that uses `useMemo` to compute an expensive calculation (e.g., sorting 1000 numbers). Add a text input that changes unrelated state. Verify the sort doesn't recompute on typing.
3. `easy/p03-solve.jsx` — Create a parent with `useCallback` for a handler passed to a `React.memo` child. Verify the child doesn't re-render when unrelated state changes.

### Medium
4. `medium/p01-solve.jsx` — Create a list of 100 items rendered with `React.memo` items. Each item has a delete button with `useCallback`. Deleting one item should NOT re-render the other 99 items. Verify with render counters.
5. `medium/p02-solve.jsx` — Create a search component with `useDeferredValue`: input updates immediately, list filtering uses the deferred value. Typing should be smooth even with 10,000 items. Show a visual indicator when filtering is deferred.
6. `medium/p03-solve.jsx` — Create a route-level code-split app: 3 lazy-loaded routes with Suspense and ErrorBoundary. Measure and compare the initial bundle size vs. without code splitting (use comments to document).

### Hard
7. `hard/p01-solve.jsx` — Build a virtualized list using `react-window`: 10,000 items, smooth scrolling, dynamic row heights. Include search filtering (filter the data, not the DOM). Compare render performance with a non-virtualized version.
8. `hard/p02-solve.jsx` — Build a dashboard with `useTransition`: a search input that filters a large dataset. The input updates immediately (urgent), the filtered results update in the background (non-urgent). Show `isPending` indicator. Verify typing is never blocked.
9. `hard/p03-solve.jsx` — Build a performance comparison demo: a toggle between "optimized" and "unoptimized" modes. Include: render counters, Profiler wrapper with timing display, and 3 scenarios (large list, expensive calculation, frequent updates). Show the actual difference in render times.

### How to work
- Write your complete React solution.
- Remove the TODO comment when done.
- Test by importing into a React app.
