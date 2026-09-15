# Lesson 05 — Common Mistakes

## Mistake 01: Expecting Date mutation to trigger update
```javascript
// WRONG — no reactivity
state.date.setDate(15);
// CORRECT — reassign
state.date = new Date(state.date);
```

## Mistake 02: Using methods instead of computed
```javascript
// WRONG — recomputes every render
methods: { double() { return this.count * 2; } }
// CORRECT — cached
computed: { double() { return this.count * 2; } }
```

## Mistake 03: Deep watching when not needed
```javascript
// WRONG — expensive
watch(obj, handler, { deep: true });
// CORRECT — watch specific property
watch(() => obj.specificProp, handler)
```

## Mistake 04: Not cleaning up watchers
```javascript
const stop = watch(count, handler);
onUnmounted(() => stop()); // or it auto-stops in setup
```

## Mistake 05: Mutating props
```javascript
// WRONG — props are readonly
props.count++;
// CORRECT — emit event
emit("update:count", props.count + 1);
```
