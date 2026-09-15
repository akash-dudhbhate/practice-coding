# Lesson 16 — Refactoring Challenges

## Refactor 01 (Easy): No Platform Check
### Before
```javascript
if (showDesktop) { /* runs on mobile too */ }
```
### After
```javascript
if ($q.platform.is.mobile) { /* mobile only */ }
```

## Refactor 02 (Medium): Small Touch Targets
### Before
```css
.btn { padding: 4px; }
```
### After
```vue
<q-btn padding="md" />
```

## Refactor 03 (Hard: Responsive Web for Native Features
### Before
```bash
quasar build -m spa
```
### After
```bash
quasar build -m capacitor -T android
```
