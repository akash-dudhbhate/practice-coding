# Complete Deployment Playbook

## Pre-Deployment Checklist

- [ ] All tests pass locally (`vitest run`)
- [ ] Lint passes with no errors (`quasar lint`)
- [ ] Code reviewed and approved (PR merged)
- [ ] Environment variables set in deployment platform
- [ ] API_URL points to correct backend (staging/prod)
- [ ] No console.log/debug statements in production code
- [ ] Sourcemaps disabled in production config
- [ ] Gzip compression enabled
- [ ] SPA routing rewrite rules configured (_redirects/vercel.json)
- [ ] HTTPS/SSL certificates valid
- [ ] CDN cache invalidation plan ready
- [ ] Rollback plan documented
- [ ] Monitoring (Sentry) configured
- [ ] Analytics tracking ID set

---

## Deployment Steps by Platform

### 1. Netlify
```bash
# Build
quasar build -m spa

# Deploy via CLI
npm i -g netlify-cli
netlify deploy --prod --dir=dist/spa
```
Or connect Git repo for auto-deploy on push to main.

### 2. Docker / AWS
```bash
# Build Docker image
docker build -t my-app .

# Push to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
docker tag my-app:latest <account>.dkr.ecr.<region>.amazonaws.com/my-app:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/my-app:latest

# Deploy to ECS/EKS
aws ecs update-service --cluster my-cluster --service my-service --force-new-deployment
```

### 3. Vercel
```bash
# Build
quasar build -m spa

# Deploy via CLI
npm i -g vercel
vercel --prod
```
Or connect Git repo for auto-deploy.

---

## Post-Deployment Verification

1. **Smoke test key flows:**
   - Home page loads
   - Login works
   - Navigation between routes works
   - API calls succeed (check Network tab)
   - Forms submit correctly

2. **Check performance:**
   - Page load < 3s (Lighthouse audit)
   - No console errors
   - No 404s for assets

3. **Verify SEO (if SSR):**
   - View page source — data is server-rendered
   - Meta tags present
   - Open Graph tags correct

4. **Check monitoring:**
   - Sentry is receiving events
   - Analytics is tracking page views

---

## Monitoring Setup

### Sentry (Error Tracking)
```bash
npm i @sentry/vue
```
Configure in `src/boot/sentry.js`:
```js
import Sentry from '@sentry/vue'
Sentry.init({ dsn: process.env.SENTRY_DSN, tracesSampleRate: 1.0 })
```

### Analytics (Google Analytics)
Add GA4 tracking ID in `quasar.config.js` env and initialize in a boot file.

### Uptime Monitoring
- Set up uptime checks (e.g., Pingdom, UptimeRobot)
- Monitor `/health` endpoint (SSR) or page load (SPA)
- Alert on > 5 min downtime

---

## Rollback Procedure

### Netlify
1. Go to Netlify dashboard → Deploys
2. Find the last known good deploy
3. Click "Publish" on that deploy
4. Verify site is working

### Docker / AWS
```bash
# Rollback to previous image
aws ecs describe-services --cluster my-cluster --services my-service
# Find previous task definition
aws ecs update-service --cluster my-cluster --service my-service --task-definition <previous-arn>
```

### Vercel
1. Go to Vercel dashboard → Deployments
2. Find the last stable deployment
3. Click "Instant Rollback"
4. Verify site is working

---

## Troubleshooting Guide

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Blank page | Wrong publicPath | Set `publicPath` to match deployment URL |
| 404 on refresh | Missing SPA rewrite | Add `_redirects` or `vercel.json` |
| API errors | Wrong API_URL | Check env vars in deployment platform |
| Assets 404 | Wrong output dir | Use `dist/spa` not `dist/` |
| Slow load | No gzip/compression | Enable gzip in build config or CDN |
| Old content | CDN cache | Invalidate CloudFront or wait for TTL |
| Sentry not working | Missing DSN | Set `SENTRY_DSN` env var |
| Build fails in CI | Node version mismatch | Pin Node version in CI config |
| Routing broken | Wrong history mode | Use `createWebHistory()` not `createWebHashHistory()` |
| PWA not updating | Old service worker | Add `SKIP_WAITING` message handler |
