# Lesson 07 — Approach Comparison

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
