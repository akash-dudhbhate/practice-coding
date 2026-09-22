# lesson-07-pinia-state — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not exporting store
```javascript
// WRONG — can't import
const useStore = defineStore(...)
// CORRECT
export const useStore = defineStore(...)
```

## Mistake 02: Destructuring without storeToRefs
```javascript
// WRONG — loses reactivity
const { count } = useStore();
// CORRECT
const { count } = storeToRefs(useStore());
```

## Mistake 03: Using state as object
```javascript
// WRONG — shared across instances
state: { count: 0 }
// CORRECT — function for fresh state
state: () => ({ count: 0 })
```

## Mistake 04: Not using actions for mutations
```javascript
// WORKS but not tracked in devtools
store.count++;
// BETTER
store.increment();
```

## Mistake 05: Creating store inside component
```javascript
// WRONG — new store each call
function Component() { const store = defineStore(...) }
// CORRECT — define at module level
export const useStore = defineStore(...)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Vuex
### Before
```javascript
new Vuex.Store({ state, mutations, actions, getters });
```
### After
```javascript
export const useStore = defineStore("main", { state, getters, actions });
```

## Refactor 02 (Medium): Destructuring Store
### Before
```javascript
const store = useStore();
const count = store.count; // not reactive
```
### After
```javascript
const store = useStore();
const { count } = storeToRefs(store);
```

## Refactor 03 (Hard: State as Object
### Before
```javascript
state: { count: 0 } // shared across instances
```
### After
```javascript
state: () => ({ count: 0 })
```

---

## Approach Comparison — different ways to solve it

## Problem: State Management

### Approach 1: Pinia
```javascript
export const useStore = defineStore("main", { state, getters, actions });
```

### Approach 2: Vuex
```javascript
export default new Vuex.Store({ state, mutations, actions, getters });
```

**Winner:** Approach 1 — Pinia is the new standard. Simpler, no mutations.

---

## Problem: Store Syntax

### Approach 1: Options
```javascript
defineStore("main", { state: () => ({}), getters: {}, actions: {} });
```

### Approach 2: Setup
```javascript
defineStore("main", () => { const count = ref(0); return { count }; });
```

**Winner:** Approach 2 for TypeScript. Approach 1 for familiarity.
