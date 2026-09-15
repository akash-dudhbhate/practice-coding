# Lesson 08 — Debug Exercises

## Debug 01 (Easy: Ref on Wrong Element
```jsx
const inputRef = useRef();
return <input ref={inputRef.value} />;
```
<details><summary>Answer</summary>
**Bug:** `ref` should be the ref object itself, not `.value`.
**Fix:** `<input ref={inputRef} />`.
</details>

## Debug 02 (Medium): Ref in Dependencies
```jsx
const inputRef = useRef();
useEffect(() => {
  inputRef.current.focus();
}, [inputRef]);
```
<details><summary>Answer</summary>
**Issue:** `inputRef` itself doesn't change, only `.current` does. React doesn't track `.current` changes.
**Fix:** Remove from deps: `[]` (run once on mount).
</details>

## Debug 03 (Hard): Ref for State
```jsx
const countRef = useRef(0);
const increment = () => { countRef.current++; };
```
<details><summary>Answer</summary>
**Issue:** Changing ref doesn't trigger re-render. UI won't update. Use `useState` for values that should trigger re-render.
**Fix:** `const [count, setCount] = useState(0);`.
</details>
