# Lesson 17 — Debug Exercises

## Debug 01: Missing Electron Mode
```bash
quasar dev -m electron
# Error: electron mode not added
```
<details><summary>Answer</summary>
**Bug:** Electron mode not added.
**Fix:** `quasar mode add electron`.
</details>

## Debug 02: Node Integration Disabled
```javascript
// preload.js
const { ipcRenderer } = require('electron');
// Error: require not defined
```
<details><summary>Answer</summary>
**Bug:** Node integration disabled by default in newer Electron.
**Fix:** Use preload script or enable `nodeIntegration: true` (less secure).
</details>

## Debug 03: No IPC Communication
```javascript
// Renderer process
window.electronAPI.saveFile(data);
// No preload bridge set up
```
<details><summary>Answer</summary>
**Bug:** No IPC bridge — renderer can't call main process.
**Fix:** Set up preload with `contextBridge.exposeInMainWorld`.
</details>
