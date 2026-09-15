# Lesson 19 — Approach Comparison

## Problem: Create Element

### Approach 1: innerHTML
```javascript
container.innerHTML = '<div class="card">Hello</div>';
```
**Pros:** Fast for bulk HTML. **Cons:** XSS risk, no event listeners on new elements.

### Approach 2: createElement
```javascript
const div = document.createElement("div");
div.className = "card";
div.textContent = "Hello";
container.appendChild(div);
```
**Pros:** Safe, can attach listeners. **Cons:** Verbose.

**Winner:** Approach 2 for dynamic content. Approach 1 for static templates.

---

## Problem: Select Elements

### Approach 1: getElementById
```javascript
document.getElementById("header");
```

### Approach 2: querySelector
```javascript
document.querySelector("#header");
```

**Winner:** Approach 2 — consistent API, supports any CSS selector.
