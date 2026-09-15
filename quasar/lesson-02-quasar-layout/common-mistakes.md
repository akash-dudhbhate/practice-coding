# Lesson 02 — Common Mistakes

## Mistake 01: Missing q-layout wrapper
```vue
<!-- WRONG -->
<q-header />
<!-- CORRECT -->
<q-layout><q-header /></q-layout>
```

## Mistake 02: q-page without q-page-container
```vue
<!-- WRONG -->
<q-layout><q-page /></q-layout>
<!-- CORRECT -->
<q-layout><q-page-container><q-page /></q-page-container></q-layout>
```

## Mistake 03: Wrong view string case
```vue
<!-- WRONG — lowercase -->
view="hhh"
<!-- CORRECT — uppercase for fixed -->
view="hHh"
```

## Mistake 04: Not using v-model for drawer
```vue
<!-- WRONG — can't control -->
<q-drawer />
<!-- CORRECT -->
<q-drawer v-model="drawerOpen" />
```

## Mistake 05: Hardcoded layout instead of Quasar's
```css
/* WRONG — custom CSS for layout */
/* CORRECT — use Quasar's layout system */
```
