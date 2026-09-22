/**
 * LESSON 17 — Quasar Electron
 * EASY P03 — IPC File Handlers
 * ============================================
 * CONCEPT: ipcMain.handle registers an async handler the renderer calls
 * via invoke(). File ops belong in the main process (it has fs access);
 * dialogs showOpenDialog/showSaveDialog return {canceled, filePaths}.
 *
 * PROBLEM: Register 'read-file' (open dialog → readFileSync → return
 * {name, content}, null on cancel, {error} on failure) and 'save-file'
 * (save dialog → writeFileSync → true/false, throw on failure). Use
 * try/catch around the fs calls.
 *
 * TRY THIS: ipcMain.handle('read-file', async () => {
 *   const r = await dialog.showOpenDialog({ properties: ['openFile'] });
 *   if (r.canceled) return null; return { name: path.basename(r.filePaths[0]),
 *   content: fs.readFileSync(r.filePaths[0], 'utf-8') } })
 *
 * EXPECTED OUTPUT: The renderer's readFile()/saveFile() calls open native
 * dialogs and read/write real files with errors handled.
 *
 * CHECK: python3 check.py easy/p03
 */
// TODO: write your IPC handlers here
