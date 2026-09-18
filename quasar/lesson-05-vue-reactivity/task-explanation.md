# Lesson 05 — Vue Reactivity System: ref vs reactive, deep reactivity, watchEffect, computed caching

## What you'll learn
- The difference between `ref()` and `reactive()` and when to use each.
- How Vue's deep reactivity tracks nested object changes.
- How `watchEffect` auto-tracks dependencies vs `watch` explicit tracking.
- Why `computed()` caching matters for performance.
- How to use `nextTick`, `shallowRef`, and `toRefs` correctly.

## Lesson

Vue's reactivity system is what makes it "magic" — change data, and the UI updates automatically. Understanding how it works under the hood prevents subtle bugs.

### ref vs reactive

```vue
<script setup>
import { ref, reactive } from 'vue'

// ref: single value, use .value in script
const count = ref(0)
count.value++

// reactive: object, direct property access
const state = reactive({ count: 0, name: 'Alice' })
state.count++
</script>
```

### Deep reactivity

```vue
<script setup>
const data = reactive({
  user: { profile: { name: 'Alice', settings: { theme: 'dark' } } }
})
// All nested changes are tracked:
data.user.profile.settings.theme = 'light'  // triggers update
</script>
```

### watchEffect vs watch

```vue
<script setup>
import { ref, watch, watchEffect } from 'vue'

const a = ref(1)
const b = ref(2)

// watch: explicit sources, gets old/new values
watch([a, b], ([newA, newB], [oldA, oldB]) => {
  console.log(`a: ${oldA}→${newA}, b: ${oldB}→${newB}`)
})

// watchEffect: auto-tracks, runs immediately, no old values
watchEffect(() => {
  console.log(`a=${a.value}, b=${b.value}`)
})
</script>
```

### Key rules
- `ref()` for primitives, `reactive()` for objects.
- `computed()` is cached — use it instead of methods for derived values.
- `watch()` when you need old values or explicit control.
- `watchEffect()` when you want auto-tracking and immediate execution.
- Use `nextTick()` before accessing DOM that was just rendered with `v-if`.
- Never destructure `reactive()` without `toRefs()`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete .vue component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.vue` — Create a `ref` and a `reactive` side by side. ref holds a string (title), reactive holds `{ author, year }`. Display all three. Add a button that updates all values.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Title:  Vue Guide            <- ref string
   Author: Evan You             <- reactive.author
   Year:   2014                 <- reactive.year
   [ Update All ]               <- changes all three at once
   ```
2. `easy/p02-solve.vue` — Create a nested reactive object (3 levels deep: `user.profile.settings.theme`). Change the deepest property via a button. Display the value and confirm the UI updates.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Theme: light                 <- deepest nested property
   [ Toggle Theme ]             -> "Theme: dark" (and back)
   ```
3. `easy/p03-solve.vue` — Create a `computed` for `fullName` from `firstName` and `lastName` refs. Display it in TWO places in the template. Add a button that changes `firstName` — confirm the computed only calculates once (add a console.log in the computed to prove caching).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Full name: Ada Lovelace      <- computed shown twice,
   Again: Ada Lovelace              one cached calculation
   [ Change First Name ]
   CONSOLE: "computed ran" logs ONCE per actual change
   ```

### Medium
4. `medium/p01-solve.vue` — Create a `watchEffect` that sets `document.title` to `firstName + ' ' + lastName`. Change both names via inputs. Confirm the effect auto-tracks both dependencies.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Browser tab: { Ada Lovelace }      <- tab title tracks both
   First: [ Ada________ ]
   Last:  [ Lovelace___ ]
   ```
5. `medium/p02-solve.vue` — Create a `watch` on a reactive object's specific property using a getter function (`() => state.count`). Log old and new values. Also watch multiple sources (`[state.count, state.name]`).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Count: 2   [ +1 ]
   Name: Ada  [ Change ]
   CONSOLE:
   count: 1 -> 2                        <- old + new values logged
   name: "Ada" -> "Bob"                     per source
   ```
6. `medium/p03-solve.vue` — Create a reactive form object. Use `toRefs` to destructure it. Watch one destructured ref. Confirm reactivity is preserved (changing the original reactive property triggers the watcher).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Name:  [ Ada_______ ]    <- destructured refs still reactive
   Email: [ a@b.com___ ]
   Display: Ada / a@b.com
   CONSOLE: watcher fires on each edit
   ```

### Hard
7. `hard/p01-solve.vue` — Build a comparison: a `computed` filtered list vs a `function` filtered list. Display both. Add a counter showing how many times each is called (use a ref counter incremented in each). Change the filter input and observe computed is called fewer times.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Filter: [ an__________ ]
   Computed list:   * Banana * Orange
   Function list:   * Banana * Orange
   ----------------------------------
   computed calls: 3        <- stays low (cached)
   function calls: 12       <- climbs on every re-render
   ```
8. `hard/p02-solve.vue` — Use `nextTick` to focus an input after showing it with `v-if`. Button toggles `showInput`. After `showInput = true`, `await nextTick()` then call `inputRef.value.focus()`. Confirm no error.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Toggle Input ]
   +----------------------+
   | |                    |   <- appears ALREADY focused
   +----------------------+      (no null errors)
   ```
9. `hard/p03-solve.vue` — Create a `shallowRef` holding an array of 100 generated items. Show that mutating a nested property (e.g., `items.value[0].name = 'X'`) does NOT update the UI, but reassigning `.value` does. Add a `triggerRef` button to force update after nested mutation.

   WHAT IT SHOULD LOOK LIKE:
   ```
   First item: Item 1
   [Mutate nested]      <- UI appears to do NOTHING
   [triggerRef]         <- NOW the mutation shows: "X"
   [Reassign .value]    <- direct change renders instantly
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete .vue component from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Test in a Quasar dev environment (see quasar/README.md for Docker setup).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
