# Lesson 17 — Common Mistakes

## Mistake 01: Not adding electron mode
```bash
quasar mode add electron
```

## Mistake 02: Enabling nodeIntegration
```javascript
// WRONG — security risk
nodeIntegration: true
// CORRECT — use preload + contextBridge
```

## Mistake 03: No IPC bridge
```javascript
// preload.js
const { contextBridge, ipcRenderer } = require("electron");
contextBridge.exposeInMainWorld("api", {
  save: (data) => ipcRenderer.invoke("save", data)
});
```

## Mistake 04: Large bundle size
```javascript
// Electron apps are large (~100MB+)
// Minimize: exclude dev dependencies, use electron-builder
```

## Mistake 05: Not handling window close
```javascript
// Save state before close
window.onbeforeunload = () => { saveState(); };
```
