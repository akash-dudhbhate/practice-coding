# lesson-11-css-grid — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: fr unit
```css
grid-template-columns: 1fr 2fr 1fr;
```
What does `fr` mean?
<details><summary>Answer</summary>
`fr` = fraction of available space. 1fr 2fr 1fr = 25% 50% 25% of the container width.
</details>

## Check 02: Grid vs Flexbox
When should you use Grid vs Flexbox?
<details><summary>Answer</summary>
- Flexbox — 1D layouts (row OR column), content-based sizing
- Grid — 2D layouts (rows AND columns), container-based sizing
Use Grid for page layout, Flexbox for component layout.
</details>

## Check 03: repeat()
```css
grid-template-columns: repeat(3, 1fr);
```
<details><summary>Answer</summary>
Creates 3 equal columns. Equivalent to `1fr 1fr 1fr`. Can use `repeat(auto-fit, minmax(200px, 1fr))` for responsive grids.
</details>

## Check 04: Grid areas
```css
grid-template-areas:
  "header header"
  "sidebar main";
```
<details><summary>Answer</summary>
Names grid cells. Items can be placed with `grid-area: header`. Visual layout in CSS.
</details>

## Check 05: auto-fit vs auto-fill
```css
repeat(auto-fit, minmax(200px, 1fr));  /* A */
repeat(auto-fill, minmax(200px, 1fr)); /* B */
```
<details><summary>Answer</summary>
`auto-fit` stretches items to fill the row. `auto-fill` keeps empty columns. Use auto-fit for responsive cards.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Grid Not Applying
```css
.container { grid-template-columns: 1fr 1fr; }
```
<details><summary>Answer</summary>
**Bug:** Missing `display: grid`. Grid properties do nothing without it.
**Fix:** `.container { display: grid; grid-template-columns: 1fr 1fr; }`.
</details>

## Debug 02 (Medium): Wrong Column Span
```css
.item { grid-column: 1 / 3; }
```
<details><summary>Answer</summary>
**Bug:** This spans columns 1 TO 3 (exclusive), so 2 columns. If you want 3 columns, use `grid-column: 1 / 4` or `grid-column: span 3`.
</details>

## Debug 03 (Hard): Grid Gap Not Working
```css
.container { display: grid; grid-gap: 20px; }
```
<details><summary>Answer</summary>
**Bug:** `grid-gap` is deprecated. Use `gap` (works for both grid and flex).
**Fix:** `.container { display: grid; gap: 20px; }`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Forgetting display: grid
```css
/* WRONG */
.container { grid-template-columns: 1fr 1fr; }
/* CORRECT */
.container { display: grid; grid-template-columns: 1fr 1fr; }
```

## Mistake 02: Using grid-gap
```css
/* DEPRECATED */
grid-gap: 20px;
/* CORRECT */
gap: 20px;
```

## Mistake 03: Overcomplicating with Grid when Flex works
```css
/* For a simple row of items, use Flexbox */
display: flex; gap: 10px;
/* Not Grid */
```

## Mistake 04: Not using minmax for responsive
```css
/* WRONG — fixed columns break on mobile */
grid-template-columns: 300px 300px 300px;
/* CORRECT — responsive */
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
```

## Mistake 05: Hardcoded row heights
```css
/* WRONG */
grid-template-rows: 100px 200px 100px;
/* BETTER — let content determine height */
/* Only set row heights when necessary */
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): .then Chains
### Before
```javascript
fetch(url).then(r => r.json()).then(data => console.log(data));
```
### After
```javascript
const data = await (await fetch(url)).json();
console.log(data);
```

## Refactor 02 (Medium): No try/catch
### Before
```javascript
async function getData() {
  const res = await fetch(url);
  return res.json();
}
```
### After
```javascript
async function getData() {
  try {
    const res = await fetch(url);
    return await res.json();
  } catch (e) { return null; }
}
```

## Refactor 03 (Hard): Sequential Independent Awaits
### Before
```javascript
const user = await getUser();
const posts = await getPosts();
const comments = await getComments();
```
### After
```javascript
const [user, posts, comments] = await Promise.all([
  getUser(), getPosts(), getComments()
]);
```

---

## Approach Comparison — different ways to solve it

## Problem: Card Grid

### Approach 1: Fixed columns
```css
grid-template-columns: 1fr 1fr 1fr;
```
**Cons:** Breaks on mobile — 3 columns too narrow.

### Approach 2: auto-fit
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```
**Pros:** Responsive — 3 columns on desktop, 1 on mobile, no media queries.

**Winner:** Approach 2 — auto-fit is the modern responsive grid.

---

## Problem: Holy Grail Layout

### Approach 1: Flexbox
```css
body { display: flex; }
main { flex: 1; }
```
**Cons:** Complex nesting needed.

### Approach 2: Grid
```css
body {
  display: grid;
  grid-template-areas:
    "header header header"
    "nav main aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 200px;
}
```

**Winner:** Approach 2 — Grid handles 2D layouts elegantly.
