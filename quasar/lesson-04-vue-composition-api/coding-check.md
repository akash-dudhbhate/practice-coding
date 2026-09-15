# Lesson 04 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Counter with ref
- [ ] `count` declared with `ref(0)`.
- [ ] `ref` imported from 'vue'.
- [ ] Uses `<script setup>`.
- [ ] `{{ count }}` in template (no `.value`).
- [ ] Increment button uses `count.value++` in handler.
- [ ] Decrement button uses `count.value--` in handler.

### p02 — Reactive user object
- [ ] `user` declared with `reactive({ name: '...', email: '...', role: '...' })`.
- [ ] `reactive` imported from 'vue'.
- [ ] Template displays `user.name`, `user.email`, `user.role`.
- [ ] Button changes `user.name` to a new value (direct mutation, no `.value`).
- [ ] UI updates when name changes.

### p03 — Computed fullName
- [ ] `firstName` and `lastName` declared with `ref()`.
- [ ] `computed` imported from 'vue'.
- [ ] `fullName` is `computed(() => firstName.value + ' ' + lastName.value)`.
- [ ] Two `<q-input>` components with `v-model` bound to `firstName` and `lastName`.
- [ ] `{{ fullName }}` updates when either input changes.
- [ ] `fullName` is read-only (not mutated directly).

## Medium

### p01 — Shopping cart with computed total
- [ ] `items` declared as `ref([])` (array of `{ name, price }` objects).
- [ ] `totalPrice` is `computed(() => items.value.reduce(...))`.
- [ ] Add button pushes a new item to `items.value`.
- [ ] Remove button removes an item from `items.value` (by index or id).
- [ ] `{{ totalPrice }}` updates automatically when items change.
- [ ] Items displayed with `v-for` and `:key`.

### p02 — Search filter with watch
- [ ] `searchQuery` declared with `ref('')`.
- [ ] `items` declared as `ref([...strings])` with at least 5 items.
- [ ] `filteredItems` is `computed` that filters by `searchQuery.value`.
- [ ] `<q-input>` bound to `searchQuery` with `v-model`.
- [ ] `watch(searchQuery, ...)` logs the new value to console.
- [ ] Filtered list updates as user types.
- [ ] Empty search shows all items.

### p03 — Timer with lifecycle hooks
- [ ] `seconds` declared with `ref(0)`.
- [ ] `onMounted` starts a `setInterval` that increments `seconds` every second.
- [ ] `onUnmounted` clears the interval with `clearInterval`.
- [ ] Interval ID stored in a variable (e.g., `let interval = null`).
- [ ] Start button starts the timer (if not already running).
- [ ] Stop button clears the interval.
- [ ] `{{ seconds }}` displays the elapsed time.
- [ ] No memory leak: interval is cleared on unmount.

## Hard

### p01 — useCounter composable
- [ ] `useCounter` function defined (in script or inline).
- [ ] Returns `{ count, double, increment, decrement, reset }`.
- [ ] `count` is a `ref`.
- [ ] `double` is `computed(() => count.value * 2)`.
- [ ] `increment` does `count.value++`.
- [ ] `decrement` does `count.value--`.
- [ ] `reset` sets count back to initial value.
- [ ] Component destructures: `const { count, double, increment } = useCounter(10)`.
- [ ] Template displays both `count` and `double`.

### p02 — Form validation with reactive + computed + watch
- [ ] `form` declared with `reactive({ name: '', email: '', age: 0, agree: false })`.
- [ ] `isValid` is `computed` checking: name non-empty, email includes '@', age > 0, agree === true.
- [ ] Four form inputs: name (q-input), email (q-input), age (q-input type="number"), agree (q-toggle).
- [ ] All inputs use `v-model` bound to `form` properties.
- [ ] Submit button has `:disable="!isValid"`.
- [ ] `watch(isValid, ...)` logs when validity changes.
- [ ] Button is enabled only when all conditions are met.
- [ ] Typing in fields updates `isValid` in real-time.

### p03 — Mouse tracker with template ref
- [ ] `x` and `y` declared with `ref(0)`.
- [ ] `onMounted` adds `window.addEventListener('mousemove', handler)`.
- [ ] Handler updates `x.value` and `y.value` from `event.clientX` / `event.clientY`.
- [ ] `onUnmounted` removes the listener with `removeEventListener`.
- [ ] Template displays `x` and `y` coordinates.
- [ ] `boxRef` declared as `ref(null)` for template ref.
- [ ] `ref="boxRef"` on a `<div>` in template.
- [ ] `onMounted` logs `boxRef.value.offsetWidth` (or `clientWidth`).
- [ ] No memory leak: listener removed on unmount.

## How to verify

Use the Docker container (see quasar/README.md):
```bash
docker build -t quasar-dev .
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
# Inside container:
quasar create test-app
cp easy/p01-solve.vue test-app/src/pages/Index.vue
cd test-app && quasar dev
```
Open http://localhost:8080 and verify:
- Counter increments/decrements when buttons clicked.
- Computed values update when dependencies change.
- Console shows watch logs when values change.
- Timer starts/stops correctly and doesn't leak (check console for cleanup log).
- Mouse coordinates update as you move the mouse.
- Submit button enables/disables based on form validity.
