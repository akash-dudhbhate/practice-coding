/**
 * Electron Preload Script
 * -----------------------
 * Runs in an isolated context with access to a limited subset of Node
 * APIs.  Uses contextBridge.exposeInMainWorld to expose a safe,
 * curated API ("window.electronAPI") to the renderer process.
 *
 * Exposed methods:
 *   - readFile()       → invoke 'read-file' IPC handler, returns { content, name }
 *   - saveFile(name, content) → invoke 'save-file' IPC handler
 *   - onMenuAction(cb) → listen for 'menu-action' messages from the main process
 *
 * This file lives at src-electron/preload-process/preload.js
 */

const { contextBridge, ipcRenderer } = require('electron')

// Expose a minimal, safe API to the renderer (window.electronAPI)
contextBridge.exposeInMainWorld('electronAPI', {
  /**
   * Open a native file dialog in the main process and return the
   * selected file's name and content.
   * @returns {Promise<{ name: string, content: string } | null>}
   */
  readFile: () => ipcRenderer.invoke('read-file'),

  /**
   * Save content to disk via a native save dialog.
   * @param {string} fileName  - suggested file name
   * @param {string} content   - file contents
   * @returns {Promise<boolean>}  - true if saved, false if cancelled
   */
  saveFile: (fileName, content) =>
    ipcRenderer.invoke('save-file', fileName, content),

  /**
   * Register a callback that fires when the main process sends a
   * 'menu-action' event (e.g. user clicked File → Open).
   * @param {(action: string) => void} callback
   */
  onMenuAction: (callback) => {
    ipcRenderer.on('menu-action', (_event, action) => callback(action))
  },
})
