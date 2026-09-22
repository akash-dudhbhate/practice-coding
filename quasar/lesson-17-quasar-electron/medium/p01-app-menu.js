/**
 * LESSON 17 — Quasar Electron
 * MEDIUM P01 — Application Menu
 * ============================================
 * CONCEPT: Menu.buildFromTemplate takes a template array of
 * {label, submenu:[{label, accelerator, click|role}]} items. `role` gives
 * native behavior for free (undo, reload, quit); `click` lets you send a
 * webContents.send('menu-action', ...) to the renderer.
 *
 * PROBLEM: Export setupMenu() building File (Open CmdOrCtrl+O, Save
 * CmdOrCtrl+S → send 'menu-action', Quit), Edit (Undo/Redo/Cut/Copy/Paste
 * roles), and View (Reload, Toggle DevTools, zoom, fullscreen) — then
 * Menu.setApplicationMenu. Add the macOS app-name first menu when on
 * darwin.
 *
 * TRY THIS: { label: 'Open…', accelerator: 'CmdOrCtrl+O',
 *   click: () => sendMenuAction('open') } where sendMenuAction does
 *   BrowserWindow.getFocusedWindow()?.webContents.send('menu-action', a)
 *
 * EXPECTED OUTPUT: A native menu where Open/Save reach the Vue app via
 * IPC and Edit/View items work natively.
 *
 * CHECK: python3 check.py medium/p01
 */
// TODO: write your application menu here
