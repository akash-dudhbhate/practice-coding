# Lesson 05 — Debug Exercises

## Debug 01 (Easy): Non-descriptive Link
```html
<a href="/page">Click here</a>
```
<details><summary>Answer</summary>
**Bug:** "Click here" doesn't describe the destination. Screen reader users scanning links hear "click here, click here, click here".
**Fix:** `<a href="/page">Read our privacy policy</a>`.
</details>

## Debug 02 (Medium): Missing ARIA
```html
<div onclick="toggle()">Menu</div>
```
<details><summary>Answer</summary>
**Bug:** Div with onclick isn't keyboard accessible or announced as interactive.
**Fix:** `<button onclick="toggle()" aria-expanded="false">Menu</button>`.
</details>

## Debug 03 (Hard): Missing skip link
```html
<body>
  <nav>...long navigation...</nav>
  <main>Content</main>
</body>
```
<details><summary>Answer</summary>
**Bug:** No skip link — keyboard users must tab through entire nav to reach content.
**Fix:** `<a href="#main" class="skip-link">Skip to content</a>` at the top.
</details>
