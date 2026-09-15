# Lesson 17 — Approach Comparison

## Problem: Desktop App

### Approach 1: Electron
```bash
quasar build -m electron
```
**Pros:** Full Node.js access, mature. **Cons:** Large bundle.

### Approach 2: PWA
```bash
quasar build -m pwa
```
**Pros:** Small, web-based. **Cons:** Limited system access.

**Winner:** Electron for system features. PWA for simple apps.

---

## Problem: Secure IPC

### Approach 1: nodeIntegration
```javascript
nodeIntegration: true
```
**Cons:** Security risk.

### Approach 2: contextBridge
```javascript
contextBridge.exposeInMainWorld("api", { save });
```

**Winner:** Approach 2 — secure, best practice.
