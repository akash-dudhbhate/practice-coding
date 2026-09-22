# lesson-17-quasar-electron — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: What is Electron?
<details><summary>Answer</summary>
Framework for building desktop apps with web technologies. Chromium renders UI, Node.js for system access. Quasar wraps it: `quasar build -m electron`.
</details>

## Check 02: Main vs renderer process
<details><summary>Answer</summary>
Main — Node.js, system access (files, menus, windows). Renderer — Chromium, UI (Vue app). Communicate via IPC. Security: renderer is sandboxed.
</details>

## Check 03: IPC
```javascript
// Main: ipcMain.handle("save", handler)
// Preload: contextBridge.exposeInMainWorld("api", { save })
// Renderer: window.api.save(data)
```
<details><summary>Answer</summary>
Inter-Process Communication. Main handles system operations. Renderer calls via exposed API. Preload bridges them securely.
</details>

## Check 04: Build targets
```bash
quasar build -m electron -T win  # Windows
quasar build -m electron -T mac  # macOS
quasar build -m electron -T linux
```
<details><summary>Answer</summary>
Builds native installer for target OS. Windows: .exe/.msi. Mac: .dmg. Linux: .deb/.AppImage.
</details>

## Check 05: Auto-update
<details><summary>Answer</summary>
Electron supports auto-updates via electron-updater. Check for new version, download, install. Configure update server URL.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): nodeIntegration
### Before
```javascript
nodeIntegration: true
```
### After
```javascript
// use preload + contextBridge
```

## Refactor 02 (Medium): No IPC Bridge
### Before
```javascript
window.electronAPI.save(data); // not set up
```
### After
```javascript
contextBridge.exposeInMainWorld("api", { save: (d) => ipcRenderer.invoke("save", d) });
```

## Refactor 03 (Hard: PWA for Desktop Features
### Before
```bash
quasar build -m pwa
```
### After
```bash
quasar build -m electron
```

---

## Approach Comparison — different ways to solve it

## Problem: Desktop App

### Approach 1: Electron
```bash
quasar build -m electron
```
**Pros:** Full Node.js access, mature. **Cons:** Large bundle.

### Approach 2: PWA
```bash
quasar build -m pwa
```
**Pros:** Small, web-based. **Cons:** Limited system access.

**Winner:** Electron for system features. PWA for simple apps.

---

## Problem: Secure IPC

### Approach 1: nodeIntegration
```javascript
nodeIntegration: true
```
**Cons:** Security risk.

### Approach 2: contextBridge
```javascript
contextBridge.exposeInMainWorld("api", { save });
```

**Winner:** Approach 2 — secure, best practice.
