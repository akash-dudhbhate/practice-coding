# Lesson 15 — Quasar PWA

## What you'll learn
- What a PWA is (offline, installable, native-like)
- Service workers (background caching)
- Manifest file (app metadata, icons)
- Offline support (caching strategies)
- Install prompt (custom "Add to Home Screen")
- Push notifications (server-sent alerts)
- App updates (notifying users of new versions)

## Lesson

### Enable PWA mode
```bash
quasar mode add pwa
quasar build -m pwa
```

### Manifest
```json
{
    "name": "My App",
    "short_name": "MyApp",
    "display": "standalone",
    "theme_color": "#1976d2",
    "icons": [...]
}
```

### Install prompt
```js
window.addEventListener('beforeinstallprompt', e => {
    e.preventDefault()
    deferredPrompt = e
})
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Write a `manifest.json` for a Quasar PWA: name, short_name, start_url, display standalone, theme_color, background_color, and 2 icon sizes (128, 512). Include a description.

   WHAT IT SHOULD LOOK LIKE:
   ```
   // manifest.json — browser accepts it for
   // "Add to Home Screen":
   {
     "name": "My App",
     "short_name": "MyApp",
     "display": "standalone",
     "theme_color": "#1976d2",
     "icons": [ {128}, {512} ]
   }
   ```
2. `easy/p02-solve.vue` — Create a component that detects if the app is running as a PWA (standalone mode) using `window.matchMedia('(display-mode: standalone)')`. Show "Running as PWA" or "Running in browser".

   WHAT IT SHOULD LOOK LIKE:
   ```
   IN BROWSER:                  AS INSTALLED PWA:
   +----------------------+     +----------------------+
   | (i) Running in       |     | (+) Running as PWA!  |  <- banner
   |     browser          |     |     (installed)      |
   +----------------------+     +----------------------+
   ```
3. `easy/p03-solve.vue` — Create an install button component: listen for `beforeinstallprompt`, show a button when available, call `prompt()` on click, and hide the button after install. Show a notification on accepted/declined.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +---------------------------+
   | [ + Install App ]         |   <- only when installable
   +---------------------------+
   click -> native install prompt
   -> banner "App installed!" (button hides forever)
   ```

### Medium
4. `medium/p01-solve.js` — Configure Workbox in `quasar.config.js` for offline support: cache static assets (CacheFirst), API calls (NetworkFirst with fallback), and images (StaleWhileRevalidate). Include expiration limits.

   WHAT IT SHOULD LOOK LIKE:
   ```
   // quasar.config.js pwa.workboxOptions —
   // behavior, not UI:
   assets  -> CacheFirst      (instant offline)
   /api/*  -> NetworkFirst    (cache fallback)
   images  -> StaleWhileRevalidate
   ```
5. `medium/p02-solve.vue` — Create an offline indicator component: detect online/offline status using `navigator.onLine` and `online`/`offline` events. Show a banner when offline. Show a notification when back online.

   WHAT IT SHOULD LOOK LIKE:
   ```
   OFFLINE:                          ONLINE AGAIN:
   +================================+   +------------------+
   | (!) You are offline            |   | Back online!     |  <- toast
   +================================+   +------------------+
     red banner while disconnected      (banner hides)
   ```
6. `medium/p03-solve.vue` — Create a push notification permission request component: button to request permission, show status (granted/denied/default), and display a test notification when granted. Handle iOS limitations gracefully.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Enable Notifications ]
   Status: granted                        <- status text
   +---------------------------+
   | Test Notification         |           <- system notification
   | Hello from the PWA!       |
   +---------------------------+
   (iOS -> note "install the app first")
   ```

### Hard
7. `hard/p01-solve.vue` — Build a complete PWA onboarding component: detect if PWA is installed, show install prompt if not, explain PWA benefits (offline, installable, push), and track if the user dismissed the prompt. Persist dismissal to localStorage.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +--------------------------------------+
   | Get the app!                         |
   |  + Works offline                     |
   |  + Installs to home screen           |   <- benefits card
   |  + Push notifications                |
   |     [ Install ]   [ Maybe later ]    |   <- dismissal persists
   +--------------------------------------+
   (installed users see a positive banner instead)
   ```
8. `hard/p02-solve.js` — Build a complete offline data sync system: store API requests while offline (IndexedDB or localStorage), detect when back online, replay stored requests, and notify the user of sync status. Handle conflicts gracefully.

   WHAT IT SHOULD LOOK LIKE:
   ```
   // logic module — observable result:
   offline write -> queued in storage
   reconnect    -> replays queue
   -> toast "Synced 3 changes (1 conflict)"
   ```
9. `hard/p03-solve.vue` — Build a PWA settings page: install status, update available notification (with refresh button), push notification toggle (with permission request), offline storage usage display, and a "clear cache" button. All settings persisted.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------------------+
   | PWA SETTINGS                             |
   | Install status:  Installed               |
   | Update:          New version  [ Refresh ]|
   | Push:            [ (o) ] granted         |
   | Storage used:    4.2 MB                  |
   | [ Clear cache ]                          |
   +------------------------------------------+
   ```

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app or checking the config.
