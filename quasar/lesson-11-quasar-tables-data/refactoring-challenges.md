# Lesson 11 — Refactoring Challenges

## Refactor 01 (Easy): No Columns
### Before
```vue
<q-table :rows="rows" />
```
### After
```vue
<q-table :rows="rows" :columns="columns" />
```

## Refactor 02 (Medium): All Rows at Once
### Before
```vue
<q-table :rows="10000rows" />
```
### After
```javascript
async function onRequest(props) { /* server-side pagination */ }
```

## Refactor 03 (Hard: No Custom Cell
### Before
```vue
<q-table :rows="rows" :columns="cols" />
```
### After
```vue
<template #body-cell-actions="props">
  <q-td><q-btn @click="edit(props.row)" /></q-td>
</template>
```
