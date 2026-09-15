# Lesson 02 — Approach Comparison

## Problem: App Layout

### Approach 1: Custom CSS layout
```css
.header { position: fixed; top: 0; }
.sidebar { position: fixed; left: 0; }
```
**Cons:** Reinventing the wheel, responsive issues.

### Approach 2: Quasar layout
```vue
<q-layout view="hHh lpR fFf">
  <q-header>...</q-header>
  <q-drawer>...</q-drawer>
  <q-page-container><q-page>...</q-page></q-page-container>
</q-layout>
```

**Winner:** Approach 2 — responsive, tested, Material Design.

---

## Problem: Navigation Drawer

### Approach 1: Always visible
```vue
<q-drawer :breakpoint="0">
```

### Approach 2: Responsive
```vue
<q-drawer :breakpoint="500" v-model="open">
```

**Winner:** Approach 2 — overlay on mobile, side bar on desktop.
