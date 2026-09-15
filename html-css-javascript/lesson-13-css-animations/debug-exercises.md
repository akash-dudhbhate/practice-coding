# Lesson 13 — Debug Exercises

## Debug 01 (Easy): Transition Not Working
```css
.box { transition: width 1s; }
.box:hover { width: 200px; }
```
<details><summary>Answer</summary>
**Bug:** No initial width set. Transition needs a starting value.
**Fix:** `.box { width: 100px; transition: width 1s; }`.
</details>

## Debug 02 (Medium): Animation Not Running
```css
.box { animation: slide 2s; }
```
<details><summary>Answer</summary>
**Bug:** No `@keyframes slide` defined.
**Fix:** Define keyframes: `@keyframes slide { from { transform: translateX(0); } to { transform: translateX(100px); } }`.
</details>

## Debug 03 (Hard): Janky Animation
```css
.box { transition: left 1s; }
.box:hover { left: 100px; }
```
<details><summary>Answer</summary>
**Bug:** Animating `left` triggers layout recalculation — janky.
**Fix:** Animate `transform: translateX(100px)` instead — GPU accelerated, smooth.
</details>
