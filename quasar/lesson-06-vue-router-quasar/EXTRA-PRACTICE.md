# lesson-06-vue-router-quasar — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Quasar routing
<details><summary>Answer</summary>
Quasar uses Vue Router. Routes defined in `src/router/routes.js`. Layout in `src/layouts/`. Pages in `src/pages/`. Quasar CLI sets up the structure.
</details>

## Check 02: Route params
```javascript
{ path: "/user/:id", component: User }
// URL: /user/123
// Access: route.params.id → "123"
```
<details><summary>Answer</summary>
`:id` is a dynamic segment. Access via `useRoute().params.id`. Can have multiple: `/post/:category/:slug`.
</details>

## Check 03: Navigation
```javascript
const router = useRouter();
router.push("/about");
router.push({ name: "user", params: { id: "123" } });
router.back();
```
<details><summary>Answer</summary>
Programmatic navigation. `push` adds to history. `replace` doesn't. Named routes are more robust than paths.
</details>

## Check 04: Route guards
```javascript
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isAuthed()) return "/login";
});
```
<details><summary>Answer</summary>
Run before navigation. `to` = destination, `from` = source. Return false or route to redirect. `meta` for route-specific config.
</details>

## Check 05: Layouts in routes
```javascript
{ path: "/", component: MainLayout, children: [
  { path: "", component: HomePage }
]}
```
<details><summary>Answer</summary>
Routes can have layouts (parent) and pages (children). Layout wraps pages. Common pattern: auth layout for login, main layout for app.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Missing Router View
```vue
<q-page>
  <div>Content</div>
</q-page>
<!-- Where do routes render? -->
```
<details><summary>Answer</summary>
**Bug:** No `<router-view>` — routes don't render.
**Fix:** `<q-page><router-view /></q-page>` or use Quasar's layout which includes it.
</details>

## Debug 02 (Medium: Route Path Mismatch
```javascript
{ path: "users", component: Users }  // missing leading /
```
<details><summary>Answer</summary>
**Bug:** Top-level routes need leading `/`. Without it, may not match.
**Fix:** `{ path: "/users", component: Users }`.
</details>

## Debug 03 (Hard: Lazy Load Syntax
```javascript
{ path: "/admin", component: () => import("./Admin.vue") }
```
<details><summary>Answer</summary>
This is correct — lazy loading with dynamic import. Creates separate chunk. Good for code splitting.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Missing router-view
```vue
<!-- WRONG — routes don't render -->
<q-page>Content</q-page>
<!-- CORRECT -->
<q-page><router-view /></q-page>
```

## Mistake 02: Missing leading slash
```javascript
// WRONG
{ path: "users" }
// CORRECT
{ path: "/users" }
```

## Mistake 03: Not using lazy loading
```javascript
// WRONG — loads everything upfront
import Admin from "./Admin.vue"
{ path: "/admin", component: Admin }
// CORRECT — loads on demand
{ path: "/admin", component: () => import("./Admin.vue") }
```

## Mistake 04: Not using route guards
```javascript
// Add auth guards for protected routes
{ path: "/admin", meta: { requiresAuth: true } }
router.beforeEach((to) => {
  if (to.meta.requiresAuth && !authed) return "/login";
});
```

## Mistake 05: Hardcoded URLs
```javascript
// WRONG
router.push("/user/" + id);
// CORRECT
router.push({ name: "user", params: { id } });
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual Page Switching
### Before
```javascript
const page = ref("home");
page.value === "about" && <About />
```
### After
```vue
<router-view />
```

## Refactor 02 (Medium): Hardcoded URL
### Before
```javascript
router.push("/users/" + id);
```
### After
```javascript
router.push({ name: "user", params: { id } });
```

## Refactor 03 (Hard): No Lazy Loading
### Before
```javascript
import Admin from "./Admin.vue";
{ path: "/admin", component: Admin }
```
### After
```javascript
{ path: "/admin", component: () => import("./Admin.vue") }
```

---

## Approach Comparison — different ways to solve it

## Problem: Route Configuration

### Approach 1: Flat routes
```javascript
[
  { path: "/", component: Home },
  { path: "/about", component: About },
  { path: "/admin", component: Admin }
]
```

### Approach 2: Nested with layouts
```javascript
[
  { path: "/", component: MainLayout, children: [
    { path: "", component: Home },
    { path: "about", component: About }
  ]},
  { path: "/admin", component: AdminLayout, children: [...] }
]
```

**Winner:** Approach 2 — layouts per section, cleaner.

---

## Problem: Protected Routes

### Approach 1: Per-route guard
```javascript
{ path: "/admin", beforeEnter: requireAuth }
```

### Approach 2: Global guard
```javascript
router.beforeEach((to) => {
  if (to.meta.requiresAuth) return checkAuth();
});
```

**Winner:** Approach 2 — centralized, consistent.
