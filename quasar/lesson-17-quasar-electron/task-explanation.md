# Lesson 17 — Quasar Electron Desktop Apps

## What you'll learn
- What Electron is in Quasar (desktop apps from web)
- Main process vs renderer process
- IPC communication (Vue ↔ Node.js)
- Native menus (File, Edit, View)
- File system access (open/save dialogs)
- System tray (background apps)
- Auto-update (keep users on latest)

## Lesson

### Enable Electron
```bash
quasar mode add electron
quasar dev -m electron
quasar build -m electron
```

### IPC bridge
```js
// Main: ipcMain.handle('read-file', handler)
// Preload: contextBridge.exposeInMainWorld('api', {...})
// Renderer: await window.api.readFile(path)
```

### File dialog
```js
const result = await dialog.showOpenDialog({ properties: ['openFile'] })
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Write an Electron main process file: create a BrowserWindow (1200x800), load the app URL, and handle window close (quit app on macOS). Include basic boilerplate.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------------------+ _
   | - [] x   MyApp                      (title)|
   +==========================================+
   |                                          |
   |        your Quasar app inside a          |  <- native 1200x800
   |        desktop window                    |     window
   +==========================================+
   close -> quits; macOS dock click -> recreates
   ```
2. `easy/p02-solve.js` — Write a preload script that exposes a safe API to the renderer: `readFile`, `saveFile`, and `onMenuAction`. Use `contextBridge.exposeInMainWorld`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   renderer  ->  window.electronAPI.readFile()
                 window.electronAPI.saveFile()
                 window.electronAPI.onMenuAction(cb)
   (nothing else crosses the bridge — safe surface)
   ```
3. `easy/p03-solve.js` — Write IPC handlers in the main process for `read-file` and `save-file` using `fs.readFileSync` and `fs.writeFileSync`. Handle errors with try/catch.

   WHAT IT SHOULD LOOK LIKE:
   ```
   readFile()  -> native Open dialog -> file contents
   saveFile()  -> native Save dialog -> writes file
   errors -> handled, returned as { error } objects
   ```

### Medium
4. `medium/p01-solve.js` — Create an application menu with File (Open, Save, Quit), Edit (Undo, Redo), and View (Reload, Toggle DevTools). Use accelerators (CmdOrCtrl+O, etc.). Send IPC messages to renderer on click.

   WHAT IT SHOULD LOOK LIKE:
   ```
   File        Edit        View
   +----------------+ +-------------+ +------------------+
   | Open   Ctrl+O  | | Undo Ctrl+Z | | Reload    Ctrl+R |
   | Save   Ctrl+S  | | Redo Ctrl+Y | | DevTools  F12    |
   | Quit   Ctrl+Q  | +-------------+ +------------------+
   +----------------+
   Open/Save clicks -> IPC event reaches the Vue app
   ```
5. `medium/p02-solve.vue` — Create a Vue component that uses the exposed Electron API: button to open a file dialog, display the file content in a text area, and a save button to write changes back. Handle cancel and errors.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Open File ]   notes.txt           <- filename shown
   +----------------------------------+
   | file contents appear here...     |  <- textarea, edits
   |                                  |     flag it dirty
   +----------------------------------+
   [ Save ]   <- writes back, clears the dirty flag
   ```
6. `medium/p03-solve.js` — Create a system tray icon with a context menu (Show, Hide, Quit). Handle click to show/hide the window. Destroy the tray on app quit. Include a tooltip.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Taskbar tray:  [app icon]   (window closed but app alive)
   right-click:
   +----------+
   | Show     |
   | Hide     |
   | Quit     |
   +----------+
   tooltip: "MyApp"
   ```

### Hard
7. `hard/p01-solve.vue` — Build a complete text editor: open files (dialog), edit (text area), save (dialog), track unsaved changes (dot in title), confirm before closing with unsaved changes, and recent files list (persisted). Use IPC for all file operations.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------------------+
   | MyEditor - notes.txt *                   |  <- dot = unsaved
   +==========================================+
   | [Open] [Save]     Recent: notes.txt, ... |
   |------------------------------------------|
   |                                          |
   |   text area with file content            |
   |                                          |
   +------------------------------------------+
   closing dirty -> "Save changes?" confirm
   ```
8. `hard/p02-solve.js` — Build a complete Electron main process: window creation, application menu, system tray, IPC handlers (file open/save, clipboard, notifications), auto-update setup, and proper lifecycle handling (single instance, window-all-closed).

   WHAT IT SHOULD LOOK LIKE:
   ```
   // main-process entry — wires everything:
   window + menu + tray + ipc handlers
   + auto-updater + single-instance lock
   (one file boots the whole desktop app)
   ```
9. `hard/p03-solve.vue` — Build a desktop settings app: window settings (size, position persisted), theme (dark/light, persisted), startup behavior (minimize to tray), auto-update settings (check on startup, notify on available), and keyboard shortcuts list. All settings persisted via Electron Store.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------------------+
   | SETTINGS                                 |
   | Dark theme            [ (o) ]            |  <- applies instantly
   | Minimize to tray      [ ( ) ]            |
   | Check updates on start[ (o) ]            |
   |------------------------------------------|
   | SHORTCUTS                                |
   |  Ctrl+O  Open   Ctrl+S  Save             |
   |  Ctrl+Q  Quit                            |
   +------------------------------------------+
   (all choices persist across app restarts)
   ```

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar Electron app.
