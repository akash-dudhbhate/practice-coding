# lesson-10-css-flexbox — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Main vs Cross axis
In `flex-direction: row`, which is the main axis?
<details><summary>Answer</summary>
Horizontal (row) is main axis. Vertical is cross axis. `justify-content` aligns on main axis, `align-items` on cross axis.
</details>

## Check 02: justify-content
```css
justify-content: space-between;
```
What does this do?
<details><summary>Answer</summary>
First item at start, last at end, equal space between. Other values: `flex-start`, `center`, `space-around`, `space-evenly`.
</details>

## Check 03: flex: 1
```css
.item { flex: 1; }
```
What does `flex: 1` mean?
<details><summary>Answer</summary>
`flex: 1` = `flex: 1 1 0` = grow: 1, shrink: 1, basis: 0. Item grows to fill available space equally with other flex:1 items.
</details>

## Check 04: flex-wrap
```css
.container { display: flex; flex-wrap: wrap; }
```
<details><summary>Answer</summary>
Items wrap to new line when they don't fit. Default is `nowrap` (items shrink to fit).
</details>

## Check 05: gap
```css
.container { display: flex; gap: 20px; }
```
<details><summary>Answer</summary>
Adds 20px gap between flex items. Replaces the old margin hacks for spacing.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Flex Not Working
```css
.container { flex: 1; }
```
<details><summary>Answer</summary>
**Bug:** `flex` on a container doesn't make children flex. Need `display: flex` on parent.
**Fix:** `.container { display: flex; }`.
</details>

## Debug 02 (Medium): Children Not Stretching
```css
.container { display: flex; }
.item { height: 100px; }
```
<details><summary>Answer</summary>
**Bug:** Items don't stretch by default in row direction (align-items: stretch applies to cross axis).
**Fix:** `align-items: stretch` (default) and remove fixed height, or use `align-self: stretch`.
</details>

## Debug 03 (Hard): Flex-shrink Unexpected
```css
.container { display: flex; }
.item { width: 300px; }
```
<details><summary>Answer</summary>
**Bug:** Items shrink to fit container (flex-shrink: 1 by default). Width 300px is a suggestion, not fixed.
**Fix:** `flex-shrink: 0` to prevent shrinking, or use `flex: 0 0 300px`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Forgetting display: flex
```css
/* WRONG — flex properties do nothing */
.container { justify-content: center; }
/* CORRECT */
.container { display: flex; justify-content: center; }
```

## Mistake 02: Using flex for everything
```css
/* Flex is great but not for everything */
/* Use Grid for 2D layouts, Flex for 1D */
```

## Mistake 03: Confusing axes
```css
/* In row direction: */
justify-content: center; /* horizontal center */
align-items: center;     /* vertical center */
```

## Mistake 04: Not using gap
```css
/* WRONG — margin hacks */
.item { margin-right: 20px; }
.item:last-child { margin-right: 0; }
/* CORRECT */
.container { gap: 20px; }
```

## Mistake 05: flex-shrink surprise
```css
/* Items shrink by default */
.item { width: 200px; } /* may be less than 200px */
/* Fix */
.item { flex-shrink: 0; width: 200px; }
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Nested Promises
### Before
```javascript
fetch(url).then(res => {
  fetch(url2).then(res2 => {
    // callback hell
  });
});
```
### After
```javascript
const res1 = await fetch(url);
const res2 = await fetch(url2);
```

## Refactor 02 (Medium): No Error Handling
### Before
```javascript
const data = await fetch(url).then(r => r.json());
```
### After
```javascript
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed");
  const data = await res.json();
} catch (e) { console.error(e); }
```

## Refactor 03 (Hard): Sequential Awaits
### Before
```javascript
const a = await fetch(url1);
const b = await fetch(url2);
```
### After
```javascript
const [a, b] = await Promise.all([fetch(url1), fetch(url2)]);
```

---

## Approach Comparison — different ways to solve it

## Problem: Center Content

### Approach 1: margin auto
```css
.parent { position: relative; }
.child { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```

### Approach 2: Flexbox
```css
.parent { display: flex; justify-content: center; align-items: center; }
```

**Winner:** Approach 2 — one line, no positioning hacks.

---

## Problem: Equal-height Columns

### Approach 1: Fixed height
```css
.col { height: 300px; }
```
**Cons:** Content may overflow.

### Approach 2: Flexbox
```css
.row { display: flex; align-items: stretch; }
```
**Pros:** Columns stretch to tallest. Automatic.

**Winner:** Approach 2 — flexbox makes equal height trivial.
