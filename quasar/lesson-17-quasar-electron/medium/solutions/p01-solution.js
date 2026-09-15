/**
 * Electron Application Menu
 * -------------------------
 * Builds the native application menu with three top-level menus:
 *
 *   File  — Open (CmdOrCtrl+O), Save (CmdOrCtrl+S), Quit (CmdOrCtrl+Q)
 *   Edit  — Undo (CmdOrCtrl+Z), Redo (CmdOrCtrl+Shift+Z)
 *   View  — Reload (CmdOrCtrl+R), Toggle DevTools (F12 / CmdOrCtrl+Shift+I)
 *
 * Each menu item sends an IPC message ('menu-action') to the focused
 * renderer window so the Vue app can react (e.g. open a file dialog).
 *
 * This file lives at src-electron/main-process/menu.js
 */

import { Menu, BrowserWindow, app } from 'electron'

/**
 * Build and set the application menu.
 * Call this after the app is ready and a window exists.
 */
export function setupMenu() {
  const isMac = process.platform === 'darwin'

  const template = [
    // ---- File menu -----------------------------------------------------
    {
      label: 'File',
      submenu: [
        {
          label: 'Open…',
          accelerator: 'CmdOrCtrl+O',
          click: () => sendMenuAction('open'),
        },
        {
          label: 'Save…',
          accelerator: 'CmdOrCtrl+S',
          click: () => sendMenuAction('save'),
        },
        { type: 'separator' },
        {
          label: 'Quit',
          accelerator: 'CmdOrCtrl+Q',
          role: isMac ? 'close' : 'quit',
        },
      ],
    },

    // ---- Edit menu -----------------------------------------------------
    {
      label: 'Edit',
      submenu: [
        { label: 'Undo', accelerator: 'CmdOrCtrl+Z', role: 'undo' },
        { label: 'Redo', accelerator: 'Shift+CmdOrCtrl+Z', role: 'redo' },
        { type: 'separator' },
        { label: 'Cut', accelerator: 'CmdOrCtrl+X', role: 'cut' },
        { label: 'Copy', accelerator: 'CmdOrCtrl+C', role: 'copy' },
        { label: 'Paste', accelerator: 'CmdOrCtrl+V', role: 'paste' },
      ],
    },

    // ---- View menu -----------------------------------------------------
    {
      label: 'View',
      submenu: [
        { label: 'Reload', accelerator: 'CmdOrCtrl+R', role: 'reload' },
        {
          label: 'Toggle DevTools',
          accelerator: isMac ? 'CmdOrCtrl+Alt+I' : 'F12',
          click: () => {
            const win = BrowserWindow.getFocusedWindow()
            win?.webContents.toggleDevTools()
          },
        },
        { type: 'separator' },
        { label: 'Actual Size', accelerator: 'CmdOrCtrl+0', role: 'resetZoom' },
        { label: 'Zoom In', accelerator: 'CmdOrCtrl+=', role: 'zoomIn' },
        { label: 'Zoom Out', accelerator: 'CmdOrCtrl+-', role: 'zoomOut' },
        { type: 'separator' },
        { label: 'Toggle Fullscreen', accelerator: 'F11', role: 'togglefullscreen' },
      ],
    },
  ]

  // macOS convention: first menu item is the app name
  if (isMac) {
    template.unshift({
      label: app.name,
      submenu: [
        { role: 'about', label: `About ${app.name}` },
        { type: 'separator' },
        { role: 'services' },
        { type: 'separator' },
        { role: 'hide' },
        { role: 'hideOthers' },
        { role: 'unhide' },
        { type: 'separator' },
        { role: 'quit' },
      ],
    })
  }

  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}

/**
 * Send a 'menu-action' IPC message to the focused renderer window.
 * The Vue app listens for this via the preload bridge.
 */
function sendMenuAction(action) {
  const win = BrowserWindow.getFocusedWindow()
  if (win) {
    win.webContents.send('menu-action', action)
  }
}
