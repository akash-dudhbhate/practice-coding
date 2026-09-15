# Lesson 03 — Refactoring Challenges

## Refactor 01 (Easy): Float for Layout
### Before
```css
.sidebar { float: left; width: 30%; }
.main { float: right; width: 70%; }
.clearfix::after { content: ""; clear: both; display: table; }
```
### After
```css
.container { display: flex; }
.sidebar { flex: 0 0 30%; }
.main { flex: 1; }
```

## Refactor 02 (Medium): Manual Centering
### Before
```css
.center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
```
### After
```css
.parent { display: flex; justify-content: center; align-items: center; }
```

## Refactor 03 (Hard): Fixed Widths
### Before
```css
.col1 { width: 200px; }
.col2 { width: 400px; }
.col3 { width: 600px; }
```
### After
```css
.row { display: flex; gap: 16px; }
.col { flex: 1; }
