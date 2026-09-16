/**
 * LESSON 17 — Quasar Electron
 * EASY P01 — electron-main.js Boilerplate
 * ============================================
 * CONCEPT: The main process is a Node.js script — it owns the app
 * lifecycle (app.whenReady, window-all-closed, activate) and creates
 * BrowserWindows that load your Quasar build. Keep a global window ref so
 * it isn't garbage-collected.
 *
 * PROBLEM: Write the main-process file: create a BrowserWindow
 * (1200x800, preload + contextIsolation), load the dev URL or built
 * index.html, null the ref on 'closed', quit on window-all-closed except
 * on macOS (darwin), and re-create on 'activate' when no windows exist.
 *
 * TRY THIS: app.whenReady().then(createWindow);
 * app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit() })
 *
 * EXPECTED OUTPUT: A main-process file Quasar Electron can boot: one
 * window appears, closes cleanly, and macOS dock-click recreates it.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your electron main process here
