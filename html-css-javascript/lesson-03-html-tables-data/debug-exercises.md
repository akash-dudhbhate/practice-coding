# Lesson 03 — Debug Exercises

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
