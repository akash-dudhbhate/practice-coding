# Lesson 20 — Debug Exercises

## Debug 01: Wrong Build Mode
```bash
quasar build  # defaults to SPA, but need PWA
```
<details><summary>Answer</summary>
**Bug:** Default mode is SPA. Need to specify.
**Fix:** `quasar build -m pwa` or `quasar build -m ssr`.
</details>

## Debug 02: Environment Variables Not Set
```bash
quasar build
# VITE_API_URL not set — uses undefined
```
<details><summary>Answer</summary>
**Bug:** Env vars not configured for production.
**Fix:** Create `.env.production` with `VITE_API_URL=https://api.example.com`.
</details>

## Debug 03: No Base Path
```javascript
// Deploying to subdirectory: example.com/app/
// Assets load from root — 404
```
<details><summary>Answer</summary>
**Bug:** Base path not configured for subdirectory deployment.
**Fix:** `build: { publicPath: "/app/" }` in quasar.config.js.
</details>
