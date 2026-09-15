# Lesson 03 — Debug Exercises

## Debug 01 (Easy): Calling Function Immediately
```jsx
<button onClick={handleClick()}>Click</button>
```
<details><summary>Answer</summary>
**Bug:** `handleClick()` is called during render, not on click.
**Fix:** `onClick={handleClick}` (pass reference, don't call).
</details>

## Debug 02 (Medium): Missing Parameter
```jsx
{items.map(item => (
  <button onClick={deleteItem(item.id)}>Delete</button>
))}
```
<details><summary>Answer</summary>
**Bug:** `deleteItem(item.id)` is called immediately during render.
**Fix:** `onClick={() => deleteItem(item.id)}`.
</details>

## Debug 03 (Hard): Synthetic Event Pooling
```jsx
const handleClick = (e) => {
  setTimeout(() => {
    console.log(e.target.value); // may be null
  }, 100);
};
```
<details><summary>Answer</summary>
**Bug:** React reuses synthetic events. `e` is nullified after the handler. (Note: React 17+ doesn't pool events, but older code may have this issue.)
**Fix:** Extract value before async: `const value = e.target.value;`.
</details>
