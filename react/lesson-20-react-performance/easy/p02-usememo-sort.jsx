/*
LESSON 20 — React Performance
EASY P02 — useMemo for Expensive Calculations
============================================
CONCEPT: `useMemo(() => compute(), [deps])` caches a computed value and only recomputes when deps change — so typing in an unrelated input doesn't re-sort 1000 numbers.
PROBLEM: Build `SortedList`: `nums` state initialized once to 1000 random numbers (lazy `useState(() => ...)`), a separate `text` state, and `sorted = useMemo(() => [...nums].sort((a,b) => a-b), [nums])`. Render the first 5 sorted numbers and a controlled text input.
TRY THIS: Render `<SortedList />` and type fast — the sort result never recomputes because `nums` didn't change.
EXPECTED OUTPUT: Sorted preview stays stable; typing is instant (no re-sort).
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
