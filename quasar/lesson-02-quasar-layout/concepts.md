# Lesson 02 — Concepts Explained (Quasar Layout System)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## QLayout — The Root Layout Container

**What:** `<q-layout>` is the top-level wrapper that sets up the entire app shell — header, drawers, footer, and page area all live inside it.

```vue
<template>
  <q-layout view="hHh lpR fFf">
    <q-header>...</q-header>
    <q-drawer>...</q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
    <q-footer>...</q-footer>
  </q-layout>
</template>
```

The `view` prop defines how header/drawer/footer relate to each other using a 9-character pattern (3 rows × 3 letters). For example, `hHh lpR fFf` means: header is always at top, left drawer pushes content, right drawer is fixed, footer at bottom.

**Why it exists:** Every app needs a consistent shell — a header at top, maybe a side drawer for navigation, a footer at bottom. Without a unified layout system, each page would need to re-implement the header and drawer, leading to duplication and inconsistency. `q-layout` provides this shell once, and every page just plugs into it.

**Where it's used:** In the `src/layouts/` folder. A typical Quasar app has one or more layout files (e.g., `MainLayout.vue`, `AdminLayout.vue`). Pages are rendered inside the layout via `<router-view />` in the `q-page-container`.

**What goes wrong without it:**
- No `q-layout` wrapper → `q-header`, `q-drawer`, `q-footer` don't render or behave incorrectly — they require a parent `q-layout`.
- Content has no consistent shell → header/drawer must be re-created on every page.
- Wrong `view` prop → drawer overlaps content instead of pushing it, or header scrolls away when it shouldn't.

---

## QHeader — Top App Bar

**What:** `<q-header>` renders a top bar, typically containing a toolbar with a title, navigation toggle, and action buttons.

```vue
<template>
  <q-header class="bg-primary text-white">
    <q-toolbar>
      <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />
      <q-toolbar-title>My App</q-toolbar-title>
      <q-btn flat round dense icon="search" />
    </q-toolbar>
  </q-header>
</template>
```

Key props: `elevated` (adds shadow), `reveal` (hides on scroll down, shows on scroll up), `height-hint` (optimizes rendering).

**Why it exists:** Almost every app needs a top bar with branding and actions. Without a dedicated header component, you'd manually position a `div` with `position: fixed`, handle scroll behavior, and manage z-index — all of which is error-prone and tedious. `q-header` handles positioning, scroll reveal, and responsive behavior automatically.

**Where it's used:** Inside `q-layout`. Common in: app dashboards, admin panels, e-commerce apps (cart icon in header), social apps (notifications bell).

**What goes wrong without it:**
- Using a fixed `div` instead → doesn't integrate with drawer (drawer won't know about header height → overlap), no scroll reveal, manual z-index management.
- Forgetting `q-toolbar` inside → content not properly aligned, no built-in spacing.
- Header outside `q-layout` → component doesn't render or throws a warning.

---

## QDrawer — Side Navigation Panel

**What:** `<q-drawer>` renders a collapsible side panel — typically for navigation menus, filters, or secondary content.

```vue
<template>
  <q-drawer v-model="leftDrawerOpen" show-if-above width="250">
    <q-list>
      <q-item clickable to="/">
        <q-item-section avatar>
          <q-icon name="home" />
        </q-item-section>
        <q-item-section>Home</q-item-section>
      </q-item>
    </q-list>
  </q-drawer>
</template>

<script setup>
import { ref } from 'vue'
const leftDrawerOpen = ref(false)
</script>
```

Key props: `v-model` (controls open/close), `side` (`left` or `right`), `show-if-above` (auto-open on desktop, toggle on mobile), `width` / `mini` (collapsed icon-only mode), `overlay` (covers content instead of pushing it).

**Why it exists:** Side navigation is a core pattern in modern apps — Gmail's folder list, Slack's channel sidebar, admin panel menus. A drawer needs to: open/close on command, respond to screen size (overlay on mobile, push on desktop), animate smoothly, and sync with the header toggle button. `q-drawer` handles all of this.

**Where it's used:** Navigation menus, filter panels in e-commerce, settings sidebars, file explorers, email folder lists.

**What goes wrong without it:**
- Not binding `v-model` → drawer can't be toggled programmatically; the menu button does nothing.
- Missing `show-if-above` → drawer is always closed on desktop (bad UX) or always open on mobile (covers content).
- Using `overlay` on desktop → content is hidden behind drawer; users must close it to see content. Use `overlay` only on mobile.
- Forgetting to declare the ref → `leftDrawerOpen is not defined` error.

---

## QFooter — Bottom Bar

**What:** `<q-footer>` renders a bar at the bottom of the screen — for navigation tabs, copyright, or action buttons.

```vue
<template>
  <q-footer class="bg-grey-8 text-white">
    <q-tabs>
      <q-tab label="Home" icon="home" />
      <q-tab label="Search" icon="search" />
      <q-tab label="Profile" icon="person" />
    </q-tabs>
  </q-footer>
</template>
```

**Why it exists:** Mobile apps commonly use bottom tab bars for primary navigation (Instagram, Twitter, iOS Settings). `q-footer` integrates with the layout system — it knows about the header and drawer, adjusts for safe areas on notched devices, and can hide on scroll like the header.

**Where it's used:** Mobile-first apps with bottom tab navigation, desktop apps with status bars, apps with persistent action bars (e.g., "Save" button always visible at bottom).

**What goes wrong without it:**
- Using a fixed `div` at bottom → doesn't account for safe areas (iPhone notch), overlaps with content, doesn't hide on scroll.
- Footer outside `q-layout` → doesn't render properly.
- Too many tabs in footer → cramped, hard to tap on mobile. Keep to 3-5 tabs max.

---

## QPageContainer — Content Wrapper

**What:** `<q-page-container>` is the wrapper that holds all page content. It sits between the header/drawer/footer and the actual page.

```vue
<template>
  <q-layout>
    <q-header>...</q-header>
    <q-drawer>...</q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
```

**Why it exists:** The layout system needs to know where page content goes so it can calculate spacing — how much padding to add for the header height, drawer width, and footer height. `q-page-container` is the bridge between the layout shell and individual pages. Without it, `q-page` inside your route components has no parent context.

**Where it's used:** Inside every `q-layout`, wrapping `<router-view />`. You never use it inside a page component — only in the layout file.

**What goes wrong without it:**
- Missing `q-page-container` → `q-page` in child routes throws an error or content has no proper spacing.
- Putting `q-page-container` inside a page instead of layout → nesting errors, broken layout.
- Wrapping non-page content in `q-page-container` → unexpected padding/spacing.

---

## QPage — Individual Page Wrapper

**What:** `<q-page>` wraps the content of a single page/route. It must be a direct child of `q-page-container` (via router-view).

```vue
<template>
  <q-page class="q-pa-md">
    <h1>Dashboard</h1>
    <p>Welcome back!</p>
  </q-page>
</template>
```

Key prop: `padding` (adds default padding) or use `class="q-pa-md"` for custom spacing.

**Why it exists:** `q-page` communicates with the layout system. It tells the layout "I'm the active content area" and receives proper top/bottom padding based on header/footer height. Without it, your content would start at pixel 0 — hidden behind the header.

**Where it's used:** Every page component in `src/pages/`. This is non-negotiable in Quasar — every route page must wrap its content in `q-page`.

**What goes wrong without it:**
- No `q-page` → content renders but is hidden behind the header (no top padding), or Quasar throws a warning about missing `q-page` inside `q-page-container`.
- Using `q-page` outside a layout → error: "q-page must be child of q-page-container".
- Adding `q-page` inside another `q-page` → nesting errors.

---

## QToolbar — Horizontal Bar Layout

**What:** `<q-toolbar>` arranges items in a horizontal row — typically used inside `q-header` or `q-footer`.

```vue
<template>
  <q-toolbar>
    <q-btn flat round dense icon="arrow_back" />
    <q-toolbar-title>Page Title</q-toolbar-title>
    <q-btn flat round dense icon="more_vert" />
  </q-toolbar>
</template>
```

`q-toolbar-title` is special — it takes all available space, pushing other items to the edges.

**Why it exists:** Toolbars have a standard pattern: left action, center/left title, right action. Without `q-toolbar`, you'd use flexbox manually, handle spacing, and ensure the title expands. `q-toolbar` does this with proper spacing and alignment built in.

**Where it's used:** Inside `q-header` (app bar), inside `q-footer` (bottom action bar), as standalone toolbars above content (e.g., filter bars, editor toolbars).

**What goes wrong without it:**
- Using raw flex `div` → inconsistent spacing, no built-in padding, title doesn't auto-expand.
- Multiple `q-toolbar-title` components → both try to expand → unpredictable layout.
- Forgetting `q-toolbar-title` → all items crammed to the left, no centered title.

---

## Layout View Prop — Positioning Matrix

**What:** The `view` prop on `q-layout` is a 9-character string that defines how header, drawer, and footer relate to each other.

```vue
<q-layout view="hHh lpR fFf">
```

The format is 3 rows (header row, content row, footer row), each with 3 letters (left, center, right):
- `l` / `L` — left drawer on this row (lowercase = fixed, uppercase = scrolls with page)
- `h` / `H` — header on this row (lowercase = fixed, uppercase = part of page scroll)
- `r` / `R` — right drawer on this row
- `f` / `F` — footer on this row
- `p` — page content (only in the middle row)

Common patterns:
- `hHh lpR fFf` — standard: header fixed, left drawer pushes content, right drawer fixed, footer fixed
- `hHh LpR lfr` — left drawer above header, right drawer below footer
- `hhh lpr fff` — everything scrolls together

**Why it exists:** Different apps need different layout behaviors. A dashboard might want the drawer to push content; a reading app might want the drawer to overlay. The `view` prop gives you a declarative way to configure this without writing CSS or JavaScript logic.

**Where it's used:** On the `q-layout` in your layout files. You set it once and it applies to all pages using that layout.

**What goes wrong without it:**
- Wrong `view` pattern → drawer overlaps content instead of pushing it, or header scrolls away when it should stay fixed.
- Using lowercase when uppercase is needed → header scrolls with content (usually not what you want).
- Invalid pattern → layout breaks silently or renders incorrectly.

---

## Drawer Mini Mode

**What:** A drawer can collapse to a narrow icon-only strip using the `mini` prop.

```vue
<template>
  <q-drawer v-model="drawerOpen" mini width="57">
    <q-list>
      <q-item to="/" clickable>
        <q-item-section avatar>
          <q-icon name="dashboard" />
        </q-item-section>
        <q-item-section>Dashboard</q-item-section>
      </q-item>
    </q-list>
  </q-drawer>
</template>
```

When `mini` is true, only the avatar/icon sections are shown. The text labels are hidden. You can toggle `mini` to expand/collapse.

**Why it exists:** Many desktop apps have a collapsible sidebar — VS Code, Slack, Gmail. Mini mode saves screen space while keeping navigation accessible. Users can expand the drawer when they need to see labels.

**Where it's used:** Desktop admin panels, IDE-like interfaces, dashboards with limited screen space.

**What goes wrong without it:**
- Setting `mini` without `show-if-above` → on mobile, a 57px drawer is too narrow to be useful.
- Toggling `mini` without animation → jarring layout shift. Quasar animates by default; don't disable it unless you have a reason.
- Icons without labels in mini mode → users can't tell what each icon does. Use tooltips.

---

## Responsive Drawer Behavior

**What:** Quasar drawers can behave differently on mobile vs. desktop using `show-if-above` and `overlay` props.

```vue
<template>
  <!-- Desktop: always open, pushes content. Mobile: overlay, toggleable. -->
  <q-drawer
    v-model="drawerOpen"
    show-if-above
    :width="260"
    :breakpoint="1024"
  >
    <q-list>...</q-list>
  </q-drawer>
</template>
```

- `show-if-above` — auto-opens on screens wider than `breakpoint` (default 1024px)
- `overlay` — drawer covers content instead of pushing it (good for mobile)
- `breakpoint` — pixel width at which drawer switches behavior

**Why it exists:** Mobile and desktop have fundamentally different navigation patterns. On desktop, a persistent sidebar is expected. On mobile, screen space is limited — the drawer should overlay and be toggleable. Without responsive behavior, you'd need separate layouts or manual CSS media queries.

**Where it's used:** Every app that works on both mobile and desktop — which is most Quasar apps since Quasar is cross-platform by design.

**What goes wrong without it:**
- No `show-if-above` → drawer is closed by default on desktop → users don't know navigation exists.
- `overlay` on desktop → content hidden behind drawer → poor UX.
- Wrong `breakpoint` → drawer switches behavior at the wrong screen size (e.g., tablet shows mobile behavior).
- Not syncing `v-model` with header toggle → button doesn't open drawer on mobile.

---

## Multiple Layouts

**What:** Quasar lets you define multiple layouts and assign different routes to different layouts.

```javascript
// src/router/routes.js
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'dashboard', component: () => import('pages/Dashboard.vue') },
    ],
  },
  {
    path: '/admin',
    component: () => import('layouts/AdminLayout.vue'),
    children: [
      { path: '', component: () => import('pages/admin/Panel.vue') },
    ],
  },
  {
    path: '/login',
    component: () => import('layouts/BlankLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Login.vue') },
    ],
  },
]
```

Each layout has its own header, drawer, and footer configuration. Routes are nested as children of the layout route.

**Why it exists:** Different parts of an app often need different shells — a marketing site has a big header with navigation, an admin panel has a dense sidebar, a login page has no header at all. Multiple layouts let you keep these separate without conditional rendering hacks.

**Where it's used:** Apps with distinct sections (public + admin + auth), apps with different navigation for different user roles, landing pages vs. app pages.

**What goes wrong without it:**
- One layout for everything → login page has a nav drawer (confusing), admin panel has marketing header (irrelevant).
- Forgetting to nest routes as children → pages don't render inside the layout.
- Same `q-layout` with `v-if` for different sections → layout re-mounts on every route change → flicker, lost state.
