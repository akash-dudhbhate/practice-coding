# Lesson 11 — Approach Comparison

## Problem: Card Grid

### Approach 1: Fixed columns
```css
grid-template-columns: 1fr 1fr 1fr;
```
**Cons:** Breaks on mobile — 3 columns too narrow.

### Approach 2: auto-fit
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```
**Pros:** Responsive — 3 columns on desktop, 1 on mobile, no media queries.

**Winner:** Approach 2 — auto-fit is the modern responsive grid.

---

## Problem: Holy Grail Layout

### Approach 1: Flexbox
```css
body { display: flex; }
main { flex: 1; }
```
**Cons:** Complex nesting needed.

### Approach 2: Grid
```css
body {
  display: grid;
  grid-template-areas:
    "header header header"
    "nav main aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 200px;
}
```

**Winner:** Approach 2 — Grid handles 2D layouts elegantly.
