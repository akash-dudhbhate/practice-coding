# Lesson 06 — Concepts Explained (Vue Router in Quasar)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Route Definitions — The Route Table

**What:** Routes are defined in `src/router/routes.js` as an array of route objects. Each route maps a URL path to a component.

```javascript
// src/router/routes.js
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'about', component: () => import('pages/About.vue') },
      { path: 'users/:id', component: () => import('pages/UserDetail.vue') },
    ],
  },
  {
    path: '/login',
    component: () => import('pages/Login.vue'),
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue'),
  },
]

export default routes
```

Key fields: `path` (URL), `component` (page/layout), `name` (optional, for named routes), `children` (nested routes), `meta` (custom data like auth requirements), `redirect`.

**Why it exists:** Without a router, a web app is a single page — you can't have different "pages" with different URLs. Routes map URLs to components so users can navigate, bookmark, share links, and use the back button. The route table is the central source of truth for all navigation.

**Where it's used:** Every multi-page Quasar app. The `routes.js` file is the navigation blueprint — every page in your app has an entry here.

**What goes wrong without it:**
- Missing route for a path → navigating to it shows a blank page or 404.
- Forgetting the catch-all route (`/:catchAll(.*)*`) → unknown URLs show blank page instead of a proper 404.
- Wrong path syntax → `path: 'users/:id'` without leading `/` → relative path, may resolve incorrectly. Use `/users/:id` for absolute paths.

---

## Lazy Loading Routes — Code Splitting

**What:** Using dynamic `import()` for route components loads them on demand — only when the user navigates to that route.

```javascript
// Lazy loading (recommended):
const routes = [
  {
    path: '/dashboard',
    component: () => import('pages/Dashboard.vue'),  // loaded when user visits /dashboard
  },
  {
    path: '/settings',
    component: () => import('pages/Settings.vue'),   // loaded when user visits /settings
  },
]

// Eager loading (NOT recommended for most routes):
import Dashboard from 'pages/Dashboard.vue'
const routes = [
  { path: '/dashboard', component: Dashboard },  // bundled in main chunk
]
```

**Why it exists:** Without lazy loading, ALL page components are bundled into one large JavaScript file. For an app with 50 pages, the user downloads all 50 pages' code even if they only visit one. Lazy loading splits each route into a separate chunk — the user only downloads the code for pages they actually visit. This dramatically reduces initial load time.

**Where it's used:** Every route in production apps. The only exception is critical pages (like the home page or login) that most users will visit immediately — these can be eagerly loaded.

**What goes wrong without it:**
- Eager loading all routes → huge initial bundle → slow first page load → poor Core Web Vitals.
- Using `import('...')` without `()` → `component: import('pages/Dashboard.vue')` → error. It must be a function: `component: () => import('...')`.
- Forgetting to configure webpack chunks → all lazy chunks may still end up in one file. Quasar handles this by default, but custom configs can break it.

---

## Navigation Guards — Route Protection

**What:** Navigation guards are functions that run before, during, or after route navigation. They can redirect, cancel, or allow navigation.

```javascript
// src/router/index.js
import { route } from 'quasar/wrappers'
import { createRouter } from 'vue-router'
import routes from './routes'

export default route(function () {
  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,
  })

  // Global before guard — runs on every navigation
  Router.beforeEach((to, from) => {
    const isLoggedIn = localStorage.getItem('token')

    // Check if route requires auth
    if (to.meta.requiresAuth && !isLoggedIn) {
      return { path: '/login', query: { redirect: to.fullPath } }
    }

    // Allow navigation
    return true
  })

  return Router
})
```

Per-route guard:
```javascript
{
  path: '/admin',
  component: () => import('pages/Admin.vue'),
  beforeEnter: (to, from) => {
    if (!isAdmin()) return '/dashboard'
    return true
  }
}
```

In-component guard:
```vue
<script setup>
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('You have unsaved changes. Leave?')
  if (!answer) return false  // cancel navigation
})
</script>
```

**Why it exists:** Not all pages should be accessible to all users. Admin pages need admin auth, profile pages need login, some pages need specific conditions (e.g., completed onboarding). Guards let you enforce these rules centrally — without them, users could type any URL and access any page.

**Where it's used:** Auth protection (redirect to login if not authenticated), role-based access (admin-only pages), unsaved changes warning, analytics tracking, loading data before navigation.

**What goes wrong without it:**
- No auth guard → users can access protected pages by typing the URL directly.
- Returning `undefined` instead of `true` → navigation may hang in some router versions. Always explicitly return `true` to allow.
- Async guards without `async/await` → `beforeEach(async (to) => { const user = await checkAuth(); if (!user) return '/login' })` works, but forgetting `async` → returns a Promise that never resolves → navigation hangs.
- Not returning anything in a guard → some versions treat it as "allow", others as "cancel". Be explicit.

---

## Route Params — Dynamic Segments

**What:** Route params are dynamic URL segments (prefixed with `:`) that you can access in the component via `useRoute()`.

```javascript
// Route definition
{ path: '/users/:id', component: () => import('pages/UserDetail.vue') }
// URL: /users/42 → params.id = '42'
```

```vue
<!-- pages/UserDetail.vue -->
<script setup>
import { useRoute, watch } from 'vue-router'
import { ref, onMounted } from 'vue'

const route = useRoute()
const user = ref(null)

async function fetchUser() {
  const res = await fetch(`/api/users/${route.params.id}`)
  user.value = await res.json()
}

onMounted(fetchUser)

// React to param changes (same component, different param)
watch(() => route.params.id, fetchUser)
</script>

<template>
  <q-page>
    <p>User ID: {{ $route.params.id }}</p>
    <p v-if="user">{{ user.name }}</p>
  </q-page>
</template>
```

**Why it exists:** Many pages display data based on a URL parameter — user profiles (`/users/:id`), product pages (`/products/:slug`), blog posts (`/posts/:id`). Params let you build one component that handles any ID, with the ID coming from the URL (bookmarkable, shareable).

**Where it's used:** User profile pages, product detail pages, blog post pages, edit forms (`/posts/:id/edit`), category pages.

**What goes wrong without it:**
- Accessing params without `useRoute()` → in `<script setup>`, `this.$route` doesn't work (no `this`). Must use `const route = useRoute()`.
- Not watching param changes → navigating from `/users/1` to `/users/2` uses the same component → Vue reuses it → `onMounted` doesn't fire again → stale data. Watch `route.params.id` to refetch.
- Params are always strings → `route.params.id` is `'42'` (string), not `42` (number). Convert with `Number()` if needed.

---

## Nested Routes — Layout + Child Pages

**What:** Nested routes let a layout component render child pages via `<router-view />`. The layout is the parent route, child pages are in `children`.

```javascript
// routes.js
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'dashboard', component: () => import('pages/Dashboard.vue') },
      { path: 'settings', component: () => import('pages/Settings.vue') },
    ],
  },
]
```

```vue
<!-- layouts/MainLayout.vue -->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header>...</q-header>
    <q-drawer>...</q-drawer>
    <q-page-container>
      <router-view />  <!-- child route renders here -->
    </q-page-container>
  </q-layout>
</template>
```

**Why it exists:** Apps have shared layouts — a header and sidebar that stay constant while the content area changes. Without nested routes, you'd put the layout in every page component (duplication) or use a global wrapper (inflexible). Nested routes let the layout be a parent route with `<router-view />` for child content.

**Where it's used:** Every Quasar app with a layout. Multiple layouts (admin, public, auth) each have their own parent route with children.

**What goes wrong without it:**
- Forgetting `<router-view />` in the layout → child pages don't render. You see the layout but no content.
- Child path without empty string → `{ path: '/', children: [{ path: '/' }] }` → double slash. Use `path: ''` for the index child.
- Not nesting children → pages render without the layout (no header, no drawer).
- Deeply nested routes (3+ levels) → complex, hard to manage. Keep to 2 levels (layout → page).

---

## RouterLink and Programmatic Navigation

**What:** `<router-link>` creates navigation links (renders as `<a>`). `useRouter()` provides programmatic navigation methods.

```vue
<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goToProfile() {
  router.push('/profile')
}

function goToUser(id) {
  router.push({ name: 'userDetail', params: { id } })
}

function goBack() {
  router.back()
}
</script>

<template>
  <!-- RouterLink for static links -->
  <router-link to="/about">About</router-link>

  <!-- Quasar components with `to` prop act as router-links -->
  <q-btn to="/dashboard" label="Dashboard" />
  <q-item to="/settings" clickable>Settings</q-item>

  <!-- Programmatic navigation -->
  <q-btn @click="goToProfile" label="Profile" />
  <q-btn @click="goToUser(42)" label="User 42" />
</template>
```

**Why it exists:** Navigation needs to be both declarative (links in templates) and imperative (navigate after form submit, after API call, on condition). `<router-link>` handles declarative — it renders an `<a>` tag, supports active classes, and works with browser history. `useRouter()` handles imperative — `push()`, `replace()`, `back()`, `forward()`.

**Where it's used:** `<router-link>` / `to` prop — navigation menus, breadcrumbs, "view all" links. `useRouter()` — redirect after login, redirect after form submit, conditional navigation, back button.

**What goes wrong without it:**
- Using `<a href="/about">` instead of `<router-link to="/about">` → full page reload → loses SPA behavior, slow navigation, loses app state.
- Calling `router.push()` without importing `useRouter` → `router is not defined` error.
- Using `router.push({ path: '/users', params: { id: 1 } })` → params are IGNORED when using `path`. Use `router.push({ name: 'users', params: { id: 1 } })` (named route) or `router.push('/users/1')` (path with param).
- `router.push()` to the same route → Vue Router 4 throws `NavigationDuplicated` error. Handle with `.catch(() => {})`.

---

## Route Meta — Custom Route Data

**What:** `meta` is an object on each route where you store custom data — auth requirements, page titles, roles, etc.

```javascript
// routes.js
const routes = [
  {
    path: '/dashboard',
    component: () => import('pages/Dashboard.vue'),
    meta: { requiresAuth: true, title: 'Dashboard' }
  },
  {
    path: '/admin',
    component: () => import('pages/Admin.vue'),
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Admin Panel' }
  },
  {
    path: '/login',
    component: () => import('pages/Login.vue'),
    meta: { guestOnly: true, title: 'Login' }
  },
]
```

```javascript
// Accessing meta in guards
Router.beforeEach((to) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    return '/login'
  }
  if (to.meta.guestOnly && isLoggedIn()) {
    return '/dashboard'
  }
  document.title = to.meta.title || 'My App'
})
```

**Why it exists:** Routes often need associated metadata — does this page require auth? What's the page title? What roles can access it? Without `meta`, you'd hardcode these checks in each component or maintain a separate lookup table. `meta` keeps route-specific data with the route definition.

**Where it's used:** Auth/role checks in navigation guards, page titles, breadcrumbs, analytics page names, feature flags per route.

**What goes wrong without it:**
- Checking auth in every component → duplicated logic, easy to forget on new pages. Use `meta.requiresAuth` + a global guard.
- `to.meta` is merged from parent and child routes → if parent has `meta.requiresAuth` and child doesn't, the child inherits it. Be aware of this.
- Using `meta` for complex logic → meta is for simple flags/data. Don't put functions in meta.

---

## Query Parameters — URL Search Params

**What:** Query params are key-value pairs after `?` in the URL. Access them via `route.query`.

```javascript
// URL: /search?q=vue&page=2&sort=desc
// route.query = { q: 'vue', page: '2', sort: 'desc' }
```

```vue
<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

function nextPage() {
  router.push({
    path: '/search',
    query: {
      q: route.query.q,
      page: Number(route.query.page) + 1,
      sort: route.query.sort,
    }
  })
}
</script>

<template>
  <p>Searching for: {{ $route.query.q }}</p>
  <p>Page: {{ $route.query.page }}</p>
</template>
```

**Why it exists:** Query params represent optional, non-hierarchical data — search terms, page numbers, filters, sort order. Unlike path params (which identify a resource), query params modify how a resource is displayed. They're bookmarkable and shareable.

**Where it's used:** Search pages, paginated lists, filter/sort controls, tracking parameters (UTM codes), shareable filtered views.

**What goes wrong without it:**
- Using path params for search → `/search/vue/page/2/sort/desc` → ugly, not semantic. Use query params: `/search?q=vue&page=2&sort=desc`.
- Query params are always strings → `route.query.page` is `'2'`, not `2`. Convert with `Number()`.
- Not watching `route.query` → changing query params (e.g., clicking "next page") reuses the same component → data doesn't refresh. Watch `route.query` to refetch.
- Pushing query without path → `router.push({ query: { page: 2 } })` → replaces query on current path. Usually fine, but be explicit if needed.

---

## Scroll Behavior — Controlling Scroll on Navigation

**What:** Vue Router's `scrollBehavior` function controls where the page scrolls when navigating between routes.

```javascript
// src/router/index.js
const Router = createRouter({
  scrollBehavior(to, from, savedPosition) {
    // If browser back/forward, restore previous position
    if (savedPosition) {
      return savedPosition
    }
    // If route has a hash (#section), scroll to that element
    if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    }
    // Default: scroll to top
    return { left: 0, top: 0 }
  },
  routes,
})
```

**Why it exists:** By default, navigating to a new route keeps the current scroll position — which is confusing (you're on a new page but scrolled halfway down). `scrollBehavior` lets you: scroll to top on new pages, restore position on back/forward, and scroll to anchors (hash links).

**Where it's used:** Every Quasar app — Quasar sets a default `scrollBehavior` that scrolls to top. Customize it for anchor links, smooth scrolling, or saved position restoration.

**What goes wrong without it:**
- No scroll behavior → navigating from a long page to a short page → user is scrolled to a position that doesn't exist → confusing.
- Forgetting `savedPosition` → back button doesn't restore scroll position → users lose their place in long lists.
- Wrong `el` selector in hash → `{ el: '#nonexistent' }` → no scroll, no error. Ensure the element exists.
