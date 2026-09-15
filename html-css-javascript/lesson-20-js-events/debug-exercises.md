# Lesson 20 — Debug Exercises

## Debug 01 (Easy): Event Listener Not Working
```javascript
document.querySelector(".btn").addEventListener("click", handleClick);
function handleClick() {
  console.log("clicked");
}
```
<details><summary>Answer</summary>
Works — function declarations are hoisted. But if using `const handleClick = () => {}`, it must be defined before the listener.
</details>

## Debug 02 (Medium): Event Bubbling
```javascript
document.querySelector(".parent").addEventListener("click", () => {
  console.log("parent");
});
document.querySelector(".child").addEventListener("click", () => {
  console.log("child");
});
```
<details><summary>Answer</summary>
Clicking child logs "child" then "parent" (bubbling). To stop: `e.stopPropagation()` in child handler.
</details>

## Debug 03 (Hard): Memory Leak
```javascript
function setup() {
  const el = document.querySelector(".btn");
  el.addEventListener("click", () => {
    console.log("clicked");
  });
}
// el removed from DOM, but listener still references it
```
<details><summary>Answer</summary>
**Bug:** Listener holds reference to element — memory leak if element is removed.
**Fix:** `removeEventListener` when done, or use `{ once: true }` for one-time listeners.
</details>
