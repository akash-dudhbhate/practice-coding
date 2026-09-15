# Lesson 07 — Concepts Explained (Pinia State Management)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Pinia?

**What:** Pinia is the official state management library for Vue.js — a successor to Vuex with a simpler API.

```js
// Pinia store: a function that returns reactive state
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
    const count = ref(0)
    function increment() {
        count.value++
    }
    return { count, increment }
})

// In a component:
const counter = useCounterStore()
console.log(counter.count)  // 0
counter.increment()
console.log(counter.count)  // 1
```

**Why it exists:** Without a state store, components share data via props/events → "prop drilling" (passing through many levels) → messy. Pinia provides a single source of truth → any component can access → clean.

**Where it's used:** Medium to large Vue/Quasar apps with shared state — user auth, cart, theme, settings.

**What goes wrong without it:**
- Prop drilling → 5 levels of components passing the same prop → hard to maintain.
- Multiple components holding the same data independently → out of sync → bugs.
- Using Pinia for everything → even component-local state goes in the store → over-engineered. Use Pinia for shared state only.

---

## Setup Stores vs Options Stores

**What:** Two ways to define a Pinia store — Setup (Composition API) or Options (Options API).

```js
// Setup Store (recommended — uses Composition API)
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
    const name = ref('Akash')
    const isAdmin = computed(() => name.value === 'admin')
    function setName(newName) {
        name.value = newName
    }
    return { name, isAdmin, setName }
})

// Options Store (alternative — uses Options API)
export const useUserStore = defineStore('user', {
    state: () => ({ name: 'Akash' }),
    getters: { isAdmin: (state) => state.name === 'admin' },
    actions: { setName(newName) { this.name = newName } },
})
```

**Why it exists:** Setup stores are more flexible (use any composable, watch, etc.). Options stores are more structured (clear separation of state/getters/actions). Choose based on your team's preference.

**Where it's used:** Every Pinia store — pick one style and be consistent.

**What goes wrong without it:**
- Mixing styles in the same project → inconsistent → hard to read.
- Setup store: forgetting to `return` a value → it's not accessible from components.
- Options store: `this` in getters → getters don't use `this`, they use `state`. Actions use `this`.

---

## State in Pinia

**What:** State is the reactive data in the store.

```js
// Setup store
const count = ref(0)
const user = ref({ name: 'Akash', age: 25 })
const items = ref([])

// In component:
const counter = useCounterStore()
counter.count          // 0
counter.count = 5      // directly mutable (Pinia allows it)
counter.user.name = 'Dev'  // deep reactivity works
```

**Why it exists:** State holds the shared data. Pinia makes it reactive → components auto-update when state changes → no manual sync.

**Where it's used:** Every store — state is the core.

**What goes wrong without it:**
- Destructuring state: `const { count } = useCounterStore()` → loses reactivity! Use `storeToRefs`: `const { count } = storeToRefs(store)`.
- Mutating state outside actions → works in Pinia (unlike Vuex) but makes debugging harder. Prefer actions for complex mutations.
- Not resetting state on logout → stale user data → security issue. Use `$reset()`.

---

## Getters (Computed State)

**What:** Getters are computed values derived from state.

```js
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
    const items = ref([
        { name: 'Book', price: 20, qty: 2 },
        { name: 'Pen', price: 5, qty: 10 },
    ])

    // Getter: derived from state
    const totalItems = computed(() =>
        items.value.reduce((sum, item) => sum + item.qty, 0)
    )
    const totalPrice = computed(() =>
        items.value.reduce((sum, item) => sum + item.price * item.qty, 0)
    )
    const isEmpty = computed(() => items.value.length === 0)

    return { items, totalItems, totalPrice, isEmpty }
})
```

**Why it exists:** Without getters, every component computes the same derived value → duplicated logic → inconsistent. Getters centralize derived state → one source of truth.

**Where it's used:** Any derived state — totals, filtered lists, user permissions.

**What goes wrong without it:**
- Computing in components → if the logic changes, you update every component → error-prone.
- Getter that depends on another store → import the other store: `const other = useOtherStore()`.
- Expensive getters → computed caches the result → only recalculates when state changes → efficient.

---

## Actions (Methods)

**What:** Actions are functions that modify state.

```js
export const useCartStore = defineStore('cart', () => {
    const items = ref([])

    // Action: adds an item
    function addItem(item) {
        const existing = items.value.find(i => i.name === item.name)
        if (existing) {
            existing.qty += item.qty
        } else {
            items.value.push({ ...item })
        }
    }

    // Action: removes an item
    function removeItem(name) {
        items.value = items.value.filter(i => i.name !== name)
    }

    // Async action: fetch data
    async function fetchItems() {
        const response = await fetch('/api/cart')
        items.value = await response.json()
    }

    return { items, addItem, removeItem, fetchItems }
})
```

**Why it exists:** Actions encapsulate state changes → logic is in one place → testable, reusable. Components call actions → don't know the implementation → separation of concerns.

**Where it's used:** Every state mutation — add, remove, update, fetch.

**What goes wrong without it:**
- Mutating state directly in components → logic scattered → hard to maintain. Use actions.
- Async actions without error handling → fetch fails → state is inconsistent. Use try/catch.
- Calling actions from other actions → fine in Pinia: `this.otherAction()` (Options) or just call the function (Setup).

---

## Using Stores in Components

**What:** How to access stores in Vue/Quasar components.

```vue
<template>
    <div>
        <p>Count: {{ counter.count }}</p>
        <q-btn @click="counter.increment" label="Increment" />
        <p>Double: {{ counter.double }}</p>
    </div>
</template>

<script setup>
import { useCounterStore } from 'stores/counter'
import { storeToRefs } from 'pinia'

const counter = useCounterStore()

// Destructure with reactivity preserved
const { count, double } = storeToRefs(counter)
// Actions can be destructured directly (no reactivity needed)
const { increment } = counter
</script>
```

**Why it exists:** Stores are useless if components can't access them. Pinia provides a simple API → `useStore()` → access state, getters, actions.

**Where it's used:** Every component that needs shared state.

**What goes wrong without it:**
- `const { count } = useCounterStore()` → `count` is NOT reactive (lost reactivity). Use `storeToRefs`.
- `const { increment } = storeToRefs(counter)` → error (actions aren't refs). Destructure actions directly from the store.
- Calling `useCounterStore()` outside `setup()` → might not work (Pinia must be installed). Always use in setup.

---

## Multiple Stores

**What:** Pinia encourages multiple small stores instead of one big store.

```js
// stores/user.js
export const useUserStore = defineStore('user', () => {
    const user = ref(null)
    function login(u) { user.value = u }
    function logout() { user.value = null }
    return { user, login, logout }
})

// stores/cart.js
export const useCartStore = defineStore('cart', () => {
    const items = ref([])
    function addItem(item) { items.value.push(item) }
    return { items, addItem }
})

// stores/theme.js
export const useThemeStore = defineStore('theme', () => {
    const dark = ref(false)
    function toggle() { dark.value = !dark.value }
    return { dark, toggle }
})
```

**Why it exists:** One big store (Vuex style) → everything in one file → hard to maintain. Multiple small stores → each feature has its own store → modular, tree-shakeable.

**Where it's used:** Every medium to large app — one store per feature/domain.

**What goes wrong without it:**
- One store for everything → huge file → hard to find things → merge conflicts.
- Too many stores → one per component → over-engineered. Group by feature, not by component.
- Cross-store dependencies → store A needs store B → import B inside A's setup → works but creates coupling.

---

## Persistence (localStorage)

**What:** Save store state to localStorage → survives page refresh.

```js
// Manual persistence
import { watch } from 'vue'

export const useUserStore = defineStore('user', () => {
    const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))

    watch(user, (val) => {
        localStorage.setItem('user', JSON.stringify(val))
    }, { deep: true })

    function login(u) { user.value = u }
    function logout() {
        user.value = null
        localStorage.removeItem('user')
    }
    return { user, login, logout }
})

// Or use pinia-plugin-persistedstate
// npm install pinia-plugin-persistedstate
// Automatically persists stores to localStorage
```

**Why it exists:** Without persistence, state resets on refresh → user logged out, cart emptied → bad UX. Persistence saves state → survives refresh → seamless experience.

**Where it's used:** Auth state, cart, theme, user preferences — any state that should survive refresh.

**What goes wrong without it:**
- Storing sensitive data (tokens) in localStorage → XSS attacks can steal them. Use httpOnly cookies for tokens.
- Not clearing state on logout → stale data → security issue. Always clear on logout.
- `JSON.stringify` on circular references → error. Don't store non-serializable data.
