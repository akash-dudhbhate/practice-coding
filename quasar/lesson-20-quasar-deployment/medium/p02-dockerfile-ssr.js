/**
 * LESSON 20 — Quasar Deployment
 * MEDIUM P02 — Dockerfile + Compose for Quasar SSR
 * ============================================
 * CONCEPT: SSR needs a running Node server, not static hosting:
 * multi-stage build (quasar build -m ssr → copy dist/ssr + prod deps via
 * npm ci --omit=dev), EXPOSE 3000, CMD node index.js. docker-compose adds
 * restart policy, env vars, healthcheck.
 *
 * PROBLEM: Write (in comments/strings) a node:18-slim multi-stage
 * Dockerfile for SSR and a docker-compose.yml service with ports
 * 3000:3000, restart: unless-stopped, environment (NODE_ENV, API_URL,
 * PORT), a healthcheck, and log limits. Document compose build/up/down.
 *
 * TRY THIS: CMD ["node", "dist/ssr/index.js"]
 *   restart: unless-stopped
 *   healthcheck: { test: ["CMD","curl","-f","http://localhost:3000/health"] }
 *
 * EXPECTED OUTPUT: `docker compose up -d` runs the SSR server with
 * auto-restart and health monitoring.
 *
 * CHECK: python3 check.py medium/p02
 */
// TODO: write your Dockerfile + docker-compose.yml here
