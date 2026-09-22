# lesson-07-css-box-model — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Box model components
What are the 4 parts of the box model (inside to outside)?
<details><summary>Answer</summary>
content → padding → border → margin. Padding is inside the border (background shows), margin is outside (transparent).
</details>

## Check 02: box-sizing
```css
/* content-box (default) */
width = content width
/* border-box */
width = content + padding + border
```
Which is more intuitive?
<details><summary>Answer</summary>
`border-box` — what you set is what you get. Always use `* { box-sizing: border-box; }` in resets.
</details>

## Check 03: margin: auto
```css
.box { width: 200px; margin: 0 auto; }
```
What does `margin: 0 auto` do?
<details><summary>Answer</summary>
Centers horizontally. `0` = top/bottom margin, `auto` = left/right share remaining space equally. Only works with a defined width.
</details>

## Check 04: display
What's the difference between `block`, `inline`, and `inline-block`?
<details><summary>Answer</summary>
- block — full width, breaks line, can set width/height
- inline — content width, no line break, can't set width/height
- inline-block — content width, no line break, CAN set width/height
</details>

## Check 05: padding shorthand
```css
padding: 10px 20px 30px 40px;
```
Which sides get which values?
<details><summary>Answer</summary>
top 10, right 20, bottom 30, left 40 (clockwise from top). Or `padding: 10px 20px` = top/bottom 10, left/right 20.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Box-sizing Confusion
```css
.box { width: 200px; padding: 20px; border: 1px solid; }
```
**Hint:** What's the total width?
<details><summary>Answer</summary>
**Bug:** Total width is 200 + 20*2 + 1*2 = 242px (default content-box). Unexpected overflow.
**Fix:** `box-sizing: border-box` makes width include padding and border.
</details>

## Debug 02 (Medium): Margin Collapse
```css
.top { margin-bottom: 30px; }
.bottom { margin-top: 20px; }
```
**Hint:** What's the gap between them?
<details><summary>Answer</summary>
**Bug:** Margins collapse — gap is 30px (the larger), not 50px. Vertical margins between adjacent elements collapse.
**Fix:** Use padding, border, or flexbox to avoid collapse.
</details>

## Debug 03 (Hard): Overflow Hidden
```css
.container { overflow: hidden; }
.child { margin-top: 20px; }
```
<details><summary>Answer</summary>
**Bug:** `overflow: hidden` on parent can clip the child's margin. Or the child's margin may collapse with parent.
**Fix:** Use padding-top on parent, or `overflow: auto`, or flexbox.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not using border-box
```css
/* WRONG — width doesn't include padding */
* { box-sizing: content-box; }
/* CORRECT */
* { box-sizing: border-box; }
```

## Mistake 02: Margin collapse surprise
```css
/* Vertical margins collapse — 30px not 50px */
.a { margin-bottom: 30px; }
.b { margin-top: 20px; }
```

## Mistake 03: Using margin for spacing inside
```css
/* WRONG — use padding for internal space */
.box { margin: 20px; }
/* CORRECT */
.box { padding: 20px; }
```

## Mistake 04: Forgetting display
```html
<!-- span can't have width -->
<span style="width: 200px;">Hi</span>
<!-- Fix: use display: inline-block or block -->
```

## Mistake 05: Negative margins
```css
/* AVOID — can cause overlap issues */
.box { margin-top: -20px; }
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): getElementById
### Before
```javascript
document.getElementById("btn");
```
### After
```javascript
document.querySelector("#btn");
```

## Refactor 02 (Medium): Inline Event Handlers
### Before
```html
<button onclick="doSomething()">Click</button>
```
### After
```html
<button id="btn">Click</button>
<script>document.querySelector("#btn").addEventListener("click", doSomething);</script>
```

## Refactor 03 (Hard): Repeated DOM Queries
### Before
```javascript
document.querySelector(".a").style.color = "red";
document.querySelector(".a").style.fontSize = "20px";
document.querySelector(".a").classList.add("active");
```
### After
```javascript
const el = document.querySelector(".a");
el.style.color = "red";
el.style.fontSize = "20px";
el.classList.add("active");
```

---

## Approach Comparison — different ways to solve it

## Problem: Center a Div

### Approach 1: margin auto
```css
.box { width: 200px; margin: 0 auto; }
```
**Pros:** Simple, works for horizontal centering. **Cons:** Needs width, doesn't center vertically.

### Approach 2: Flexbox
```css
.parent { display: flex; justify-content: center; align-items: center; }
```
**Pros:** Centers both directions, no width needed. **Cons:** Affects parent.

**Winner:** Approach 2 (flexbox) for most cases. Approach 1 for simple horizontal centering.

---

## Problem: Box Sizing

### Approach 1: content-box (default)
Width = content only. Padding and border add to total.
**Cons:** Unexpected overflow.

### Approach 2: border-box
Width includes padding and border.
**Pros:** Predictable sizing.

**Winner:** Approach 2 — always use `box-sizing: border-box`.
