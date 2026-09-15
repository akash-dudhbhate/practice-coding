# Lesson 06 — Approach Comparison

## Problem: Style Navigation Links

### Approach 1: Deep selector
```css
header nav ul li a { color: blue; }
```
**Cons:** Brittle — any HTML change breaks it.

### Approach 2: Class
```css
.nav-link { color: blue; }
```
**Pros:** Decoupled from HTML structure.

**Winner:** Approach 2 — classes are more maintainable.

---

## Problem: Override a Style

### Approach 1: !important
```css
.text { color: red !important; }
```
**Cons:** Creates arms race.

### Approach 2: Increase specificity
```css
.parent .text { color: red; }
```

**Winner:** Approach 2 — manage specificity, don't use !important.
