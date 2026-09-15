# Lesson 15 — Refactoring Challenges

## Refactor 01 (Easy): Empty Manifest
### Before
```javascript
pwa: { manifest: {} }
```
### After
```javascript
pwa: { manifest: { name: "App", icons: [...] } }
```

## Refactor 02 (Medium): No Service Worker
### Before
```javascript
pwa: { workboxPluginMode: null }
```
### After
```javascript
pwa: { workboxPluginMode: "GenerateSW" }
```

## Refactor 03 (Hard: SPA for Installable App
### Before
```bash
quasar build -m spa
```
### After
```bash
quasar build -m pwa
```
