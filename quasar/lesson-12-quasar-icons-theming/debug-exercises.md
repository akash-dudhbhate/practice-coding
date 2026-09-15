# Lesson 12 — Debug Exercises

## Debug 01: Wrong Icon Set
```javascript
// quasar.config.js
iconSet: 'fontawesome-v6'
// but not installed
```
<details><summary>Answer</summary>
**Bug:** Icon set not installed. Icons won't show.
**Fix:** `npm i @quasar/extras` and configure properly.
</details>

## Debug 02: CSS Variables Not Applied
```css
:root { --q-primary: #ff0000; }
```
<details><summary>Answer</summary>
**Bug:** Quasar uses `$primary` in SCSS, not CSS variables directly. Need to set in quasar.variables.scss.
**Fix:** Edit `src/css/quasar.variables.scss`: `$primary: #ff0000;`.
</details>

## Debug 03: Dark Mode Not Toggling
```javascript
$q.dark.toggle(); // nothing happens
```
<details><summary>Answer</summary>
**Bug:** Dark mode CSS not imported. Need `@import 'quasar/src/css/index.sass'` or dark mode extras.
**Fix:** Ensure dark mode is enabled in config.
</details>
