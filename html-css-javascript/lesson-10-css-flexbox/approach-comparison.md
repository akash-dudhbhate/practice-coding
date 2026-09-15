# Lesson 10 — Approach Comparison

## Problem: Center Content

### Approach 1: margin auto
```css
.parent { position: relative; }
.child { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```

### Approach 2: Flexbox
```css
.parent { display: flex; justify-content: center; align-items: center; }
```

**Winner:** Approach 2 — one line, no positioning hacks.

---

## Problem: Equal-height Columns

### Approach 1: Fixed height
```css
.col { height: 300px; }
```
**Cons:** Content may overflow.

### Approach 2: Flexbox
```css
.row { display: flex; align-items: stretch; }
```
**Pros:** Columns stretch to tallest. Automatic.

**Winner:** Approach 2 — flexbox makes equal height trivial.
