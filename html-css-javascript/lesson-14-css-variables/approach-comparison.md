# Lesson 14 — Approach Comparison

## Problem: Theming

### Approach 1: Multiple stylesheets
```html
<link rel="stylesheet" href="light.css">
<link rel="stylesheet" href="dark.css" disabled>
```

### Approach 2: CSS variables
```css
:root { --bg: white; --text: black; }
[data-theme="dark"] { --bg: black; --text: white; }
body { background: var(--bg); color: var(--text); }
```

**Winner:** Approach 2 — switch themes by changing one attribute. No stylesheet swapping.

---

## Problem: Spacing System

### Approach 1: Hardcoded
```css
.margin-sm { margin: 8px; }
.margin-md { margin: 16px; }
```

### Approach 2: Variables
```css
:root { --space-sm: 8px; --space-md: 16px; }
.box { margin: var(--space-md); }
```

**Winner:** Approach 2 — change one variable to update all spacing.
