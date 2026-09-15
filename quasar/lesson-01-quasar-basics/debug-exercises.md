# Lesson 01 — Debug Exercises

## Debug 01 (Easy: Missing Quasar Import
```vue
<template>
  <q-btn label="Click" />
</template>
```
<details><summary>Answer</summary>
**Bug:** Quasar components need the framework imported. If not auto-imported, component won't render.
**Fix:** Ensure `app.use(Quasar)` in main.js, or configure auto-import in quasar.config.js.
</details>

## Debug 02 (Medium: Wrong Component Name
```vue
<q-button label="Click" />
```
<details><summary>Answer</summary>
**Bug:** Component is `q-btn`, not `q-button`. Quasar uses abbreviated names.
**Fix:** `<q-btn label="Click" />`.
</details>

## Debug 03 (Hard: CSS Not Loading
```javascript
// quasar.config.js
framework: { css: false }  // Quasar CSS disabled
```
<details><summary>Answer</summary>
**Bug:** CSS disabled — components render unstyled.
**Fix:** Remove `css: false` or set to true (default).
</details>
