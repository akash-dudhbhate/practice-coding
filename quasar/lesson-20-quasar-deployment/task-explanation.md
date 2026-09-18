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

   WHAT IT SHOULD LOOK LIKE:
   ```
   // quasar.config.js -> build: { publicPath: '/',
   //   sourcemap: false, env: { API_URL: ... } }
   $ quasar build -m spa
   -> dist/spa/  (gzipped assets, prod API_URL baked in)
   ```
2. `easy/p02-solve.txt` — Write a `_redirects` file for Netlify and a `vercel.json` file for Vercel. Both should redirect all routes to `index.html` for SPA routing. Include comments explaining why.

   WHAT IT SHOULD LOOK LIKE:
   ```
   # _redirects (Netlify)
   /*    /index.html   200
   // vercel.json (Vercel)
   { "rewrites": [ { "source": "/(.*)",
                     "destination": "/index.html" } ] }
   (so /users/42 doesn't 404 on refresh)
   ```
3. `easy/p03-solve.md` — Write a deployment guide for a Quasar SPA: prerequisites, build command, output directory, and deployment steps for Netlify, Vercel, and GitHub Pages. Include common issues and fixes.

   WHAT IT SHOULD LOOK LIKE:
   ```
   # Deployment Guide
   ## Prerequisites      ## Build (quasar build -m spa)
   ## Deploy: Netlify    ## Deploy: Vercel
   ## Deploy: GH Pages   ## Common issues & fixes
   (a readable markdown doc covering all sections)
   ```

### Medium
4. `medium/p01-solve.js` — Write a Dockerfile for a Quasar SPA: use nginx:alpine, copy the build output, configure nginx for SPA routing (try_files), expose port 80. Include the nginx.conf content. Document build and run commands.

   WHAT IT SHOULD LOOK LIKE:
   ```
   FROM nginx:alpine
   COPY dist/spa/ /usr/share/nginx/html/
   # nginx.conf: try_files $uri /index.html;
   $ docker build -t myapp . && docker run -p 8080:80 myapp
   -> SPA served at localhost:8080, routes work
   ```
5. `medium/p02-solve.js` — Write a Dockerfile for a Quasar SSR app: use node:18-slim, copy the build, install production dependencies, expose port 3000, and set the CMD. Include a docker-compose.yml with restart policy and environment variables.

   WHAT IT SHOULD LOOK LIKE:
   ```
   FROM node:18-slim   ->  EXPOSE 3000 -> CMD node index.js
   docker-compose.yml: restart: always, env vars,
   healthcheck -> `docker compose up -d` runs SSR
   ```
6. `medium/p03-solve.yml` — Write a GitHub Actions CI/CD pipeline: on push to main, install dependencies, run lint, run tests, build SPA, and deploy to Netlify. Use secrets for tokens. Include caching for node_modules.

   WHAT IT SHOULD LOOK LIKE:
   ```
   push -> [checkout] -> [setup node + cache]
        -> [npm ci] -> [lint] -> [test]
        -> [quasar build -m spa] -> [deploy Netlify]
   (secrets.* for tokens — nothing hardcoded)
   ```

### Hard
7. `hard/p01-solve.yml` — Write a complete CI/CD pipeline with multiple stages: lint, test, build (SPA + PWA), security scan (npm audit), and deploy to staging (on push) and production (on tag). Include environment variables, caching, and Slack notification on failure.

   WHAT IT SHOULD LOOK LIKE:
   ```
   lint -> test (coverage artifact)
        -> build matrix: [spa] [pwa]  (dist artifacts)
        -> security (npm audit)
        -> staging deploy (push) / prod deploy (release)
        -> notify Slack on any failure
   ```
8. `hard/p02-solve.js` — Build a deployment script (Node.js): reads the build output, uploads to S3 (simulated), invalidates CloudFront cache (simulated), and sends a Slack notification. Include rollback capability (keep last 3 versions). Document the full deployment process.

   WHAT IT SHOULD LOOK LIKE:
   ```
   $ node deploy.js
   Uploading dist/spa -> s3://bucket/v1.2.4 ...
   Invalidating CloudFront /* ...
   Slack: "Deployed v1.2.4"            <- notify
   $ node deploy.js --rollback v1.2.3  <- restores previous
   ```
9. `hard/p03-solve.md` — Write a complete deployment playbook: pre-deployment checklist (10+ items), deployment steps for 3 platforms (Netlify, Docker/AWS, Vercel), post-deployment verification, monitoring setup (Sentry, analytics), rollback procedure, and troubleshooting guide. Be thorough.

   WHAT IT SHOULD LOOK LIKE:
   ```
   # Deployment Playbook
   ## Pre-deploy checklist (10+ boxes)
   ## Deploy: Netlify | Docker/AWS | Vercel
   ## Post-deploy verification
   ## Monitoring (Sentry + analytics)
   ## Rollback procedures (per platform)
   ## Troubleshooting: symptom -> cause -> fix
   ```

### How to work
- Write your complete solution.
- Remove the TODO comment when done.
- Test by checking the config/scripts are valid.
