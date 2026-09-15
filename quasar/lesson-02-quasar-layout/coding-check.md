# Lesson 02 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Basic layout with header
- [ ] Root element is `<q-layout>` with a `view` prop (e.g., `view="hHh lpR fFf"`).
- [ ] `<q-header>` contains a `<q-toolbar>` with a `<q-toolbar-title>`.
- [ ] `<q-page-container>` wraps a `<q-page>` (or `<router-view />`).
- [ ] Header has a background color (`class="bg-primary text-white"` or similar).
- [ ] Page content shows at least a heading or text inside `<q-page>`.

### p02 — Left drawer with nav list
- [ ] `<q-drawer>` has `v-model` bound to a ref (e.g., `drawerOpen`).
- [ ] `drawerOpen` declared with `ref(false)` in `<script setup>`.
- [ ] Header has a button with `@click="toggleDrawer"` (or inline `@click="drawerOpen = !drawerOpen"`).
- [ ] Drawer contains a `<q-list>` with 3 `<q-item>` entries (Home, About, Contact).
- [ ] Each `q-item` has an icon (`q-item-section avatar` + `q-icon`) and a label.
- [ ] Clicking the header button opens/closes the drawer.

### p03 — Footer with tabs
- [ ] `<q-footer>` is inside `<q-layout>`, after `<q-page-container>`.
- [ ] Footer contains `<q-tabs>` with 3 `<q-tab>` components.
- [ ] Each `q-tab` has a `label` and `icon` prop.
- [ ] Footer has a background color (e.g., `class="bg-grey-8 text-white"`).
- [ ] Footer renders at the bottom of the screen, below page content.

## Medium

### p01 — Responsive drawer
- [ ] `<q-drawer>` has `show-if-above` prop.
- [ ] `breakpoint` is set to `1024` (or similar).
- [ ] On desktop (wide screen), drawer is open by default.
- [ ] On mobile (narrow screen), drawer is closed and can be toggled.
- [ ] Header menu button toggles drawer on mobile.
- [ ] `drawerOpen` ref is declared and used in `v-model`.

### p02 — Left and right drawers
- [ ] Two `<q-drawer>` components: one with `side="left"`, one with `side="right"`.
- [ ] Left drawer contains navigation items (q-list).
- [ ] Right drawer contains notification items (q-list or q-card).
- [ ] Header has two buttons: one toggles left drawer, one toggles right drawer.
- [ ] Two separate refs: `leftDrawer` and `rightDrawer`.
- [ ] Both drawers can be open at the same time without breaking layout.

### p03 — Mini mode drawer
- [ ] `<q-drawer>` has `:mini="miniMode"` (or `mini` with a ref).
- [ ] `miniMode` declared with `ref(false)`.
- [ ] Header has a button that toggles `miniMode`.
- [ ] In mini mode, only icons are visible (labels hidden).
- [ ] In full mode, both icons and labels are visible.
- [ ] Drawer width changes when toggling (narrow in mini, wider in full).

## Hard

### p01 — Header with reveal
- [ ] `<q-header>` has `reveal` prop.
- [ ] Header also has `elevated` prop (shadow).
- [ ] Toolbar contains: menu button (icon="menu"), toolbar-title, and 2 action buttons.
- [ ] Scrolling down hides the header; scrolling up reveals it.
- [ ] Menu button toggles the drawer (`@click` handler).
- [ ] Action buttons have icons (e.g., "search", "notifications").

### p02 — Admin layout with collapsible nav
- [ ] Header has a user avatar (use `q-avatar` with an icon or image).
- [ ] Left drawer has collapsible sections using `q-expansion-item`.
- [ ] At least 3 sections: Dashboard, Users, Settings.
- [ ] Each section has sub-items (e.g., Users → List, Add User, Roles).
- [ ] Footer shows status text (e.g., "Connected" or "v1.0.0").
- [ ] Drawer is responsive (`show-if-above`).
- [ ] Sections expand/collapse when clicked.

### p03 — Multiple layouts with routes
- [ ] Two layout components: `MainLayout.vue` and `BlankLayout.vue`.
- [ ] `MainLayout` has `q-header` + `q-drawer` + `q-page-container`.
- [ ] `BlankLayout` has only `q-page-container` + `router-view` (no header/drawer).
- [ ] Routes file defines two parent routes: `/` → MainLayout, `/login` → BlankLayout.
- [ ] `/dashboard` is a child of MainLayout route.
- [ ] `/login` page is a child of BlankLayout route.
- [ ] Navigating to `/login` shows no header/drawer.
- [ ] Navigating to `/dashboard` shows full layout with header and drawer.
- [ ] Each layout uses `q-layout` as root with a `view` prop.

## How to verify

Use the Docker container (see quasar/README.md):
```bash
docker build -t quasar-dev .
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
# Inside container:
quasar create test-app
# Copy your layout to test-app/src/layouts/MainLayout.vue
# Copy your page to test-app/src/pages/Index.vue
cd test-app && quasar dev
```
Open http://localhost:8080 to see your layout. Test:
- Resize browser to mobile width → drawer should change behavior.
- Click menu button → drawer should toggle.
- Scroll page → header reveal should work (if using `reveal`).
