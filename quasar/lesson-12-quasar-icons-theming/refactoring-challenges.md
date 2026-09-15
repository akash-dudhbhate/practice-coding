# Lesson 12 — Refactoring Challenges

## Refactor 01 (Easy): Hardcoded Colors
### Before
```vue
<q-btn style="background: #1976d2" />
```
### After
```vue
<q-btn color="primary" />
```

## Refactor 02 (Medium): CSS Overrides
### Before
```css
.q-btn { background: red !important; }
```
### After
```scss
$primary: #ff0000;
```

## Refactor 03 (Hard: Manual Dark Mode
### Before
```css
.dark { background: #000; color: #fff; }
```
### After
```javascript
$q.dark.set(true);
```
