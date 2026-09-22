/**
 * LESSON 16 — Quasar Mobile (Capacitor)
 * EASY P01 — capacitor.config.js
 * ============================================
 * CONCEPT: capacitor.config.js is read by the Capacitor CLI when wrapping
 * your web build in a native shell. appId is the unique reverse-DNS id,
 * webDir points at Quasar's build output, and the plugins map configures
 * each native plugin.
 *
 * PROBLEM: Export a config object with appId, appName, webDir (e.g.
 * 'dist/capacitor'), a server block, and plugins config for Camera
 * (quality, saveToGallery, source) and Geolocation (enableHighAccuracy,
 * timeout). Document required iOS/Android permissions in comments.
 *
 * TRY THIS: const config = { appId: 'com.example.app', appName: '...',
 *   webDir: 'dist/capacitor', plugins: { Camera: { quality: 80,
 *   saveToGallery: true }, Geolocation: { enableHighAccuracy: true } } };
 * export default config
 *
 * EXPECTED OUTPUT: A config Capacitor would accept; comments note the
 * NSCameraUsageDescription / ACCESS_FINE_LOCATION native permissions.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your capacitor config here
