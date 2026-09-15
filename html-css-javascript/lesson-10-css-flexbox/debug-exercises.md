# Lesson 10 — Debug Exercises

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
