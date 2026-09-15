# Lesson 07 — Debug Exercises

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
