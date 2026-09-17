# lesson-15-css-pseudo — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: :hover vs :focus
Why do you need :focus styles?
<details><summary>Answer</summary>
Keyboard users navigate with Tab. `:focus` shows where they are. `:hover` only works with mouse. Always provide `:focus` (or `:focus-visible`).
</details>

## Check 02: ::before and ::after
```css
.quote::before { content: "\""; }
.quote::after { content: "\""; }
```
<details><summary>Answer</summary>
Adds quotation marks before and after. Pseudo-elements create virtual elements. Need `content` property to render.
</details>

## Check 03: :nth-child vs :nth-of-type
```css
li:nth-child(2) { }     /* A */
li:nth-of-type(2) { }   /* B */
```
<details><summary>Answer</summary>
A — 2nd child of its parent (regardless of type). B — 2nd `<li>` of its parent. Use nth-of-type when parent has mixed element types.
</details>

## Check 04: :not()
```css
a:not(.external) { color: blue; }
```
<details><summary>Answer</summary>
Styles all links EXCEPT those with class "external". Useful for exceptions.
</details>

## Check 05: :focus-visible
```css
:focus { outline: 2px solid blue; }        /* A */
:focus-visible { outline: 2px solid blue; } /* B */
```
<details><summary>Answer</summary>
`:focus` shows outline for ALL focus (mouse click too). `:focus-visible` only shows for keyboard focus. B is better — no outline for mouse users.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): :hover on non-interactive
```css
div:hover { cursor: pointer; }
```
<details><summary>Answer</summary>
**Issue:** Hover on div doesn't work on touch devices. Also, div isn't keyboard accessible.
**Fix:** Use `<button>` or add `tabindex` and `:focus` styles.
</details>

## Debug 02 (Medium): ::before without content
```css
.box::before { display: block; width: 100px; height: 100px; background: red; }
```
<details><summary>Answer</summary>
**Bug:** `::before` needs `content: ""` to render, even if empty.
**Fix:** Add `content: "";`.
</details>

## Debug 03 (Hard): :nth-child confusion
```css
li:nth-child(2n) { background: gray; }
```
<details><summary>Answer</summary>
This styles EVEN children (2nd, 4th, 6th...). For odd, use `2n+1` or `odd`. Common confusion: `nth-child` counts ALL siblings, not just the type.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: No :focus styles
```css
/* WRONG — keyboard users lost */
.btn:hover { background: blue; }
/* CORRECT */
.btn:hover, .btn:focus { background: blue; }
```

## Mistake 02: ::before without content
```css
/* WRONG — doesn't render */
.box::before { width: 100px; }
/* CORRECT */
.box::before { content: ""; width: 100px; }
```

## Mistake 03: Removing outline
```css
/* WRONG */
*:focus { outline: none; }
/* CORRECT — provide alternative */
*:focus-visible { outline: 2px solid blue; }
```

## Mistake 04: :nth-child confusion
```css
/* nth-child counts ALL siblings, not just <li> */
/* If there's an <h1> before <li>s, nth-child(1) is the <h1> */
```

## Mistake 05: Overusing ::before/::after
```css
/* Don't use pseudo-elements for important content */
/* Screen readers may not announce them */
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Script Tags
### Before
```html
<script src="utils.js"></script>
<script src="api.js"></script>
<script src="app.js"></script>
```
### After
```html
<script type="module" src="app.js"></script>
<!-- app.js: import { utils } from "./utils.js"; -->
```

## Refactor 02 (Medium): Global Variables
### Before
```javascript
// utils.js
window.utils = { helper() { ... } };
// app.js
window.utils.helper();
```
### After
```javascript
// utils.js
export function helper() { ... }
// app.js
import { helper } from "./utils.js";
```

## Refactor 03 (Hard): Default Export Confusion
### Before
```javascript
export default { foo, bar, baz };
// import * as utils from "./utils"; utils.default.foo
```
### After
```javascript
export { foo, bar, baz };
// import { foo } from "./utils";
```

---

## Approach Comparison — different ways to solve it

## Problem: Focus Styles

### Approach 1: :focus
```css
*:focus { outline: 2px solid blue; }
```
**Cons:** Shows outline on mouse click too.

### Approach 2: :focus-visible
```css
*:focus-visible { outline: 2px solid blue; }
```
**Pros:** Only keyboard users get outline.

**Winner:** Approach 2 — better UX for mouse users.

---

## Problem: Clearfix

### Approach 1: ::after clearfix
```css
.clearfix::after { content: ""; display: table; clear: both; }
```

### Approach 2: Use flexbox/grid
```css
.parent { display: flow-root; }
/* or */
.parent { display: flex; }
```

**Winner:** Approach 2 — modern CSS makes clearfix obsolete.
