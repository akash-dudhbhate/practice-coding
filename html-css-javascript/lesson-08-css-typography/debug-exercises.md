# Lesson 08 — Debug Exercises

## Debug 01 (Easy): px for Font Size
```css
body { font-size: 16px; }
```
<details><summary>Answer</summary>
**Issue:** `px` doesn't scale with user's browser font size settings.
**Fix:** Use `rem` — `font-size: 1rem` (16px by default, scales with user settings).
</details>

## Debug 02 (Medium): Line-height Too Tight
```css
p { line-height: 1; }
```
<details><summary>Answer</summary>
**Bug:** line-height: 1 is too tight for readability.
**Fix:** Use 1.5-1.6 for body text (WCAG recommends 1.5).
</details>

## Debug 03 (Hard): Too Many Fonts
```css
body { font-family: Arial, Helvetica, sans-serif; }
h1 { font-family: Georgia, serif; }
h2 { font-family: "Comic Sans MS", cursive; }
```
<details><summary>Answer</summary>
**Bug:** 3 different font families — looks inconsistent and loads slowly.
**Fix:** Use 1-2 font families max. One for headings, one for body.
</details>
