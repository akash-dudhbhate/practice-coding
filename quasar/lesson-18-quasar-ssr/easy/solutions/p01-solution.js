/**
 * quasar.config.js — SSR Configuration
 * -------------------------------------
 * Enables Server-Side Rendering with:
 *   - Component cache (max 1000 entries, 15-minute maxAge)
 *   - Compression middleware for smaller/faster responses
 *
 * Each setting is documented inline so the rationale is clear.
 *
 * This is a partial config showing only the ssr section; merge it
 * into your project's quasar.config.js.
 */

/* eslint-env node */

module.exports = function (/* ctx */) {
  return {
    // ------------------------------------------------------------------
    // SSR — Server-Side Rendering
    // ------------------------------------------------------------------
    ssr: {
      // Enable SSR mode. When true, `quasar dev` and `quasar build`
      // produce a server-rendered app instead of a plain SPA.
      ssr: true,

      // Component caching uses lru-cache to store rendered component
      // output.  This dramatically speeds up repeated renders (e.g.
      // header, footer, product cards) at the cost of memory.
      componentCache: {
        // Maximum number of cached components in memory
        max: 1000,

        // Time-to-live: each cached entry expires after 15 minutes
        // (value in milliseconds).  Adjust based on how often your
        // content changes.
        maxAge: 1000 * 60 * 15, // 15 minutes
      },

      // Middleware executed on every SSR request, in order.
      // 'compression' is built-in and gzips responses to reduce
      // payload size over the wire.
      middlewares: [
        'compression', // gzip / deflate responses
        'render',      // Quasar's core SSR renderer (always last)
      ],

      // Whether to generate a separate PWA service worker alongside
      // the SSR server.  Set to true for SSR + PWA hybrid apps.
      pwa: false,
    },

    // ------------------------------------------------------------------
    // Build settings that complement SSR
    // ------------------------------------------------------------------
    build: {
      // Vue's SSR transform is handled automatically by Quasar when
      // ssr is enabled; no extra transpile flags are needed.
      target: {
        browser: ['es2019', 'edge88', 'firefox78', 'chrome87', 'safari13.1'],
        node: 'node16',
      },

      // Vite options for SSR
      viteVuePluginOptions: {
        // Enable SSR-specific compile flags
        template: {
          ssr: true,
        },
      },
    },
  }
}
