# Lesson 06 — Common Mistakes

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
