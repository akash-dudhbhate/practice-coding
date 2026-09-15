# Lesson 01 — Common Mistakes

## Mistake 01: Wrong component names
```vue
<!-- WRONG -->
<q-button>
<!-- CORRECT -->
<q-btn>
```

## Mistake 02: Not using Quasar CLI
```bash
# WRONG — manual setup
npm install quasar
# CORRECT — use CLI
npm i -g @quasar/cli
quasar create my-app
```

## Mistake 03: Modifying quasar.config.js incorrectly
```javascript
// Always restart dev server after changing config
# quasar dev
```

## Mistake 04: Not using Quasar components
```vue
<!-- WRONG — reinventing the wheel -->
<button class="my-btn">
<!-- CORRECT — use Quasar -->
<q-btn>
```

## Mistake 05: Ignoring Material Design guidelines
```css
/* Quasar follows Material Design */
/* Don't fight it with custom CSS */
/* Use Quasar's theming system */
```
