// quasar.config.js — SPA production build configuration
// Documentation for each setting is in comments

// .quasar.config.js
export default {
  build: {
    // publicPath: Base path for the deployed app.
    // Use '/' for root deployment, '/my-app/' for subdirectory.
    publicPath: '/',

    // sourcemap: Disable sourcemaps in production to reduce bundle size
    // and prevent source code exposure.
    sourcemap: false,

    // gzip: Enable gzip compression for static assets.
    // Reduces file sizes by ~70%, faster downloads.
    gzip: true,

    // env: Environment variables available in the app via process.env.
    // Different values for dev vs prod.
    env: {
      // API_URL: Backend API base URL
      API_URL: process.env.NODE_ENV === 'production'
        ? 'https://api.myapp.com'    // Production API
        : 'http://localhost:3001',   // Development API
    },
  },
}

/*
Build command: quasar build -m spa
Output directory: dist/spa

Settings explained:
- publicPath: Ensures assets load from the correct path after deployment
- sourcemap: false: Smaller bundles, no source code leaked in production
- gzip: true: Compressed assets served directly, faster page loads
- env.API_URL: App talks to different API servers in dev vs prod
*/
