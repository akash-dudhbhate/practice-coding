# Lesson 03 — Concepts Explained (Quasar Components Deep Dive)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## QCard — Content Container

**What:** `<q-card>` is a container with border, shadow, and rounded corners for grouping related content. It has sub-components for structured layout.

```vue
<template>
  <q-card class="my-card" flat bordered>
    <q-img src="https://cdn.quasar.dev/img/parallax2.jpg" />
    <q-card-section>
      <div class="text-h6">Card Title</div>
      <div class="text-subtitle2">Subtitle</div>
    </q-card-section>
    <q-card-section>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </q-card-section>
    <q-card-actions align="right">
      <q-btn flat label="Share" />
      <q-btn flat label="Details" />
    </q-card-actions>
  </q-card>
</template>
```

Sub-components: `q-card-section` (padded content area), `q-card-actions` (button row), `q-card-section horizontal` (side-by-side layout).

**Why it exists:** Cards are the most common UI pattern for grouping content — a product card, a user profile, a news article preview. Without `q-card`, you'd build this with multiple `div`s, custom CSS for shadows/borders/spacing, and inconsistent results. `q-card` provides a consistent, themeable container.

**Where it's used:** Product listings, user profiles, dashboard widgets, article previews, image galleries, settings panels.

**What goes wrong without it:**
- Using raw `div` → no consistent shadow, border, or spacing. Manual CSS needed for every card.
- Forgetting `q-card-section` → content touches card edges, looks cramped.
- Putting buttons outside `q-card-actions` → no alignment, inconsistent spacing between cards.

---

## QList and QItem — List Collections

**What:** `<q-list>` renders a styled list, and `<q-item>` is each entry. Items can have avatars, icons, labels, sublabels, and side actions.

```vue
<template>
  <q-list bordered separator>
    <q-item clickable v-ripple to="/profile">
      <q-item-section avatar>
        <q-icon name="person" />
      </q-item-section>
      <q-item-section>
        <q-item-label>John Doe</q-item-label>
        <q-item-label caption>john@example.com</q-item-label>
      </q-item-section>
      <q-item-section side>
        <q-badge color="primary" label="Admin" />
      </q-item-section>
    </q-item>
  </q-list>
</template>
```

Key `q-item` sections: `avatar` (left icon/avatar), main (label + caption), `side` (right content like badges or toggle). Props on `q-list`: `separator` (dividers between items), `padding`, `dense`.

**Why it exists:** Lists are everywhere — contacts, settings, search results, chat messages. Raw `<ul>/<li>` gives you no styling, no interaction states, no avatar/icon layout. `q-list`/`q-item` provides a structured, consistent list with built-in ripple effects, click handling, and section layout.

**Where it's used:** Navigation menus, contact lists, settings pages, search results, chat message lists, file explorers.

**What goes wrong without it:**
- Using `<ul>/<li>` → no Quasar styling, no ripple effect, inconsistent with app theme.
- Forgetting `q-item-section` → content not properly aligned, avatar and label overlap.
- Missing `:key` when using `v-for` with `q-item` → Vue warnings, rendering bugs on list changes.
- Using `clickable` without `v-ripple` → no tap feedback → feels broken on mobile.

---

## QTable — Data Table

**What:** `<q-table>` renders a full-featured data table with sorting, pagination, filtering, and selection out of the box.

```vue
<template>
  <q-table
    title="Users"
    :rows="users"
    :columns="columns"
    row-key="id"
    :pagination="pagination"
  >
    <template #body-cell-status="props">
      <q-td :props="props">
        <q-badge :color="props.row.active ? 'green' : 'red'">
          {{ props.row.active ? 'Active' : 'Inactive' }}
        </q-badge>
      </q-td>
    </template>
  </q-table>
</template>

<script setup>
import { ref } from 'vue'
const columns = [
  { name: 'name', label: 'Name', field: 'name', sortable: true, align: 'left' },
  { name: 'email', label: 'Email', field: 'email', sortable: true },
  { name: 'status', label: 'Status', field: 'status' },
]
const users = ref([
  { id: 1, name: 'John', email: 'john@test.com', active: true },
  { id: 2, name: 'Jane', email: 'jane@test.com', active: false },
])
const pagination = ref({ sortBy: 'name', descending: false, page: 1, rowsPerPage: 10 })
</script>
```

Key props: `rows` (data array), `columns` (column definitions), `row-key` (unique ID field), `loading`, `filter` (search string), `selection` (`'single'` or `'multiple'`). Slots: `body-cell-[name]` for custom cell rendering, `top` for custom header, `bottom` for custom footer.

**Why it exists:** Data tables are complex — sorting, pagination, filtering, custom cell rendering, row selection, loading states. Building this from scratch takes hundreds of lines. `q-table` handles all of it declaratively and is themeable.

**Where it's used:** Admin dashboards (user lists, orders, products), data-heavy apps (analytics, reports), CRUD interfaces.

**What goes wrong without it:**
- Building a table with raw `<table>` → no sorting, no pagination, no filtering. You'd write all of it manually.
- Missing `row-key` → Vue can't track rows properly → selection and pagination bugs.
- Wrong `field` in column definition → column shows empty or wrong data.
- Forgetting `sortable: true` → column headers not clickable for sorting.

---

## QDialog — Modal Dialogs

**What:** `<q-dialog>` renders a modal overlay. It uses `v-model` to control visibility and can wrap any content.

```vue
<template>
  <q-btn label="Open" @click="dialogOpen = true" />
  <q-dialog v-model="dialogOpen">
    <q-card class="q-pa-md" style="min-width: 300px">
      <q-card-section>
        <div class="text-h6">Confirm Action</div>
      </q-card-section>
      <q-card-section>
        Are you sure you want to delete this item?
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="Cancel" v-close-popup />
        <q-btn color="negative" label="Delete" @click="deleteItem" v-close-popup />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref } from 'vue'
const dialogOpen = ref(false)
function deleteItem() {
  console.log('Deleted!')
}
</script>
```

`v-close-popup` is a directive that closes the dialog when the element is clicked. The dialog can wrap `q-card`, custom components, or even other Quasar components like `q-form`.

**Why it exists:** Modals are essential for confirmations, forms, quick edits, and detail views. Building a modal from scratch requires: overlay positioning, z-index management, focus trapping, click-outside-to-close, escape key handling, and scroll lock. `q-dialog` handles all of this.

**Where it's used:** Delete confirmations, edit forms, detail views, login prompts, image lightboxes, settings modals.

**What goes wrong without it:**
- Building a modal with a fixed `div` → no focus trapping (keyboard users stuck), no escape key, no scroll lock, z-index conflicts.
- Forgetting `v-model` → dialog can't be opened/closed programmatically.
- Not using `v-close-popup` → buttons inside dialog don't close it; you must manually set `dialogOpen = false`.
- Dialog content without `q-card` → raw content with no styling, no border, looks broken.

---

## QTabs — Tabbed Navigation

**What:** `<q-tabs>` renders a row of tabs, and `<q-tab>` is each tab. Used with `<q-tab-panels>` for content switching.

```vue
<template>
  <q-tabs v-model="activeTab" class="text-primary">
    <q-tab name="profile" label="Profile" icon="person" />
    <q-tab name="settings" label="Settings" icon="settings" />
    <q-tab name="activity" label="Activity" icon="history" />
  </q-tabs>

  <q-tab-panels v-model="activeTab" animated>
    <q-tab-panel name="profile">
      <div class="text-h6">Profile</div>
      <p>Name: John Doe</p>
    </q-tab-panel>
    <q-tab-panel name="settings">
      <div class="text-h6">Settings</div>
      <p>Theme: Dark mode</p>
    </q-tab-panel>
    <q-tab-panel name="activity">
      <div class="text-h6">Activity</div>
      <p>Last login: Today</p>
    </q-tab-panel>
  </q-tab-panels>
</template>

<script setup>
import { ref } from 'vue'
const activeTab = ref('profile')
</script>
```

Key: `name` on `q-tab` must match `name` on `q-tab-panel`. `v-model` syncs the active tab. Props: `dense`, `inline-label`, `narrow-indicator`, `animated` (on panels).

**Why it exists:** Tabs organize content into sections without requiring navigation — users switch views by clicking tabs. Without `q-tabs`, you'd use `v-if` with buttons, manage active state manually, and build the indicator animation yourself. `q-tabs` handles all of this with proper accessibility (ARIA tab roles).

**Where it's used:** Settings pages (Profile/Privacy/Notifications tabs), dashboards (Overview/Charts/Reports), product pages (Description/Reviews/Specs), user profiles.

**What goes wrong without it:**
- Mismatched `name` between `q-tab` and `q-tab-panel` → clicking tab shows empty panel.
- Forgetting `v-model` on both `q-tabs` and `q-tab-panels` → they don't sync; clicking tab doesn't change content.
- Too many tabs → overflow on mobile. Use `q-tabs` with `dense` or switch to a dropdown.

---

## QChip — Compact Information Tag

**What:** `<q-chip>` renders a small tag/pill — for labels, categories, filters, or contact badges.

```vue
<template>
  <q-chip icon="bookmark" color="primary" text-color="white">
    Vue.js
  </q-chip>
  <q-chip removable @remove="removeChip" color="teal" text-color="white">
    Selected Filter
  </q-chip>
  <q-chip outline color="deep-orange">
    Priority: High
  </q-chip>
</template>

<script setup>
function removeChip() {
  console.log('Chip removed')
}
</script>
```

Key props: `removable` (shows X button), `outline` (border only, no fill), `dense`, `icon` (left icon), `avatar` (left image). Events: `@remove`.

**Why it exists:** Tags and badges are used everywhere — filtering, categorizing, showing selected items, displaying status. `q-chip` provides a consistent, compact, styled tag that can be removable, outlined, or filled, with icons and avatars.

**Where it's used:** Filter bars (selected filters as chips), blog post tags, email labels, shopping cart items, skill badges in profiles.

**What goes wrong without it:**
- Using raw `<span>` with CSS → no consistent styling, no removable button, no icon support.
- `removable` without `@remove` → X button appears but clicking it does nothing useful (chip closes visually but data isn't removed).
- Too many chips → overflow. Use `dense` or wrap in a scrollable container.

---

## QBadge — Status/Count Indicator

**What:** `<q-badge>` renders a small badge — for counts, status indicators, or notification dots.

```vue
<template>
  <q-btn icon="notifications" flat round>
    <q-badge color="red" floating>5</q-badge>
  </q-btn>
  <q-badge color="green" label="Active" />
  <q-badge color="orange" text-color="black">
    <q-icon name="warning" size="14px" class="q-mr-xs" />
    Pending
  </q-badge>
</template>
```

Key props: `color`, `text-color`, `floating` (positions at top-right corner of parent), `transparent`, `label`, `align` (`top`/`middle`/`bottom`).

**Why it exists:** Badges communicate status at a glance — unread count, active/inactive, pending/rejected. `q-badge` provides consistent sizing, colors, and positioning (especially `floating` for notification dots on icons/buttons).

**Where it's used:** Notification counts on bell icons, status indicators in tables/lists, cart item counts, "new" labels on items.

**What goes wrong without it:**
- Using a raw `<span>` → no `floating` positioning, inconsistent colors and sizes.
- `floating` without a positioned parent → badge appears in wrong place.
- Too much text in a badge → badge stretches and looks broken. Badges are for short text (1-3 chars or a word).

---

## QExpansionItem — Collapsible Section

**What:** `<q-expansion-item>` renders a header that expands/collapses to show nested content.

```vue
<template>
  <q-list>
    <q-expansion-item
      icon="settings"
      label="Settings"
      v-model="expanded"
    >
      <q-card>
        <q-card-section>
          <q-toggle v-model="darkMode" label="Dark Mode" />
          <q-toggle v-model="notifications" label="Notifications" />
        </q-card-section>
      </q-card>
    </q-expansion-item>
    <q-expansion-item icon="help" label="Help">
      <q-card>
        <q-card-section>FAQ content here...</q-card-section>
      </q-card>
    </q-expansion-item>
  </q-list>
</template>

<script setup>
import { ref } from 'vue'
const expanded = ref(false)
const darkMode = ref(false)
const notifications = ref(true)
</script>
```

Key props: `v-model` (controlled expand/collapse), `default-opened`, `expand-separator`, `dense`, `switch-toggle-side`, `header-inset-level` / `content-inset-level` (indentation).

**Why it exists:** Collapsible sections organize complex content — settings groups, FAQ items, navigation submenus. Without `q-expansion-item`, you'd use `v-if` with a toggle button and manually manage open/close state and animation. This component handles it with smooth expand/collapse animation.

**Where it's used:** Settings pages (grouped settings), FAQ accordions, sidebar navigation with submenus, filter panels with collapsible sections.

**What goes wrong without it:**
- Manual `v-if` toggle → no smooth animation, no ARIA accessibility, more code.
- Forgetting `v-model` → can't control expansion programmatically.
- Deeply nested expansion items → confusing UX. Limit to 2 levels max.

---

## QAvatar — User/Image Placeholder

**What:** `<q-avatar>` renders a circular container for user images, initials, or icons.

```vue
<template>
  <q-avatar size="40px" class="q-mr-sm">
    <img src="https://cdn.quasar.dev/img/avatar.png" />
  </q-avatar>
  <q-avatar color="primary" text-color="white" size="40px">
    JD
  </q-avatar>
  <q-avatar size="32px" color="teal" text-color="white" icon="person" />
</template>
```

Key props: `size` (e.g., `"40px"`, `"md"`, `"xl"`), `color`, `text-color`, `square` (non-circular), `font-size`.

**Why it exists:** User avatars are everywhere — headers, comments, lists, chat. Without `q-avatar`, you'd manually style circular images with CSS, handle fallbacks (initials when no image), and ensure consistent sizing. `q-avatar` does all of this.

**Where it's used:** App headers (logged-in user), comment sections, user lists, chat messages, profile cards.

**What goes wrong without it:**
- Using raw `<img>` with border-radius → inconsistent sizing, no fallback for missing images.
- Image with wrong aspect ratio → distorted circle. Use square images or `object-fit: cover`.
- Forgetting `size` → avatar defaults to a size that may not fit your layout.

---

## QSeparator — Visual Divider

**What:** `<q-separator>` renders a horizontal or vertical line to separate content.

```vue
<template>
  <q-card>
    <q-card-section>Top content</q-card-section>
    <q-separator />
    <q-card-section>Bottom content</q-card-section>
  </q-card>

  <div class="row">
    <div class="col">Left</div>
    <q-separator vertical />
    <div class="col">Right</div>
  </div>
</template>
```

Key props: `vertical`, `spaced` (adds margin), `inset`, `color`, `dark`.

**Why it exists:** Visual separation improves readability — dividing sections in a card, separating list items, or splitting columns. Without `q-separator`, you'd use CSS borders, which are inconsistent and don't adapt to dark mode automatically.

**Where it's used:** Between card sections, in lists, between toolbar items, in side-by-side layouts.

**What goes wrong without it:**
- Using CSS `<hr>` → no Quasar theming, doesn't adapt to dark mode.
- `vertical` separator without flex row → separator doesn't stretch vertically. Must be in a flex container.
- Forgetting separator → sections blend together, poor visual hierarchy.
