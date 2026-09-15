# Lesson 04 — Refactoring Challenges

## Refactor 01 (Easy): Flex for Grid Layout
### Before
```css
.row { display: flex; flex-wrap: wrap; }
.col { flex: 1 1 33.33%; }
```
### After
```css
.grid { display: grid; grid-template-columns: repeat(3, 1fr); }
```

## Refactor 02 (Medium): Media Query for Columns
### Before
```css
.grid { grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1024px) { .grid { grid-template-columns: 1fr 1fr 1fr; } }
```
### After
```css
.grid { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
```

## Refactor 03 (Hard): Nested Flex for Grid
### Before
```css
.layout { display: flex; }
.sidebar { width: 250px; }
.content { display: flex; flex-direction: column; }
```
### After
```css
.layout { display: grid; grid-template-columns: 250px 1fr; }
