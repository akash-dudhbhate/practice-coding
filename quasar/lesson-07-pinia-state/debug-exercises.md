# Lesson 07 — Debug Exercises

## Debug 01 (Easy: Not Exporting Store
```javascript
const useCounter = defineStore("counter", { ... });
// not exported
```
<details><summary>Answer</summary>
**Bug:** Store not exported — can't import in components.
**Fix:** `export const useCounter = defineStore(...)`.
</details>

## Debug 02 (Medium: Mutating State Directly
```javascript
const store = useCounter();
store.count = 5; // works but not recommended
```
<details><summary>Answer</summary>
Works in Pinia (unlike Redux), but actions are preferred for clarity and devtools tracking.
**Fix:** `store.increment()` or `store.$patch({ count: 5 })`.
</details>

## Debug 03 (Hard: Computed Not Reactive
```javascript
const store = useCounter();
const double = computed(() => store.count * 2);
// store.count changes but double doesn't update
```
<details><summary>Answer</summary>
Should work. If not, check that you're using `store.count` (reactive) not a destructured value (loses reactivity). Use `storeToRefs`.
**Fix:** `const { count } = storeToRefs(store); const double = computed(() => count.value * 2);`.
</details>
