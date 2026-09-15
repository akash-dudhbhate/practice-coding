# Dockerfile — Quasar Framework development environment
# Installs Node.js 20 LTS + Quasar CLI so you can build/run Quasar projects
# without polluting your host machine.
#
# Build:
#   docker build -t quasar-dev .
#
# Run (dev server on port 8080):
#   docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
#
# Create a new project:
#   docker run -it --rm -v "$(pwd)":/app quasar-dev quasar create my-app

FROM node:20-slim

# Install system dependencies needed by Quasar/Capacitor for mobile builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Install Quasar CLI globally (Vue 3 based, @quasar/cli v2)
RUN npm install -g @quasar/cli@2

# Set working directory
WORKDIR /app

# Expose Quasar dev server default port
EXPOSE 8080

# Default command: start an interactive shell so you can run quasar commands
CMD ["bash"]
