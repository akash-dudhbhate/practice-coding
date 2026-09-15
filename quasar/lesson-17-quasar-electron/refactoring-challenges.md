# Lesson 17 — Refactoring Challenges

## Refactor 01 (Easy): nodeIntegration
### Before
```javascript
nodeIntegration: true
```
### After
```javascript
// use preload + contextBridge
```

## Refactor 02 (Medium): No IPC Bridge
### Before
```javascript
window.electronAPI.save(data); // not set up
```
### After
```javascript
contextBridge.exposeInMainWorld("api", { save: (d) => ipcRenderer.invoke("save", d) });
```

## Refactor 03 (Hard: PWA for Desktop Features
### Before
```bash
quasar build -m pwa
```
### After
```bash
quasar build -m electron
```
