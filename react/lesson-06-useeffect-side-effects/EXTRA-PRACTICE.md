# lesson-06-useeffect-side-effects — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Dependency array
```jsx
useEffect(() => {}, []);        // A — runs once
useEffect(() => {}, [x]);       // B — runs when x changes
useEffect(() => {});            // C — runs every render
```
<details><summary>Answer</summary>
A — mount only (like componentDidMount). B — mount + when x changes. C — every render (rarely what you want).
</details>

## Check 02: Cleanup
```jsx
useEffect(() => {
  const sub = subscribe();
  return () => unsubscribe(sub);
}, []);
```
<details><summary>Answer</summary>
Return value is cleanup function. Runs before unmount or before next effect. Essential for subscriptions, timers, listeners.
</details>

## Check 03: Effect timing
When does useEffect run?
<details><summary>Answer</summary>
After render, asynchronously. Not during render. Good for side effects (fetch, subscriptions). For layout effects, use useLayoutEffect.
</details>

## Check 04: Multiple effects
```jsx
useEffect(() => { /* A */ }, [a]);
useEffect(() => { /* B */ }, [b]);
```
<details><summary>Answer</summary>
Each effect runs independently based on its deps. A runs when `a` changes, B when `b` changes. Can have multiple effects.
</details>

## Check 05: Async in useEffect
```jsx
useEffect(() => {
  fetchData(); // async function
}, []);
```
<details><summary>Answer</summary>
Can't make useEffect callback async (must return cleanup or undefined). Call async function inside: `useEffect(() => { fetchData(); }, [])` or use IIFE.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Infinite Loop
```jsx
const [count, setCount] = useState(0);
useEffect(() => {
  setCount(count + 1);
});
```
<details><summary>Answer</summary>
**Bug:** No dependency array — runs after every render. setCount triggers re-render, effect runs again → infinite loop.
**Fix:** Add `[count]` or `[setCount]` dependency.
</details>

## Debug 02 (Medium): Missing Dependency
```jsx
useEffect(() => {
  fetchData(userId);
}, []);
```
<details><summary>Answer</summary>
**Bug:** `userId` not in deps. If userId changes, effect doesn't re-run. Stale data.
**Fix:** `useEffect(() => { fetchData(userId); }, [userId]);`.
</details>

## Debug 03 (Hard): Cleanup Missing
```jsx
useEffect(() => {
  const interval = setInterval(() => console.log("tick"), 1000);
}, []);
```
<details><summary>Answer</summary>
**Bug:** No cleanup — interval keeps running after unmount. Memory leak.
**Fix:** `return () => clearInterval(interval);`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Infinite loop
```jsx
// WRONG — no deps, runs every render
useEffect(() => { setCount(c => c + 1); });
// CORRECT
useEffect(() => { setCount(c => c + 1); }, []);
```

## Mistake 02: Missing dependencies
```jsx
// WRONG — stale data
useEffect(() => { fetch(id); }, []);
// CORRECT
useEffect(() => { fetch(id); }, [id]);
```

## Mistake 03: No cleanup
```jsx
// WRONG — memory leak
useEffect(() => {
  const timer = setInterval(tick, 1000);
}, []);
// CORRECT
useEffect(() => {
  const timer = setInterval(tick, 1000);
  return () => clearInterval(timer);
}, []);
```

## Mistake 04: Async useEffect
```jsx
// WRONG — can't be async
useEffect(async () => { await fetch(); }, []);
// CORRECT
useEffect(() => { fetch(); }, []);
```

## Mistake 05: Over-fetching
```jsx
// WRONG — fetches on every render
useEffect(() => { fetch(); });
// CORRECT — fetch once
useEffect(() => { fetch(); }, []);
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Dependency Array
### Before
```jsx
useEffect(() => { fetchData(); }); // runs every render
```
### After
```jsx
useEffect(() => { fetchData(); }, []); // runs once
```

## Refactor 02 (Medium): Missing Dependency
### Before
```jsx
useEffect(() => { setUser(currentUser); }, []); // stale currentUser
```
### After
```jsx
useEffect(() => { setUser(currentUser); }, [currentUser]);
```

## Refactor 03 (Hard): Effect for Derived Data
### Before
```jsx
const [total, setTotal] = useState(0);
useEffect(() => { setTotal(items.reduce((s, i) => s + i.price, 0)); }, [items]);
```
### After
```jsx
const total = useMemo(() => items.reduce((s, i) => s + i.price, 0), [items]);
```

---

## Approach Comparison — different ways to solve it

## Problem: Fetch on Mount

### Approach 1: useEffect with empty deps
```jsx
useEffect(() => {
  fetch('/api/data').then(setData);
}, []);
```

### Approach 2: React Query
```jsx
const { data } = useQuery('data', () => fetch('/api/data').then(r => r.json()));
```

**Winner:** Approach 2 for production — handles caching, loading, error states. Approach 1 for learning.

---

## Problem: Event Listener

### Approach 1: useEffect
```jsx
useEffect(() => {
  const handler = () => console.log('resize');
  window.addEventListener('resize', handler);
  return () => window.removeEventListener('resize', handler);
}, []);
```

### Approach 2: Custom hook
```jsx
useEventListener('resize', () => console.log('resize'));
```

**Winner:** Approach 2 — reusable, encapsulated.
