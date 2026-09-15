# Lesson 04 — Debug Exercises

## Debug 01 (Easy: setup Without Return
```vue
<script setup>
const count = ref(0);
// count not accessible in template
</script>
```
<details><summary>Answer</summary>
**Bug:** With `<script setup>`, variables ARE accessible (auto-exposed). But with `setup()` function, must return them.
**Fix:** If using `setup()`: `return { count };`. If `<script setup>`: already works.
</details>

## Debug 02 (Medium: ref Not Unwrapped in Script
```javascript
const count = ref(0);
console.log(count); // Ref object, not 0
```
<details><summary>Answer</summary>
**Bug:** In script, need `.value` to access ref value. In template, auto-unwrapped.
**Fix:** `console.log(count.value)`.
</details>

## Debug 03 (Hard: Reactive Object Destructured
```javascript
const state = reactive({ count: 0 });
const { count } = state; // loses reactivity!
```
<details><summary>Answer</summary>
**Bug:** Destructuring reactive object loses reactivity.
**Fix:** Use `toRefs`: `const { count } = toRefs(state);`.
</details>
