# Lesson 02 — Quasar Layout System: q-layout, q-header, q-drawer, q-footer, q-page-container

## What you'll learn
- How Quasar's layout system works (the app shell: header, drawer, footer, content).
- How to configure the `view` prop for different layout behaviors.
- How to build responsive drawers that work on mobile and desktop.
- How to use multiple layouts for different sections of your app.

## Lesson

Quasar's layout system is the **app shell** — the persistent frame around your content. It consists of:

```
┌─────────────────────────────────┐
│  q-header (top bar)             │
├──────┬──────────────────────────┤
│      │                          │
│ q-   │  q-page-container        │
│ drawer│   ┌──────────────────┐  │
│      │   │  q-page (route)  │  │
│      │   └──────────────────┘  │
├──────┴──────────────────────────┤
│  q-footer (bottom bar)          │
└─────────────────────────────────┘
```

### Basic layout structure

```vue
<!-- src/layouts/MainLayout.vue -->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn flat round dense icon="menu" @click="toggleDrawer" />
        <q-toolbar-title>My App</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawerOpen" show-if-above width="250">
      <q-list>
        <q-item-label header>Navigation</q-item-label>
        <q-item clickable to="/">
          <q-item-section avatar><q-icon name="home" /></q-item-section>
          <q-item-section>Home</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
const drawerOpen = ref(false)
function toggleDrawer() {
  drawerOpen.value = !drawerOpen.value
}
</script>
```

### The `view` prop

The `view` prop is a 9-character string: `hHh lpR fFf`
- Row 1 (header): `hHh` — header spans full width, fixed
- Row 2 (content): `lpR` — left drawer pushes content, right drawer is fixed
- Row 3 (footer): `fFf` — footer spans full width, fixed

Uppercase = scrolls with page, lowercase = fixed. `p` = page content (middle row only).

### Key rules
- Every layout must have `q-layout` as the root, with `q-page-container` wrapping `router-view`.
- Every page component must use `q-page` as its root (inside `q-page-container`).
- Use `v-model` on `q-drawer` to control it programmatically.
- Use `show-if-above` for responsive drawer behavior.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete .vue component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.vue` — Build a basic layout with q-layout, q-header (toolbar + title), and q-page-container with a simple q-page.
2. `easy/p02-solve.vue` — Add a left drawer with a navigation list (3 items: Home, About, Contact) and a toggle button in the header.
3. `easy/p03-solve.vue` — Add a footer with 3 q-tabs (Home, Search, Settings) below the page container.

### Medium
4. `medium/p01-solve.vue` — Build a responsive layout: drawer auto-opens on desktop (`show-if-above`), toggleable on mobile, with breakpoint at 1024px.
5. `medium/p02-solve.vue` — Create a layout with both left and right drawers. Left = nav menu, Right = notifications panel. Both toggleable from header buttons.
6. `medium/p03-solve.vue` — Build a layout with `mini` mode drawer. A button in the header toggles between mini (icons only) and full (icons + labels) mode.

### Hard
7. `hard/p01-solve.vue` — Create a header with `reveal` behavior (hides on scroll down, shows on scroll up). Include a toolbar with menu button, title, and 2 action buttons.
8. `hard/p02-solve.vue` — Build a complete admin layout: header with user avatar dropdown, left drawer with collapsible nav sections (Dashboard, Users, Settings with sub-items), footer with status text.
9. `hard/p03-solve.vue` — Create two separate layouts (MainLayout with header+drawer, BlankLayout with just q-page-container) and wire up routes so /login uses BlankLayout and /dashboard uses MainLayout.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete .vue component from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Test in a Quasar dev environment (see quasar/README.md for Docker setup).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
