# Lesson 09 — Coding Check

## Easy

### p01-solve.jsx — Sum with useMemo
- [ ] List of numbers displayed
- [ ] Text input exists (unrelated state)
- [ ] `useMemo` computes sum of numbers
- [ ] Typing in input does NOT recompute sum
- [ ] Dependency array only includes the numbers array

### p02-solve.jsx — React.memo + useCallback
- [ ] Parent has a counter state
- [ ] Child is wrapped in `React.memo`
- [ ] Handler is wrapped in `useCallback`
- [ ] Incrementing counter does NOT re-render child
- [ ] Child has a console.log or render counter to verify

### p03-solve.jsx — Sort 1000 numbers
- [ ] Array of 1000 random numbers
- [ ] `useMemo` sorts the array
- [ ] Button regenerates array (triggers re-sort)
- [ ] Text input does NOT trigger re-sort
- [ ] Dependency array only includes the numbers array

## Medium

### p01-solve.jsx — SearchFilter
- [ ] 100+ items in a list
- [ ] Search input filters items
- [ ] `useMemo` used for filtering
- [ ] Unrelated state change (e.g., a counter) does NOT re-filter
- [ ] Filter is case-insensitive

### p02-solve.jsx — TodoList with memo
- [ ] Todo items wrapped in `React.memo`
- [ ] Delete handler wrapped in `useCallback`
- [ ] Adding a new todo does NOT re-render existing items
- [ ] Each item has a render counter (console.log)
- [ ] Deleting an item works correctly

### p03-solve.jsx — Dashboard widgets
- [ ] 3 widgets: stats, chart, table
- [ ] Each widget is `React.memo`-wrapped
- [ ] `useMemo` for computed data per widget
- [ ] `useCallback` for handlers
- [ ] Updating one widget's data does NOT re-render others
- [ ] Render counters verify isolation

## Hard

### p01-solve.jsx — DataTable
- [ ] 1000 rows rendered
- [ ] Sortable by clicking column headers
- [ ] Filterable by search input
- [ ] `useMemo` for both sort and filter
- [ ] Render count displayed (should stay low on unrelated changes)
- [ ] Sorting and filtering are chained efficiently

### p02-solve.jsx — Form with isolated fields
- [ ] Multiple form fields (at least 4)
- [ ] Each field is `React.memo`-wrapped
- [ ] Each field has `useCallback` change handler
- [ ] Typing in one field does NOT re-render others
- [ ] Render counters verify isolation
- [ ] Form data is collected correctly

### p03-solve.jsx — PerformanceDemo
- [ ] Toggle to enable/disable memoization
- [ ] Render counter for each mode
- [ ] `Profiler` wrapper measures actual render times
- [ ] Difference in render counts is visible
- [ ] Difference in render times is displayed
- [ ] Clear visual comparison between modes
