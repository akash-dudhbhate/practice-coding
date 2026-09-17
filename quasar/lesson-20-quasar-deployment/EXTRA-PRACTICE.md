# lesson-20-quasar-deployment — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Build modes
<details><summary>Answer</summary>
SPA — single page app (default). SSR — server-side rendering. PWA — progressive web app. Capacitor — mobile. Electron — desktop. Each has different deployment.
</details>

## Check 02: Build output
```bash
quasar build -m spa
# Output: dist/spa/
```
<details><summary>Answer</summary>
`dist/spa/` contains static files. Deploy to any static host (Netlify, Vercel, GitHub Pages, S3). For SSR: `dist/ssr/` needs Node.js server.
</details>

## Check 03: Environment files
```bash
.env                # all environments
.env.development    # quasar dev
.env.production     # quasar build
```
<details><summary>Answer</summary>
Different env files for different modes. VITE_ prefix required. Loaded automatically based on mode.
</details>

## Check 04: Deployment targets
<details><summary>Answer</summary>
SPA/PWA — static hosting (Netlify, Vercel, GitHub Pages, S3, Nginx). SSR — Node.js server (Heroku, Railway, VPS). Capacitor — app stores (Google Play, App Store). Electron — installer download.
</details>

## Check 05: CI/CD
```yaml
# GitHub Actions example
- run: npm install
- run: npx quasar build -m spa
- uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./dist/spa
```
<details><summary>Answer</summary>
Automate build and deploy. Push to main → build → deploy. Each platform has its own deploy action.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01: Wrong Build Mode
```bash
quasar build  # defaults to SPA, but need PWA
```
<details><summary>Answer</summary>
**Bug:** Default mode is SPA. Need to specify.
**Fix:** `quasar build -m pwa` or `quasar build -m ssr`.
</details>

## Debug 02: Environment Variables Not Set
```bash
quasar build
# VITE_API_URL not set — uses undefined
```
<details><summary>Answer</summary>
**Bug:** Env vars not configured for production.
**Fix:** Create `.env.production` with `VITE_API_URL=https://api.example.com`.
</details>

## Debug 03: No Base Path
```javascript
// Deploying to subdirectory: example.com/app/
// Assets load from root — 404
```
<details><summary>Answer</summary>
**Bug:** Base path not configured for subdirectory deployment.
**Fix:** `build: { publicPath: "/app/" }` in quasar.config.js.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Wrong Build Mode
### Before
```bash
quasar build
```
### After
```bash
quasar build -m pwa
```

## Refactor 02 (Medium): No .env.production
### Before
```bash
quasar build  # uses dev env vars
```
### After
```bash
# create .env.production
quasar build
```

## Refactor 03 (Hard: Manual Deploy
### Before
```bash
quasar build && scp dist/spa/* server:
```
### After
```yaml
# CI/CD pipeline
- run: quasar build -m spa
- uses: deploy-action
```

---

## Approach Comparison — different ways to solve it

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
