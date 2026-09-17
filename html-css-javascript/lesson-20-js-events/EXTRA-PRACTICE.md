# lesson-20-js-events — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Inline event handlers
```html
<!-- WRONG — mixes HTML and JS -->
<button onclick="handleClick()">
<!-- CORRECT -->
<button id="myBtn">
<script>
document.getElementById("myBtn").addEventListener("click", handleClick);
</script>
```

## Mistake 02: Not using event delegation
```javascript
// WRONG — listener per item
items.forEach(item => item.addEventListener("click", handler));
// CORRECT — one listener on parent
list.addEventListener("click", (e) => {
  if (e.target.matches(".item")) handler(e);
});
```

## Mistake 03: Memory leaks
```javascript
// WRONG — never removed
el.addEventListener("click", handler);
// CORRECT — remove when done
el.removeEventListener("click", handler);
// or use { once: true }
```

## Mistake 04: Forgetting preventDefault
```javascript
// WRONG — form submits and reloads page
form.addEventListener("submit", () => {
  saveData();
});
// CORRECT
form.addEventListener("submit", (e) => {
  e.preventDefault();
  saveData();
});
```

## Mistake 05: Not checking event target
```javascript
// WRONG — fires for any click in container
container.addEventListener("click", handler);
// CORRECT — check what was actually clicked
container.addEventListener("click", (e) => {
  if (e.target.matches(".button")) handler(e);
});
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Project Structure
### Before
```html
<!-- index.html with all CSS and JS inline -->
<style>/* 500 lines */</style>
<script>/* 800 lines */</script>
```
### After
```html
<link rel="stylesheet" href="styles.css">
<script type="module" src="app.js"></script>
```

## Refactor 02 (Medium): Spaghetti Code
### Before
```javascript
function handleEverything() {
  fetchData();
  updateUI();
  saveToStorage();
  sendAnalytics();
}
```
### After
```javascript
async function loadAndDisplay() { await fetchData(); updateUI(); }
async function saveAndTrack() { saveToStorage(); sendAnalytics(); }
```

## Refactor 03 (Hard): No Build Tool
### Before
```html
<script src="lib1.js"></script>
<script src="lib2.js"></script>
<script src="lib3.js"></script>
<script src="app.js"></script>
```
### After
```bash
# Use Vite or similar
npm create vite@min
# imports bundled automatically
```

---

## Approach Comparison — different ways to solve it

## Problem: Handle Button Clicks

### Approach 1: Individual listeners
```javascript
buttons.forEach(btn => btn.addEventListener("click", handler));
```
**Cons:** New buttons need new listeners. Performance issues with many buttons.

### Approach 2: Event delegation
```javascript
container.addEventListener("click", (e) => {
  if (e.target.matches(".btn")) handler(e);
});
```
**Pros:** One listener, works for dynamically added buttons.

**Winner:** Approach 2 — event delegation is more efficient and flexible.

---

## Problem: Form Submission

### Approach 1: Submit button click
```javascript
submitBtn.addEventListener("click", validateForm);
```
**Cons:** Doesn't handle Enter key submission.

### Approach 2: Form submit event
```javascript
form.addEventListener("submit", (e) => {
  e.preventDefault();
  validateForm();
});
```
**Pros:** Handles all submission methods (button, Enter key).

**Winner:** Approach 2 — always listen on form submit, not button click.
