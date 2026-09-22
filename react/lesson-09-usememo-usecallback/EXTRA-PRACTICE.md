# lesson-09-usememo-usecallback — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Overusing useMemo
```jsx
// WRONG — useMemo overhead > computation cost
const sum = useMemo(() => a + b, [a, b]);
// CORRECT — just compute it
const sum = a + b;
```

## Mistake 02: Missing dependencies
```jsx
// WRONG — stale value
const data = useMemo(() => filter(items, query), [items]);
// CORRECT
const data = useMemo(() => filter(items, query), [items, query]);
```

## Mistake 03: useCallback without memoized child
```jsx
// WRONG — no benefit if child isn't memoized
const handleClick = useCallback(() => {}, []);
<MyComponent onClick={handleClick} /> // not wrapped in React.memo
```

## Mistake 04: Using useMemo for side effects
```jsx
// WRONG — useMemo is for computing values, not side effects
const data = useMemo(() => { fetchData(); }, []);
// CORRECT — use useEffect
useEffect(() => { fetchData(); }, []);
```

## Mistake 05: Recreating objects every render
```jsx
// WRONG — new object every render
<Component style={{ color: "red" }} />
// CORRECT — stable reference
const style = useMemo(() => ({ color: "red" }), []);
<Component style={style} />
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): useMemo for Primitive
### Before
```jsx
const value = useMemo(() => 42, []);
```
### After
```jsx
const value = 42; // primitives don't need memo
```

## Refactor 02 (Medium): Inline Object Prop
### Before
```jsx
<Child style={{ color: 'red' }} onClick={() => doSomething()} />
```
### After
```jsx
const style = useMemo(() => ({ color: 'red' }), []);
const handleClick = useCallback(() => doSomething(), []);
<Child style={style} onClick={handleClick} />
```

## Refactor 03 (Hard): Memo Everything
### Before
```jsx
const a = useMemo(() => x + 1, [x]);
const b = useMemo(() => a * 2, [a]);
const c = useMemo(() => b - 1, [b]);
```
### After
```jsx
const a = x + 1;
const b = a * 2;
const c = b - 1;
// Only memo expensive computations
```

---

## Approach Comparison — different ways to solve it

## Problem: Expensive Calculation

### Approach 1: useMemo
```jsx
const result = useMemo(() => expensiveCalc(data), [data]);
```

### Approach 2: Compute every render
```jsx
const result = expensiveCalc(data);
```

**Winner:** Approach 1 — only when calculation is actually expensive. Measure first.

---

## Problem: Callback to Memoized Child

### Approach 1: useCallback
```jsx
const handleClick = useCallback(() => { ... }, [deps]);
<MemoizedChild onClick={handleClick} />
```

### Approach 2: Regular function
```jsx
const handleClick = () => { ... };
<MemoizedChild onClick={handleClick} />
```

**Winner:** Approach 1 — prevents child re-render when only the callback reference changes.
