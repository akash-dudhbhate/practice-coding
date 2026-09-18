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

   WHAT IT SHOULD LOOK LIKE:
   ```
   // capacitor.config.json
   { "appId": "com.example.myapp",
     "appName": "MyApp",
     "webDir": "dist/capacitor",
     "plugins": { Camera, Geolocation } }
   // comments note NSCameraUsageDescription /
   // ACCESS_FINE_LOCATION permissions
   ```
2. `easy/p02-solve.vue` — Create a responsive layout: left drawer on desktop, bottom tabs on mobile. Use `$q.platform.is.mobile` and `$q.platform.is.desktop`. Include 3 navigation items.

   WHAT IT SHOULD LOOK LIKE:
   ```
   DESKTOP:                  MOBILE:
   +===+=====================+   +========================+
   | = | App                 |   | App                    |
   +---+---------------------+   +------------------------+
   |Nav| content             |   | content                |
   +---+---------------------+   +------------------------+
                                 |(home)(search)(settings)| <- tabs
                                 +========================+
   ```
3. `easy/p03-solve.vue` — Create a component with touch gestures: swipe left/right to change a counter, long-press to reset. Display the current value and instructions. Use Quasar touch directives.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   |             3                    |   <- big counter
   |   <- swipe left: -1              |
   |      swipe right: +1 ->          |   <- gesture hints
   |      long-press: reset           |
   +----------------------------------+
   ```

### Medium
4. `medium/p01-solve.vue` — Create a camera component using Capacitor Camera plugin. Button to take a photo, display the photo, and save to gallery. Handle permission denial gracefully. Include a web fallback (file input).

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Take Photo ]   [ Save to gallery ]
   +------------------+
   | ###############  |   <- photo preview (camera on mobile,
   | ###############  |     file picker on web)
   +------------------+
   denied -> polite error toast
   ```
5. `medium/p02-solve.vue` — Create a geolocation component: button to get current location, display latitude/longitude, and show on a map (use a simple iframe or link). Handle permission denial and errors.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Get Location ]
   Lat: 37.7749   Long: -122.4194
   +------------------+
   |      MAP         |   <- map renders at those coords
   +------------------+
   denied -> clear error toast
   ```
6. `medium/p03-solve.vue` — Create a share component: button to share text/URL using Capacitor Share plugin. Include fallback to Web Share API or clipboard copy. Show a notification on success.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Share ]
   +----------------------------------+
   | Native share sheet (mobile) OR   |
   | web share sheet OR "Copied!"     |   <- fallback chain
   +----------------------------------+
   -> success toast whichever path ran
   ```

### Hard
7. `hard/p01-solve.vue` — Build a mobile photo gallery: take photos (Camera), display in a grid, swipe to navigate between photos, long-press to delete, and share button per photo. Use touch gestures and Capacitor plugins. Include empty state.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----+ +----+ +----+
   |img1| |img2| |img3|          <- photo grid
   +----+ +----+ +----+
   tap -> +======================+
          |  img2  < swipe >     |  <- swipeable viewer
          |       [share]        |
          +======================+
   long-press -> confirm delete
   (empty grid -> "No photos yet")
   ```
8. `hard/p02-solve.vue` — Build a mobile-aware app shell: detect platform (web/iOS/Android), adapt layout (bottom tabs on mobile, drawer on desktop), use haptics on button presses (mobile only), and handle safe area insets (notches). Include platform-specific styling.

   WHAT IT SHOULD LOOK LIKE:
   ```
   MOBILE (iOS):              DESKTOP (web):
   +========================+   +===+=====================+
   |.. notch-safe header .. |   | = | App                 |
   |   content              |   +---+---------------------+
   |                        |   |Nav| content             |
   +========================+   +---+---------------------+
   |(h)(s)(p)  haptic taps  |     drawer + normal clicks
   +========================+
   ```
9. `hard/p03-solve.vue` — Build an offline-first mobile app: cache data using Capacitor Storage, detect online/offline status, sync when online, show offline banner, and use haptics for feedback. Include a pull-to-refresh gesture (v-touch-pull) that refetches data.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +================================+
   | (!) Offline — showing cache    |  <- red banner offline
   +================================+
   |  v pull to refresh (haptics)   |
   | * Item 1             [pending] |  <- added offline, syncs later
   | * Item 2                       |
   | * Item 3                       |
   +================================+
   reload -> items still there (persisted)
   ```

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
