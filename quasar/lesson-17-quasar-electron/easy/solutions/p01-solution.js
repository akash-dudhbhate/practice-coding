/**
 * Electron Main Process — Basic Boilerplate
 * ------------------------------------------
 * Creates a BrowserWindow (1200×800), loads the Quasar app, and
 * handles the window-close lifecycle correctly (quit on all platforms
 * except macOS, where the app stays active in the dock).
 *
 * This file lives at src-electron/main-process/electron-main.js
 * in a standard Quasar Electron project.
 */

import { app, BrowserWindow } from 'electron'

// Keep a global reference to avoid garbage collection
let mainWindow

/**
 * Create the application window and load the Quasar build.
 */
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      // The preload script bridges safe APIs to the renderer
      preload: require('path').join(__dirname, '../preload-process/preload.js'),
      // Disable Node integration in the renderer for security
      nodeIntegration: false,
      contextIsolation: true,
    },
  })

  // In development load from the Vite dev server; in production load the built index.html
  if (process.env.DEV) {
    mainWindow.loadURL(process.env.APP_URL)
  } else {
    mainWindow.loadFile('dist/electron/index.html')
  }

  // Open DevTools automatically in dev mode
  if (process.env.DEBUGGING) {
    mainWindow.webContents.openDevTools()
  }

  // Dereference the window when it is closed
  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

// ---- App lifecycle -------------------------------------------------------

// Create the window when Electron has finished initialising
app.whenReady().then(createWindow)

// On macOS, re-create the window when the dock icon is clicked and no
// windows are open.
app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

// Quit the app when all windows are closed — except on macOS, where
// apps conventionally stay active until the user explicitly quits.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
