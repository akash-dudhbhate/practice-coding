# Lesson 02 — Intuition Checks

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
