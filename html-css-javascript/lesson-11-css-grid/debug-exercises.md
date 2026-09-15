# Lesson 11 — Debug Exercises

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
