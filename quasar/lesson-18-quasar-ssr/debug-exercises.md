# Lesson 18 — Debug Exercises

## Debug 01: Window Used on Server
```javascript
if (window.innerWidth < 600) { /* responsive */ }
// Error: window is not defined (SSR)
```
<details><summary>Answer</summary>
**Bug:** `window` not available during SSR. Only in browser.
**Fix:** `if (process.env.CLIENT && window.innerWidth < 600)`.
</details>

## Debug 02: localStorage on Server
```javascript
const token = localStorage.getItem("token");
// SSR: localStorage not defined
```
<details><summary>Answer</summary>
**Bug:** localStorage only exists in browser.
**Fix:** Wrap in `if (process.env.CLIENT)` or use `onMounted`.
</details>

## Debug 03: No Hydration Mismatch
```javascript
const time = new Date().toISOString();
// Server renders one time, client another → mismatch
```
<details><summary>Answer</summary>
**Bug:** Different output on server vs client → hydration error.
**Fix:** Use `onMounted` for time-dependent content, or use consistent data.
</details>
