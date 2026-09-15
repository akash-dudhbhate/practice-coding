# Lesson 15 — Debug Exercises

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
