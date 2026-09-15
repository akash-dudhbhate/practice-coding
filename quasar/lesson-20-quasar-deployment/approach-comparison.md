# Lesson 20 — Approach Comparison

## Problem: Deploy SPA

### Approach 1: Manual
```bash
quasar build -m spa
# upload dist/spa/ to server
```

### Approach 2: CI/CD
```yaml
- run: quasar build -m spa
- uses: deploy-action
```

**Winner:** Approach 2 — automated, consistent.

---

## Problem: Hosting

### Approach 1: Static hosting
```bash
# Netlify, Vercel, GitHub Pages
# Free, easy, CDN included
```

### Approach 2: VPS
```bash
# Full control, can run SSR
# More maintenance
```

**Winner:** Approach 1 for SPA/PWA. Approach 2 for SSR.
