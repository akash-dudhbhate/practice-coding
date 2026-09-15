# Lesson 03 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Card with image and actions
- [ ] `<q-card>` contains `<q-img>` with a src.
- [ ] First `<q-card-section>` has a title (`text-h6` class).
- [ ] Second `<q-card-section>` has body text.
- [ ] `<q-card-actions>` has two `<q-btn>` components (Share, Read More).
- [ ] Buttons use `flat` prop for card-style buttons.
- [ ] Card is wrapped in `<q-page>`.

### p02 — List with badges
- [ ] `<q-list>` contains 3 `<q-item>` components.
- [ ] Each `q-item` has `q-item-section avatar` with a `q-icon`.
- [ ] Each `q-item` has main section with `q-item-label` and `q-item-label caption`.
- [ ] Each `q-item` has `q-item-section side` with a `q-badge`.
- [ ] Badges have different colors (e.g., green for active, red for inactive).
- [ ] List has `separator` or `bordered` prop for visual separation.

### p03 — Tabs with panels
- [ ] `<q-tabs>` has `v-model` bound to a ref (e.g., `activeTab`).
- [ ] 3 `<q-tab>` components with `name` props: "overview", "details", "reviews".
- [ ] Each `q-tab` has a `label` prop.
- [ ] `<q-tab-panels>` has the same `v-model` as `q-tabs`.
- [ ] 3 `<q-tab-panel>` components with matching `name` props.
- [ ] Each panel has different text content.
- [ ] `activeTab` starts at "overview".

## Medium

### p01 — Data table with sorting
- [ ] `columns` array has 3 column objects (name, email, role).
- [ ] Each column has `name`, `label`, `field`, and `sortable: true` (at least for name and email).
- [ ] `rows` array has 5 data objects.
- [ ] `<q-table>` has `:rows`, `:columns`, and `row-key="id"` (or similar unique key).
- [ ] Clicking a sortable column header sorts the table.
- [ ] Table renders all 5 rows with correct data in each column.

### p02 — Dialog with form
- [ ] `dialogOpen` ref declared with `ref(false)`.
- [ ] Button with `@click="dialogOpen = true"` opens the dialog.
- [ ] `<q-dialog>` has `v-model="dialogOpen"`.
- [ ] Inside dialog, `<q-card>` with `q-card-section` for title and form fields.
- [ ] Two `<q-input>` components: name (v-model) and email (v-model).
- [ ] Cancel button has `v-close-popup`.
- [ ] Save button has `v-close-popup` and `@click` handler.
- [ ] Dialog closes when clicking outside or pressing Escape.

### p03 — Removable filter chips
- [ ] `chips` ref is an array of strings (e.g., `['JavaScript', 'Vue', 'Quasar', 'CSS']`).
- [ ] `v-for` renders a `<q-chip>` for each chip with `:key`.
- [ ] Each chip has `removable` prop.
- [ ] `@remove` handler removes the chip from the array (using `.splice` or `.filter`).
- [ ] Clicking X on a chip removes it from the screen.
- [ ] Chips have `color` and `text-color` props for styling.

## Hard

### p01 — Table with custom status badge
- [ ] `columns` array includes a `status` column.
- [ ] `rows` array has 5 objects with `status` field (boolean or string).
- [ ] `#body-cell-status` slot is defined in the q-table.
- [ ] Slot template uses `<q-td :props="props">`.
- [ ] Inside the slot, `<q-badge>` shows "Active" (green) or "Inactive" (red).
- [ ] Badge color is determined by `props.row.active` (or status field).
- [ ] Other columns render normally (not overridden by custom slot).

### p02 — User profile card
- [ ] `<q-card>` wraps the entire profile.
- [ ] `<q-avatar>` shows an image or initials (size at least 60px).
- [ ] Name displayed with `text-h6` class.
- [ ] Bio text in a `q-card-section`.
- [ ] 3 `<q-chip>` components for skills (e.g., "Vue", "JavaScript", "CSS").
- [ ] `<q-separator>` between bio and contact sections.
- [ ] `<q-list>` with 3 `q-item` entries for contact info (email, phone, location).
- [ ] Each contact item has an icon in the avatar section.

### p03 — Settings with expansion items
- [ ] 3 `<q-expansion-item>` components (Profile, Privacy, Notifications).
- [ ] Each has an `icon` and `label` prop.
- [ ] Profile section has toggles for "Show Email" and "Show Phone".
- [ ] Privacy section has toggles for "Private Account" and "Allow Tags".
- [ ] Notifications section has toggles for "Email Alerts" and "Push Notifications".
- [ ] Each `q-expansion-item` wraps content in a `q-card` with `q-card-section`.
- [ ] `<q-separator>` between expansion items (or `expand-separator` prop).
- [ ] Toggles use `q-toggle` with `v-model` and `label`.
- [ ] All toggle refs declared in script setup.

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
- Cards render with proper shadow and spacing.
- Table sorts when clicking column headers.
- Dialog opens/closes correctly and closes on Escape.
- Tabs switch content when clicked.
- Chips disappear when X is clicked.
- Expansion items expand/collapse smoothly.
