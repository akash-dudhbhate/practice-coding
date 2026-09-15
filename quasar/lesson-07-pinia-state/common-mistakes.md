# Lesson 07 — Common Mistakes

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
