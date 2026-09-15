# Lesson 20 — Quasar Deployment

## What you'll learn
- Deployment overview (SPA, PWA, SSR, mobile, desktop)
- SPA deployment (static hosting)
- SPA redirects (client-side routing)
- SSR deployment (Node.js server)
- Environment variables (dev vs prod)
- Docker deployment (containerization)
- CI/CD pipeline (automated deployment)
- Performance optimization for production
- Pre-deployment checklist

## Lesson

### Build
```bash
quasar build -m spa    # static
quasar build -m ssr    # needs server
quasar build -m capacitor -T android  # mobile
```

### Environment
```js
build: {
    env: { API_URL: ctx.dev ? 'http://localhost:3000' : 'https://api.prod.com' }
}
```

### Docker (SPA)
```dockerfile
FROM nginx:alpine
COPY dist/spa/ /usr/share/nginx/html/
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Write a `quasar.config.js` build section for SPA production: set `publicPath`, disable sourcemaps, enable gzip, and set environment variables (API_URL for dev and prod). Document each setting.
2. `easy/p02-solve.txt` — Write a `_redirects` file for Netlify and a `vercel.json` file for Vercel. Both should redirect all routes to `index.html` for SPA routing. Include comments explaining why.
3. `easy/p03-solve.md` — Write a deployment guide for a Quasar SPA: prerequisites, build command, output directory, and deployment steps for Netlify, Vercel, and GitHub Pages. Include common issues and fixes.

### Medium
4. `medium/p01-solve.js` — Write a Dockerfile for a Quasar SPA: use nginx:alpine, copy the build output, configure nginx for SPA routing (try_files), expose port 80. Include the nginx.conf content. Document build and run commands.
5. `medium/p02-solve.js` — Write a Dockerfile for a Quasar SSR app: use node:18-slim, copy the build, install production dependencies, expose port 3000, and set the CMD. Include a docker-compose.yml with restart policy and environment variables.
6. `medium/p03-solve.yml` — Write a GitHub Actions CI/CD pipeline: on push to main, install dependencies, run lint, run tests, build SPA, and deploy to Netlify. Use secrets for tokens. Include caching for node_modules.

### Hard
7. `hard/p01-solve.yml` — Write a complete CI/CD pipeline with multiple stages: lint, test, build (SPA + PWA), security scan (npm audit), and deploy to staging (on push) and production (on tag). Include environment variables, caching, and Slack notification on failure.
8. `hard/p02-solve.js` — Build a deployment script (Node.js): reads the build output, uploads to S3 (simulated), invalidates CloudFront cache (simulated), and sends a Slack notification. Include rollback capability (keep last 3 versions). Document the full deployment process.
9. `hard/p03-solve.md` — Write a complete deployment playbook: pre-deployment checklist (10+ items), deployment steps for 3 platforms (Netlify, Docker/AWS, Vercel), post-deployment verification, monitoring setup (Sentry, analytics), rollback procedure, and troubleshooting guide. Be thorough.

### How to work
- Write your complete solution.
- Remove the TODO comment when done.
- Test by checking the config/scripts are valid.
