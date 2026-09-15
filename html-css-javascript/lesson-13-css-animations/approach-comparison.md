# Lesson 13 — Approach Comparison

## Problem: Hover Effect

### Approach 1: transition
```css
.btn { background: blue; transition: background 200ms; }
.btn:hover { background: darkblue; }
```

### Approach 2: animation
```css
.btn:hover { animation: colorChange 200ms forwards; }
@keyframes colorChange { to { background: darkblue; } }
```

**Winner:** Approach 1 (transition) — simpler for state changes. Use animation for complex sequences.

---

## Problem: Loading Spinner

### Approach 1: CSS animation
```css
.spinner { animation: spin 1s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
```

### Approach 2: JS animation
```javascript
let rotation = 0;
function spin() {
  rotation += 5;
  el.style.transform = `rotate(${rotation}deg)`;
  requestAnimationFrame(spin);
}
```

**Winner:** Approach 1 — CSS is smoother and more efficient.
