# Lesson 18 — Approach Comparison

## Problem: Button Styles

### Approach 1: Utility classes
```jsx
<button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
```

### Approach 2: @apply in CSS
```css
.btn { @apply bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600; }
```
```jsx
<button className="btn">
```

### Approach 3: Component
```jsx
function Button({ children }) {
  return <button className="bg-blue-500 ...">{children}</button>;
}
```

**Winner:** Approach 3 for reusable buttons. Approach 1 for one-off styling.

---

## Problem: Responsive Design

### Approach 1: Tailwind responsive prefixes
```jsx
<div className="grid grid-cols-1 md:grid-cols-3">
```

### Approach 2: Custom CSS media queries
```css
@media (min-width: 768px) { .grid { grid-template-columns: repeat(3, 1fr); } }
```

**Winner:** Approach 1 — faster, consistent.
