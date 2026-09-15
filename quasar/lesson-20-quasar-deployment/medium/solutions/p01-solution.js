// Dockerfile for Quasar SPA — nginx:alpine
// Build: docker build -t my-quasar-app .
// Run:   docker run -p 8080:80 my-quasar-app

// --- Dockerfile ---
/*
FROM node:18-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npx quasar build -m spa

FROM nginx:alpine
COPY --from=build /app/dist/spa /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
*/

// --- nginx.conf ---
/*
server {
    listen 80;
    server_name _;
    root /usr/share/nginx/html;
    index index.html;

    # SPA routing: try files, fall back to index.html
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Don't cache index.html
    location = /index.html {
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }
}
*/

// --- Build and Run Commands ---
/*
# Build the Docker image
docker build -t my-quasar-app .

# Run on port 8080
docker run -d -p 8080:80 --name quasar-app my-quasar-app

# View logs
docker logs quasar-app

# Stop and remove
docker stop quasar-app && docker rm quasar-app
*/

// Explanation:
// - Multi-stage build: first stage builds the SPA, second stage serves it
// - nginx:alpine: lightweight web server (~7MB)
// - try_files: redirects all routes to index.html for SPA routing
// - Static asset caching: 1 year with immutable flag for performance
// - index.html no-cache: ensures users get the latest HTML with updated asset hashes
