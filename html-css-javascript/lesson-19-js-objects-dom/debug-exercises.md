# Lesson 19 — Debug Exercises

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
