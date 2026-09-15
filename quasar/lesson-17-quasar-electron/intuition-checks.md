# Lesson 17 — Intuition Checks

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
