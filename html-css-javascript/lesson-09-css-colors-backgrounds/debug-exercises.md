# Lesson 09 — Debug Exercises

## Debug 01 (Easy): Invalid Color
```css
.box { color: bluet; }
```
<details><summary>Answer</summary>
**Bug:** Typo "bluet" — invalid color. Property is ignored.
**Fix:** `color: blue` or use hex/rgb.
</details>

## Debug 02 (Medium): Opacity Affects Children
```css
.panel { opacity: 0.5; }
```
<details><summary>Answer</summary>
**Bug:** `opacity` affects the element AND all children. Text becomes hard to read.
**Fix:** Use `rgba()` for background only: `background: rgba(0,0,0,0.5)`.
</details>

## Debug 03 (Hard): Background Not Covering
```css
.hero { background: url("bg.jpg"); height: 500px; }
```
<details><summary>Answer</summary>
**Bug:** Image may not cover the area, leaving gaps or repeating.
**Fix:** `background-size: cover; background-position: center;`.
</details>
