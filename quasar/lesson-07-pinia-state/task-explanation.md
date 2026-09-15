# Lesson 07 — Pinia State Management

## What you'll learn
- What Pinia is (Vue state management)
- Setup stores vs Options stores
- State (reactive data in the store)
- Getters (computed derived state)
- Actions (methods that modify state)
- Using stores in components (storeToRefs)
- Multiple stores (modular state)
- Persistence (saving to localStorage)

## Lesson

### Define a store
```js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
    const count = ref(0)
    const double = computed(() => count.value * 2)
    function increment() { count.value++ }
    return { count, double, increment }
})
```

### Use in component
```vue
<script setup>
import { useCounterStore } from 'stores/counter'
import { storeToRefs } from 'pinia'
const store = useCounterStore()
const { count } = storeToRefs(store)
const { increment } = store
</script>
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Create a Pinia store (`useCounterStore`) with `count` (ref), `double` (computed), and `increment`/`decrement` actions. Export the store.
2. `easy/p02-solve.js` — Create a component that uses `useCounterStore`. Display the count and double. Add increment and decrement buttons. Use `storeToRefs` for reactive destructuring.
3. `easy/p03-solve.js` — Create a `useThemeStore` with `dark` (boolean ref) and a `toggle` action. Create a component that uses it to toggle dark mode (use Quasar's `$q.dark.set()`).

### Medium
4. `medium/p01-solve.js` — Create a `useCartStore` with `items` (array), `totalItems` (getter), `totalPrice` (getter), `addItem`/`removeItem`/`clearCart` actions. Create a cart component that displays items and totals.
5. `medium/p02-solve.js` — Create two stores: `useUserStore` (user, login, logout) and `useProductStore` (products, fetchProducts). Create a component that uses both stores. Show user info and product list.
6. `medium/p03-solve.js` — Add persistence to `useUserStore`: save user to localStorage on change, load on init, clear on logout. Use `watch` for auto-save. Test by simulating login, refresh, and logout.

### Hard
7. `hard/p01-solve.js` — Build a complete auth store: `useAuthStore` with user, token, isAuthenticated (getter), login (async API call), logout, and persistence. Include error handling and loading state. Create a login form component that uses it.
8. `hard/p02-solve.js` — Build a multi-store app: `useUserStore`, `useCartStore`, `useOrderStore`. Cart can create orders (moves items to order). Orders reference the user. Create components that interact with all three stores.
9. `hard/p03-solve.js` — Build a store with cross-store dependencies: `useCartStore` that depends on `useAuthStore` (only logged-in users can add items). Include: computed that shows cart only if authenticated, action that redirects to login if not authenticated, and a watcher that clears cart on logout.

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
