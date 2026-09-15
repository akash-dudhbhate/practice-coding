# Quasar SPA Deployment Guide

## Prerequisites
- Node.js 18+ and npm
- Quasar CLI: `npm i -g @quasar/cli`
- A built Quasar SPA project

## Build Command
```bash
quasar build -m spa
```
Output directory: `dist/spa/`

---

## Deployment Platforms

### 1. Netlify
1. Run `quasar build -m spa`
2. Go to [netlify.com](https://netlify.com) → New site from Git
3. Connect your repository
4. Build command: `quasar build -m spa`
5. Publish directory: `dist/spa`
6. Add `public/_redirects` with `/* /index.html 200` (for SPA routing)
7. Deploy

### 2. Vercel
1. Run `quasar build -m spa`
2. Go to [vercel.com](https://vercel.com) → New Project
3. Import your repository
4. Build command: `quasar build -m spa`
5. Output directory: `dist/spa`
6. Add `vercel.json` with rewrites to `index.html` (for SPA routing)
7. Deploy

### 3. GitHub Pages
1. Run `quasar build -m spa`
2. Set `publicPath: '/<repo-name>/'` in `quasar.config.js`
3. Push `dist/spa/` contents to `gh-pages` branch:
   ```bash
   npx gh-pages -d dist/spa
   ```
4. Enable GitHub Pages in repo Settings → Pages

---

## Common Issues and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| 404 on refresh | No SPA rewrite rule | Add `_redirects` (Netlify) or `vercel.json` (Vercel) |
| Blank page | Wrong `publicPath` | Set `publicPath` to match deployment subdirectory |
| Assets 404 | Wrong output directory | Use `dist/spa` not `dist/` |
| Routing broken | Missing Vue Router history mode | Ensure `createWebHistory()` is used |
| Environment vars missing | Not set in build env | Set env vars in platform dashboard or `.env` file |
