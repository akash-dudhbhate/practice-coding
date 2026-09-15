# Lesson 07 — Coding Check

## Easy

### p01-solve.js — Counter store
- [ ] `defineStore` used
- [ ] `count` as ref
- [ ] `double` as computed
- [ ] `increment` action defined
- [ ] `decrement` action defined
- [ ] All values returned from the store

### p02-solve.js — Counter component
- [ ] `useCounterStore` imported
- [ ] `storeToRefs` used for reactive destructuring
- [ ] Count displayed
- [ ] Double displayed
- [ ] Increment button works
- [ ] Decrement button works

### p03-solve.js — Theme store + component
- [ ] `useThemeStore` with `dark` ref
- [ ] `toggle` action defined
- [ ] Component uses the store
- [ ] `$q.dark.set()` called on toggle
- [ ] Dark mode toggles correctly

## Medium

### p01-solve.js — Cart store + component
- [ ] `items` as ref (array)
- [ ] `totalItems` as computed
- [ ] `totalPrice` as computed
- [ ] `addItem` action
- [ ] `removeItem` action
- [ ] `clearCart` action
- [ ] Cart component displays items
- [ ] Totals displayed
- [ ] Add/remove/clear buttons work

### p02-solve.js — Two stores + component
- [ ] `useUserStore` created (user, login, logout)
- [ ] `useProductStore` created (products, fetchProducts)
- [ ] Component imports both stores
- [ ] User info displayed
- [ ] Product list displayed
- [ ] Both stores work independently

### p03-solve.js — Persistent user store
- [ ] User saved to localStorage on change
- [ ] `watch` used for auto-save
- [ ] User loaded from localStorage on init
- [ ] User cleared from localStorage on logout
- [ ] `JSON.stringify`/`JSON.parse` used
- [ ] Logout clears state

## Hard

### p01-solve.js — Complete auth store
- [ ] `user` ref
- [ ] `token` ref
- [ ] `isAuthenticated` computed
- [ ] `login` async action (simulated API)
- [ ] `logout` action
- [ ] `loading` ref for UI state
- [ ] `error` ref for error handling
- [ ] Persistence (localStorage)
- [ ] Login form component
- [ ] Error displayed on failure
- [ ] Loading state shown

### p02-solve.js — Multi-store app
- [ ] `useUserStore` created
- [ ] `useCartStore` created
- [ ] `useOrderStore` created
- [ ] Cart can create orders
- [ ] Orders reference the user
- [ ] Components interact with all stores
- [ ] Data flows between stores correctly

### p03-solve.js — Cross-store dependencies
- [ ] `useCartStore` imports `useAuthStore`
- [ ] Cart only visible if authenticated (computed)
- [ ] `addItem` checks auth → redirects if not
- [ ] Watcher clears cart on logout
- [ ] Auth state affects cart behavior
- [ ] Edge cases handled (logged out with items)
