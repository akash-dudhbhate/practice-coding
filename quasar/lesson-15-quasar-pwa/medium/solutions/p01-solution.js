// Workbox configuration for quasar.config.js — offline support
// This configures caching strategies for different resource types

const workboxConfig = {
  workboxPluginMode: 'GenerateSW',
  workboxOptions: {
    navigateFallback: 'index.html',
    runtimeCaching: [
      {
        // Static assets: CacheFirst (fast, rarely change)
        urlPattern: ({ url }) => url.pathname.startsWith('/css') || url.pathname.startsWith('/js'),
        handler: 'CacheFirst',
        options: {
          cacheName: 'static-assets',
          expiration: {
            maxEntries: 60,
            maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
          },
        },
      },
      {
        // API calls: NetworkFirst with fallback (fresh data preferred)
        urlPattern: ({ url }) => url.pathname.startsWith('/api'),
        handler: 'NetworkFirst',
        options: {
          cacheName: 'api-cache',
          networkTimeoutSeconds: 5,
          expiration: {
            maxEntries: 50,
            maxAgeSeconds: 24 * 60 * 60, // 1 day
          },
        },
      },
      {
        // Images: StaleWhileRevalidate (fast display, update in background)
        urlPattern: ({ request }) => request.destination === 'image',
        handler: 'StaleWhileRevalidate',
        options: {
          cacheName: 'image-cache',
          expiration: {
            maxEntries: 100,
            maxAgeSeconds: 7 * 24 * 60 * 60, // 7 days
          },
        },
      },
    ],
  },
}

export default workboxConfig
