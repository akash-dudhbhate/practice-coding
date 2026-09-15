# Lesson 06 — Vue Router in Quasar: routes, lazy loading, navigation guards, route params, nested

## What you'll learn
- How to define routes with lazy loading and nested layouts.
- How to protect routes with navigation guards.
- How to use route params and query parameters.
- How to navigate programmatically and with router-link.

## Lesson

Vue Router is the official router for Vue. Quasar pre-configures it — you just define routes in `src/router/routes.js`.

### Route structure

```javascript
// src/router/routes.js
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'about', component: () => import('pages/About.vue') },
    ],
  },
  { path: '/:catchAll(.*)*', component: () => import('pages/Error404.vue') },
]
```

### Navigation guards

```javascript
// src/router/index.js
Router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isLoggedIn()) return '/login'
  return true
})
```

### Using route params and navigation

```vue
<script setup>
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
// route.params.id — from /users/:id
// route.query.q — from /search?q=vue
// router.push('/dashboard') — navigate
</script>
```

### Key rules
- Use `() => import('...')` for lazy loading (code splitting).
- Parent routes (layouts) need `<router-view />` for child content.
- Always add a catch-all 404 route.
- Use `meta` for auth requirements and page titles.
- Use `useRoute()` to read params/query, `useRouter()` to navigate.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete .vue component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.vue` — Create a page that reads a route param (`:id`) and displays it. Use `useRoute()` to access `route.params.id`. Show "User ID: X".
2. `easy/p02-solve.vue` — Create a navigation menu with 3 `q-item` components using the `to` prop (Home, About, Contact). Highlight the active route using Quasar's `exact-active-class` or default active styling.
3. `easy/p03-solve.vue` — Create a page that reads query parameters (`?q=search&page=1`). Display the search term and page number. Add a button that navigates to the next page using `router.push`.

### Medium
4. `medium/p01-solve.vue` — Create a route configuration (as a JavaScript object/array in the script section) with 3 routes: Home, About, and a 404 catch-all. Use lazy loading with `() => import(...)`. Include `meta: { title: '...' }` on each route.
5. `medium/p02-solve.vue` — Create a component with a navigation guard using `onBeforeRouteLeave`. Show a confirm dialog (using `window.confirm`) when the user tries to leave with unsaved changes. Cancel navigation if they say no.
6. `medium/p03-solve.vue` — Create a user list page with links to user detail pages. Use `router-link` or `q-btn :to` with named routes and params (`{ name: 'userDetail', params: { id: user.id } }`). Display 5 user links.

### Hard
7. `hard/p01-solve.vue` — Build a full route configuration with nested routes: MainLayout with children (Home, Dashboard, Settings) and BlankLayout with children (Login, Register). Add `meta: { requiresAuth: true }` on Dashboard and Settings.
8. `hard/p02-solve.vue` — Build a `beforeEach` navigation guard function that checks `localStorage.getItem('token')` for auth. If route `meta.requiresAuth` is true and no token, redirect to `/login` with `query: { redirect: to.fullPath }`. If `meta.guestOnly` and already logged in, redirect to `/dashboard`.
9. `hard/p03-solve.vue` — Build a product detail page that reads `route.params.id`, fetches product data (mock with a local array), and watches for param changes (navigating from `/products/1` to `/products/2` should update the displayed product without remounting).

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete .vue component from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Test in a Quasar dev environment (see quasar/README.md for Docker setup).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
