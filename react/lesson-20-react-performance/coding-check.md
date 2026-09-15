# Lesson 20 — Coding Check

## Easy

### p01-solve.jsx — React.memo basic
- [ ] Parent has a counter state
- [ ] Child is wrapped in `React.memo`
- [ ] Child has a render counter (console.log)
- [ ] Incrementing counter does NOT re-render child
- [ ] Render counter verifies this

### p02-solve.jsx — useMemo expensive calc
- [ ] Expensive calculation (sorting 1000 numbers)
- [ ] `useMemo` wraps the calculation
- [ ] Text input changes unrelated state
- [ ] Typing does NOT trigger re-sort
- [ ] Dependency array only includes the data

### p03-solve.jsx — useCallback + React.memo
- [ ] Handler wrapped in `useCallback`
- [ ] Child wrapped in `React.memo`
- [ ] Unrelated state change in parent
- [ ] Child does NOT re-render
- [ ] Render counter verifies this

## Medium

### p01-solve.jsx — Memoized list items
- [ ] 100 items in a list
- [ ] Each item is `React.memo`-wrapped
- [ ] Delete button uses `useCallback`
- [ ] Deleting one item doesn't re-render others
- [ ] Render counters verify isolation
- [ ] Delete works correctly

### p02-solve.jsx — useDeferredValue search
- [ ] Search input updates immediately
- [ ] List filtering uses `useDeferredValue`
- [ ] 10,000 items in the list
- [ ] Typing is smooth (not blocked)
- [ ] Visual indicator when deferred (e.g., opacity change)
- [ ] Results update after a brief delay

### p03-solve.jsx — Code-split routes
- [ ] 3 routes lazy-loaded with `React.lazy`
- [ ] `Suspense` wraps the routes
- [ ] `ErrorBoundary` handles import failures
- [ ] Loading fallback shown
- [ ] Initial bundle is smaller (documented)
- [ ] Routes load on demand

## Hard

### p01-solve.jsx — Virtualized list
- [ ] `react-window` or similar used
- [ ] 10,000 items rendered
- [ ] Smooth scrolling (no jank)
- [ ] Search filtering works (filters data array)
- [ ] Only visible items are in the DOM
- [ ] Performance comparison documented

### p02-solve.jsx — useTransition dashboard
- [ ] Search input updates immediately (urgent)
- [ ] `useTransition` wraps the filtering
- [ ] `isPending` indicator shown
- [ ] Large dataset (1000+ items)
- [ ] Typing is never blocked
- [ ] Results update in the background

### p03-solve.jsx — Performance comparison demo
- [ ] Toggle between optimized and unoptimized modes
- [ ] Render counters for each mode
- [ ] `Profiler` wrapper with timing display
- [ ] Scenario 1: large list rendering
- [ ] Scenario 2: expensive calculation
- [ ] Scenario 3: frequent state updates
- [ ] Actual render times displayed
- [ ] Clear visual difference between modes
