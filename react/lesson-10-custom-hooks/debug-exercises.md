# Lesson 10 — Debug Exercises

## Debug 01 (Easy: Hook Outside Component
```jsx
function useCounter() { ... }
const count = useCounter(); // at module level
```
<details><summary>Answer</summary>
**Bug:** Hooks can only be called inside components or other hooks.
**Fix:** Call inside a component: `function App() { const count = useCounter(); }`.
</details>

## Debug 02 (Medium): Conditional Hook
```jsx
function useData(enabled) {
  if (enabled) {
    const [data, setData] = useState(null);
  }
}
```
<details><summary>Answer</summary>
**Bug:** Hooks can't be conditional — violates Rules of Hooks.
**Fix:** Always call the hook, conditionally use the value: `const [data, setData] = useState(null); if (!enabled) return null;`.
</details>

## Debug 03 (Hard): Hook Not Returning Value
```jsx
function useFetch(url) {
  useEffect(() => {
    fetch(url).then(setData);
  }, [url]);
}
```
<details><summary>Answer</summary>
**Bug:** Hook doesn't return anything. Useless to caller.
**Fix:** `return { data, loading, error };`.
</details>
