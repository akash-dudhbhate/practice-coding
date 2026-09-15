# Lesson 09 — Intuition Checks

## Check 01: useMemo purpose
What does useMemo do?
<details><summary>Answer</summary>
Caches (memoizes) a computed value. Only recomputes when dependencies change. Use for expensive calculations.
</details>

## Check 02: useCallback purpose
What does useCallback do?
<details><summary>Answer</summary>
Caches a function reference. Only creates a new function when deps change. Use when passing callbacks to memoized children.
</details>

## Check 03: When NOT to use useMemo
```jsx
// Don't use for:
const value = useMemo(() => a + b, [a, b]); // simple addition — cheaper than useMemo
```
<details><summary>Answer</summary>
Don't use useMemo for cheap operations. The overhead of useMemo (storing deps, comparing) may be more than the computation. Use only for expensive calculations.
</details>

## Check 04: useMemo with objects
```jsx
const style = useMemo(() => ({ color: "red", fontSize: 16 }), []);
```
<details><summary>Answer</summary>
Without useMemo, `{ color: "red" }` creates a new object every render. With useMemo, same object reference. Matters for child component re-renders.
</details>

## Check 05: useCallback vs useMemo
```jsx
const fn = useCallback(() => x + 1, [x]);
const fn2 = useMemo(() => () => x + 1, [x]);
```
<details><summary>Answer</summary>
Both are equivalent. useCallback(fn, deps) is shorthand for useMemo(() => fn, deps). useCallback is more readable.
</details>
