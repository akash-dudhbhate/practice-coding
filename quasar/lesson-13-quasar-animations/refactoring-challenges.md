# Lesson 13 — Refactoring Challenges

## Refactor 01 (Easy): No Transition
### Before
```vue
<div v-if="show">Content</div>
```
### After
```vue
<transition name="fade"><div v-if="show">Content</div></transition>
```

## Refactor 02 (Medium): Animating Layout Properties
### Before
```css
.fade-enter-active { transition: width 0.3s; }
```
### After
```css
.fade-enter-active { transition: opacity 0.3s, transform 0.3s; }
```

## Refactor 03 (Hard: No Key in transition-group
### Before
```vue
<transition-group><div v-for="item in items" /></transition-group>
```
### After
```vue
<transition-group><div v-for="item in items" :key="item.id" /></transition-group>
```
