# Lesson 17 — Concepts Explained (Quasar Electron Desktop Apps)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Electron in Quasar?

**What:** Quasar can build desktop apps (Windows, macOS, Linux) using Electron.

```bash
# Add Electron mode
quasar mode add electron

# Develop
quasar dev -m electron

# Build for production
quasar build -m electron
# Builds installers for the current platform
```

**Why it exists:** Web apps run in a browser → limited (no file system, no OS integration). Electron wraps the web app in a desktop window → full OS access → native desktop app from web code.

**Where it's used:** Desktop apps — VS Code, Slack, Discord are all Electron. Quasar makes it easy to build similar apps with Vue.

**What goes wrong without it:**
- Not installing Electron dependencies → `quasar dev -m electron` fails. Run `npm install` in `src-electron`.
- Building on one platform → installer for that platform only. Cross-compilation needs additional setup.
- Large bundle size → Electron includes Chromium → ~100MB minimum. Acceptable for desktop, not for web.

---

## Electron Main Process vs Renderer Process

**What:** Electron has two processes — Main (Node.js, OS access) and Renderer (Chromium, UI).

```js
// src-electron/electron-main.js (Main process)
import { app, BrowserWindow } from 'electron'

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            preload: 'electron-preload.js',
            contextIsolation: true,
        }
    })
    win.loadURL(process.env.APP_URL)
}

app.whenReady().then(createWindow)
```

```js
// src-electron/electron-preload.js (Bridge)
import { contextBridge, ipcRenderer } from 'electron'

contextBridge.exposeInMainWorld('electronAPI', {
    readFile: (path) => ipcRenderer.invoke('read-file', path),
    saveFile: (path, data) => ipcRenderer.invoke('save-file', path, data),
})
```

**Why it exists:** Security — the renderer (web page) shouldn't have direct Node.js access (malicious code could access the file system). The preload script exposes a safe, controlled API → security + functionality.

**Where it's used:** Every Electron app — main process for OS, renderer for UI, preload for the bridge.

**What goes wrong without it:**
- `contextIsolation: false` → security risk (renderer can access Node.js directly). Always use `true`.
- Not using preload → no bridge → can't access OS features from Vue. Always set up preload.
- Blocking the main process → UI freezes. Keep main process fast, delegate heavy work.

---

## IPC Communication

**What:** Inter-Process Communication — how the renderer (Vue) talks to the main process (Node.js).

```js
// Main process: handle requests
import { ipcMain } from 'electron'
import fs from 'fs'

ipcMain.handle('read-file', async (event, filePath) => {
    return fs.readFileSync(filePath, 'utf-8')
})

ipcMain.handle('save-file', async (event, filePath, data) => {
    fs.writeFileSync(filePath, data)
    return true
})
```

```js
// Preload: expose to renderer
contextBridge.exposeInMainWorld('electronAPI', {
    readFile: (path) => ipcRenderer.invoke('read-file', path),
    saveFile: (path, data) => ipcRenderer.invoke('save-file', path, data),
})
```

```js
// In Vue component (renderer):
async function loadFile() {
    const content = await window.electronAPI.readFile('/path/to/file.txt')
    console.log(content)
}

async function saveFile() {
    await window.electronAPI.saveFile('/path/to/file.txt', 'Hello World')
}
```

**Why it exists:** The renderer can't access Node.js directly (security). IPC → renderer sends a message → main process does the work → returns the result → safe and controlled.

**Where it's used:** Every Electron feature — file system, dialogs, menus, clipboard, notifications.

**What goes wrong without it:**
- `ipcRenderer.invoke` → returns a promise (async). `ipcRenderer.send` → fire and forget (no response). Use `invoke` for most cases.
- Not exposing the API in preload → `window.electronAPI` is undefined → error.
- Not handling errors in main → renderer gets a rejection → unhandled. Always try/catch in main.

---

## Native Menus

**What:** Add application menus (File, Edit, View, etc.).

```js
// Main process
import { Menu } from 'electron'

const template = [
    {
        label: 'File',
        submenu: [
            {
                label: 'Open',
                accelerator: 'CmdOrCtrl+O',
                click: () => mainWindow.webContents.send('menu-open')
            },
            {
                label: 'Save',
                accelerator: 'CmdOrCtrl+S',
                click: () => mainWindow.webContents.send('menu-save')
            },
            { type: 'separator' },
            { role: 'quit' }
        ]
    },
    {
        label: 'View',
        submenu: [
            { role: 'reload' },
            { role: 'toggledevtools' },
            { type: 'separator' },
            { role: 'resetzoom' },
            { role: 'zoomin' },
            { role: 'zoomout' },
        ]
    }
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
```

**Why it exists:** Desktop apps are expected to have menus → users expect File/Edit/View. Electron makes it easy → native menus → platform-appropriate (Mac top bar, Windows in-window).

**Where it's used:** Every desktop app — standard menus are expected.

**What goes wrong without it:**
- Mac → app menu should have app name first (auto-added by Electron). Don't override.
- `accelerator: 'CmdOrCtrl+O'` → Cmd on Mac, Ctrl on Windows/Linux. Use `CmdOrCtrl` for cross-platform.
- Menu click sends to renderer → renderer must listen: `ipcRenderer.on('menu-open', handler)`.

---

## File System Access

**What:** Read/write files on the user's computer.

```js
// Main process
import { ipcMain, dialog } from 'electron'
import fs from 'fs'

ipcMain.handle('open-file-dialog', async () => {
    const result = await dialog.showOpenDialog({
        properties: ['openFile'],
        filters: [{ name: 'Text', extensions: ['txt', 'md'] }]
    })
    if (result.canceled) return null
    const filePath = result.filePaths[0]
    return { path: filePath, content: fs.readFileSync(filePath, 'utf-8') }
})

ipcMain.handle('save-file-dialog', async (event, content) => {
    const result = await dialog.showSaveDialog({
        filters: [{ name: 'Text', extensions: ['txt'] }]
    })
    if (result.canceled) return null
    fs.writeFileSync(result.filePath, content)
    return result.filePath
})
```

**Why it exists:** Web apps can't access the file system (sandboxed). Electron → full file system access → text editors, image tools, any app that reads/writes files.

**Where it's used:** Text editors, image viewers, file managers, any app that works with local files.

**What goes wrong without it:**
- Not checking `result.canceled` → user cancels → `filePaths[0]` is undefined → crash.
- Not setting filters → user can select any file → might not be the expected format.
- Reading large files synchronously → blocks the main process → UI freezes. Use async `fs.promises`.

---

## System Tray

**What:** Add an icon to the system tray (taskbar).

```js
import { Tray, Menu, nativeImage } from 'electron'

let tray = null

function createTray() {
    const icon = nativeImage.createFromPath('path/to/icon.png')
    tray = new Tray(icon)

    const contextMenu = Menu.buildFromTemplate([
        { label: 'Show App', click: () => mainWindow.show() },
        { label: 'Quit', click: () => app.quit() }
    ])

    tray.setContextMenu(contextMenu)
    tray.setToolTip('My App')

    tray.on('click', () => {
        mainWindow.show()
    })
}
```

**Why it exists:** Background apps (chat, email, music) should minimize to tray → not clutter the taskbar. Tray icon → quick access → quit from tray → standard desktop UX.

**Where it's used:** Chat apps, download managers, background services, any app that runs in the background.

**What goes wrong without it:**
- Not destroying tray on quit → icon stays after app closes. `tray.destroy()` on `app.on('quit')`.
- Tray icon too large → OS resizes, might look bad. Use 16x16 or 22x22.
- Not handling click → user can't reopen the app from tray. Always add a click handler.

---

## Auto-Update

**What:** Automatically update the app when a new version is available.

```js
import { autoUpdater } from 'electron-updater'

autoUpdater.checkForUpdatesAndNotify()

autoUpdater.on('update-available', () => {
    mainWindow.webContents.send('update-available')
})

autoUpdater.on('update-downloaded', () => {
    mainWindow.webContents.send('update-downloaded')
    // Ask user to restart
})

// In renderer:
window.electronAPI.onUpdateDownloaded(() => {
    $q.dialog({
        title: 'Update Ready',
        message: 'A new version is downloaded. Restart?',
        ok: 'Restart',
        cancel: 'Later'
    }).onOk(() => {
        autoUpdater.quitAndInstall()
    })
})
```

**Why it exists:** Without auto-update, users run old versions → bugs, security issues. Auto-update → users always on the latest → fewer support tickets → better security.

**Where it's used:** Every production desktop app — users expect auto-updates.

**What goes wrong without it:**
- Not code-signing the app → auto-updater doesn't work (security requirement). Sign with Apple Developer ID / Windows cert.
- Not hosting the update feed → auto-updater can't find updates. Use GitHub Releases or a static server.
- Updating during critical work → user loses data. Ask before restarting.
