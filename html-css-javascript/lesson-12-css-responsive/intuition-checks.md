# Lesson 12 — Intuition Checks

## Check 01: Mobile-first vs desktop-first
Which approach is preferred?
<details><summary>Answer</summary>
Mobile-first — start with mobile styles, add `min-width` media queries for larger screens. Forces simplicity and improves mobile performance.
</details>

## Check 02: viewport meta
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
<details><summary>Answer</summary>
`width=device-width` — sets viewport width to device width. `initial-scale=1.0` — no zoom on load. Essential for responsive design.
</details>

## Check 03: rem vs px in media queries
```css
@media (min-width: 48rem) { }  /* A */
@media (min-width: 768px) { }  /* B */
```
<details><summary>Answer</summary>
Both work. px is more common. rem respects user font size settings but browser support varies in media queries.
</details>

## Check 04: max-width
```css
.container { max-width: 1200px; margin: 0 auto; width: 100%; }
```
<details><summary>Answer</summary>
Container is 100% width up to 1200px, then fixed at 1200px and centered. Standard responsive container pattern.
</details>

## Check 05: responsive images
```css
img { max-width: 100%; height: auto; }
```
<details><summary>Answer</summary>
Images scale down to fit container but never scale up beyond natural size. Essential responsive rule.
</details>
