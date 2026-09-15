/**
 * Electron IPC Handlers — File Read / Save
 * ----------------------------------------
 * Registers 'read-file' and 'save-file' IPC handlers in the main
 * process.  The renderer invokes these through the preload bridge
 * (ipcRenderer.invoke → ipcMain.handle).
 *
 * Uses fs.readFileSync / fs.writeFileSync with try/catch error
 * handling so a failed read/write does not crash the app.
 *
 * This code is added to the main process file (electron-main.js)
 * after `app.whenReady()`.
 */

import { app, BrowserWindow, ipcMain, dialog } from 'electron'
import * as fs from 'fs'
import * as path from 'path'

// ---- read-file handler ---------------------------------------------------
/**
 * Show an open-file dialog, read the selected file, and return its
 * name and content.  Returns null if the user cancels.
 */
ipcMain.handle('read-file', async () => {
  const win = BrowserWindow.getFocusedWindow()

  const result = await dialog.showOpenDialog(win, {
    title: 'Open File',
    properties: ['openFile'],
    filters: [
      { name: 'Text Files', extensions: ['txt', 'md', 'json', 'js', 'vue'] },
      { name: 'All Files', extensions: ['*'] },
    ],
  })

  // User cancelled the dialog
  if (result.canceled || result.filePaths.length === 0) {
    return null
  }

  const filePath = result.filePaths[0]

  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    return {
      name: path.basename(filePath),
      content,
    }
  } catch (err) {
    // Return an error object so the renderer can display a message
    return { error: err.message }
  }
})

// ---- save-file handler ---------------------------------------------------
/**
 * Show a save-file dialog and write the provided content to the
 * chosen path.  Returns true on success, false if cancelled.
 */
ipcMain.handle('save-file', async (_event, fileName, content) => {
  const win = BrowserWindow.getFocusedWindow()

  const result = await dialog.showSaveDialog(win, {
    title: 'Save File',
    defaultPath: fileName || 'untitled.txt',
    filters: [
      { name: 'Text Files', extensions: ['txt', 'md', 'json', 'js', 'vue'] },
      { name: 'All Files', extensions: ['*'] },
    ],
  })

  if (result.canceled || !result.filePath) {
    return false
  }

  try {
    fs.writeFileSync(result.filePath, content, 'utf-8')
    return true
  } catch (err) {
    // Re-throw so the renderer's invoke() promise rejects
    throw new Error(`Failed to save file: ${err.message}`)
  }
})
