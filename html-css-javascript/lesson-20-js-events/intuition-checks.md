# Lesson 20 — Intuition Checks

## Check 01: Event phases
What are the 3 phases of event propagation?
<details><summary>Answer</summary>
1. Capturing (from root to target)
2. Target (at the element)
3. Bubbling (from target back to root)
Default listeners fire in bubbling phase.
</details>

## Check 02: preventDefault
```javascript
form.addEventListener("submit", (e) => {
  e.preventDefault();
  // handle with JS
});
```
<details><summary>Answer</summary>
Stops the default browser behavior (form submission, link navigation). Lets you handle it with JavaScript.
</details>

## Check 03: Event delegation
```javascript
document.querySelector(".list").addEventListener("click", (e) => {
  if (e.target.matches(".item")) {
    console.log("item clicked");
  }
});
```
<details><summary>Answer</summary>
One listener on parent handles clicks on all children. Better performance than individual listeners. Works for dynamically added elements.
</details>

## Check 04: once option
```javascript
el.addEventListener("click", handler, { once: true });
```
<details><summary>Answer</summary>
Listener auto-removes after first call. Prevents memory leaks for one-time events.
</details>

## Check 05: Custom events
```javascript
const event = new CustomEvent("myEvent", { detail: { data: 123 } });
el.dispatchEvent(event);
```
<details><summary>Answer</summary>
Create and dispatch custom events. Useful for decoupled communication between components.
</details>
