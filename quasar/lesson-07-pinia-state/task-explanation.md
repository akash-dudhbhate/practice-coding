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

   WHAT IT SHOULD LOOK LIKE:
   ```
   // store file — no UI, but a component using it renders:
   Count: 0     Double: 0         <- count + computed getter
   [ + ] [ - ]                    <- buttons call store actions
   ```
2. `easy/p02-solve.js` — Create a component that uses `useCounterStore`. Display the count and double. Add increment and decrement buttons. Use `storeToRefs` for reactive destructuring.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Count: 0                       <- live from store
   Double: 0                      <- getter tracks it
   +-----+ +-----+
   | +1  | | -1  |
   +-----+ +-----+
   ```
3. `easy/p03-solve.js` — Create a `useThemeStore` with `dark` (boolean ref) and a `toggle` action. Create a component that uses it to toggle dark mode (use Quasar's `$q.dark.set()`).

   WHAT IT SHOULD LOOK LIKE:
   ```
   LIGHT:                     DARK (after click):
   +------------------+       +##################+
   | [ Toggle dark ]  |       |# [ Toggle dark ]#|
   | Dark mode: off   |       |# Dark mode: on  #|
   +------------------+       +##################+
   ```

### Medium
4. `medium/p01-solve.js` — Create a `useCartStore` with `items` (array), `totalItems` (getter), `totalPrice` (getter), `addItem`/`removeItem`/`clearCart` actions. Create a cart component that displays items and totals.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Add Apple $1 ]  [ Add Bread $2 ]
   Cart (3 items):
   * Apple  x2  $2.00    [x]
   * Bread  x1  $2.00    [x]
   ---------------------------
   Total: $4.00      [ Clear ]
   ```
5. `medium/p02-solve.js` — Create two stores: `useUserStore` (user, login, logout) and `useProductStore` (products, fetchProducts). Create a component that uses both stores. Show user info and product list.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Logged in as: alice    [ Logout ]    <- useUserStore
   [ Load Products ]
   * Product A  $10                     <- useProductStore
   * Product B  $20
   * Product C  $30
   ```
6. `medium/p03-solve.js` — Add persistence to `useUserStore`: save user to localStorage on change, load on init, clear on logout. Use `watch` for auto-save. Test by simulating login, refresh, and logout.

   WHAT IT SHOULD LOOK LIKE:
   ```
   BEFORE RELOAD:              AFTER RELOAD:
   Logged in: alice            Logged in: alice   <- restored!
   [ Logout ] -> clears localStorage "user" key
   ```

### Hard
7. `hard/p01-solve.js` — Build a complete auth store: `useAuthStore` with user, token, isAuthenticated (getter), login (async API call), logout, and persistence. Include error handling and loading state. Create a login form component that uses it.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   | alice            |
   +------------------+
   | ***              |
   +------------------+
   Invalid credentials          <- red error text
   [ (o) Logging in... ]        <- spinner on the button
   ```
8. `hard/p02-solve.js` — Build a multi-store app: `useUserStore`, `useCartStore`, `useOrderStore`. Cart can create orders (moves items to order). Orders reference the user. Create components that interact with all three stores.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Cart: * Apple x2  * Bread x1      [ Checkout ]
   -------------------------------------------
   Orders:
   +------------------------------------------+
   | #1001  alice        $5.00                |  <- checkout moved
   +------------------------------------------+     cart -> order row
   ```
9. `hard/p03-solve.js` — Build a store with cross-store dependencies: `useCartStore` that depends on `useAuthStore` (only logged-in users can add items). Include: computed that shows cart only if authenticated, action that redirects to login if not authenticated, and a watcher that clears cart on logout.

   WHAT IT SHOULD LOOK LIKE:
   ```
   LOGGED OUT:                LOGGED IN:
   [ Add ] -> "Please login"  [ Add ] -> item appears
   (no cart shown)            Cart: * Apple x1
   (logging out empties the cart automatically)
   ```

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
