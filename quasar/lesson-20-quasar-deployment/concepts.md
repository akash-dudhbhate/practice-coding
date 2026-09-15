# Lesson 20 — Concepts Explained (Quasar Deployment)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Deployment Overview

**What:** Deploying a Quasar app means building it for a target platform and hosting it.

```bash
# SPA (web app)
quasar build -m spa    # → dist/spa/

# PWA
quasar build -m pwa    # → dist/pwa/

# SSR
quasar build -m ssr    # → dist/ssr/ (needs Node.js server)

# Mobile
quasar build -m capacitor -T android  # → APK
quasar build -m capacitor -T ios      # → IPA

# Desktop
quasar build -m electron  # → installer
```

**Why it exists:** Each platform has different requirements → different build outputs. Understanding the options → deploy to the right place → app is accessible.

**Where it's used:** Every Quasar project — the final step before users can access the app.

**What goes wrong without it:**
- Deploying SSR to a static host (Netlify, GitHub Pages) → SSR needs a Node.js server → fails. Use SPA/PWA for static hosts.
- Not setting the base URL → assets load from wrong path → blank page. Set `publicPath` in config.
- Forgetting to set environment variables → API URLs point to localhost in production → broken.

---

## SPA Deployment (Static Hosting)

**What:** Deploy the SPA build to a static host (Netlify, Vercel, GitHub Pages, S3).

```bash
# Build
quasar build -m spa
# Output: dist/spa/
# Contains: index.html, JS, CSS, assets
```

```js
// quasar.config.js — set base path
build: {
    publicPath: '/',  // default (for root domain)
    // publicPath: '/my-app/',  // for subdirectory (GitHub Pages)
}
```

**Why it exists:** SPA is the simplest deployment → static files → any static host. No server needed → cheap, fast, scalable via CDN.

**Where it's used:** Most Quasar apps — dashboards, marketing sites, simple web apps.

**What goes wrong without it:**
- `publicPath` wrong → assets 404 → blank page. Set it to the subdirectory path.
- Client-side routing → refresh on `/about` → server looks for `/about/index.html` → 404. Configure redirects (see below).
- Not gzipping → large files → slow. Enable compression on the host.

---

## SPA Redirects (Client-Side Routing)

**What:** Redirect all routes to `index.html` so Vue Router handles them.

```nginx
# Nginx
location / {
    try_files $uri $uri/ /index.html;
}
```

```js
// Netlify — _redirects file
/*    /index.html   200

// Vercel — vercel.json
{
    "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

**Why it exists:** SPA has one HTML file (`index.html`). Routes (`/about`, `/users`) are handled by JavaScript. Server doesn't know these routes → 404 on refresh. Redirect → always serve `index.html` → JS handles routing.

**Where it's used:** Every SPA deployment to a static host.

**What goes wrong without it:**
- User refreshes `/about` → 404 → broken. Redirects fix this.
- Not configuring redirects → works on navigation (JS) but breaks on refresh/direct link.
- Redirecting everything including assets → JS/CSS also redirected to HTML → broken. Use `try_files` (serves real files first).

---

## SSR Deployment (Node.js Server)

**What:** Deploy the SSR build to a Node.js host (VPS, Railway, Render, Docker).

```bash
# Build
quasar build -m ssr
# Output: dist/ssr/
# Contains: server-side code + client assets

# Run the server
node dist/ssr/index.js
# Or with PM2:
pm2 start dist/ssr/index.js
```

```js
// Dockerfile for SSR
FROM node:18-slim
WORKDIR /app
COPY dist/ssr/ .
COPY package.json .
RUN npm install --production
EXPOSE 3000
CMD ["node", "index.js"]
```

**Why it exists:** SSR needs a running Node.js process (to render pages on request). Static hosts can't run Node.js → need a server host → VPS, Railway, Render, or Docker.

**Where it's used:** SSR apps — e-commerce, blogs, any SEO-focused site.

**What goes wrong without it:**
- Deploying to Netlify/Vercel as static → SSR doesn't work → serves as SPA → no SEO.
- Not setting PORT env var → server uses default port → might conflict. Set `PORT=3000`.
- No process manager → server crashes → app down. Use PM2 or Docker with restart policy.

---

## Environment Variables

**What:** Different settings for development and production.

```bash
# Development
API_URL=http://localhost:3000/api

# Production
API_URL=https://api.myapp.com
```

```js
// quasar.config.js
build: {
    env: {
        API_URL: ctx.dev ? 'http://localhost:3000/api' : 'https://api.myapp.com',
    }
}

// In Vue components:
const apiUrl = process.env.API_URL
```

**Why it exists:** Development uses local APIs, production uses live APIs. Hardcoding → wrong API in production → broken. Environment variables → correct API per environment → safe.

**Where it's used:** Every app with different environments (dev/staging/prod).

**What goes wrong without it:**
- Hardcoding `http://localhost:3000` → production calls localhost → fails.
- Not setting env vars on the server → uses defaults → wrong API.
- Committing secrets (API keys) to the repo → security risk. Use `.env` files (gitignored).

---

## Docker Deployment

**What:** Package the app in a Docker container → runs anywhere.

```dockerfile
# SPA with Nginx
FROM nginx:alpine
COPY dist/spa/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

# nginx.conf
server {
    listen 80;
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }
}
```

```bash
# Build and run
docker build -t my-quasar-app .
docker run -p 80:80 my-quasar-app
```

**Why it exists:** Without Docker, deployment depends on the host's setup → "works on my machine." Docker packages everything → identical environment → reliable deployment.

**Where it's used:** Production deployments — VPS, Kubernetes, cloud platforms.

**What goes wrong without it:**
- Large image → slow to pull/deploy. Use `nginx:alpine` (small) for SPA.
- Not configuring Nginx for SPA routing → 404 on refresh. Add `try_files`.
- Not exposing the right port → can't access the app. `EXPOSE 80` and map with `-p 80:80`.

---

## CI/CD Pipeline

**What:** Automate build and deployment on every push.

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
    push:
        branches: [main]

jobs:
    deploy:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v3
            - uses: actions/setup-node@v3
              with:
                  node-version: 18
            - run: npm install
            - run: npm run lint
            - run: npm run test
            - run: npx quasar build -m spa
            - name: Deploy to Netlify
              uses: nwtgck/actions-netlify@v1
              with:
                  publish-dir: './dist/spa'
                  production-branch: main
              env:
                  NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_TOKEN }}
                  NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
```

**Why it exists:** Without CI/CD, deployment is manual → error-prone, slow. CI/CD → push to main → automatic build, test, deploy → consistent, fast, reliable.

**Where it's used:** Every production app — automate the deployment process.

**What goes wrong without it:**
- Not testing in CI → broken code deploys → users see bugs. Add `npm run test` before deploy.
- Secrets in the workflow file → visible in repo. Use GitHub Secrets.
- Deploying on every push to any branch → only deploy on `main`. Use branch filters.

---

## Performance Optimization for Production

**What:** Optimize the build for production.

```js
// quasar.config.js
build: {
    // Code splitting (lazy load routes)
    // Quasar does this automatically with dynamic imports

    // Minification (enabled by default in production)
    minify: true,

    // Source maps (disable in production for smaller bundle)
    sourcemap: false,

    // Gzip compression
    gzip: true,

    // Analyze bundle
    // analyze: true,  // shows bundle composition
}
```

**Why it exists:** Development builds are unoptimized → large, slow. Production optimization → smaller bundle → faster load → better UX and SEO.

**Where it's used:** Every production build.

**What goes wrong without it:**
- Source maps in production → exposes source code → security risk. Disable.
- Not code-splitting → one huge JS file → slow initial load. Use lazy-loaded routes.
- Not analyzing the bundle → don't know what's large → can't optimize. Use `analyze: true` periodically.

---

## Pre-Deployment Checklist

**What:** A checklist before going live:

1. **Environment variables** → correct API URLs, no localhost
2. **Build** → `quasar build` succeeds without errors
3. **Test** → all tests pass
4. **Lint** → no linting errors
5. **Redirects** → SPA redirects configured (for static hosts)
6. **HTTPS** → SSL certificate configured
7. **Performance** → bundle size reasonable, images optimized
8. **SEO** → meta tags, sitemap, robots.txt (for SSR/SSG)
9. **Monitoring** → error tracking (Sentry), analytics
10. **Rollback plan** → how to revert if something breaks

**Why it exists:** Without a checklist, you forget steps → broken deployment → downtime. Checklist → consistent, reliable deployments.

**Where it's used:** Every production deployment.

**What goes wrong without it:**
- No HTTPS → browsers warn "not secure" → users leave. Always use HTTPS.
- No monitoring → errors happen silently → users report bugs → reactive, not proactive.
- No rollback → broken deployment → can't revert → downtime until fix.
