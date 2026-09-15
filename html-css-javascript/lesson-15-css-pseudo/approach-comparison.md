# Lesson 15 — Approach Comparison

## Problem: Focus Styles

### Approach 1: :focus
```css
*:focus { outline: 2px solid blue; }
```
**Cons:** Shows outline on mouse click too.

### Approach 2: :focus-visible
```css
*:focus-visible { outline: 2px solid blue; }
```
**Pros:** Only keyboard users get outline.

**Winner:** Approach 2 — better UX for mouse users.

---

## Problem: Clearfix

### Approach 1: ::after clearfix
```css
.clearfix::after { content: ""; display: table; clear: both; }
```

### Approach 2: Use flexbox/grid
```css
.parent { display: flow-root; }
/* or */
.parent { display: flex; }
```

**Winner:** Approach 2 — modern CSS makes clearfix obsolete.
