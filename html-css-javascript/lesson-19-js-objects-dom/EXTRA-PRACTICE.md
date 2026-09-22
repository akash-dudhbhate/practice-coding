# lesson-19-js-objects-dom — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: querySelector vs querySelectorAll
```javascript
document.querySelector(".box");    // first match
document.querySelectorAll(".box"); // all matches
```
<details><summary>Answer</summary>
`querySelector` returns the first matching element (or null). `querySelectorAll` returns a NodeList of all matches (can be empty).
</details>

## Check 02: innerHTML vs textContent
```javascript
el.innerHTML = "<b>Bold</b>";  // renders as HTML
el.textContent = "<b>Bold</b>"; // shows as text
```
<details><summary>Answer</summary>
`innerHTML` parses HTML (XSS risk with user input). `textContent` treats everything as plain text (safe). Use textContent unless you need HTML.
</details>

## Check 03: classList
```javascript
el.classList.add("active");
el.classList.remove("active");
el.classList.toggle("active");
el.classList.contains("active");
```
<details><summary>Answer</summary>
Modern API for class manipulation. Better than `el.className += " active"` which can add duplicates.
</details>

## Check 04: dataset
```html
<div data-user-id="123"></div>
```
```javascript
el.dataset.userId; // "123"
```
<details><summary>Answer</summary>
`data-*` attributes accessed via `dataset`. Hyphenated names become camelCase: `data-user-id` → `dataset.userId`.
</details>

## Check 05:createElement
```javascript
const div = document.createElement("div");
div.textContent = "Hello";
document.body.appendChild(div);
```
<details><summary>Answer</summary>
Creates an element in memory, then appends to DOM. More efficient than innerHTML for individual elements.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): getElementById vs querySelector
```javascript
const el = document.getElementById(".box");
```
<details><summary>Answer</summary>
**Bug:** `getElementById` takes an ID (no `#`), not a selector. `.box` is a class selector.
**Fix:** `document.querySelector(".box")` or `document.getElementById("box")`.
</details>

## Debug 02 (Medium): innerHTML XSS
```javascript
el.innerHTML = userInput;
```
<details><summary>Answer</summary>
**Bug:** XSS vulnerability — user input is rendered as HTML.
**Fix:** `el.textContent = userInput;`.
</details>

## Debug 03 (Hard): NodeList vs Array
```javascript
const items = document.querySelectorAll(".item");
items.map(x => x.textContent);
```
<details><summary>Answer</summary>
**Bug:** `querySelectorAll` returns a NodeList, not an array. No `.map()`.
**Fix:** `[...items].map(...)` or `Array.from(items).map(...)`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: innerHTML with user input
```javascript
// WRONG — XSS risk
el.innerHTML = userInput;
// CORRECT
el.textContent = userInput;
```

## Mistake 02: Confusing getElementById and querySelector
```javascript
// WRONG — . is for class selectors
document.getElementById(".box");
// CORRECT
document.getElementById("box");     // by ID, no #
document.querySelector(".box");     // CSS selector
```

## Mistake 03: NodeList doesn't have array methods
```javascript
// WRONG
document.querySelectorAll(".x").map(...);
// CORRECT
[...document.querySelectorAll(".x")].map(...);
```

## Mistake 04: className overwriting
```javascript
// WRONG — overwrites all classes
el.className = "active";
// CORRECT — adds to existing
el.classList.add("active");
```

## Mistake 05: Not using textContent
```javascript
// WRONG — slower, parses HTML
el.innerHTML = "Just text";
// CORRECT — faster, safer
el.textContent = "Just text";
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Callback Instead of Promise
### Before
```javascript
navigator.geolocation.getCurrentPosition(pos => { ... });
```
### After
```javascript
const pos = await new Promise((res, rej) =>
  navigator.geolocation.getCurrentPosition(res, rej)
);
```

## Refactor 02 (Medium): Manual Interval
### Before
```javascript
setInterval(() => { if (done) clearInterval(id); }, 1000);
```
### After
```javascript
const check = async () => {
  while (!done) await new Promise(r => setTimeout(r, 1000));
};
```

## Refactor 03 (Hard): No AbortController
### Before
```javascript
const res = await fetch(url); // can't cancel
```
### After
```javascript
const ctrl = new AbortController();
setTimeout(() => ctrl.abort(), 5000);
const res = await fetch(url, { signal: ctrl.signal });
```

---

## Approach Comparison — different ways to solve it

## Problem: Create Element

### Approach 1: innerHTML
```javascript
container.innerHTML = '<div class="card">Hello</div>';
```
**Pros:** Fast for bulk HTML. **Cons:** XSS risk, no event listeners on new elements.

### Approach 2: createElement
```javascript
const div = document.createElement("div");
div.className = "card";
div.textContent = "Hello";
container.appendChild(div);
```
**Pros:** Safe, can attach listeners. **Cons:** Verbose.

**Winner:** Approach 2 for dynamic content. Approach 1 for static templates.

---

## Problem: Select Elements

### Approach 1: getElementById
```javascript
document.getElementById("header");
```

### Approach 2: querySelector
```javascript
document.querySelector("#header");
```

**Winner:** Approach 2 — consistent API, supports any CSS selector.
