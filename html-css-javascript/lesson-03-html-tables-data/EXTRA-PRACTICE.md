# lesson-03-html-tables-data — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Table Semantics
What's the difference between `<thead>`, `<tbody>`, `<tfoot>`?
<details><summary>Answer</summary>
- `<thead>` — header rows (column titles)
- `<tbody>` — main data rows
- `<tfoot>` — footer rows (totals, summaries)
Separating them helps with styling and accessibility.
</details>

## Check 02: th vs td
When should you use `<th>`?
<details><summary>Answer</summary>
For headers — row or column labels. `<th>` is bold and centered by default, and announces as "header" to screen readers.
</details>

## Check 03: colspan vs rowspan
```html
<td colspan="3">Spans 3 columns</td>
<td rowspan="2">Spans 2 rows</td>
```
<details><summary>Answer</summary>
`colspan` merges horizontally (across columns). `rowspan` merges vertically (across rows).
</details>

## Check 04: Tables for Layout
Why is using tables for page layout bad?
<details><summary>Answer</summary>
Tables are for tabular DATA. Using them for layout: breaks accessibility, hard to make responsive, harder to maintain, slower to render. Use CSS Flexbox/Grid for layout.
</details>

## Check 05: caption
```html
<table>
  <caption>Sales by Quarter</caption>
  ...
</table>
```
What does `<caption>` do?
<details><summary>Answer</summary>
Provides a title for the table. Screen readers announce it first. Better than a `<h3>` above the table for accessibility.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Missing Table Header
```html
<table>
  <tr>
    <td>Name</td>
    <td>Age</td>
  </tr>
  <tr>
    <td>Akash</td>
    <td>25</td>
  </tr>
</table>
```
<details><summary>Answer</summary>
**Bug:** Headers use `<td>` instead of `<th>`. No semantic distinction.
**Fix:** Use `<th>` for headers, wrap in `<thead>`.
</details>

## Debug 02 (Medium): Wrong Cell Span
```html
<tr>
  <td colspan="2">Merged</td>
  <td>Extra</td>
</tr>
```
<details><summary>Answer</summary>
**Bug:** colspan="2" makes the cell span 2 columns, but there's an extra `<td>`. Total = 3 columns, may misalign.
**Fix:** Remove the extra `<td>` or adjust colspan.
</details>

## Debug 03 (Hard): No Scope
```html
<th>Name</th>
<th>Age</th>
```
<details><summary>Answer</summary>
**Bug:** No `scope` attribute — screen readers can't associate headers with cells.
**Fix:** `<th scope="col">Name</th>`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Tables for layout
```html
<!-- WRONG -->
<table>
  <tr><td class="sidebar">...</td><td class="content">...</td></tr>
</table>

<!-- CORRECT — use CSS -->
<div class="layout">
  <aside>...</aside>
  <main>...</main>
</div>
```

## Mistake 02: Missing th scope
```html
<!-- WRONG -->
<th>Name</th>

<!-- CORRECT -->
<th scope="col">Name</th>
```

## Mistake 03: No thead/tbody
```html
<!-- WRONG — all in one block -->
<table>
  <tr><th>A</th></tr>
  <tr><td>1</td></tr>
</table>

<!-- CORRECT -->
<table>
  <thead><tr><th>A</th></tr></thead>
  <tbody><tr><td>1</td></tr></tbody>
</table>
```

## Mistake 04: Forgetting caption
```html
<!-- Add caption for accessibility -->
<table>
  <caption>Monthly Sales</caption>
  ...
</table>
```

## Mistake 05: Not handling responsive tables
```html
<!-- Tables overflow on mobile — wrap in a scroll container -->
<div style="overflow-x: auto;">
  <table>...</table>
</div>
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Float for Layout
### Before
```css
.sidebar { float: left; width: 30%; }
.main { float: right; width: 70%; }
.clearfix::after { content: ""; clear: both; display: table; }
```
### After
```css
.container { display: flex; }
.sidebar { flex: 0 0 30%; }
.main { flex: 1; }
```

## Refactor 02 (Medium): Manual Centering
### Before
```css
.center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```
### After
```css
.parent { display: flex; justify-content: center; align-items: center; }
```

## Refactor 03 (Hard): Fixed Widths
### Before
```css
.col1 { width: 200px; }
.col2 { width: 400px; }
.col3 { width: 600px; }
```
### After
```css
.row { display: flex; gap: 16px; }
.col { flex: 1; }

---

## Approach Comparison — different ways to solve it

## Problem: Data Table

### Approach 1: Basic table
```html
<table>
  <tr><th>Name</th><th>Age</th></tr>
  <tr><td>Akash</td><td>25</td></tr>
</table>
```

### Approach 2: Semantic table
```html
<table>
  <caption>Users</caption>
  <thead>
    <tr><th scope="col">Name</th><th scope="col">Age</th></tr>
  </thead>
  <tbody>
    <tr><td>Akash</td><td>25</td></tr>
  </tbody>
</table>
```

**Winner:** Approach 2 — accessible, semantic, styled easily.

---

## Problem: Responsive Table

### Approach 1: Scroll wrapper
```html
<div style="overflow-x: auto;">
  <table>...</table>
</div>
```

### Approach 2: CSS transform to cards on mobile
```css
@media (max-width: 600px) {
  table, thead, tbody, th, td, tr { display: block; }
  /* restyle as cards */
}
```

**Winner:** Approach 1 for simplicity. Approach 2 for better mobile UX.
