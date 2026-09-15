# Lesson 15 — Concepts Explained (Quasar PWA)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is a PWA?

**What:** Progressive Web App — a web app that works offline, is installable, and feels native.

```bash
# Create a Quasar PWA
quasar create my-app --kit pwa
# or add PWA mode to existing app:
quasar mode add pwa

# Build for PWA
quasar build -m pwa
```

**Why it exists:** Native apps (iOS/Android) require app store approval, separate codebase. PWAs are web apps with native-like features → installable, offline, push notifications → one codebase → no app store.

**Where it's used:** E-commerce, news, social, any web app that benefits from offline/installability.

**What goes wrong without it:**
- Treating PWA as a regular web app → no offline, no install → misses the point.
- Not testing on mobile → PWA features (install prompt, push) behave differently on iOS vs Android.
- Not serving HTTPS → PWA requires HTTPS (service workers only work on HTTPS).

---

## Service Workers

**What:** A script that runs in the background → caches files, handles offline, enables push notifications.

```js
// Quasar generates the service worker automatically
// Configuration in quasar.config.js:

framework: {
    pwa: {
        workboxPluginMode: 'GenerateSW',  // or 'InjectManifest'
        workboxOptions: {
            navigateFallback: 'index.html',
            precache: ['index.html', 'css/app.css'],
        },
        // Custom service worker (InjectManifest mode)
        // swFilename: 'custom-sw.js',
    }
}
```

**Why it exists:** Without a service worker, the app can't work offline (no caching) or receive push notifications. The SW intercepts network requests → serves from cache → offline works.

**Where it's used:** Every PWA — the service worker is the core.

**What goes wrong without it:**
- `GenerateSW` → Quasar generates the SW automatically (easy, limited customization).
- `InjectManifest` → you provide a custom SW (full control, more work).
- SW caching old files → users see stale content. Use cache-busting or update strategies.

---

## Manifest File

**What:** The `manifest.json` file defines the app's metadata (name, icons, theme).

```json
{
    "name": "My Quasar App",
    "short_name": "MyApp",
    "description": "A progressive web app",
    "start_url": "/",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#ffffff",
    "theme_color": "#1976d2",
    "icons": [
        {
            "src": "icons/icon-128x128.png",
            "sizes": "128x128",
            "type": "image/png"
        },
        {
            "src": "icons/icon-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}
```

**Why it exists:** Without a manifest, the browser doesn't know the app is installable → no "Add to Home Screen" → not a real PWA. The manifest provides the metadata → installable → native-like.

**Where it's used:** Every PWA — configured once in `public/manifest.json` or `quasar.config.js`.

**What goes wrong without it:**
- Missing icons → install prompt shows default icon → unprofessional. Provide all sizes.
- `display: "standalone"` → no browser UI (like native). `display: "browser"` → regular web page.
- Not setting `theme_color` → status bar uses default color → doesn't match brand.

---

## Offline Support

**What:** Cache assets and API responses → app works without internet.

```js
// Quasar's Workbox configuration (quasar.config.js)
pwa: {
    workboxPluginMode: 'GenerateSW',
    workboxOptions: {
        // Cache all assets
        globPatterns: ['**/*.{js,css,html,svg,png,woff2}'],
        // Runtime caching for API calls
        runtimeCaching: [
            {
                urlPattern: /^https:\/\/api\.example\.com\/.*/,
                handler: 'NetworkFirst',
                options: {
                    cacheName: 'api-cache',
                    expiration: {
                        maxEntries: 50,
                        maxAgeSeconds: 60 * 60,  // 1 hour
                    }
                }
            }
        ]
    }
}
```

**Why it exists:** Without offline support, the app shows "no internet" error → useless. Caching → app loads from cache → works offline → seamless experience.

**Where it's used:** Every PWA that needs to function without internet.

**What goes wrong without it:**
- Caching too much → storage limits → eviction → inconsistent offline. Cache only what's needed.
- `NetworkFirst` → tries network, falls back to cache (good for fresh data). `CacheFirst` → uses cache first (good for static assets).
- Not handling cache updates → user sees old data. Use `StaleWhileRevalidate` for a balance.

---

## Install Prompt

**What:** Show a custom "Add to Home Screen" prompt.

```js
// Capture the install event
let deferredPrompt = null

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault()
    deferredPrompt = e
    // Show your custom install button
    showInstallButton.value = true
})

async function installApp() {
    if (!deferredPrompt) return
    deferredPrompt.prompt()
    const { outcome } = await deferredPrompt.userChoice
    if (outcome === 'accepted') {
        console.log('User installed the app')
    }
    deferredPrompt = null
    showInstallButton.value = false
}

// In template:
<q-btn v-if="showInstallButton" @click="installApp" label="Install App" />
```

**Why it exists:** The browser's default install prompt is subtle → users miss it. A custom button → more visible → higher install rate → more engagement.

**Where it's used:** PWA landing pages, settings, anywhere you want to encourage installation.

**What goes wrong without it:**
- `beforeinstallprompt` doesn't fire on iOS → Safari doesn't support custom prompts. Show instructions for iOS.
- Prompting too early → user hasn't engaged → declines. Wait until they've used the app.
- `deferredPrompt` is null after use → can only prompt once. Handle gracefully.

---

## Push Notifications

**What:** Send notifications to the user even when the app is closed.

```js
// Request permission
const permission = await Notification.requestPermission()
if (permission === 'granted') {
    // Subscribe to push service
    const registration = await navigator.serviceWorker.ready
    const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: VAPID_PUBLIC_KEY,
    })
    // Send subscription to your server
    await fetch('/api/subscribe', {
        method: 'POST',
        body: JSON.stringify(subscription),
    })
}

// In the service worker (custom-sw.js):
self.addEventListener('push', event => {
    const data = event.data.json()
    self.registration.showNotification(data.title, {
        body: data.body,
        icon: 'icons/icon-192x192.png',
    })
})
```

**Why it exists:** Without push notifications, the app can only notify when open → limited engagement. Push → notify anytime → re-engage users → like native apps.

**Where it's used:** Chat apps, news, promotions, any app that needs to alert users.

**What goes wrong without it:**
- iOS Safari → limited push support (only since iOS 16.4). Detect and handle gracefully.
- Not requesting permission first → `Notification.requestPermission()` → user must allow.
- Sending too many pushes → user disables notifications → lost channel. Be selective.

---

## App Updates

**What:** Notify users when a new version is available.

```js
// In App.vue or a boot file
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Quasar PWA handles updates automatically
// But you can customize the update notification:
// quasar.config.js → pwa: { updateNotify: true }

// Or manual:
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.addEventListener('controllerchange', () => {
        $q.notify({
            message: 'New version available',
            timeout: 0,
            actions: [{ label: 'Refresh', handler: () => window.location.reload() }],
        })
    })
}
```

**Why it exists:** Without update notifications, users run old versions → bugs, security issues. Notifying → users refresh → get the latest → consistent.

**Where it's used:** Every PWA — ensure users are on the latest version.

**What goes wrong without it:**
- Auto-refreshing → user loses form data → bad UX. Ask before refreshing.
- Not updating → user stuck on old version → service worker cache is stubborn. Use `skipWaiting`.
- Update loop → SW updates → refresh → SW updates again → use version checks.
