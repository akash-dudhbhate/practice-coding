# Lesson 02 — Refactoring Challenges

## Refactor 01 (Easy): Repeated Properties
### Before
```css
.btn { padding: 10px; margin: 5px; border: 1px solid #ccc; }
.card { padding: 10px; margin: 5px; border: 1px solid #ccc; }
```
### After
```css
.btn, .card { padding: 10px; margin: 5px; border: 1px solid #ccc; }
```

## Refactor 02 (Medium): Magic Numbers
### Before
```css
.box { margin: 23px; padding: 17px; width: 347px; }
```
### After
```css
:root { --spacing: 16px; --width: 350px; }
.box { margin: var(--spacing); padding: var(--spacing); width: var(--width); }
```

## Refactor 03 (Hard): Over-Specific Selectors
### Before
```css
body div.container main section article p.text { color: blue; }
```
### After
```css
.text { color: blue; }
