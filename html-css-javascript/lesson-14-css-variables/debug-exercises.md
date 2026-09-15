# Lesson 14 — Debug Exercises

## Debug 01 (Easy): Variable Not Defined
```css
.btn { background: var(--primary); }
```
<details><summary>Answer</summary>
**Bug:** `--primary` not defined anywhere.
**Fix:** `:root { --primary: #007bff; }`.
</details>

## Debug 02 (Medium): Wrong Scope
```css
.card { --padding: 20px; }
.btn { padding: var(--padding); }
```
<details><summary>Answer</summary>
**Bug:** `--padding` is scoped to `.card`. `.btn` can't access it.
**Fix:** Define in `:root` or a shared parent.
</details>

## Debug 03 (Hard): No Fallback
```css
.box { color: var(--text-color); }
```
<details><summary>Answer</summary>
**Bug:** If `--text-color` isn't defined, color is invalid (defaults to inherited).
**Fix:** `color: var(--text-color, black)`.
</details>
