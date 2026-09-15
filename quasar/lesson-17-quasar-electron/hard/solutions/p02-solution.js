/**
 * Complete Electron Main Process
 * ------------------------------
 * Combines: window creation, application menu, system tray, IPC
 * handlers (file open/save, clipboard, notifications), auto-update
 * setup, and lifecycle handling (single-instance lock,
 * window-all-closed).
 *
 * This file replaces the default electron-main.js in a Quasar Electron
 * project.  It imports the menu and tray modules created in earlier
 * lessons.
 */

import { app, BrowserWindow, ipcMain, clipboard, Notification, shell } from 'electron'
import * as fs from 'fs'
import * as path from 'path'
import { setupMenu } from './menu.js'
import { createTray, destroyTray } from './tray.js'

// ---- Globals -------------------------------------------------------------
let mainWindow = null

// ---- Single-instance lock ------------------------------------------------
// Prevent multiple instances of the app from running simultaneously.
const gotLock = app.requestSingleInstanceLock()
if (!gotLock) {
  app.quit()
} else {
  app.on('second-instance', () => {
    // Focus the existing window when a second instance is launched
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore()
      mainWindow.focus()
    }
  })
}

// ---- Window creation -----------------------------------------------------
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, '../preload-process/preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
  })

  if (process.env.DEV) {
    mainWindow.loadURL(process.env.APP_URL)
  } else {
    mainWindow.loadFile('dist/electron/index.html')
  }

  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

// ---- App lifecycle -------------------------------------------------------
app.whenReady().then(() => {
  createWindow()
  setupMenu()
  createTray(mainWindow)
  setupAutoUpdater()
})

app.on('window-all-closed', () => {
  // On macOS keep the app running in the dock / tray
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

app.on('quit', () => {
  destroyTray()
})

// ---- IPC Handlers --------------------------------------------------------

// File: open
ipcMain.handle('read-file', async () => {
  const { dialog } = require('electron')
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openFile'],
    filters: [{ name: 'All Files', extensions: ['*'] }],
  })
  if (result.canceled) return null
  try {
    const content = fs.readFileSync(result.filePaths[0], 'utf-8')
    return { name: path.basename(result.filePaths[0]), content, path: result.filePaths[0] }
  } catch (err) {
    return { error: err.message }
  }
})

// File: save
ipcMain.handle('save-file', async (_e, fileName, content) => {
  const { dialog } = require('electron')
  const result = await dialog.showSaveDialog(mainWindow, {
    defaultPath: fileName || 'untitled.txt',
  })
  if (result.canceled) return false
  try {
    fs.writeFileSync(result.filePath, content, 'utf-8')
    return true
  } catch (err) {
    throw new Error(err.message)
  }
})

// Clipboard: write text
ipcMain.handle('clipboard-write', (_e, text) => {
  clipboard.writeText(text)
  return true
})

// Clipboard: read text
ipcMain.handle('clipboard-read', () => clipboard.readText())

// Notification: show a desktop notification
ipcMain.handle('show-notification', (_e, title, body) => {
  if (Notification.isSupported()) {
    new Notification({ title, body }).show()
    return true
  }
  return false
})

// Open URL in the user's default browser (not inside the app)
ipcMain.handle('open-external', (_e, url) => {
  shell.openExternal(url)
})

// ---- Auto-update ---------------------------------------------------------
/**
 * Set up electron-updater to check for updates automatically.
 * Requires the `electron-updater` package.
 */
function setupAutoUpdater() {
  try {
    const { autoUpdater } = require('electron-updater')

    autoUpdater.autoDownload = false
    autoUpdater.autoInstallOnAppQuit = true

    autoUpdater.on('update-available', (info) => {
      if (mainWindow) {
        mainWindow.webContents.send('update-available', info)
      }
    })

    autoUpdater.on('update-downloaded', () => {
      if (mainWindow) {
        mainWindow.webContents.send('update-downloaded')
      }
    })

    // Check for updates in production only
    if (!process.env.DEV) {
      autoUpdater.checkForUpdates()
    }
  } catch {
    // electron-updater not installed — skip auto-update
  }
}
