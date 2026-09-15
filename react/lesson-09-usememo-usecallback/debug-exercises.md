# Lesson 09 — Debug Exercises

## Debug 01 (Easy: useMemo Without Dependencies
```jsx
const value = useMemo(() => computeExpensive(a, b));
```
<details><summary>Answer</summary>
**Bug:** No dependency array — recomputes every render (no benefit).
**Fix:** `useMemo(() => computeExpensive(a, b), [a, b]);`.
</details>

## Debug 02 (Medium): useCallback for Simple Function
```jsx
const handleClick = useCallback(() => { setCount(c => c + 1); }, []);
```
<details><summary>Answer</summary>
**Issue:** Over-optimization. useCallback has its own cost. Only use when passing to memoized child or effect dependencies.
**Fix:** Often just `const handleClick = () => setCount(c => c + 1);` is fine.
</details>

## Debug 03 (Hard): Stale Closure in useMemo
```jsx
const data = useMemo(() => filter(items, query), [items]);
```
<details><summary>Answer</summary>
**Bug:** `query` used but not in deps. Uses stale query value.
**Fix:** `useMemo(() => filter(items, query), [items, query]);`.
</details>
