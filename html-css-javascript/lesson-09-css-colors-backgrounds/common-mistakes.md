# Lesson 09 — Common Mistakes

## Mistake 01: opacity for backgrounds
```css
/* WRONG — affects children too */
.panel { opacity: 0.5; }
/* CORRECT */
.panel { background: rgba(255,255,255,0.5); }
```

## Mistake 02: No background-size
```css
/* WRONG — image repeats or doesn't cover */
.hero { background: url("bg.jpg"); }
/* CORRECT */
.hero { background: url("bg.jpg") center/cover no-repeat; }
```

## Mistake 03: Hardcoded colors
```css
/* WRONG — repeated everywhere */
.btn { background: #007bff; }
.link { color: #007bff; }
/* CORRECT — use variables */
:root { --primary: #007bff; }
.btn { background: var(--primary); }
```

## Mistake 04: Bad contrast
```css
/* WRONG — unreadable */
.text { color: #ccc; background: #ddd; }
```

## Mistake 05: Too many colors
```css
/* WRONG — rainbow */
/* CORRECT — 3-5 colors max in a palette */
```
