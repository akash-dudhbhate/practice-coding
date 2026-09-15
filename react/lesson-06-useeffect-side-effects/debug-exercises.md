# Lesson 06 — Debug Exercises

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
