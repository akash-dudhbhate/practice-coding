# Lesson 05 — Approach Comparison

## Problem: Interactive Menu

### Approach 1: Div with onclick
```html
<div onclick="toggleMenu()" class="menu">Menu</div>
```
**Cons:** Not keyboard accessible, not announced as interactive.

### Approach 2: Button with ARIA
```html
<button onclick="toggleMenu()" aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" role="menu">...</ul>
```
**Pros:** Keyboard accessible, screen reader friendly.

**Winner:** Approach 2 — always use semantic HTML + ARIA when needed.

---

## Problem: Form Error Messages

### Approach 1: Visual only
```html
<input type="text" class="error">
<span class="error-text">Required</span>
```

### Approach 2: ARIA live
```html
<input type="text" aria-invalid="true" aria-describedby="error">
<span id="error" role="alert">Required</span>
```

**Winner:** Approach 2 — screen readers announce the error.
