# lesson-02-quasar-layout — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Layout structure
What's the correct nesting?
<details><summary>Answer</summary>
`q-layout` → `q-header`, `q-drawer`, `q-page-container` → `q-page` → `router-view`. Each has a specific role.
</details>

## Check 02: View string
```vue
<q-layout view="hHh lpR fFf">
```
<details><summary>Answer</summary>
3 parts: header, middle (left/page/right), footer. Each 3 chars: uppercase = fixed, lowercase = scroll with page. `hHh` = header fixed. `lpR` = left drawer, page, right drawer fixed.
</details>

## Check 03: q-drawer
```vue
<q-drawer v-model="drawerOpen" side="left" bordered>
```
<details><summary>Answer</summary>
Side navigation. `v-model` controls open/close. `side` = left or right. `bordered` adds border. Can be `overlay` (mobile) or `mini` (collapsed).
</details>

## Check 04: q-header
```vue
<q-header elevated>
  <q-toolbar>
    <q-btn flat round icon="menu" @click="drawer = !drawer" />
    <q-toolbar-title>My App</q-toolbar-title>
  </q-toolbar>
</q-header>
```
<details><summary>Answer</summary>
Top bar. `elevated` adds shadow. Contains `q-toolbar` with buttons and title. Common pattern: menu button toggles drawer.
</details>

## Check 05: Responsive drawer
```vue
<q-drawer :breakpoint="500" v-model="drawerOpen">
```
<details><summary>Answer</summary>
`breakpoint` — below this width, drawer becomes overlay (auto-close on navigation). Default 992. Mobile-friendly.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Missing q-layout
```vue
<template>
  <q-header>My Header</q-header>
  <q-page>Content</q-page>
</template>
```
<details><summary>Answer</summary>
**Bug:** Layout components must be inside `<q-layout>`.
**Fix:** Wrap in `<q-layout view="hHh lpR fFf">`.
</details>

## Debug 02 (Medium: Wrong View String
```vue
<q-layout view="hhh lpr fff">
```
<details><summary>Answer</summary>
**Bug:** View string must be uppercase: `hHh lpR fFf`. Lowercase has different meaning.
**Fix:** Use correct format: `view="hHh lpR fFf"`.
</details>

## Debug 03 (Hard: No q-page-container
```vue
<q-layout>
  <q-header>Header</q-header>
  <q-page>Content</q-page>
</q-layout>
```
<details><summary>Answer</summary>
**Bug:** `q-page` must be inside `q-page-container`.
**Fix:** `<q-page-container><q-page>Content</q-page></q-page-container>`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Missing q-layout wrapper
```vue
<!-- WRONG -->
<q-header />
<!-- CORRECT -->
<q-layout><q-header /></q-layout>
```

## Mistake 02: q-page without q-page-container
```vue
<!-- WRONG -->
<q-layout><q-page /></q-layout>
<!-- CORRECT -->
<q-layout><q-page-container><q-page /></q-page-container></q-layout>
```

## Mistake 03: Wrong view string case
```vue
<!-- WRONG — lowercase -->
view="hhh"
<!-- CORRECT — uppercase for fixed -->
view="hHh"
```

## Mistake 04: Not using v-model for drawer
```vue
<!-- WRONG — can't control -->
<q-drawer />
<!-- CORRECT -->
<q-drawer v-model="drawerOpen" />
```

## Mistake 05: Hardcoded layout instead of Quasar's
```css
/* WRONG — custom CSS for layout */
/* CORRECT — use Quasar's layout system */
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): CSS Fixed Header
### Before
```css
.header { position: fixed; top: 0; width: 100%; }
```
### After
```vue
<q-header elevated>...</q-header>
```

## Refactor 02 (Medium): Manual Drawer Toggle
### Before
```javascript
const drawerOpen = ref(false);
function toggleDrawer() { drawerOpen.value = !drawerOpen.value; }
```
### After
```vue
<q-drawer v-model="drawerOpen" />
<q-btn @click="drawerOpen = !drawerOpen" />
```

## Refactor 03 (Hard): No Responsive Drawer
### Before
```vue
<q-drawer :breakpoint="0" v-model="open" />
```
### After
```vue
<q-drawer :breakpoint="500" v-model="open" />
```

---

## Approach Comparison — different ways to solve it

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
