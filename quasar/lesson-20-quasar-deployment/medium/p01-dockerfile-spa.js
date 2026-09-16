/**
 * LESSON 20 — Quasar Deployment
 * MEDIUM P01 — Dockerfile for a Quasar SPA
 * ============================================
 * CONCEPT: Multi-stage Docker: stage 1 builds (node image + quasar
 * build -m spa), stage 2 serves static files from nginx:alpine. nginx's
 * try_files $uri /index.html gives you SPA routing inside the container.
 *
 * PROBLEM: Write (as comments or heredoc strings in this .js file) a
 * multi-stage Dockerfile: build stage → nginx:alpine stage copying
 * dist/spa into /usr/share/nginx/html, EXPOSE 80, CMD nginx. Include an
 * nginx.conf with try_files, 1-year immutable caching for static assets,
 * and no-cache for index.html. Document docker build/run commands.
 *
 * TRY THIS: FROM nginx:alpine
 * COPY --from=build /app/dist/spa /usr/share/nginx/html
 * location / { try_files $uri $uri/ /index.html; }
 *
 * EXPECTED OUTPUT: docker build + run serves the SPA with correct routing
 * and sane caching headers.
 *
 * CHECK: python3 check.py medium/p01
 */
// TODO: write your Dockerfile + nginx.conf here
