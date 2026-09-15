# Lesson 15 — Common Mistakes

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
