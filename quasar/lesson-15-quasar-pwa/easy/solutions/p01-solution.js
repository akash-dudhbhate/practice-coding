// manifest.json for Quasar PWA
// This file defines how the app appears when installed as a PWA
{
  "name": "My Quasar PWA App",
  "short_name": "QuasarApp",
  "description": "A Progressive Web App built with Quasar Framework",
  "start_url": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#1976d2",
  "background_color": "#ffffff",
  "icons": [
    {
      "src": "icons/icon-128.png",
      "sizes": "128x128",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ]
}
