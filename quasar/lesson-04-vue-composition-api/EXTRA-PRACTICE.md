# lesson-04-vue-composition-api — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: setup Without Return
```vue
<script setup>
const count = ref(0);
// count not accessible in template
</script>
```
<details><summary>Answer</summary>
**Bug:** With `<script setup>`, variables ARE accessible (auto-exposed). But with `setup()` function, must return them.
**Fix:** If using `setup()`: `return { count };`. If `<script setup>`: already works.
</details>

## Debug 02 (Medium: ref Not Unwrapped in Script
```javascript
const count = ref(0);
console.log(count); // Ref object, not 0
```
<details><summary>Answer</summary>
**Bug:** In script, need `.value` to access ref value. In template, auto-unwrapped.
**Fix:** `console.log(count.value)`.
</details>

## Debug 03 (Hard: Reactive Object Destructured
```javascript
const state = reactive({ count: 0 });
const { count } = state; // loses reactivity!
```
<details><summary>Answer</summary>
**Bug:** Destructuring reactive object loses reactivity.
**Fix:** Use `toRefs`: `const { count } = toRefs(state);`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Options API for Simple Component
### Before
```javascript
export default { data() { return { count: 0 }; }, methods: { inc() { this.count++; } } }
```
### After
```javascript
const count = ref(0);
const inc = () => count.value++;
```

## Refactor 02 (Medium): setup() Function
### Before
```javascript
export default {
  setup() {
    const count = ref(0);
    return { count };
  }
}
```
### After
```vue
<script setup>
const count = ref(0);
</script>
```

## Refactor 03 (Hard: Destructured Reactive
### Before
```javascript
const state = reactive({ count: 0 });
const { count } = state; // loses reactivity
```
### After
```javascript
const state = reactive({ count: 0 });
const { count } = toRefs(state);
```

---

## Approach Comparison — different ways to solve it

## Problem: Component Logic

### Approach 1: Options API
```javascript
export default {
  data() { return { count: 0 }; },
  methods: { increment() { this.count++; } },
  computed: { double() { return this.count * 2; } }
}
```

### Approach 2: Composition API
```javascript
const count = ref(0);
const increment = () => count.value++;
const double = computed(() => count.value * 2);
```

**Winner:** Approach 2 — better organization, TypeScript, reusability.

---

## Problem: Reactive State

### Approach 1: ref
```javascript
const count = ref(0);
const name = ref("");
```

### Approach 2: reactive
```javascript
const state = reactive({ count: 0, name: "" });
```

**Winner:** ref for independent values. reactive for grouped state.
