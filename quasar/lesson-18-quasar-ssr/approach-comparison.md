# Lesson 18 — Approach Comparison

## Problem: SEO

### Approach 1: SPA
```bash
quasar build -m spa
```
**Cons:** Poor SEO — content loaded by JS.

### Approach 2: SSR
```bash
quasar build -m ssr
```

**Winner:** Approach 2 — HTML in source, good SEO.

---

## Problem: Browser APIs

### Approach 1: process.env check
```javascript
if (process.env.CLIENT) { window... }
```

### Approach 2: onMounted
```javascript
onMounted(() => { window... });
```

**Winner:** Approach 2 — cleaner, guaranteed browser.
