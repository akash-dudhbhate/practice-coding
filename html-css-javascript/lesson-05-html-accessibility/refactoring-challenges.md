# Lesson 05 — Refactoring Challenges

## Refactor 01 (Easy): Fixed Pixel Widths
### Before
```css
.container { width: 1200px; }
```
### After
```css
.container { max-width: 1200px; width: 100%; }
```

## Refactor 02 (Medium): Many Media Queries
### Before
```css
@media (max-width: 1200px) { .grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 900px) { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px) { .grid { grid-template-columns: 1fr; } }
```
### After
```css
.grid { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
```

## Refactor 03 (Hard): Device-Specific Breakpoints
### Before
```css
@media (max-width: 768px) { /* iPad */ }
@media (max-width: 414px) { /* iPhone */ }
```
### After
```css
/* Content-based breakpoints, not device-based */
@media (max-width: 600px) { /* content needs 1 col */ }
