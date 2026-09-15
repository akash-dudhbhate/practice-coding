# Lesson 06 — Debug Exercises

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
