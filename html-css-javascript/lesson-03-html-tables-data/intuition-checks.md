# Lesson 03 — Intuition Checks

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
