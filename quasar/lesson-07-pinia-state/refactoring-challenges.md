# Lesson 07 — Refactoring Challenges

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
