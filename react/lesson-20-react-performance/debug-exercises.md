# Lesson 20 — Debug Exercises

## Debug 01 (Easy: React.memo Without Stable Props
```jsx
const MemoChild = React.memo(Child);
<MemoChild onClick={() => handleClick()} style={{ color: "red" }} />
```
<details><summary>Answer</summary>
**Bug:** New function and object every render → memo is useless (props always "change").
**Fix:** `useCallback` for onClick, `useMemo` for style.
</details>

## Debug 02 (Medium): Large Bundle
```jsx
import _ from "lodash"; // imports entire lodash
```
<details><summary>Answer</summary>
**Bug:** Imports entire lodash (~70KB). Most of it unused.
**Fix:** `import debounce from "lodash/debounce";` — imports only what's needed.
</details>

## Debug 03 (Hard): Unnecessary Re-renders
```jsx
function Parent() {
  const [count, setCount] = useState(0);
  return <div><ExpensiveChild /><button onClick={() => setCount(c => c + 1)}>{count}</button></div>;
}
```
<details><summary>Answer</summary>
**Bug:** ExpensiveChild re-renders when count changes (Parent re-renders).
**Fix:** Wrap ExpensiveChild in `React.memo`, or move count state to the button component.
</details>
