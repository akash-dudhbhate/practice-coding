# Lesson 05 — Refactoring Challenges

## Refactor 01 (Easy): Method Instead of Computed
### Before
```javascript
function double() { return count.value * 2; } // recomputes every call
```
### After
```javascript
const double = computed(() => count.value * 2);
```

## Refactor 02 (Medium): Deep Watch
### Before
```javascript
watch(obj, handler, { deep: true });
```
### After
```javascript
watch(() => obj.specificProp, handler);
```

## Refactor 03 (Hard: Mutating Props
### Before
```javascript
props.count++;
```
### After
```javascript
emit("update:count", props.count + 1);
```
