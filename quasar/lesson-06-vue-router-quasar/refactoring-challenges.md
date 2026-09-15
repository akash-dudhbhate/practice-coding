# Lesson 06 — Refactoring Challenges

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
