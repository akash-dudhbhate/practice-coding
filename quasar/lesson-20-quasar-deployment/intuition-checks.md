# Lesson 20 — Intuition Checks

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
