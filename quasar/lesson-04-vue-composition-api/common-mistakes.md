# Lesson 04 — Common Mistakes

## Mistake 01: Forgetting .value
```javascript
// WRONG — in script
count = 5;
// CORRECT
count.value = 5;
```

## Mistake 02: Destructuring reactive
```javascript
// WRONG — loses reactivity
const { count } = reactive({ count: 0 });
// CORRECT
const { count } = toRefs(state);
// or use ref
const count = ref(0);
```

## Mistake 03: Not returning from setup()
```javascript
// If using setup() (not script setup)
setup() {
  const count = ref(0);
  return { count }; // must return!
}
```

## Mistake 04: Using watch when computed works
```javascript
// WRONG — manual tracking
watch(count, () => { double.value = count.value * 2; });
// CORRECT — computed
const double = computed(() => count.value * 2);
```

## Mistake 05: Lifecycle hooks outside setup
```javascript
// WRONG — must be in setup
onMounted(() => {}); // at module level
// CORRECT — inside setup
setup() { onMounted(() => {}); }
```
