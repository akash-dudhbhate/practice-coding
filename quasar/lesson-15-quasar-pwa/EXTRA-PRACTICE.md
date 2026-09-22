# lesson-15-quasar-pwa — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: What is PWA?
<details><summary>Answer</summary>
Progressive Web App — installable, offline-capable, push notifications. Works like native app but runs in browser. Quasar builds PWA with `quasar build -m pwa`.
</details>

## Check 02: manifest.json
```javascript
pwa: {
  manifest: {
    name: "My App",
    short_name: "App",
    display: "standalone",
    theme_color: "#000",
    icons: [...]
  }
}
```
<details><summary>Answer</summary>
Controls how PWA appears when installed. Name, icons, theme color, display mode. Essential for installability.
</details>

## Check 03: Service worker
<details><summary>Answer</summary>
Background script that caches files, enables offline. Quasar uses Workbox. `GenerateSW` — auto-generated. `InjectManifest` — custom service worker.
</details>

## Check 04: Installability
<details><summary>Answer</summary>
PWA is installable if: served over HTTPS, has manifest with name + icons + start_url, has service worker, has icons (192px + 512px). Browser shows install prompt.
</details>

## Check 05: Offline support
<details><summary>Answer</summary>
Service worker caches app shell (HTML, CSS, JS). On revisit without network, loads from cache. Data requests may fail — handle gracefully.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01: Missing manifest
```javascript
// quasar.config.js
pwa: { manifest: {} } // empty
```
<details><summary>Answer</summary>
**Bug:** Empty manifest — no app name, icons, theme color. PWA not installable.
**Fix:** Configure name, short_name, icons, theme_color, display.
</details>

## Debug 02: No Service Worker
```javascript
pwa: { workboxPluginMode: null }
```
<details><summary>Answer</summary>
**Bug:** No service worker — no offline support.
**Fix:** Set `workboxPluginMode: "GenerateSW"` or `"InjectManifest"`.
</details>

## Debug 03: Icons Missing
```bash
# No icons in public/icons/
```
<details><summary>Answer</summary>
**Bug:** No app icons — can't install PWA.
**Fix:** Add icons (192x192, 512x512 minimum) in `public/icons/`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Empty manifest
```javascript
// WRONG
pwa: { manifest: {} }
// CORRECT
pwa: { manifest: { name: "App", icons: [...] } }
```

## Mistake 02: No service worker
```javascript
pwa: { workboxPluginMode: "GenerateSW" }
```

## Mistake 03: Missing icons
```bash
# Add 192x192 and 512x512 PNG icons
```

## Mistake 04: Not testing offline
```bash
# DevTools → Application → Service Workers → Offline
# Reload — should still work
```

## Mistake 05: Not using HTTPS
```bash
# PWA requires HTTPS (or localhost for dev)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Empty Manifest
### Before
```javascript
pwa: { manifest: {} }
```
### After
```javascript
pwa: { manifest: { name: "App", icons: [...] } }
```

## Refactor 02 (Medium): No Service Worker
### Before
```javascript
pwa: { workboxPluginMode: null }
```
### After
```javascript
pwa: { workboxPluginMode: "GenerateSW" }
```

## Refactor 03 (Hard: SPA for Installable App
### Before
```bash
quasar build -m spa
```
### After
```bash
quasar build -m pwa
```

---

## Approach Comparison — different ways to solve it

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
