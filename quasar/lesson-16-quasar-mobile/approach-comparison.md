# Lesson 16 — Approach Comparison

## Problem: Mobile App

### Approach 1: Responsive web
```bash
quasar build -m spa
```
**Cons:** No native features, no app store.

### Approach 2: Capacitor
```bash
quasar build -m capacitor -T android
```

**Winner:** Approach 2 for native features/app store. Approach 1 for web-only.

---

## Problem: Platform-Specific UI

### Approach 1: CSS media queries
```css
@media (max-width: 600px) { ... }
```

### Approach 2: $q.platform
```javascript
:class="{ 'mobile-layout': $q.platform.is.mobile }"
```

**Winner:** Use both. CSS for styling, $q for logic.
