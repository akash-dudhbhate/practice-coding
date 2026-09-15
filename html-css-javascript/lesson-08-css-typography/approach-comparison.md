# Lesson 08 — Approach Comparison

## Problem: Responsive Typography

### Approach 1: Media queries
```css
h1 { font-size: 2rem; }
@media (min-width: 768px) { h1 { font-size: 3rem; } }
```

### Approach 2: clamp()
```css
h1 { font-size: clamp(2rem, 5vw, 3rem); }
```

**Winner:** Approach 2 (clamp) — fluid, no breakpoints, scales smoothly.

---

## Problem: Font Loading

### Approach 1: @font-face
```css
@font-face {
  font-family: "Custom";
  src: url("font.woff2") format("woff2");
}
```

### Approach 2: Google Fonts
```html
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
```

**Winner:** Approach 1 for performance (self-host). Approach 2 for convenience.
