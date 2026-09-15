# Lesson 20 — Coding Check

## Easy

### p01-solve.js — Build config
- [ ] `publicPath` set
- [ ] `sourcemap: false` (production)
- [ ] `gzip: true`
- [ ] Environment variables (API_URL dev/prod)
- [ ] `ctx.dev` check for environment
- [ ] Each setting documented

### p02-solve.txt — Redirects
- [ ] `_redirects` file for Netlify
- [ ] `/*  /index.html  200` rule
- [ ] `vercel.json` for Vercel
- [ ] Rewrites configuration
- [ ] Comments explaining why (SPA routing)

### p03-solve.md — Deployment guide
- [ ] Prerequisites listed
- [ ] Build command documented
- [ ] Output directory mentioned
- [ ] Netlify steps included
- [ ] Vercel steps included
- [ ] GitHub Pages steps included
- [ ] Common issues and fixes

## Medium

### p01-solve.js — SPA Dockerfile
- [ ] `FROM nginx:alpine`
- [ ] Build output copied to nginx html
- [ ] nginx.conf included (try_files)
- [ ] Port 80 exposed
- [ ] Build command documented
- [ ] Run command documented

### p02-solve.js — SSR Dockerfile
- [ ] `FROM node:18-slim`
- [ ] SSR build copied
- [ ] Production dependencies installed
- [ ] Port 3000 exposed
- [ ] CMD set to `node index.js`
- [ ] docker-compose.yml included
- [ ] Restart policy set
- [ ] Environment variables in compose

### p03-solve.yml — CI/CD pipeline
- [ ] Trigger on push to main
- [ ] Checkout action
- [ ] Node.js setup
- [ ] npm install
- [ ] Lint step
- [ ] Test step
- [ ] Build step (SPA)
- [ ] Deploy to Netlify
- [ ] Secrets used for tokens
- [ ] Caching for node_modules

## Hard

### p01-solve.yml — Multi-stage CI/CD
- [ ] Lint stage
- [ ] Test stage
- [ ] Build stage (SPA + PWA)
- [ ] Security scan (npm audit)
- [ ] Deploy to staging (on push)
- [ ] Deploy to production (on tag)
- [ ] Environment variables
- [ ] Caching
- [ ] Slack notification on failure
- [ ] Separate jobs for each stage

### p02-solve.js — Deployment script
- [ ] Reads build output
- [ ] Uploads to S3 (simulated)
- [ ] Invalidates CloudFront (simulated)
- [ ] Sends Slack notification
- [ ] Rollback capability (keep last 3)
- [ ] Version tracking
- [ ] Error handling
- [ ] Full process documented

### p03-solve.md — Deployment playbook
- [ ] Pre-deployment checklist (10+ items)
- [ ] Netlify deployment steps
- [ ] Docker/AWS deployment steps
- [ ] Vercel deployment steps
- [ ] Post-deployment verification
- [ ] Monitoring setup (Sentry, analytics)
- [ ] Rollback procedure
- [ ] Troubleshooting guide
- [ ] Thorough and complete
