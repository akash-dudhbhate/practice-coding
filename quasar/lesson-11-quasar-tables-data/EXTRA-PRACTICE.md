# lesson-11-quasar-tables-data — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01: Missing Columns
```vue
<q-table :rows="rows" />
```
<details><summary>Answer</summary>
**Bug:** No `columns` prop — table doesn't know what to show.
**Fix:** Define columns: `:columns="columns"` with `[{ name: 'id', label: 'ID', field: 'id' }]`.
</details>

## Debug 02: Wrong Field Mapping
```javascript
{ name: 'name', label: 'Name', field: 'fullName' }
```
<details><summary>Answer</summary>
**Bug:** `field: 'fullName'` but row has `name` key. Cell shows empty.
**Fix:** `field: 'name'` or `field: row => row.fullName`.
</details>

## Debug 03: No Pagination
```vue
<q-table :rows="1000rows" :columns="cols" />
```
<details><summary>Answer</summary>
**Bug:** 1000 rows render at once — slow.
**Fix:** Add `:rows-per-page-options="[10, 20, 50]"` or server-side pagination.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Missing columns prop
```vue
<!-- WRONG -->
<q-table :rows="rows" />
<!-- CORRECT -->
<q-table :rows="rows" :columns="columns" />
```

## Mistake 02: Rendering all rows
```javascript
// WRONG — 10000 rows at once
// CORRECT — paginate
:rows-per-page-options="[10, 25, 50]"
```

## Mistake 03: Not using slots for custom cells
```vue
<!-- WRONG — can't add buttons -->
<!-- CORRECT -->
<template #body-cell-actions="props">
  <q-td><q-btn label="Edit" @click="edit(props.row)" /></q-td>
</template>
```

## Mistake 04: Wrong field name
```javascript
// field must match row key
{ field: 'price' } // row must have .price
```

## Mistake 05: Not using row-key
```vue
<q-table row-key="id" />
```

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Large Dataset Table

### Approach 1: Client-side
```vue
<q-table :rows="allRows" :rows-per-page-options="[10,25,50]" />
```
**Cons:** Loads all data upfront.

### Approach 2: Server-side
```javascript
async function onRequest(props) {
  const { page, rowsPerPage } = props.pagination;
  const res = await api.get(`/users?page=${page}&limit=${rowsPerPage}`);
  rows.value = res.data.items;
  pagination.value.rowsNumber = res.data.total;
}
```

**Winner:** Approach 2 for 1000+ rows. Approach 1 for small data.
