# Lesson 06 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — Read route param
- [ ] `useRoute` imported from 'vue-router'.
- [ ] `const route = useRoute()` in script setup.
- [ ] Template displays `route.params.id` (or `$route.params.id`).
- [ ] Text shows "User ID: X" where X is the param value.
- [ ] Component is wrapped in `<q-page>`.

### p02 — Navigation menu with active highlighting
- [ ] 3 `<q-item>` components with `to` prop: `/`, `/about`, `/contact`.
- [ ] Each `q-item` has `clickable` prop.
- [ ] Each has an icon and label.
- [ ] Active route item is visually highlighted (Quasar does this automatically with `to`).
- [ ] Items are inside a `<q-list>`.

### p03 — Query parameters and next page
- [ ] `useRoute` and `useRouter` imported from 'vue-router'.
- [ ] `route.query.q` and `route.query.page` displayed in template.
- [ ] "Next Page" button calls `router.push` with incremented page number.
- [ ] Page number is converted with `Number()` (query params are strings).
- [ ] Search term is preserved when navigating to next page.

## Medium

### p01 — Route configuration with lazy loading
- [ ] Routes defined as an array of objects.
- [ ] Each route uses `component: () => import('...')` (lazy loading).
- [ ] 3 routes: Home (`/`), About (`/about`), 404 catch-all (`/:catchAll(.*)*`).
- [ ] Each route has `meta: { title: '...' }`.
- [ ] Catch-all route is last in the array.
- [ ] Routes exported as default.

### p02 — onBeforeRouteLeave guard
- [ ] `onBeforeRouteLeave` imported from 'vue-router'.
- [ ] `hasUnsavedChanges` ref declared (default false).
- [ ] Guard checks `hasUnsavedChanges.value` — if true, calls `window.confirm()`.
- [ ] Returns `false` if user cancels (navigation blocked).
- [ ] Returns `true` (or nothing) if user confirms.
- [ ] A form input or toggle sets `hasUnsavedChanges` to true.
- [ ] Navigation works normally when no unsaved changes.

### p03 — User list with named route links
- [ ] `users` array with 5 objects `{ id, name }`.
- [ ] `v-for` renders links for each user.
- [ ] Each link uses `:to="{ name: 'userDetail', params: { id: user.id } }"`.
- [ ] Alternatively uses `:to="'/users/' + user.id"`.
- [ ] Each link displays the user's name.
- [ ] `:key="user.id"` on the v-for element.

## Hard

### p01 — Full nested route configuration
- [ ] Two parent routes: `/` → MainLayout, `/auth` → BlankLayout.
- [ ] MainLayout children: `''` (Home), `dashboard`, `settings`.
- [ ] BlankLayout children: `login`, `register`.
- [ ] All components use lazy loading `() => import('...')`.
- [ ] `meta: { requiresAuth: true }` on Dashboard and Settings routes.
- [ ] Catch-all 404 route at the end.
- [ ] Each route has a `meta.title`.

### p02 — Auth navigation guard
- [ ] `beforeEach` function defined.
- [ ] Checks `localStorage.getItem('token')` for auth status.
- [ ] If `to.meta.requiresAuth` is true AND no token → returns `{ path: '/login', query: { redirect: to.fullPath } }`.
- [ ] If `to.meta.guestOnly` is true AND token exists → returns `/dashboard`.
- [ ] Otherwise returns `true` (allow navigation).
- [ ] Guard handles all three cases correctly.
- [ ] Redirect URL is preserved in query param for post-login redirect.

### p03 — Product detail with param watching
- [ ] `route.params.id` read in the component.
- [ ] `products` array (mock data) with at least 3 products `{ id, name, price, description }`.
- [ ] `currentProduct` ref or computed that finds the product by `route.params.id`.
- [ ] `watch(() => route.params.id, ...)` detects param changes.
- [ ] Watcher updates the displayed product when navigating to a different ID.
- [ ] Product details displayed: name, price, description.
- [ ] Handles invalid ID gracefully (shows "Product not found").
- [ ] No remounting needed — same component handles different params.

## How to verify

Use the Docker container (see quasar/README.md):
```bash
docker build -t quasar-dev .
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
# Inside container:
quasar create test-app
# Copy routes to test-app/src/router/routes.js
# Copy pages to test-app/src/pages/
cd test-app && quasar dev
```
Open http://localhost:8080 and verify:
- Navigating to `/users/42` shows "User ID: 42".
- Query params display correctly and "Next Page" updates the URL.
- Active nav item is highlighted.
- Confirm dialog appears when leaving with unsaved changes.
- Auth guard redirects to `/login` when accessing protected routes without a token.
- Navigating between product IDs updates the page without full reload.
