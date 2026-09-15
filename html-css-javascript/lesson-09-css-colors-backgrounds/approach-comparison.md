# Lesson 09 — Approach Comparison

## Problem: Semi-transparent Background

### Approach 1: opacity
```css
.panel { opacity: 0.5; }
```
**Cons:** Makes text transparent too.

### Approach 2: rgba
```css
.panel { background: rgba(0,0,0,0.5); }
```
**Pros:** Only background is transparent.

**Winner:** Approach 2 — use rgba for transparent backgrounds.

---

## Problem: Color Theming

### Approach 1: Hardcoded
```css
.btn { background: #007bff; }
```
**Cons:** Hard to change, no consistency.

### Approach 2: CSS variables
```css
:root { --primary: #007bff; }
.btn { background: var(--primary); }
```

**Winner:** Approach 2 — variables enable theming and consistency.
