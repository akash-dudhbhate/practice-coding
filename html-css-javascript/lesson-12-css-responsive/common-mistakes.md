# Lesson 12 — Common Mistakes

## Mistake 01: No viewport meta
```html
<!-- WRONG — site looks tiny on mobile -->
<!-- CORRECT -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Mistake 02: Fixed widths
```css
/* WRONG */
.container { width: 1200px; }
/* CORRECT */
.container { max-width: 1200px; width: 100%; }
```

## Mistake 03: Desktop-first media queries
```css
/* WRONG — desktop then override for mobile */
.box { font-size: 18px; }
@media (max-width: 768px) { .box { font-size: 14px; } }
/* CORRECT — mobile first */
.box { font-size: 14px; }
@media (min-width: 768px) { .box { font-size: 18px; } }
```

## Mistake 04: Not testing on real devices
```css
/* Always test on actual phones, not just browser dev tools */
```

## Mistake 05: Forgetting responsive images
```css
/* WRONG — images overflow */
img { width: 800px; }
/* CORRECT */
img { max-width: 100%; height: auto; }
```
