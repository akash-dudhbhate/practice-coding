# Lesson 12 — Approach Comparison

## Problem: Responsive Navigation

### Approach 1: Media queries
```css
.nav { display: flex; }
@media (max-width: 768px) {
  .nav { flex-direction: column; }
}
```

### Approach 2: Container queries
```css
@container (min-width: 768px) {
  .nav { flex-direction: row; }
}
```

**Winner:** Approach 2 (container queries) for components. Approach 1 for page layout.

---

## Problem: Responsive Font Size

### Approach 1: Media queries
```css
h1 { font-size: 1.5rem; }
@media (min-width: 768px) { h1 { font-size: 2rem; } }
@media (min-width: 1024px) { h1 { font-size: 3rem; } }
```

### Approach 2: clamp()
```css
h1 { font-size: clamp(1.5rem, 5vw, 3rem); }
```

**Winner:** Approach 2 — fluid, no breakpoints.
