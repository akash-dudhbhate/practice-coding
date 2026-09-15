# Lesson 07 — Intuition Checks

## Check 01: Pinia vs Vuex
<details><summary>Answer</summary>
Pinia is the new official Vue state management. Simpler than Vuex: no mutations (just actions), better TypeScript, better devtools, smaller. Vuex is legacy.
</details>

## Check 02: defineStore
```javascript
export const useStore = defineStore("main", {
  state: () => ({ count: 0 }),
  getters: { double: (state) => state.count * 2 },
  actions: { increment() { this.count++; } }
});
```
<details><summary>Answer</summary>
Three parts: state (data), getters (computed), actions (methods). `this` in actions refers to store. State is a function (fresh per instance).
</details>

## Check 03: Setup store
```javascript
export const useStore = defineStore("main", () => {
  const count = ref(0);
  const double = computed(() => count.value * 2);
  function increment() { count.value++; }
  return { count, double, increment };
});
```
<details><summary>Answer</summary>
Alternative syntax — like Composition API. More flexible, better TypeScript. Both syntaxes work.
</details>

## Check 04: Using in component
```javascript
const store = useStore();
store.count;       // state
store.double;      // getter
store.increment(); // action
```
<details><summary>Answer</summary>
Call `useStore()` in setup. Access state, getters, actions directly. Destructuring loses reactivity — use `storeToRefs`.
</details>

## Check 05: storeToRefs
```javascript
const store = useStore();
const { count, double } = storeToRefs(store); // reactive
const { increment } = store; // actions don't need refs
```
<details><summary>Answer</summary>
`storeToRefs` converts state and getters to refs (preserves reactivity). Actions are functions — destructure directly.
</details>
