# Lesson 11 — Debug Exercises

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
