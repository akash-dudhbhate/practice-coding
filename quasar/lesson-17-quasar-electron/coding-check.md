# Lesson 17 — Coding Check

## Easy

### p01-solve.js — Electron main process
- [ ] `app` and `BrowserWindow` imported
- [ ] Window created (1200x800)
- [ ] App URL loaded
- [ ] `app.whenReady()` used
- [ ] Window close handled
- [ ] macOS activate handled (re-create window)

### p02-solve.js — Preload script
- [ ] `contextBridge` imported
- [ ] `ipcRenderer` imported
- [ ] `exposeInMainWorld` called
- [ ] `readFile` exposed (invoke)
- [ ] `saveFile` exposed (invoke)
- [ ] `onMenuAction` exposed (on listener)
- [ ] `contextIsolation` compatible

### p03-solve.js — IPC handlers
- [ ] `ipcMain.handle` for read-file
- [ ] `ipcMain.handle` for save-file
- [ ] `fs.readFileSync` used
- [ ] `fs.writeFileSync` used
- [ ] try/catch on both
- [ ] Errors returned (not thrown)

## Medium

### p01-solve.js — Application menu
- [ ] File menu (Open, Save, Quit)
- [ ] Edit menu (Undo, Redo)
- [ ] View menu (Reload, Toggle DevTools)
- [ ] Accelerators set (CmdOrCtrl+O, etc.)
- [ ] Click handlers send IPC to renderer
- [ ] `Menu.buildFromTemplate` used
- [ ] `Menu.setApplicationMenu` called

### p02-solve.vue — File editor component
- [ ] Open button calls `window.electronAPI`
- [ ] File dialog opened
- [ ] Content displayed in text area
- [ ] Save button writes changes
- [ ] Cancel handled (no crash)
- [ ] Errors handled (notification)

### p03-solve.js — System tray
- [ ] `Tray` imported
- [ ] Tray icon created
- [ ] Context menu (Show, Hide, Quit)
- [ ] Click handler (show/hide window)
- [ ] Tooltip set
- [ ] `tray.destroy()` on quit

## Hard

### p01-solve.vue — Complete text editor
- [ ] Open files (dialog)
- [ ] Edit content (text area)
- [ ] Save files (dialog)
- [ ] Unsaved changes tracked (dot in title)
- [ ] Confirm before closing with unsaved changes
- [ ] Recent files list
- [ ] Recent files persisted
- [ ] All file operations via IPC

### p02-solve.js — Complete Electron main
- [ ] Window creation
- [ ] Application menu
- [ ] System tray
- [ ] IPC handlers (file, clipboard, notifications)
- [ ] Auto-update setup
- [ ] Single instance lock
- [ ] `window-all-closed` handled
- [ ] Proper lifecycle management

### p03-solve.vue — Desktop settings app
- [ ] Window size/position persisted
- [ ] Theme toggle (dark/light, persisted)
- [ ] Startup behavior (minimize to tray)
- [ ] Auto-update settings (check on startup)
- [ ] Update notification
- [ ] Keyboard shortcuts list displayed
- [ ] All settings persisted (Electron Store)
- [ ] Clean settings UI
