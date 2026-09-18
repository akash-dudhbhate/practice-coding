# Lesson 01 — Quasar Basics: Layout, Pages & Components

## What you'll learn
- What Quasar is and why it's built on Vue 3.
- The Quasar project structure.
- How to create a page and use Quasar components.

## Lesson

**Quasar** is a Vue 3 framework that lets you build SPA, PWA, SSR, mobile (Capacitor/Cordova), and desktop (Electron) apps from **one codebase**.

### Project structure (key folders)
```
src/
  layouts/      -> page layouts (header, drawer, footer wrappers)
  pages/        -> individual route pages
  components/   -> reusable Vue components
  router/       -> route definitions
  App.vue       -> root component
```

### A Quasar page is a Vue Single-File Component (.vue)
```vue
<template>
  <q-page class="flex flex-center">
    <q-btn color="primary" label="Click me" @click="onClick" />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
const count = ref(0)
function onClick() {
  count.value++
}
</script>
```
- `<template>` — the HTML structure. Quasar components start with `q-` (e.g., `q-btn`, `q-page`, `q-card`).
- `<script setup>` — Vue 3 Composition API, the modern way to write components.
- `ref(0)` — reactive state. Access/mutate via `.value` in script, directly in template.

### Key rules
- Every page must wrap content in `<q-page>`.
- Use Quasar components (`q-*`) instead of raw HTML where possible — they handle styling, accessibility, and responsiveness for you.
- `<script setup>` is the recommended style (not Options API).

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete .vue component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-qpage-with-heading.vue` — q-page wrapper with an h1.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------------------+
   |                                          |
   |        Welcome to Quasar                 |   <- <h1> centered on
   |                                          |       q-page (flex-center)
   +------------------------------------------+
   ```
2. `easy/p02-two-buttons-colors.vue` — two q-btn components with different colors.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +--------------+  +--------------+
   | [ Primary ]  |  | [Secondary]  |   <- two q-btn, side by side,
   +--------------+  +--------------+      different colors
   ```
3. `easy/p03-toggle-visibility.vue` — toggle button showing/hiding a message with ref + v-if.

   WHAT IT SHOULD LOOK LIKE:
   ```
   HIDDEN:                  SHOWN (after click):
   +-----------+            +-----------+
   | [ Toggle ]|            | [ Toggle ]|
   +-----------+            +-----------+
                            Hello! I am visible   <- v-if message
   ```

### Medium
4. `medium/p01-text-input-display.vue` — q-input with v-model, real-time display.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | hello                |   <- q-input (v-model)
   +----------------------+
   You typed: hello            <- live echo below
   ```
5. `medium/p02-counter-inc-dec.vue` — counter with increment/decrement/reset, disabled state.

   WHAT IT SHOULD LOOK LIKE:
   ```
        2                        <- big number
   +-----+ +-----+ +-------+
   |  -  | |  +  | | Reset |
   +-----+ +-----+ +-------+
   ("-" button greyed out / disabled at 0)
   ```
6. `medium/p03-todo-list-add-only.vue` — add items to a list with q-input, q-btn, q-list.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------+ +-----+
   | Buy milk       | | Add |   <- q-input + q-btn
   +----------------+ +-----+
   * Buy milk                    <- q-item rows below
   * Walk the dog
   ```

### Hard
7. `hard/p01-todo-complete-delete.vue` — full todo list with toggle done, delete, empty state.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------+ [ Add ]
   | new task       |
   +----------------+
   [ ] Buy milk              [x]
   [x] -Walk the dog-        [x]   <- checked = strikethrough
   ---------------------------------
   1 of 2 completed                <- live counter
   (empty list shows "No todos yet!")
   ```
8. `hard/p02-color-picker-card.vue` — q-color picker with live preview using q-card.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-------------+   +------------------+
   |  q-color    |   | Selected: #1976d2|
   |  picker     |   | +--------------+ |
   |  [######]   |   | |############| |   <- card box filled
   |             |   | |############| |      with the color
   +-------------+   | +--------------+ |
                     +------------------+
   ```
9. `hard/p03-multi-step-form.vue` — 3-step form wizard with conditional rendering.

   WHAT IT SHOULD LOOK LIKE:
   ```
   STEP 1 of 3:             STEP 3 (review):
   Name: [ Ada________ ]    Name:  Ada
   Email: (hidden)          Email: ada@x.com
                [ Next ]    [ Back ] [ Submit ]
   (each step shows ONLY its own fields)
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete .vue component from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Test in a Quasar dev environment (see quasar/README.md for Docker setup).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
