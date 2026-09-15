# Lesson 11 — Common Mistakes

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
