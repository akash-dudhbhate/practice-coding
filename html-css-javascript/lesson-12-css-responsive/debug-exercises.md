# Lesson 12 — Debug Exercises

## Debug 01 (Easy): Missing viewport meta
```html
<head>
  <title>My Site</title>
</head>
```
<details><summary>Answer</summary>
**Bug:** No viewport meta tag — site doesn't scale on mobile.
**Fix:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
</details>

## Debug 02 (Medium): Fixed Width
```css
.container { width: 1200px; }
```
<details><summary>Answer</summary>
**Bug:** Fixed width overflows on screens < 1200px.
**Fix:** `max-width: 1200px; width: 100%;`.
</details>

## Debug 03 (Hard): Media Query Order
```css
@media (max-width: 768px) { .box { font-size: 14px; } }
@media (min-width: 1024px) { .box { font-size: 18px; } }
/* What size on a 500px screen? */
```
<details><summary>Answer</summary>
14px — only the max-width: 768px query applies. But on 1024px+, both could apply if not careful. Order matters: mobile-first should use min-width in ascending order.
</details>
