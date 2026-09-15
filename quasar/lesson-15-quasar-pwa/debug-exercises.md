# Lesson 15 — Debug Exercises

## Debug 01: Missing manifest
```javascript
// quasar.config.js
pwa: { manifest: {} } // empty
```
<details><summary>Answer</summary>
**Bug:** Empty manifest — no app name, icons, theme color. PWA not installable.
**Fix:** Configure name, short_name, icons, theme_color, display.
</details>

## Debug 02: No Service Worker
```javascript
pwa: { workboxPluginMode: null }
```
<details><summary>Answer</summary>
**Bug:** No service worker — no offline support.
**Fix:** Set `workboxPluginMode: "GenerateSW"` or `"InjectManifest"`.
</details>

## Debug 03: Icons Missing
```bash
# No icons in public/icons/
```
<details><summary>Answer</summary>
**Bug:** No app icons — can't install PWA.
**Fix:** Add icons (192x192, 512x512 minimum) in `public/icons/`.
</details>
