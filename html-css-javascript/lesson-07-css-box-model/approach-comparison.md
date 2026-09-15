# Lesson 07 — Approach Comparison

## Problem: Center a Div

### Approach 1: margin auto
```css
.box { width: 200px; margin: 0 auto; }
```
**Pros:** Simple, works for horizontal centering. **Cons:** Needs width, doesn't center vertically.

### Approach 2: Flexbox
```css
.parent { display: flex; justify-content: center; align-items: center; }
```
**Pros:** Centers both directions, no width needed. **Cons:** Affects parent.

**Winner:** Approach 2 (flexbox) for most cases. Approach 1 for simple horizontal centering.

---

## Problem: Box Sizing

### Approach 1: content-box (default)
Width = content only. Padding and border add to total.
**Cons:** Unexpected overflow.

### Approach 2: border-box
Width includes padding and border.
**Pros:** Predictable sizing.

**Winner:** Approach 2 — always use `box-sizing: border-box`.
