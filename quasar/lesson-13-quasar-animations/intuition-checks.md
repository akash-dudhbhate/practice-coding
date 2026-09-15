# Lesson 13 — Intuition Checks

## Check 01: Vue transitions
```vue
<transition name="slide">
  <div v-if="show">Content</div>
</transition>
```
<details><summary>Answer</summary>
Wraps element with v-if/v-show. Applies CSS classes during enter/leave. `name` prefix for CSS classes.
</details>

## Check 02: Transition classes
```css
.slide-enter-from { transform: translateX(100%); }
.slide-enter-active { transition: transform 0.3s; }
.slide-enter-to { transform: translateX(0); }
/* Same for leave */
```
<details><summary>Answer</summary>
6 classes: enter-from, enter-active, enter-to, leave-from, leave-active, leave-to. Vue 3 uses `-from` (Vue 2 used `-enter`).
</details>

## Check 03: Transition group
```vue
<transition-group name="list" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item }}</li>
</transition-group>
```
<details><summary>Answer</summary>
For lists — animates add/remove/move. Each item needs key. `tag` specifies wrapper element.
</details>

## Check 04: Quasar transitions
```vue
<q-transition name="slide-up">
  <div v-if="show">Content</div>
</q-transition>
```
<details><summary>Answer</summary>
Quasar provides built-in transitions: slide-up, slide-down, fade, scale, flip. No CSS needed — pre-built.
</details>

## Check 05: Performance
```css
/* Animate transform/opacity only — GPU accelerated */
/* Avoid animating width/height/top/left — causes reflow */
```
