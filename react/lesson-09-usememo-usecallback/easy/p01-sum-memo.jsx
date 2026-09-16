/*
LESSON 09 — useMemo & useCallback
EASY P01 — Memoized Sum
============================================
CONCEPT: useMemo caches a computed VALUE between renders — it recomputes only when a dependency changes, so unrelated state stays cheap.
PROBLEM: Build a `SumDemo` with `nums` state ([1..5]) and a separate `text` state. `const sum = useMemo(() => nums.reduce((a,b) => a+b, 0), [nums])`. Render the sum and a text input.
TRY THIS: Render `<SumDemo />` and type in the input.
EXPECTED OUTPUT: Sum stays "Sum: 15" — typing re-renders but does NOT recompute.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
