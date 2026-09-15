# Lesson 16 — Coding Check

## Easy

### p01-solve.js — Capacitor config
- [ ] `appId` set (com.example.app)
- [ ] `appName` set
- [ ] `webDir` set to "dist"
- [ ] Camera plugin configured
- [ ] Geolocation plugin configured
- [ ] Permissions listed

### p02-solve.vue — Responsive layout
- [ ] Left drawer on desktop (`$q.platform.is.desktop`)
- [ ] Bottom tabs on mobile (`$q.platform.is.mobile`)
- [ ] 3 navigation items
- [ ] Icons and labels
- [ ] Layout switches correctly

### p03-solve.vue — Touch gestures
- [ ] `v-touch:swipe.left` used
- [ ] `v-touch:swipe.right` used
- [ ] `v-touch:hold` used
- [ ] Swipe left/right changes counter
- [ ] Long-press resets counter
- [ ] Current value displayed
- [ ] Instructions shown

## Medium

### p01-solve.vue — Camera component
- [ ] Capacitor Camera imported
- [ ] Button to take photo
- [ ] Photo displayed
- [ ] Permission denial handled
- [ ] Web fallback (file input)
- [ ] Quality parameter set

### p02-solve.vue — Geolocation component
- [ ] Capacitor Geolocation imported
- [ ] Button to get location
- [ ] Latitude/longitude displayed
- [ ] Map link or iframe shown
- [ ] Permission denial handled
- [ ] Error handling (timeout, unavailable)

### p03-solve.vue — Share component
- [ ] Capacitor Share imported
- [ ] Button to share
- [ ] Text/URL shared
- [ ] Web Share API fallback
- [ ] Clipboard fallback
- [ ] Notification on success
- [ ] Error handling

## Hard

### p01-solve.vue — Mobile photo gallery
- [ ] Camera integration (take photos)
- [ ] Photos displayed in grid
- [ ] Swipe to navigate between photos
- [ ] Long-press to delete
- [ ] Share button per photo
- [ ] Touch gestures used
- [ ] Empty state (no photos)
- [ ] Permission handling

### p02-solve.vue — Mobile-aware app shell
- [ ] Platform detection (web/iOS/Android)
- [ ] Bottom tabs on mobile
- [ ] Drawer on desktop
- [ ] Haptics on button press (mobile only)
- [ ] Safe area insets handled
- [ ] Platform-specific styling
- [ ] Capacitor Device plugin used

### p03-solve.vue — Offline-first mobile app
- [ ] Capacitor Storage for caching
- [ ] Online/offline detection
- [ ] Sync when online
- [ ] Offline banner shown
- [ ] Haptics for feedback
- [ ] Pull-to-refresh gesture (v-touch-pull)
- [ ] Data refetches on pull
- [ ] Smooth UX
