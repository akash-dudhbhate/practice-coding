# Lesson 15 — Intuition Checks

## Check 01: What is PWA?
<details><summary>Answer</summary>
Progressive Web App — installable, offline-capable, push notifications. Works like native app but runs in browser. Quasar builds PWA with `quasar build -m pwa`.
</details>

## Check 02: manifest.json
```javascript
pwa: {
  manifest: {
    name: "My App",
    short_name: "App",
    display: "standalone",
    theme_color: "#000",
    icons: [...]
  }
}
```
<details><summary>Answer</summary>
Controls how PWA appears when installed. Name, icons, theme color, display mode. Essential for installability.
</details>

## Check 03: Service worker
<details><summary>Answer</summary>
Background script that caches files, enables offline. Quasar uses Workbox. `GenerateSW` — auto-generated. `InjectManifest` — custom service worker.
</details>

## Check 04: Installability
<details><summary>Answer</summary>
PWA is installable if: served over HTTPS, has manifest with name + icons + start_url, has service worker, has icons (192px + 512px). Browser shows install prompt.
</details>

## Check 05: Offline support
<details><summary>Answer</summary>
Service worker caches app shell (HTML, CSS, JS). On revisit without network, loads from cache. Data requests may fail — handle gracefully.
</details>
