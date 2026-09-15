# Lesson 01 — Approach Comparison

## Problem: Page Layout Structure

### Approach 1: Div soup
```html
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">...</div>
<div class="footer">...</div>
```
**Cons:** No semantic meaning. Bad for accessibility/SEO.

### Approach 2: Semantic HTML5
```html
<header>
  <nav>...</nav>
</header>
<main>...</main>
<footer>...</footer>
```
**Pros:** Meaningful, accessible, better SEO.

**Winner:** Approach 2 — always use semantic HTML5 tags.

---

## Problem: Image with Caption

### Approach 1: Div wrapper
```html
<div class="figure">
  <img src="photo.jpg" alt="Sunset">
  <p class="caption">A beautiful sunset</p>
</div>
```

### Approach 2: figure/figcaption
```html
<figure>
  <img src="photo.jpg" alt="Sunset">
  <figcaption>A beautiful sunset</figcaption>
</figure>
```

**Winner:** Approach 2 — semantic, built for this exact use case.
