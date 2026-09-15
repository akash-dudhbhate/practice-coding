# Lesson 16 — Debug Exercises

## Debug 01: Missing Capacitor
```bash
quasar build -m capacitor
# Error: capacitor not installed
```
<details><summary>Answer</summary>
**Bug:** Capacitor not installed.
**Fix:** `npm i @capacitor/core @capacitor/cli` and `quasar mode add capacitor`.
</details>

## Debug 02: No Platform Check
```javascript
if (showDesktop) { /* desktop only */ }
// runs on mobile too
```
<details><summary>Answer</summary>
**Bug:** No platform check — desktop code runs on mobile.
**Fix:** `if ($q.platform.is.mobile) { /* mobile only */ }`.
</details>

## Debug 03: Touch Targets Too Small
```css
.btn { padding: 4px; } /* too small for touch */
```
<details><summary>Answer</summary>
**Bug:** Touch target too small — hard to tap on mobile.
**Fix:** Minimum 44x44px touch targets. Use Quasar components (sized appropriately).
</details>
