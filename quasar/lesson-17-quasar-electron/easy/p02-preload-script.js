/**
 * LESSON 17 — Quasar Electron
 * EASY P02 — preload.js (contextBridge)
 * ============================================
 * CONCEPT: The preload script runs between Node and the web page. With
 * contextIsolation on, the renderer can't touch ipcRenderer directly —
 * contextBridge.exposeInMainWorld publishes a whitelisted API instead.
 *
 * PROBLEM: Expose `window.electronAPI` with three members: readFile()
 * → ipcRenderer.invoke('read-file'); saveFile(name, content) →
 * invoke('save-file', ...); onMenuAction(cb) → ipcRenderer.on('menu-action').
 *
 * TRY THIS: const { contextBridge, ipcRenderer } = require('electron')
 * contextBridge.exposeInMainWorld('electronAPI', { readFile: () =>
 *   ipcRenderer.invoke('read-file'), ... })
 *
 * EXPECTED OUTPUT: Renderer code can call window.electronAPI.readFile()
 * and receive menu-action events — nothing else leaks through.
 *
 * CHECK: python3 check.py easy/p02
 */
// TODO: write your preload script here
