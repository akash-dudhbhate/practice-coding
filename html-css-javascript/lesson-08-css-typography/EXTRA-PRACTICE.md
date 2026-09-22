# lesson-08-css-typography — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Units
What's the difference between `em`, `rem`, `px`, `%`?
<details><summary>Answer</summary>
- `px` — absolute pixels
- `em` — relative to parent's font size
- `rem` — relative to root (html) font size
- `%` — relative to parent
</details>

## Check 02: font-weight
```css
.normal { font-weight: 400; }
.bold { font-weight: 700; }
```
<details><summary>Answer</summary>
400 = normal, 700 = bold. Range is 100-900. Not all fonts have all weights.
</details>

## Check 03: line-height units
```css
p { line-height: 1.5; }     /* A */
p { line-height: 1.5em; }   /* B */
p { line-height: 24px; }    /* C */
```
<details><summary>Answer</summary>
A (unitless) is best — inherits as a multiplier. B and C are fixed values that don't scale with font size changes.
</details>

## Check 04: font shorthand
```css
font: bold 16px/1.5 Arial, sans-serif;
```
<details><summary>Answer</summary>
Shorthand: weight, size/line-height, family. Must include size and family. Order matters.
</details>

## Check 05: text-align
```css
.center { text-align: center; }
```
What does this center?
<details><summary>Answer</summary>
Centers inline text within the element. Does NOT center the element itself (use margin: auto or flexbox for that).
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): px for Font Size
```css
body { font-size: 16px; }
```
<details><summary>Answer</summary>
**Issue:** `px` doesn't scale with user's browser font size settings.
**Fix:** Use `rem` — `font-size: 1rem` (16px by default, scales with user settings).
</details>

## Debug 02 (Medium): Line-height Too Tight
```css
p { line-height: 1; }
```
<details><summary>Answer</summary>
**Bug:** line-height: 1 is too tight for readability.
**Fix:** Use 1.5-1.6 for body text (WCAG recommends 1.5).
</details>

## Debug 03 (Hard): Too Many Fonts
```css
body { font-family: Arial, Helvetica, sans-serif; }
h1 { font-family: Georgia, serif; }
h2 { font-family: "Comic Sans MS", cursive; }
```
<details><summary>Answer</summary>
**Bug:** 3 different font families — looks inconsistent and loads slowly.
**Fix:** Use 1-2 font families max. One for headings, one for body.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: px for font size
```css
/* WRONG — doesn't scale */
body { font-size: 16px; }
/* CORRECT */
body { font-size: 1rem; }
```

## Mistake 02: Too many fonts
```css
/* WRONG — 5 font families */
/* CORRECT — 1-2 max */
```

## Mistake 03: Tight line-height
```css
/* WRONG */
p { line-height: 1.1; }
/* CORRECT */
p { line-height: 1.6; }
```

## Mistake 04: Small font size
```css
/* WRONG — hard to read */
.text { font-size: 10px; }
/* CORRECT */
.text { font-size: 0.875rem; } /* 14px */
```

## Mistake 05: Justify text
```css
/* WRONG — creates rivers of whitespace */
p { text-align: justify; }
/* CORRECT — left align for web */
p { text-align: left; }
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): onclick Property
### Before
```javascript
btn.onclick = handleClick;
```
### After
```javascript
btn.addEventListener("click", handleClick);
```

## Refactor 02 (Medium): Many Individual Listeners
### Before
```javascript
document.querySelectorAll(".btn").forEach(b => {
  b.addEventListener("click", handleClick);
});
```
### After
```javascript
document.addEventListener("click", e => {
  if (e.target.matches(".btn")) handleClick(e);
});
```

## Refactor 03 (Hard): No Event Delegation
### Before
```javascript
list.forEach(item => item.addEventListener("click", () => deleteItem(item.id)));
```
### After
```javascript
parent.addEventListener("click", e => {
  const item = e.target.closest(".item");
  if (item) deleteItem(item.dataset.id);
});
```

---

## Approach Comparison — different ways to solve it

## Problem: Responsive Typography

### Approach 1: Media queries
```css
h1 { font-size: 2rem; }
@media (min-width: 768px) { h1 { font-size: 3rem; } }
```

### Approach 2: clamp()
```css
h1 { font-size: clamp(2rem, 5vw, 3rem); }
```

**Winner:** Approach 2 (clamp) — fluid, no breakpoints, scales smoothly.

---

## Problem: Font Loading

### Approach 1: @font-face
```css
@font-face {
  font-family: "Custom";
  src: url("font.woff2") format("woff2");
}
```

### Approach 2: Google Fonts
```html
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
```

**Winner:** Approach 1 for performance (self-host). Approach 2 for convenience.
