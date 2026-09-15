// Dockerfile for Quasar SSR — node:18-slim + docker-compose.yml
// Build: docker compose build
// Run:   docker compose up -d

// --- Dockerfile ---
/*
FROM node:18-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npx quasar build -m ssr

FROM node:18-slim
WORKDIR /app
COPY --from=build /app/dist/ssr ./
COPY package*.json ./
RUN npm ci --omit=dev
EXPOSE 3000
ENV NODE_ENV=production
CMD ["node", "dist/ssr/index.js"]
*/

// --- docker-compose.yml ---
/*
version: '3.8'
services:
  quasar-ssr:
    build: .
    ports:
      - "3000:3000"
    restart: unless-stopped
    environment:
      - NODE_ENV=production
      - API_URL=https://api.myapp.com
      - PORT=3000
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
*/

// --- Build and Run Commands ---
/*
# Build the image
docker compose build

# Run in background
docker compose up -d

# View logs
docker compose logs -f

# Stop
docker compose down

# Rebuild after code changes
docker compose up -d --build
*/

// Explanation:
// - Multi-stage build: first stage builds SSR, second stage runs it
// - node:18-slim: minimal Node.js image (~180MB)
// - npm ci --omit=dev: install only production dependencies
// - restart: unless-stopped: auto-restart on crash, not on manual stop
// - healthcheck: monitors if the server is responding
// - logging: limits log file size to prevent disk fill
// - Environment variables: API_URL and PORT configurable per deployment
