# lesson-05-vue-reactivity — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: How Vue reactivity works
<details><summary>Answer</summary>
Vue 3 uses Proxy. When you access reactive data, Vue tracks it as a dependency. When data changes, Vue triggers updates. Automatic — no manual subscribe.
</details>

## Check 02: Reactive limitations
```javascript
const state = reactive({ date: new Date() });
state.date.setDate(15); // triggers update?
```
<details><summary>Answer</summary>
No — mutating Date object doesn't trigger reactivity (Proxy doesn't intercept Date methods). Need to reassign: `state.date = new Date(state.date)`.
</details>

## Check 03: watch vs watchEffect
```javascript
watch(count, (newVal) => { ... });      // explicit dependency
watchEffect(() => { console.log(count.value); }); // auto-tracks
```
<details><summary>Answer</summary>
watch — specify what to watch, callback gets old/new values. watchEffect — runs immediately, auto-tracks dependencies used inside. Use watch for specific values, watchEffect for side effects.
</details>

## Check 04: Computed caching
```javascript
const expensive = computed(() => heavyCalc(data.value));
console.log(expensive.value); // computes
console.log(expensive.value); // cached
data.value = "new";
console.log(expensive.value); // recomputes
```
<details><summary>Answer</summary>
Computed caches result. Only recomputes when dependencies change. Multiple accesses use cache. More efficient than methods.
</details>

## Check 05: Shallow reactivity
```javascript
const state = shallowReactive({ a: { b: 1 } });
state.a.b = 2; // not reactive
```
<details><summary>Answer</summary>
`shallowReactive` — only top-level properties are reactive. Nested changes don't trigger updates. Use for performance with deep objects you don't need to track.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Adding New Property
```javascript
const state = reactive({ user: { name: "A" } });
state.user.age = 25; // reactive?
```
<details><summary>Answer</summary>
In Vue 3, this IS reactive (Proxy-based). In Vue 2, it wasn't (needed `Vue.set`). Vue 3 fixed this.
</details>

## Debug 02 (Medium: Array Index Assignment
```javascript
const list = reactive([1, 2, 3]);
list[0] = 99; // reactive?
```
<details><summary>Answer</summary>
In Vue 3, yes (Proxy). In Vue 2, no (needed `Vue.set(list, 0, 99)`). Vue 3 handles this correctly.
</details>

## Debug 03 (Hard: Computed Not Updating
```javascript
const data = ref({ count: 0 });
const double = computed(() => data.value.count * 2);
data.value.count = 5; // does double update?
```
<details><summary>Answer</summary>
Yes — `data.value` is a reactive object. Changing `.count` triggers reactivity. `double` updates to 10.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Track Changes

### Approach 1: watch
```javascript
watch(count, (newVal) => { saveToLocalStorage(newVal); });
```

### Approach 2: watchEffect
```javascript
watchEffect(() => { saveToLocalStorage(count.value); });
```

**Winner:** Approach 1 — explicit, gets old value. Approach 2 for simple side effects.

---

## Problem: Derived State

### Approach 1: Method
```javascript
function fullName() { return first.value + " " + last.value; }
```
**Cons:** Recomputes every call.

### Approach 2: Computed
```javascript
const fullName = computed(() => first.value + " " + last.value);
```

**Winner:** Approach 2 — cached, reactive.
