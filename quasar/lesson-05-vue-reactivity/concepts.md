# Lesson 05 — Concepts Explained (Vue Reactivity System)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Ref vs Reactive — When to Use Which

**What:** `ref()` wraps any value (primitive or object) in a reactive container accessed via `.value`. `reactive()` makes an existing object's properties reactive directly.

```vue
<script setup>
import { ref, reactive } from 'vue'

// ref: best for single values
const count = ref(0)
const name = ref('Alice')
const isLoading = ref(false)

// reactive: best for grouped object state
const form = reactive({
  username: '',
  password: '',
  remember: false
})

// ref with object: works, but .value is the object
const user = ref({ name: 'Alice', age: 25 })
user.value.name = 'Bob'  // .value to access the object
</script>
```

**Why it exists:** Vue needs to track when values change to trigger UI updates. Primitives (numbers, strings, booleans) can't be made reactive by wrapping an object — `reactive(5)` doesn't work. `ref()` solves this by wrapping the value in a `{ value: T }` container. `reactive()` is optimized for objects — it uses Proxy to intercept property access/mutation without a `.value` wrapper.

**Where it's used:** `ref()` — single values (counters, toggles, strings, fetched data). `reactive()` — grouped state (form objects, user profiles, configuration). Rule of thumb: use `ref()` for primitives, `reactive()` for objects with multiple related properties.

**What goes wrong without it:**
- `reactive(0)` → doesn't work, returns a non-reactive value. Use `ref(0)`.
- `ref` for a huge object with 20 properties → verbose, every access needs `.value`. Use `reactive` instead.
- Mixing both for the same state → `const state = reactive({ count: 0 })` + `const double = ref(computed(() => state.count * 2))` → confusing. Pick one approach per state group.

---

## Deep Reactivity — Nested Object Tracking

**What:** Vue's reactivity system tracks changes at ALL levels of an object — not just top-level properties. Nested objects, arrays, and maps are all reactive.

```vue
<script setup>
import { reactive, ref } from 'vue'

const state = reactive({
  user: {
    name: 'Alice',
    preferences: {
      theme: 'dark',
      fontSize: 14
    }
  },
  items: [
    { id: 1, name: 'Item 1' }
  ]
})

// ALL of these trigger reactivity:
state.user.name = 'Bob'                          // top-level
state.user.preferences.theme = 'light'           // nested 2 levels deep
state.user.preferences.fontSize = 16             // nested 2 levels deep
state.items.push({ id: 2, name: 'Item 2' })      // array mutation
state.items[0].name = 'Updated Item'             // array element property
</script>
```

With `ref`, deep reactivity also works:
```javascript
const data = ref({ nested: { value: 1 } })
data.value.nested.value = 2  // triggers reactivity
```

**Why it exists:** Real-world data is deeply nested — a user has a profile, which has settings, which have preferences. If reactivity only tracked top-level properties, you'd need to reassign the entire object to trigger an update. Deep reactivity means you can mutate any nested property and Vue detects it.

**Where it's used:** Anytime you have nested objects — user profiles, form data with sections, API response data, configuration trees.

**What goes wrong without it:**
- Adding a NEW property to an object → `state.newProp = 'value'` → in Vue 2 this wasn't reactive (fixed in Vue 3 with Proxy). In Vue 3, this works.
- Replacing a nested object entirely → `state.user = { name: 'Bob' }` → works in Vue 3 (Proxy intercepts the set). But if you destructured first, the old reference is stale.
- Using `Object.assign()` on reactive → `Object.assign(state, { newKey: 'val' })` → works in Vue 3. In Vue 2 it didn't.

---

## WatchEffect — Auto-Tracked Reactive Effect

**What:** `watchEffect()` runs a callback immediately, automatically tracks any reactive dependencies accessed inside it, and re-runs when any of them change.

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')
const age = ref(25)

// Auto-tracks firstName, lastName, and age
watchEffect(() => {
  console.log(`${firstName.value} ${lastName.value}, age ${age.value}`)
  document.title = `${firstName.value} ${lastName.value}`
})
// Runs immediately: "John Doe, age 25"
// If firstName changes → re-runs automatically
</script>
```

Unlike `watch()`, you don't specify what to watch — Vue tracks it automatically based on what you access inside the callback.

**Why it exists:** When a side effect depends on multiple reactive values, listing them all in `watch([a, b, c], ...)` is verbose and error-prone (forget one → bug). `watchEffect()` auto-tracks — if you access it, it's tracked. This is simpler and less error-prone for multi-dependency effects.

**Where it's used:** Setting document title from multiple refs, syncing multiple state values to localStorage, logging/debugging, simple DOM updates based on reactive state.

**What goes wrong without it:**
- Using `watchEffect` when you need old values → `watchEffect` doesn't provide `(newVal, oldVal)`. Use `watch` if you need to compare.
- Using `watchEffect` for API calls → runs immediately on setup → unwanted API call on mount. Use `watch` (which is lazy by default).
- Conditional access → `watchEffect(() => { if (showAge.value) console.log(age.value) })` → if `showAge` is false initially, `age` is NOT tracked. When `showAge` becomes true, `age` gets tracked. But if `age` changes while `showAge` is false, the effect doesn't re-run.
- Forgetting cleanup → `watchEffect` can return a cleanup function via `onCleanup` param. Not cleaning up async operations leads to stale updates.

---

## Computed Caching — Why Computed Is Better Than Methods

**What:** `computed()` caches its result. It only re-calculates when a dependency actually changes. Multiple template uses of the same computed only calculate once.

```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([
  { name: 'Apple', price: 1, inStock: true },
  { name: 'Banana', price: 0.5, inStock: false },
  { name: 'Cherry', price: 3, inStock: true },
])

// This computed is CACHED — only recalculates when items changes
const inStockItems = computed(() => items.value.filter(i => i.inStock))
const totalInStock = computed(() => inStockItems.value.reduce((s, i) => s + i.price, 0))

// Compare with a function (NOT cached — runs on every render):
function getInStockItems() {
  return items.value.filter(i => i.inStock)
}
</script>

<template>
  <!-- computed: calculated once, cached, reused -->
  <p>In stock: {{ inStockItems.length }}</p>
  <p>Total: {{ totalInStock }}</p>

  <!-- function: called TWICE per render (once for each use) -->
  <p>Count: {{ getInStockItems().length }}</p>
</template>
```

**Why it exists:** Expensive calculations (filtering 1000 items, sorting, aggregating) should not run on every render. `computed()` caches the result and only re-computes when a dependency changes. If the template uses the same computed 5 times, it calculates once. A function called 5 times in template runs 5 times.

**Where it's used:** Filtered/sorted lists, totals and aggregations, formatted display values, any derived data used in templates.

**What goes wrong without it:**
- Using a method/function instead of computed → recalculates on every render, even if nothing changed → performance issue with large data.
- Using a plain variable → `let total = items.value.reduce(...)` → doesn't update when items change.
- Mutating a computed → `total.value = 100` → error: computed is read-only. You need a setter: `computed({ get: () => ..., set: (val) => ... })`.
- Side effects in computed → `computed(() => { fetch('/api') })` → computed should be pure. Side effects cause unpredictable behavior.

---

## Watch — Selective Reactivity

**What:** `watch()` explicitly watches specific reactive sources and runs a callback when they change. It provides `newValue` and `oldValue`.

```vue
<script setup>
import { ref, reactive, watch, toRef } from 'vue'

const count = ref(0)
const user = reactive({ name: 'Alice', age: 25 })

// Watch a ref
watch(count, (newVal, oldVal) => {
  console.log(`Count: ${oldVal} → ${newVal}`)
})

// Watch a specific reactive property (use getter function)
watch(() => user.name, (newName, oldName) => {
  console.log(`Name: ${oldName} → ${newName}`)
})

// Watch multiple sources
watch([count, () => user.age], ([newCount, newAge], [oldCount, oldAge]) => {
  console.log(`Count: ${oldCount}→${newCount}, Age: ${oldAge}→${newAge}`)
})

// Watch with options
watch(() => user, (newUser) => {
  saveToServer(newUser)
}, { deep: true, immediate: false })
</script>
```

Watch options:
- `immediate: true` — run callback immediately on setup (not just on change)
- `deep: true` — watch nested properties of an object
- `flush: 'post'` — run after DOM update (default is 'pre')
- `once: true` — run only once, then stop watching

**Why it exists:** Not all state changes need side effects. `watch()` lets you selectively respond to specific changes — call an API when a filter changes, save to localStorage when a form updates, navigate when a step changes. It's explicit: you say exactly what to watch and what to do.

**Where it's used:** API calls on filter/page changes, auto-save, analytics logging, resetting dependent fields, triggering navigation, validation on change.

**What goes wrong without it:**
- Watching a reactive property directly → `watch(user.name, ...)` → `user.name` is a string, not reactive. Use `watch(() => user.name, ...)`.
- Forgetting `deep: true` for nested objects → `watch(user, callback)` without `deep` → changes to `user.profile.theme` don't trigger.
- Infinite loops → watcher modifies the watched value → triggers watcher again → stack overflow or frozen app. Never mutate the watched value inside the watcher.
- Watching a destructured reactive property → `const { name } = user; watch(name, ...)` → `name` is a plain string. Use `toRef(user, 'name')` or a getter.

---

## Shallow Ref — Opt-Out of Deep Reactivity

**What:** `shallowRef()` creates a ref that is only reactive at the top level — `.value` changes trigger updates, but mutations to nested properties do NOT.

```vue
<script setup>
import { shallowRef, triggerRef } from 'vue'

const largeList = shallowRef([
  { id: 1, name: 'Item 1' },
  { id: 2, name: 'Item 2' },
  // ... 10,000 items
])

// This does NOT trigger reactivity (nested mutation):
largeList.value[0].name = 'Updated'

// This DOES trigger reactivity (top-level change):
largeList.value = [...largeList.value, { id: 3, name: 'Item 3' }]

// Force update after nested mutation:
largeList.value[0].name = 'Updated'
triggerRef(largeList)  // manually trigger reactivity
</script>
```

**Why it exists:** Deep reactivity has a cost — Vue wraps every nested object in a Proxy. For large data (10,000 items in a table, large API responses), this overhead is significant. `shallowRef()` skips deep proxying — only `.value` reassignment is tracked. This is a performance optimization for large data.

**Where it's used:** Large datasets (tables with thousands of rows), large API responses where you only replace the whole array, integration with external state management (Redux, Zustand) where Vue shouldn't proxy the internals.

**What goes wrong without it:**
- Using `shallowRef` when you need deep reactivity → mutating nested properties doesn't update UI. Use `ref` instead.
- Forgetting `triggerRef()` after nested mutation → UI doesn't update. You must either reassign `.value` or call `triggerRef()`.
- Using `shallowRef` for small objects → no benefit, just adds complexity. Use regular `ref`.

---

## Reactive Proxy — How Vue Tracks Changes

**What:** Vue 3 uses JavaScript `Proxy` objects to intercept get/set operations on reactive objects. When you read a property, Vue tracks it as a dependency. When you write, Vue triggers updates.

```vue
<script setup>
import { reactive, isReactive, isProxy } from 'vue'

const state = reactive({ count: 0, nested: { value: 1 } })

console.log(isReactive(state))        // true
console.log(isReactive(state.nested)) // true (deep reactivity)
console.log(isProxy(state))           // true

// When you access state.count in a computed/template:
// Vue's proxy intercepts the "get" and registers a dependency
// When you set state.count = 5:
// Vue's proxy intercepts the "set" and triggers updates
</script>
```

**Why it exists:** Vue 2 used `Object.defineProperty` which had limitations — couldn't detect new property additions, couldn't track array index changes, needed `$set` and `$delete` workarounds. Vue 3's Proxy approach handles all of these natively: adding properties, array index changes, `Map`/`Set` support, and better performance.

**Where it's used:** Internally by Vue — you don't write Proxy code yourself. But understanding it helps you debug: `isReactive()` checks if an object is a reactive proxy, `toRaw()` gets the original non-reactive object.

**What goes wrong without it:**
- Spreading a reactive object → `const copy = { ...state }` → `copy` is a plain object, NOT reactive. Changes to `copy` don't trigger updates.
- `JSON.parse(JSON.stringify(state))` → loses reactivity entirely. The result is a plain object.
- Using `toRaw(state)` and then mutating → bypasses the proxy → no reactivity → UI doesn't update.
- Comparing reactive objects → `reactive({a:1}) === reactive({a:1})` → false (different proxies). Same object: `const a = reactive({}); const b = a; a === b` → true.

---

## NextTick — Waiting for DOM Updates

**What:** `nextTick()` returns a Promise that resolves after Vue has finished updating the DOM. Use it when you need to interact with the DOM after a reactive change.

```vue
<script setup>
import { ref, nextTick } from 'vue'

const showInput = ref(false)
const inputRef = ref(null)

async function showAndFocus() {
  showInput.value = true
  // DOM isn't updated yet — inputRef.value is still null
  await nextTick()
  // Now DOM is updated — input exists, we can focus it
  inputRef.value.focus()
}
</script>

<template>
  <q-btn @click="showAndFocus" label="Show Input" />
  <q-input v-if="showInput" ref="inputRef" />
</template>
```

**Why it exists:** Vue batches DOM updates for performance. When you change a ref, the DOM doesn't update synchronously — Vue waits for the next "tick" to apply all pending changes. If you try to access a DOM element that was just `v-if`'d into existence, it won't exist yet. `nextTick()` lets you wait for the DOM to catch up.

**Where it's used:** Focusing an input after showing it with `v-if`, scrolling to a newly added element, measuring element dimensions after a data change, integrating with non-Vue DOM libraries after render.

**What goes wrong without it:**
- Accessing DOM right after `v-if = true` → element doesn't exist yet → `null.focus()` → error.
- Using `setTimeout(() => ..., 0)` instead of `nextTick` → works but is fragile (timing depends on browser). `nextTick` is Vue's official way.
- Forgetting `await` → `nextTick().then(() => inputRef.value.focus())` works, but `nextTick(); inputRef.value.focus()` doesn't (runs before DOM update).

---

## ToRef and ToRefs — Connecting Refs to Reactive Objects

**What:** `toRef()` creates a ref that's connected to a specific property of a reactive object. `toRefs()` converts all properties of a reactive object to refs.

```vue
<script setup>
import { reactive, toRef, toRefs, watch } from 'vue'

const state = reactive({
  count: 0,
  name: 'Alice'
})

// toRef: single property
const count = toRef(state, 'count')
count.value++  // updates state.count AND triggers reactivity

// toRefs: all properties (for destructuring)
const { name } = toRefs(state)
name.value = 'Bob'  // updates state.name AND triggers reactivity

// Useful for watching destructured properties
watch(count, (newVal) => {
  console.log('Count changed:', newVal)
})
</script>
```

**Why it exists:** When you destructure a `reactive()` object, you lose reactivity — `const { count } = state` gives you a plain number. `toRefs()` converts each property to a ref that stays connected to the original reactive object. This lets you destructure for cleaner code while preserving reactivity.

**Where it's used:** Returning reactive state from composables (so consumers can destructure), passing individual reactive properties to child components, watching specific properties after destructuring.

**What goes wrong without it:**
- Destructuring reactive without `toRefs` → `const { count } = state` → `count` is a plain number → no reactivity → UI doesn't update.
- Using `toRef` on a non-existent property → `toRef(state, 'nonExistent')` → returns a ref with `undefined` value. It works but may be a bug if you expected the property to exist.
- Confusing `toRef` (singular) with `toRefs` (plural) → `toRef` takes `(object, key)`, `toRefs` takes `(object)` and returns all properties as refs.
