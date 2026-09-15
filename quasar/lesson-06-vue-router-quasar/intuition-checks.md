# Lesson 06 — Intuition Checks

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
