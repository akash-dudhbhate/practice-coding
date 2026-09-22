# lesson-13-quasar-animations — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01: Missing Transition Component
```vue
<div v-if="show">Content</div>
```
<details><summary>Answer</summary>
**Bug:** No transition — appears/disappears instantly.
**Fix:** `<transition name="fade"><div v-if="show">Content</div></transition>`.
</details>

## Debug 02: Wrong CSS Class Names
```css
.fade-enter { opacity: 0; }
```
<details><summary>Answer</summary>
**Bug:** Vue uses `fade-enter-active`, `fade-enter-from`, `fade-enter-to`. Not just `fade-enter`.
**Fix:** `.fade-enter-active { transition: opacity 0.3s; } .fade-enter-from { opacity: 0; }`.
</details>

## Debug 03: Animation on q-layout
```vue
<transition><q-layout /></transition>
```
<details><summary>Answer</summary>
**Bug:** Can't transition q-layout directly. Use transitions on content inside.
**Fix:** Wrap inner content, not the layout component.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Animate Show/Hide

### Approach 1: CSS animation
```css
@keyframes fadeIn { from { opacity: 0; } }
.show { animation: fadeIn 0.3s; }
```

### Approach 2: Vue transition
```vue
<transition name="fade"><div v-if="show" /></transition>
```

**Winner:** Approach 2 — handles enter/leave automatically.

---

## Problem: List Animation

### Approach 1: transition
```vue
<transition><ul v-if="items.length" /></transition>
```

### Approach 2: transition-group
```vue
<transition-group name="list" tag="ul"><li v-for="..." :key="..." /></transition-group>
```

**Winner:** Approach 2 — animates individual items.
