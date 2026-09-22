/**
 * LESSON 17 — Quasar Electron
 * MEDIUM P03 — System Tray
 * ============================================
 * CONCEPT: new Tray(nativeImage) puts an icon in the OS tray. Give it a
 * context menu (Menu.buildFromTemplate + setContextMenu) and a click
 * handler that toggles window visibility. Intercept the window 'close'
 * event to hide-to-tray unless the app is really quitting; destroy the
 * tray on quit.
 *
 * PROBLEM: Export createTray(mainWindow) — build the icon, set a tooltip,
 * add a context menu with Show / Hide / Quit, toggle show/hide on tray
 * click, and preventDefault on 'close' to hide instead. Export
 * destroyTray() to clean up.
 *
 * TRY THIS: tray.on('click', () => mainWindow.isVisible()
 *   ? mainWindow.hide() : (mainWindow.show(), mainWindow.focus()))
 * mainWindow.on('close', (e) => { if (!app.isQuitting) { e.preventDefault(); mainWindow.hide() } })
 *
 * EXPECTED OUTPUT: Closing the window leaves the app in the tray; the
 * menu can show/hide/quit it.
 *
 * CHECK: python3 check.py medium/p03
 */
// TODO: write your tray module here
