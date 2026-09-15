# Lesson 15 — Debug Exercises

## Debug 01 (Easy: Modal Inside Component Tree
```jsx
function App() {
  return (
    <div style={{ overflow: "hidden" }}>
      <Modal /> {/* can't overflow parent */}
    </div>
  );
}
```
<details><summary>Answer</summary>
**Bug:** Modal is trapped inside `overflow: hidden` parent. May be clipped.
**Fix:** Use Portal to render at document.body level.
</details>

## Debug 02 (Medium): Portal Without DOM Node
```jsx
return ReactDOM.createPortal(<Modal />, document.getElementById("modal-root"));
// modal-root div doesn't exist
```
<details><summary>Answer</summary>
**Bug:** `getElementById` returns null. `createPortal` throws.
**Fix:** Ensure `<div id="modal-root"></div>` exists in HTML, or create it dynamically.
</details>

## Debug 03 (Hard): Event Bubbling Through Portals
```jsx
<div onClick={() => console.log("parent")}>
  {ReactDOM.createPortal(<button onClick={handleClick}>Click</button>, document.body)}
</div>
```
<details><summary>Answer</summary>
**Note:** Portal events bubble through React tree (not DOM tree). Clicking button triggers parent's onClick in React, even though DOM-wise they're separate.
</details>
