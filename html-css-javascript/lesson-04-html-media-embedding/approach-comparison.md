# Lesson 04 — Approach Comparison

## Problem: Responsive Images

### Approach 1: srcset
```html
<img src="small.jpg"
     srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 2000w"
     sizes="(max-width: 600px) 100vw, 50vw"
     alt="Photo">
```

### Approach 2: picture
```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile.jpg">
  <source media="(min-width: 601px)" srcset="desktop.jpg">
  <img src="fallback.jpg" alt="Photo">
</picture>
```

**Winner:** `srcset` for same image at different resolutions. `picture` for different images at different breakpoints or formats.
