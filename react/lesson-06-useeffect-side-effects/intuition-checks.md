# Lesson 06 — Intuition Checks

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
