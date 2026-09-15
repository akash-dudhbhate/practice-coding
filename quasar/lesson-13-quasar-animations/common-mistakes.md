# Lesson 13 — Common Mistakes

## Mistake 01: No transition wrapper
```vue
<!-- WRONG — instant show/hide -->
<div v-if="show" />
<!-- CORRECT -->
<transition name="fade"><div v-if="show" /></transition>
```

## Mistake 02: Wrong CSS class names
```css
/* WRONG — Vue 2 syntax */
.fade-enter { }
/* CORRECT — Vue 3 */
.fade-enter-from { }
```

## Mistake 03: Animating layout properties
```css
/* WRONG — janky */
.fade-enter-active { transition: width 0.3s; }
/* CORRECT */
.fade-enter-active { transition: opacity 0.3s, transform 0.3s; }
```

## Mistake 04: Missing key in transition-group
```vue
<!-- WRONG — no key -->
<transition-group><div v-for="item in items" /></transition-group>
<!-- CORRECT -->
<transition-group><div v-for="item in items" :key="item.id" /></transition-group>
```

## Mistake 05: Not respecting prefers-reduced-motion
```css
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; }
}
```
