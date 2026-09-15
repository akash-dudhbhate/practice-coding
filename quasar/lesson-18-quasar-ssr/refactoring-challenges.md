# Lesson 18 — Refactoring Challenges

## Refactor 01 (Easy): window on Server
### Before
```javascript
if (window.innerWidth < 600)
```
### After
```javascript
if (process.env.CLIENT && window.innerWidth < 600)
```

## Refactor 02 (Medium): localStorage in setup
### Before
```javascript
setup() { const x = localStorage.getItem("key"); }
```
### After
```javascript
onMounted(() => { const x = localStorage.getItem("key"); });
```

## Refactor 03 (Hard: SPA for SEO
### Before
```bash
quasar build -m spa
```
### After
```bash
quasar build -m ssr
```
