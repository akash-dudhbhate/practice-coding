# Lesson 04 — Concepts Explained (Vue 3 Composition API)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Script Setup — The Modern Component Syntax

**What:** `<script setup>` is Vue 3's recommended way to write component logic. It's a compiler macro that automatically exposes top-level bindings to the template.

```vue
<template>
  <q-page>
    <p>{{ count }}</p>
    <q-btn @click="increment" label="Click" />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)
function increment() {
  count.value++
}
</script>
```

Everything declared at the top level of `<script setup>` (variables, functions, imports) is automatically available in the template — no `return` statement needed.

**Why it exists:** Before `<script setup>`, you used the Options API (`data()`, `methods:`, `computed:`, `mounted()`) or the Composition API with a `setup()` function that required an explicit `return` of every binding. `<script setup>` reduces boilerplate dramatically — less code, better performance (compiler optimization), and better TypeScript inference.

**Where it's used:** Every new Vue 3 / Quasar component. This is the default and recommended approach.

**What goes wrong without it:**
- Using Options API → more boilerplate (`data()`, `methods`), worse TypeScript support, harder to extract reusable logic.
- Using `setup()` function → must manually `return` every variable and function → easy to forget one → template shows "undefined".
- Importing a component but forgetting it's auto-exposed in `<script setup>` → trying to register it in `components: {}` (Options API style) → error.

---

## Ref — Reactive Primitive

**What:** `ref()` creates a reactive reference to a single value (string, number, boolean, object). Access via `.value` in script, auto-unwrapped in template.

```vue
<script setup>
import { ref } from 'vue'

const name = ref('Alice')
const age = ref(25)
const isActive = ref(false)

function birthday() {
  age.value++           // use .value in script
  name.value = 'Alice ' + age.value
}
</script>

<template>
  <p>{{ name }}</p>      <!-- no .value needed in template -->
  <p>Age: {{ age }}</p>
  <q-toggle v-model="isActive" label="Active" />
</template>
```

**Why it exists:** JavaScript primitives (strings, numbers, booleans) are passed by value, not reference. You can't track changes to a plain `let count = 0` because reassigning it creates a new binding. `ref()` wraps the value in a reactive object — Vue can track when `.value` changes and trigger updates.

**Where it's used:** Every component with state — counters, form inputs, toggles, fetched data, UI flags (loading, error, dialog open).

**What goes wrong without it:**
- Using `let count = 0` instead of `ref(0)` → changing `count` does NOT update the UI. No reactivity.
- Forgetting `.value` in script → `count++` throws "count is not a number" (it's a ref object). Must use `count.value++`.
- Using `.value` in template → `{{ count.value }}` shows the raw object. Vue auto-unwraps, so just `{{ count }}`.

---

## Reactive — Reactive Object

**What:** `reactive()` creates a reactive object (not a ref). You access properties directly — no `.value` needed.

```vue
<script setup>
import { reactive } from 'vue'

const user = reactive({
  name: 'Alice',
  age: 25,
  preferences: { theme: 'dark', notifications: true }
})

function updateName(newName) {
  user.name = newName        // direct access, no .value
}
</script>

<template>
  <p>{{ user.name }}</p>     <!-- direct access in template too -->
  <p>{{ user.age }}</p>
</template>
```

**Why it exists:** For objects with many properties, using `ref()` for each is tedious: `const name = ref('Alice')`, `const age = ref(25)`, etc. `reactive()` wraps the entire object — any property change triggers reactivity. It's cleaner for grouped state.

**Where it's used:** Form state (multiple fields grouped), user profile objects, configuration objects, any state with multiple related properties.

**What goes wrong without it:**
- Destructuring a reactive object → `const { name } = reactive({ name: 'Alice' })` → `name` is now a plain string, reactivity is LOST. Use `toRefs()` to preserve reactivity.
- Reassigning the entire reactive object → `user = { name: 'Bob' }` → error or reactivity lost. Mutate properties instead: `user.name = 'Bob'`.
- Using `reactive()` for primitives → `reactive(0)` doesn't work. Use `ref()` for primitives.

---

## Computed — Derived State

**What:** `computed()` creates a value that automatically recalculates when its dependencies change. The result is cached — it only re-computes when a dependency actually changes.

```vue
<script setup>
import { ref, computed } from 'vue'

const price = ref(100)
const quantity = ref(3)

const total = computed(() => price.value * quantity.value)
const discountedTotal = computed(() => total.value * 0.9)

function applyDiscount() {
  // discountedTotal auto-updates because it depends on total,
  // which depends on price and quantity
}
</script>

<template>
  <p>Total: {{ total }}</p>
  <p>With 10% off: {{ discountedTotal }}</p>
</template>
```

**Why it exists:** Without `computed()`, you'd recalculate derived values on every render (wasteful) or manually recalculate in every place that changes a dependency (error-prone). `computed()` is declarative — it tracks dependencies automatically and caches the result.

**Where it's used:** Filtered/sorted lists, totals/subtotals, formatted display values, conditional flags based on multiple refs, anything derived from other state.

**What goes wrong without it:**
- Using a function instead → `function getTotal() { return price.value * quantity.value }` → recalculates on every render, no caching → performance issue for expensive calculations.
- Using a plain variable → `let total = price.value * quantity.value` → doesn't update when price/quantity change.
- Mutating a computed → `total.value = 500` → error. Computed properties are read-only unless they have a setter.

---

## Watch — Reactive Side Effects

**What:** `watch()` runs a callback when one or more reactive values change. It gives you the old and new values.

```vue
<script setup>
import { ref, watch } from 'vue'

const searchQuery = ref('')
const selectedCategory = ref('all')

// Watch a single ref
watch(searchQuery, (newValue, oldValue) => {
  console.log(`Search changed from "${oldValue}" to "${newValue}"`)
  performSearch(newValue)
})

// Watch multiple sources
watch([searchQuery, selectedCategory], ([newQuery, newCategory]) => {
  console.log(`Searching "${newQuery}" in ${newCategory}`)
})

// Watch with options
watch(searchQuery, (val) => {
  saveToLocalStorage(val)
}, { immediate: true, deep: true })
</script>
```

Watch options: `immediate` (run on mount, not just on change), `deep` (watch nested object properties), `flush` (timing: `'pre'`, `'post'`, `'sync'`).

**Why it exists:** Sometimes you need to perform a side effect when data changes — fetch API data, save to localStorage, trigger an animation, log analytics. `watch()` lets you react to state changes declaratively without putting logic in every place that modifies state.

**Where it's used:** API calls on filter changes, auto-save on form changes, logging/analytics, resetting dependent fields, triggering animations.

**What goes wrong without it:**
- Putting side effects in computed properties → computed should be pure (no side effects). Side effects in computed cause unexpected behavior and debugging nightmares.
- Watching a reactive object property incorrectly → `watch(() => user.name, ...)` works, but `watch(user.name, ...)` doesn't (it's a string, not reactive).
- Forgetting `deep: true` for nested objects → changes to `user.preferences.theme` don't trigger the watcher.
- Infinite loops → watcher modifies the watched value → triggers watcher again → forever. Avoid mutating watched values inside the watcher.

---

## WatchEffect — Auto-Tracked Effects

**What:** `watchEffect()` runs a callback immediately and auto-tracks any reactive dependencies used inside it. It re-runs whenever any tracked dependency changes.

```vue
<script setup>
import { ref, watchEffect } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

// Auto-tracks firstName and lastName — no need to list them
watchEffect(() => {
  console.log(`${firstName.value} ${lastName.value}`)
  document.title = `${firstName.value} ${lastName.value}`
})

// Unlike watch(), you don't specify what to watch — it's inferred
</script>
```

**Why it exists:** `watch()` requires you to explicitly list dependencies. If you forget one, the callback doesn't fire when it changes. `watchEffect()` auto-tracks — any reactive value used inside the callback becomes a dependency automatically. Simpler for cases where you use multiple reactive values.

**Where it's used:** Setting document title, syncing state to DOM/localStorage, logging, simple side effects with multiple dependencies.

**What goes wrong without it:**
- Using `watchEffect` when you need the old value → `watchEffect` doesn't provide `oldValue`. Use `watch` instead.
- Using `watchEffect` for async API calls → it runs immediately on mount, which may trigger an unwanted API call. Use `watch` with `immediate: false` (default).
- Accessing a reactive value conditionally inside `watchEffect` → if the condition is false on first run, that dependency isn't tracked → changes to it won't trigger re-run.

---

## Lifecycle Hooks — onMounted, onUnmounted, etc.

**What:** Lifecycle hooks let you run code at specific points in a component's life. In `<script setup>`, they're imported functions prefixed with `on`.

```vue
<script setup>
import { ref, onMounted, onUnmounted, onUpdated } from 'vue'

const data = ref(null)
let interval = null

onMounted(() => {
  console.log('Component is now in the DOM')
  fetchData()
  interval = setInterval(() => {
    console.log('Tick')
  }, 1000)
})

onUnmounted(() => {
  console.log('Component is being destroyed')
  clearInterval(interval)  // cleanup!
})

onUpdated(() => {
  console.log('Component re-rendered')
})

async function fetchData() {
  const res = await fetch('/api/data')
  data.value = await res.json()
}
</script>
```

Key hooks: `onBeforeMount`, `onMounted`, `onBeforeUpdate`, `onUpdated`, `onBeforeUnmount`, `onUnmounted`, `onErrorCaptured`, `onActivated`, `onDeactivated`.

**Why it exists:** Components have a lifecycle — they're created, mounted to DOM, updated when state changes, and destroyed. You need to hook into these moments: fetch data after mount (DOM is ready), clean up timers/listeners before unmount (prevent memory leaks), log on updates.

**Where it's used:** `onMounted` — API calls, initializing libraries (charts, maps), setting up event listeners. `onUnmounted` — clearing intervals, removing listeners, destroying library instances. `onUpdated` — DOM measurements after re-render.

**What goes wrong without it:**
- Fetching data in `setup()` (top level) → DOM isn't ready yet, and in SSR the code runs on server where there's no DOM. Use `onMounted`.
- Forgetting cleanup in `onUnmounted` → memory leaks (timers keep running, listeners keep firing) even after component is gone.
- Using `onMounted` inside a conditional → hooks must be called synchronously during setup. Never inside `if` statements or loops.

---

## ToRefs — Preserving Reactivity on Destructure

**What:** `toRefs()` converts each property of a reactive object into a ref, so you can destructure without losing reactivity.

```vue
<script setup>
import { reactive, toRefs } from 'vue'

const state = reactive({
  count: 0,
  name: 'Alice'
})

// Without toRefs: const { count } = state → count is plain number, NOT reactive
// With toRefs:
const { count, name } = toRefs(state)

function increment() {
  count.value++  // it's a ref now, so use .value
}
</script>

<template>
  <p>{{ count }}</p>
  <p>{{ name }}</p>
</template>
```

**Why it exists:** Destructuring a `reactive()` object breaks reactivity — `const { count } = state` copies the value at that moment, and future changes to `state.count` won't update `count`. `toRefs()` wraps each property in a ref that stays connected to the original reactive object.

**Where it's used:** When returning reactive state from composables, when destructuring reactive objects for cleaner code, when passing individual properties to child components.

**What goes wrong without it:**
- Destructuring without `toRefs` → `const { count } = state` → `count` is a plain number → UI never updates when `state.count` changes.
- Using `toRef` (singular) instead of `toRefs` → `toRef` is for a single property: `const count = toRef(state, 'count')`. Different API.
- Forgetting `.value` after `toRefs` → destructured properties are refs, so `count++` fails. Use `count.value++`.

---

## Composables — Reusable Logic

**What:** A composable is a function that uses Composition API to encapsulate reusable reactive logic. Convention: name starts with `use`.

```javascript
// composables/useCounter.js
import { ref, computed } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  const double = computed(() => count.value * 2)
  
  function increment() { count.value++ }
  function decrement() { count.value-- }
  function reset() { count.value = initialValue }
  
  return { count, double, increment, decrement, reset }
}
```

```vue
<!-- Component using the composable -->
<script setup>
import { useCounter } from 'composables/useCounter'

const { count, double, increment, reset } = useCounter(10)
</script>

<template>
  <p>Count: {{ count }}</p>
  <p>Double: {{ double }}</p>
  <q-btn @click="increment" label="+" />
  <q-btn @click="reset" label="Reset" />
</template>
```

**Why it exists:** In Options API, reusable logic was shared via mixins — which had naming conflicts, unclear origins, and no type safety. Composables solve all of this: explicit imports, clear function names, full TypeScript support, and no hidden state pollution.

**Where it's used:** Shared logic across components — `useFetch` (API calls), `useAuth` (authentication state), `useLocalStorage` (persisted state), `useMousePosition` (mouse tracking), `useBreakpoints` (responsive helpers).

**What goes wrong without it:**
- Duplicating logic in every component → maintenance nightmare, bugs fixed in one place but not others.
- Using mixins (Options API) → naming conflicts, unclear where state/methods come from, hard to type.
- Forgetting to return values from the composable → `const { count } = useCounter()` → `count` is undefined if not returned.
- Each call to a composable creates independent state → `useCounter()` in two components gives two separate counters. For shared state, use a module-level ref or Pinia.

---

## Template Refs — Accessing DOM Elements

**What:** Template refs let you get a direct reference to a DOM element or child component in `<script setup>`.

```vue
<template>
  <q-input ref="emailInput" v-model="email" label="Email" />
  <q-btn @click="focusInput" label="Focus Email" />
</template>

<script setup>
import { ref, onMounted } from 'vue'

const emailInput = ref(null)    // must match the ref="" name
const email = ref('')

function focusInput() {
  emailInput.value.focus()      // access the DOM/component API
}

onMounted(() => {
  // emailInput.value is available after mount
  emailInput.value.focus()
})
</script>
```

**Why it exists:** Sometimes you need direct DOM access — focus an input, measure an element's size, integrate a non-Vue library (jQuery plugin, charting library). Template refs provide a safe, reactive way to get DOM references without `document.getElementById()`.

**Where it's used:** Auto-focusing inputs on form open, scrolling to elements, measuring element dimensions, integrating third-party DOM libraries, triggering Quasar component methods (e.g., `validate()` on `q-form`).

**What goes wrong without it:**
- Using `document.getElementById()` → breaks in SSR (no document on server), not reactive, fragile if ID changes.
- Accessing `ref.value` before `onMounted` → it's `null` because the DOM element doesn't exist yet.
- Mismatched names → `ref="myInput"` in template but `const input = ref(null)` in script → `input.value` is always null. Names must match exactly.
