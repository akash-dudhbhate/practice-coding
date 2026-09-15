# Lesson 15 — Approach Comparison

## Problem: Offline Support

### Approach 1: Manual caching
```javascript
// Custom service worker logic
```

### Approach 2: Workbox (Quasar built-in)
```javascript
pwa: { workboxPluginMode: "GenerateSW" }
```

**Winner:** Approach 2 — auto-caches, handles updates.

---

## Problem: Build Target

### Approach 1: SPA only
```bash
quasar build -m spa
```

### Approach 2: PWA
```bash
quasar build -m pwa
```

**Winner:** Approach 2 — installable, offline. Approach 1 if PWA features not needed.
