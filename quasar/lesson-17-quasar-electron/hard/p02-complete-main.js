/**
 * LESSON 17 — Quasar Electron
 * HARD P02 — Complete Electron Main Process
 * ============================================
 * CONCEPT: The production main file composes everything: a single-
 * instance lock, window creation, your menu and tray modules, a set of
 * ipcMain.handle endpoints (file, clipboard, notification, openExternal),
 * and electron-updater wiring that pushes 'update-available' events to
 * the renderer.
 *
 * PROBLEM: Write electron-main.js: requestSingleInstanceLock + focus on
 * second-instance; createWindow (1200x800, preload); on ready create
 * window + setupMenu + createTray + setupAutoUpdater; window-all-closed /
 * activate / quit→destroyTray lifecycle; IPC handlers for read-file,
 * save-file, clipboard-read/write, show-notification, open-external; and
 * an autoUpdater that checks for updates in production and notifies the
 * window.
 *
 * TRY THIS: const gotLock = app.requestSingleInstanceLock();
 * if (!gotLock) app.quit(); autoUpdater.on('update-available', i =>
 *   mainWindow?.webContents.send('update-available', i))
 *
 * EXPECTED OUTPUT: One entry point wiring every desktop feature together.
 *
 * CHECK: python3 check.py hard/p02
 */
// TODO: write your complete main process here
