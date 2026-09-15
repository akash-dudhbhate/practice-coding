# Lesson 16 — Quasar Mobile (Capacitor/Cordova)

## What you'll learn
- Quasar mobile overview (one codebase, 3 platforms)
- Capacitor integration (native API bridge)
- Mobile-specific layouts (bottom tabs, touch-friendly)
- Touch events and gestures (swipe, pan, hold)
- Native device features (camera, GPS, haptics, share)
- Mobile app configuration (permissions, metadata)
- Testing on devices and emulators

## Lesson

### Add mobile mode
```bash
quasar mode add capacitor
npx cap add android
npx cap add ios
```

### Use native plugin
```js
import { Camera } from '@capacitor/camera'
const photo = await Camera.getPhoto({ quality: 80 })
```

### Touch gestures
```vue
<div v-touch:swipe.left="onSwipe">Swipe</div>
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Write a `capacitor.config.json` with appId, appName, webDir, and plugin configurations for Camera and Geolocation. Include proper permissions.
2. `easy/p02-solve.vue` — Create a responsive layout: left drawer on desktop, bottom tabs on mobile. Use `$q.platform.is.mobile` and `$q.platform.is.desktop`. Include 3 navigation items.
3. `easy/p03-solve.vue` — Create a component with touch gestures: swipe left/right to change a counter, long-press to reset. Display the current value and instructions. Use Quasar touch directives.

### Medium
4. `medium/p01-solve.vue` — Create a camera component using Capacitor Camera plugin. Button to take a photo, display the photo, and save to gallery. Handle permission denial gracefully. Include a web fallback (file input).
5. `medium/p02-solve.vue` — Create a geolocation component: button to get current location, display latitude/longitude, and show on a map (use a simple iframe or link). Handle permission denial and errors.
6. `medium/p03-solve.vue` — Create a share component: button to share text/URL using Capacitor Share plugin. Include fallback to Web Share API or clipboard copy. Show a notification on success.

### Hard
7. `hard/p01-solve.vue` — Build a mobile photo gallery: take photos (Camera), display in a grid, swipe to navigate between photos, long-press to delete, and share button per photo. Use touch gestures and Capacitor plugins. Include empty state.
8. `hard/p02-solve.vue` — Build a mobile-aware app shell: detect platform (web/iOS/Android), adapt layout (bottom tabs on mobile, drawer on desktop), use haptics on button presses (mobile only), and handle safe area insets (notches). Include platform-specific styling.
9. `hard/p03-solve.vue` — Build an offline-first mobile app: cache data using Capacitor Storage, detect online/offline status, sync when online, show offline banner, and use haptics for feedback. Include a pull-to-refresh gesture (v-touch-pull) that refetches data.

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
