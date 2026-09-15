# Lesson 20 — Common Mistakes

## Mistake 01: Wrong build mode
```bash
# WRONG
quasar build
# CORRECT
quasar build -m pwa  # or ssr, capacitor, electron
```

## Mistake 02: No .env.production
```bash
# Create .env.production with production URLs
VITE_API_URL=https://api.example.com
```

## Mistake 03: Wrong publicPath
```javascript
// For subdirectory deployment
build: { publicPath: "/my-app/" }
```

## Mistake 04: Not testing production build
```bash
# Always test: quasar build && npx serve dist/spa
```

## Mistake 05: No SPA fallback
```javascript
// Hosting must redirect all routes to index.html
// Netlify: _redirects file → /* /index.html 200
```
