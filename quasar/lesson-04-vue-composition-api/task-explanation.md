# Lesson 04 — Vue 3 Composition API: script setup, ref, reactive, computed, watch, lifecycle hooks

## What you'll learn
- How to write components using `<script setup>` (the modern Vue 3 way).
- How to manage state with `ref()` and `reactive()`.
- How to derive state with `computed()` and react to changes with `watch()`.
- How to use lifecycle hooks and extract reusable logic into composables.

## Lesson

The Composition API is Vue 3's way of writing component logic. It replaces the Options API (`data()`, `methods:`, `computed:`) with a more flexible, composable approach.

### ref vs reactive

```vue
<script setup>
import { ref, reactive } from 'vue'

// ref: for single values (primitives)
const count = ref(0)
count.value++  // .value in script

// reactive: for objects with multiple properties
const user = reactive({ name: 'Alice', age: 25 })
user.name = 'Bob'  // no .value needed
</script>
```

### computed and watch

```vue
<script setup>
import { ref, computed, watch } from 'vue'

const items = ref([{ price: 10 }, { price: 20 }])
const total = computed(() => items.value.reduce((sum, i) => sum + i.price, 0))

watch(total, (newVal, oldVal) => {
  console.log(`Total changed from ${oldVal} to ${newVal}`)
})
</script>
```

### Lifecycle hooks

```vue
<script setup>
import { onMounted, onUnmounted } from 'vue'

onMounted(() => { console.log('DOM ready') })
onUnmounted(() => { console.log('Cleaning up') })
</script>
```

### Key rules
- Use `ref()` for primitives, `reactive()` for objects.
- Always use `.value` with refs in script (not in template).
- `computed()` is cached and read-only — use it for derived values.
- `watch()` for side effects, `computed()` for derived state.
- Lifecycle hooks must be called synchronously in `<script setup>`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete .vue component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.vue` — Create a counter using `ref(0)`. Display the count, with increment and decrement buttons. Use `<script setup>`.

   WHAT IT SHOULD LOOK LIKE:
   ```
        0                            <- big count display
   +-----------+ +-----------+
   | Increment | | Decrement |         <- q-btn pair
   +-----------+ +-----------+
   ```
2. `easy/p02-solve.vue` — Create a reactive user object (`reactive({ name, email, role })`). Display all three properties. Add a button that changes the name.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------+
   | Alice                        |   <- name
   | alice@x.com                  |   <- email
   | [Admin]                      |   <- role badge
   +------------------------------+
   [ Change Name ]                <- updates name on click
   ```
3. `easy/p03-solve.vue` — Create a computed `fullName` from `firstName` and `lastName` refs. Display it. Add inputs to change both names.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Ada Lovelace                        <- computed fullName
   +------------------+
   | Ada              |                <- firstName input
   +------------------+
   | Lovelace         |                <- lastName input
   +------------------+
   ```

### Medium
4. `medium/p01-solve.vue` — Create a shopping cart: `items` ref (array of `{ name, price }`), `computed` for `totalPrice`, add/remove item buttons. Display the total.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +---------+ +-----+ +-----+
   | Apple   | | 1.5 | | Add |         <- name+price inputs + Add
   +---------+ +-----+ +-----+
   * Apple  $1.50            [x]
   * Bread  $2.25            [x]
   ---------------------------------
   Total: $3.75                        <- computed, updates live
   ```
5. `medium/p02-solve.vue` — Create a search filter: `searchQuery` ref, `items` ref (array of strings). Use `computed` to filter items by search query. Watch `searchQuery` and log changes.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   | an               |                <- q-input (v-model)
   +------------------+
   * Banana
   * Orange                            <- computed filtered list
   CONSOLE: "an" (each keystroke logs via watch)
   ```
6. `medium/p03-solve.vue` — Create a timer using `onMounted` (start `setInterval`) and `onUnmounted` (clear interval). Display elapsed seconds. Add start/stop buttons.

   WHAT IT SHOULD LOOK LIKE:
   ```
   7s                                  <- ticks up each second
   +-------+ +------+
   | Start | | Stop |
   +-------+ +------+
   ```

### Hard
7. `hard/p01-solve.vue` — Build a composable `useCounter` (in the same file or inline) that returns `{ count, double, increment, decrement, reset }`. Use it in the component. Display count and double.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Count: 3                            <- from useCounter()
   Doubled: 6                          <- computed from composable
   +-----------+ +-------+ +-----------+
   | Decrement | | Reset | | Increment |
   +-----------+ +-------+ +-----------+
   ```
8. `hard/p02-solve.vue` — Build a form with `reactive` state (`{ name, email, age, agree }`). Use `computed` for `isValid` (name non-empty, email contains @, age > 0, agree is true). Disable submit button when invalid. Watch `isValid` and log when it changes.

   WHAT IT SHOULD LOOK LIKE:
   ```
   INVALID (submit greyed):        VALID:
   Name:  [ Ada_______ ]           Name:  [ Ada_______ ]
   Email: [ a@b.com____ ]          Email: [ a@b.com____ ]
   Age:   [ 30_________ ]          Age:   [ 30_________ ]
   [x] I agree                     [x] I agree
   [ Submit ]  (disabled)          [ Submit ]  (enabled)
   "Fill in the form"              "Form is valid!"   <- status text
   ```
9. `hard/p03-solve.vue` — Build a mouse position tracker: `onMounted` adds a `mousemove` listener that updates `x` and `y` refs. `onUnmounted` removes the listener. Display coordinates. Add a template ref to a div and log its width on mount.

   WHAT IT SHOULD LOOK LIKE:
   ```
   + - - - - - - - - - - - - - - +
   .  Mouse X: 342   Mouse Y: 187 .   <- dashed box, live values
   .            * cursor            .
   + - - - - - - - - - - - - - - +
   CONSOLE: box width = 400 (once on mount)
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete .vue component from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Test in a Quasar dev environment (see quasar/README.md for Docker setup).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
