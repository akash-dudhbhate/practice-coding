# Lesson 20 — Refactoring Challenges

## Refactor 01 (Easy): No Project Structure
### Before
```html
<!-- index.html with all CSS and JS inline -->
<style>/* 500 lines */</style>
<script>/* 800 lines */</script>
```
### After
```html
<link rel="stylesheet" href="styles.css">
<script type="module" src="app.js"></script>
```

## Refactor 02 (Medium): Spaghetti Code
### Before
```javascript
function handleEverything() {
  fetchData();
  updateUI();
  saveToStorage();
  sendAnalytics();
}
```
### After
```javascript
async function loadAndDisplay() { await fetchData(); updateUI(); }
async function saveAndTrack() { saveToStorage(); sendAnalytics(); }
```

## Refactor 03 (Hard): No Build Tool
### Before
```html
<script src="lib1.js"></script>
<script src="lib2.js"></script>
<script src="lib3.js"></script>
<script src="app.js"></script>
```
### After
```bash
# Use Vite or similar
npm create vite@min
# imports bundled automatically
```
