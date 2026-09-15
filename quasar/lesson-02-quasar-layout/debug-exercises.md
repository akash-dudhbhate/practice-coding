# Lesson 02 — Debug Exercises

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
