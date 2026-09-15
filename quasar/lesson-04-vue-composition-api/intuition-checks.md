# Lesson 04 — Intuition Checks

## Check 01: Composition vs Options API
<details><summary>Answer</summary>
Options API — data, methods, computed as separate options. Composition API — organize by feature in setup(). Composition is more flexible, better TypeScript support, easier to extract logic.
</details>

## Check 02: ref vs reactive
```javascript
const count = ref(0);           // primitive
const state = reactive({ x: 0 }); // object
```
<details><summary>Answer</summary>
ref — for primitives (and objects). Access via `.value` in script. reactive — for objects only. Direct access. Use ref for simple values, reactive for complex objects.
</details>

## Check 03: computed
```javascript
const double = computed(() => count.value * 2);
```
<details><summary>Answer</summary>
Computed values are cached and reactive. Only recomputes when dependencies change. Like computed in Options API.
</details>

## Check 04: watch
```javascript
watch(count, (newVal, oldVal) => {
  console.log(`Changed from ${oldVal} to ${newVal}`);
});
```
<details><summary>Answer</summary>
Runs callback when watched value changes. `watchEffect` runs immediately and tracks dependencies automatically.
</details>

## Check 05: Lifecycle hooks
```javascript
onMounted(() => { console.log("mounted"); });
onUnmounted(() => { console.log("unmounted"); });
```
<details><summary>Answer</summary>
Composition API equivalents: `onMounted`, `onUnmounted`, `onUpdated`, etc. Must be called synchronously in setup().
</details>
