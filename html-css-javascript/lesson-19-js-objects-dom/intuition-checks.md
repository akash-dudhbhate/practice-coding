# Lesson 19 — Intuition Checks

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
