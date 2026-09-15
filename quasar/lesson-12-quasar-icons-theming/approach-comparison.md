# Lesson 12 — Approach Comparison

## Problem: Theming

### Approach 1: CSS overrides
```css
.q-btn { background: red !important; }
```
**Cons:** Fragile, breaks on updates.

### Approach 2: SCSS variables
```scss
$primary: #ff0000;
```

**Winner:** Approach 2 — official, clean, applies everywhere.

---

## Problem: Dark Mode

### Approach 1: Manual CSS
```css
.dark-theme { background: #000; color: #fff; }
```

### Approach 2: $q.dark
```javascript
$q.dark.set(true);
```

**Winner:** Approach 2 — auto-adapts all components.
