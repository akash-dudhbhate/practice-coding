# Lesson 03 — Quasar Components Deep Dive: q-card, q-list, q-table, q-dialog, q-tabs, q-chip, q-badge

## What you'll learn
- How to use Quasar's most common UI components for content display.
- How to compose components together (cards with lists, dialogs with forms, tabs with panels).
- How to use slots and props to customize component behavior.

## Lesson

Quasar provides 80+ UI components. This lesson covers the most frequently used ones for displaying content and collecting user input.

### QCard — content grouping

```vue
<q-card flat bordered>
  <q-img src="photo.jpg" />
  <q-card-section>
    <div class="text-h6">Title</div>
  </q-card-section>
  <q-card-actions align="right">
    <q-btn flat label="OK" />
  </q-card-actions>
</q-card>
```

### QTable — data display

```vue
<q-table :rows="data" :columns="cols" row-key="id" />
```

Column definitions: `{ name, label, field, sortable, align }`. Use `#body-cell-[name]` slot for custom cell content.

### QDialog — modals

```vue
<q-dialog v-model="open">
  <q-card>...</q-card>
</q-dialog>
```

Use `v-close-popup` on buttons to close the dialog.

### QTabs — content switching

```vue
<q-tabs v-model="tab">
  <q-tab name="a" label="A" />
</q-tabs>
<q-tab-panels v-model="tab">
  <q-tab-panel name="a">Content A</q-tab-panel>
</q-tab-panels>
```

### Key rules
- `q-card` sections provide padding — don't add your own.
- `q-table` needs `row-key` for proper row tracking.
- `q-dialog` needs `v-model` for open/close control.
- `q-tab` `name` must match `q-tab-panel` `name`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete .vue component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.vue` — Build a q-card with an image, title section, body text section, and two action buttons (Share, Read More).
2. `easy/p02-solve.vue` — Build a q-list with 3 q-items, each having an avatar icon, a label, a caption, and a side badge showing a status.
3. `easy/p03-solve.vue` — Build a simple q-tabs with 3 tabs (Overview, Details, Reviews) and matching q-tab-panels showing different text content.

### Medium
4. `medium/p01-solve.vue` — Build a q-table with 3 columns (Name, Email, Role) and 5 sample rows. Enable sorting on Name and Email columns.
5. `medium/p02-solve.vue` — Build a q-dialog that opens from a button click. Inside the dialog, show a q-card with a form (name input, email input) and Cancel/Save buttons using v-close-popup.
6. `medium/p03-solve.vue` — Build a filter bar with 4 removable q-chips (e.g., "JavaScript", "Vue", "Quasar", "CSS"). Clicking the X on a chip removes it from the list.

### Hard
7. `hard/p01-solve.vue` — Build a q-table with a custom body-cell slot for the Status column — render a q-badge (green "Active" or red "Inactive") based on row data. Include 5 rows with mixed statuses.
8. `hard/p02-solve.vue` — Build a user profile card using q-card, q-avatar, q-chip (for skills), q-separator, and q-list (for contact info). The card should have an avatar, name, bio, 3 skill chips, and a contact list with 3 items.
9. `hard/p03-solve.vue` — Build a settings page with q-expansion-item sections (Profile, Privacy, Notifications). Each section expands to show relevant q-toggle switches. Use q-separator between sections.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete .vue component from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Test in a Quasar dev environment (see quasar/README.md for Docker setup).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
