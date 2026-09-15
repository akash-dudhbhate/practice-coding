/**
 * Electron System Tray
 * --------------------
 * Creates a system tray icon with a context menu (Show, Hide, Quit).
 * Left-click toggles window visibility.  The tray is destroyed when
 * the app quits to avoid lingering icons.
 *
 * This file lives at src-electron/main-process/tray.js
 */

import { Tray, Menu, BrowserWindow, app, nativeImage } from 'electron'
import * as path from 'path'

let tray = null

/**
 * Create the system tray icon and wire up its behaviour.
 * Call this after the main window has been created.
 *
 * @param {BrowserWindow} mainWindow
 */
export function createTray(mainWindow) {
  // Use a small 16×16 icon; adjust path to your project's icon
  const iconPath = path.join(__dirname, '../../icons/icon-16x16.png')
  const icon = nativeImage.createFromPath(iconPath)

  tray = new Tray(icon)
  tray.setToolTip('Quasar Electron App')

  // Context menu — Show, Hide, Quit
  const contextMenu = Menu.buildFromTemplate([
    {
      label: 'Show',
      click: () => {
        mainWindow.show()
        mainWindow.focus()
      },
    },
    {
      label: 'Hide',
      click: () => mainWindow.hide(),
    },
    { type: 'separator' },
    {
      label: 'Quit',
      click: () => {
        app.quit()
      },
    },
  ])

  tray.setContextMenu(contextMenu)

  // Left-click toggles window visibility
  tray.on('click', () => {
    if (mainWindow.isVisible()) {
      mainWindow.hide()
    } else {
      mainWindow.show()
      mainWindow.focus()
    }
  })

  // Prevent the app from quitting when the window is closed —
  // keep it running in the tray instead.
  mainWindow.on('close', (event) => {
    if (!app.isQuitting) {
      event.preventDefault()
      mainWindow.hide()
    }
  })
}

/**
 * Destroy the tray icon — call on app quit.
 */
export function destroyTray() {
  if (tray) {
    tray.destroy()
    tray = null
  }
}
