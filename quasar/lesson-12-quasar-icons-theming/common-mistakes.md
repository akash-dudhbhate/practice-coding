# Lesson 12 — Common Mistakes

## Mistake 01: Not installing icon extras
```bash
npm i @quasar/extras
# Then configure in quasar.config.js
```

## Mistake 02: Editing wrong file for theme
```css
/* WRONG — custom CSS */
/* CORRECT — quasar.variables.scss */
```

## Mistake 03: Not restarting after theme change
```bash
# SCSS changes require restart
quasar dev
```

## Mistake 04: Hardcoding colors
```vue
<!-- WRONG -->
<q-btn style="background: #1976d2" />
<!-- CORRECT -->
<q-btn color="primary" />
```

## Mistake 05: Not persisting dark mode
```javascript
// Save preference
watch(() => $q.dark.isActive, (val) => {
  localStorage.setItem('dark', val);
});
```
