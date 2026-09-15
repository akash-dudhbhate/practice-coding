# Lesson 15 — Coding Check

## Easy

### p01-solve.js — Manifest file
- [ ] `name` and `short_name` set
- [ ] `start_url` set to "/"
- [ ] `display: "standalone"`
- [ ] `theme_color` set
- [ ] `background_color` set
- [ ] 2 icon sizes (128, 512)
- [ ] `description` included

### p02-solve.vue — PWA detection
- [ ] `window.matchMedia` used
- [ ] Detects standalone mode
- [ ] Shows "Running as PWA" when installed
- [ ] Shows "Running in browser" otherwise
- [ ] Reactive (updates on change)

### p03-solve.vue — Install button
- [ ] `beforeinstallprompt` event listener
- [ ] `e.preventDefault()` called
- [ ] Button shown when prompt available
- [ ] `deferredPrompt.prompt()` on click
- [ ] `userChoice` handled
- [ ] Button hidden after install
- [ ] Notification on accepted/declined

## Medium

### p01-solve.js — Workbox configuration
- [ ] `workboxPluginMode: 'GenerateSW'`
- [ ] Static assets: CacheFirst
- [ ] API calls: NetworkFirst
- [ ] Images: StaleWhileRevalidate
- [ ] Expiration limits set (maxEntries, maxAgeSeconds)
- [ ] Cache names defined

### p02-solve.vue — Offline indicator
- [ ] `navigator.onLine` checked
- [ ] `online` event listener
- [ ] `offline` event listener
- [ ] Banner shown when offline
- [ ] Notification when back online
- [ ] Banner hidden when online

### p03-solve.vue — Push permission
- [ ] Button to request permission
- [ ] `Notification.requestPermission()` called
- [ ] Status displayed (granted/denied/default)
- [ ] Test notification shown when granted
- [ ] iOS limitations handled (graceful message)
- [ ] Status persisted

## Hard

### p01-solve.vue — PWA onboarding
- [ ] Detects if PWA is installed
- [ ] Shows install prompt if not
- [ ] Explains PWA benefits (offline, installable, push)
- [ ] Tracks dismissal
- [ ] Dismissal persisted to localStorage
- [ ] Doesn't show again if dismissed
- [ ] Clean, user-friendly UI

### p02-solve.js — Offline sync system
- [ ] Store API requests while offline
- [ ] Uses IndexedDB or localStorage
- [ ] Detects when back online
- [ ] Replays stored requests
- [ ] Notifies user of sync status
- [ ] Handles conflicts (gracefully)
- [ ] Clears queue after successful sync

### p03-solve.vue — PWA settings page
- [ ] Install status displayed
- [ ] Update notification with refresh button
- [ ] Push notification toggle
- [ ] Permission request on toggle
- [ ] Offline storage usage displayed
- [ ] Clear cache button
- [ ] All settings persisted to localStorage
- [ ] Clean settings UI
