# Lesson 17 — Coding Check

## Easy

### p01-solve.jsx — Counter store
- [ ] Store created with `create()`
- [ ] `count`, `increment`, `decrement`, `reset` in store
- [ ] Component uses selectors (not entire store)
- [ ] No Provider wrapper needed
- [ ] Buttons work correctly

### p02-solve.jsx — Theme store
- [ ] `theme` and `toggleTheme` in store
- [ ] 3 components consume the store
- [ ] Each component selects only `theme`
- [ ] Toggling updates all 3 components
- [ ] No unnecessary re-renders

### p03-solve.jsx — Todo store
- [ ] `todos` array in store
- [ ] `addTodo` adds a new todo
- [ ] `toggleTodo` toggles done status
- [ ] `deleteTodo` removes by id
- [ ] Form to add todos
- [ ] List displays all todos

## Medium

### p01-solve.jsx — Async auth store
- [ ] `login` is an async function
- [ ] `loading` state set during login
- [ ] `error` state set on failure
- [ ] `user` state set on success
- [ ] `logout` clears user
- [ ] Login form uses the store
- [ ] Protected component checks auth

### p02-solve.jsx — Cart store
- [ ] `items` array in store
- [ ] `addItem` adds product
- [ ] `removeItem` removes by id
- [ ] `updateQuantity` changes qty
- [ ] `clearCart` empties the cart
- [ ] Total calculated correctly
- [ ] Cart display shows items and total

### p03-solve.jsx — Persisted store
- [ ] `persist` middleware used
- [ ] Storage name specified
- [ ] Theme persists across reload
- [ ] User preferences persist across reload
- [ ] `partialize` used to persist only specific fields
- [ ] Functions are NOT persisted (only state)

## Hard

### p01-solve.jsx — Multi-slice store
- [ ] `createAuthSlice` defined separately
- [ ] `createCartSlice` defined separately
- [ ] `createThemeSlice` defined separately
- [ ] Slices combined into one store
- [ ] Components select from different slices
- [ ] Updating auth doesn't re-render theme-only consumers
- [ ] All slices work independently

### p02-solve.jsx — Immer middleware tree
- [ ] `immer` middleware used
- [ ] Nested tree structure in state
- [ ] `addFolder` uses direct mutation (push)
- [ ] `addFile` uses direct mutation
- [ ] `rename` modifies nested property directly
- [ ] `delete` uses splice or filter
- [ ] `move` relocates items in the tree
- [ ] No spread operators needed

### p03-solve.jsx — E-commerce store
- [ ] Products slice (with fetch action)
- [ ] Cart slice (with persist)
- [ ] Auth slice
- [ ] Wishlist slice (with persist)
- [ ] Notifications slice
- [ ] `devtools` middleware applied
- [ ] Multiple components consume efficiently
- [ ] Selectors prevent unnecessary re-renders
- [ ] Cart and wishlist survive reload
