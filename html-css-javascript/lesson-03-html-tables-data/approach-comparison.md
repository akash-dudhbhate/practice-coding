# Lesson 03 — Approach Comparison

## Problem: Data Table

### Approach 1: Basic table
```html
<table>
  <tr><th>Name</th><th>Age</th></tr>
  <tr><td>Akash</td><td>25</td></tr>
</table>
```

### Approach 2: Semantic table
```html
<table>
  <caption>Users</caption>
  <thead>
    <tr><th scope="col">Name</th><th scope="col">Age</th></tr>
  </thead>
  <tbody>
    <tr><td>Akash</td><td>25</td></tr>
  </tbody>
</table>
```

**Winner:** Approach 2 — accessible, semantic, styled easily.

---

## Problem: Responsive Table

### Approach 1: Scroll wrapper
```html
<div style="overflow-x: auto;">
  <table>...</table>
</div>
```

### Approach 2: CSS transform to cards on mobile
```css
@media (max-width: 600px) {
  table, thead, tbody, th, td, tr { display: block; }
  /* restyle as cards */
}
```

**Winner:** Approach 1 for simplicity. Approach 2 for better mobile UX.
