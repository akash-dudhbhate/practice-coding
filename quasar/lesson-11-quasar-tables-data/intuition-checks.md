# Lesson 11 — Intuition Checks

## Check 01: Column definition
```javascript
{ name: 'price', label: 'Price', field: 'price', sortable: true, align: 'right' }
```
<details><summary>Answer</summary>
`name` — internal id. `label` — header text. `field` — row property or function. `sortable` — enable sorting. `align` — left/right/center.
</details>

## Check 02: Server-side pagination
<details><summary>Answer</summary>
For large datasets: fetch only current page from server. Use `@request` event, send page/rowsPerPage/sortBy to API. Set `rows` and `pagination` from response.
</details>

## Check 03: Slot customization
```vue
<template #body-cell-actions="props">
  <q-td><q-btn @click="edit(props.row)" /></q-td>
</template>
```
<details><summary>Answer</summary>
`#body-cell-{name}` customizes specific column. `props.row` has the row data. Common for action buttons.
</details>

## Check 04: Filtering
```vue
<q-table :filter="search" :columns="cols" :rows="rows" />
```
<details><summary>Answer</summary>
`filter` — client-side text search across all fields. For complex filtering, use `filter-method` function.
</details>

## Check 05: Selection
```vue
<q-table selection="multiple" :selected="selected" @update:selected="v => selected = v" />
```
<details><summary>Answer</summary>
`selection` — none/single/multiple. `selected` — v-model for selected rows. Shows checkboxes.
</details>
