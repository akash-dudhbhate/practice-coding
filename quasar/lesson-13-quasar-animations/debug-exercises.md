# Lesson 13 — Debug Exercises

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
