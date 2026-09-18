# Lesson 11 — Quasar Tables & Data

## What you'll learn
- QTable basics (columns, rows, row-key)
- Sorting and pagination (built-in)
- Filtering (search)
- Custom cell rendering (body-cell slots)
- Row selection (single/multiple)
- Server-side pagination (large datasets)
- Exporting data (CSV)
- Virtual scrolling (thousands of rows)

## Lesson

### Basic table
```vue
<q-table :rows="rows" :columns="columns" row-key="id" />
```

### Custom cell
```vue
<template #body-cell-status="props">
    <q-td :props="props">
        <q-badge :color="props.row.active ? 'green' : 'red'" />
    </q-td>
</template>
```

### Server-side
```vue
<q-table @request="onRequest" :loading="loading" v-model:pagination="pagination" />
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a QTable with 5 users (id, name, email, age). Define columns with labels. Enable sorting on name and age. Display the table.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Users
   +-------+---------------+-----+
   | Name v| Email         | Age v|   <- sortable headers
   +-------+---------------+-----+
   | Alice | alice@x.com   | 30  |
   | Bob   | bob@x.com     | 25  |
   | ...   | ...           | ... |   (5 rows)
   +-------+---------------+-----+
   ```
2. `easy/p02-solve.vue` — Add a search filter to the table. Use a QInput with debounce. Filter the rows by the search term. Display the filter input above the table.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | (mag) ali            |   <- debounced q-input above table
   +----------------------+
   +-------+---------------+-----+
   | Alice | alice@x.com   | 30  |   <- only matching rows
   +-------+---------------+-----+
   (clearing shows all rows again)
   ```
3. `easy/p03-solve.vue` — Add a custom cell for the "status" column. Show a green badge for "active" and red for "inactive". Add an "actions" column with edit and delete buttons.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-------+-----------+----------+
   | Name  | Status    | Actions  |
   +-------+-----------+----------+
   | Alice | ( Active )| [e] [d]  |  <- green badge, icon buttons
   | Bob   | (Inactive)| [e] [d]  |  <- red badge; delete removes
   +-------+-----------+----------+
   ```

### Medium
4. `medium/p01-solve.vue` — Create a table with pagination (10 rows per page). Generate 50 sample rows. Show page navigation. Allow changing rows per page (5, 10, 20, 50).

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----+-------+-----+
   | ... 10 rows of data ...        |
   +-----+-------+-----+
   Rows per page: [10 v]   1-10 of 50   [<] [>]
   ```
5. `medium/p02-solve.vue` — Create a table with multiple row selection. Add a "Delete Selected" button that shows how many rows are selected. On click, confirm with a dialog and clear selection after.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Delete Selected (3) ]              <- live count in label
   +---+-------+---------------+
   |[x]| Alice | alice@x.com   |
   |[ ]| Bob   | bob@x.com     |
   |[x]| Carol | carol@x.com   |       <- row checkboxes
   +---+-------+---------------+
   click -> confirm dialog -> rows removed, boxes unchecked
   ```
6. `medium/p03-solve.vue` — Create a table with server-side pagination. Simulate an API call (setTimeout) that returns 10 items per page from a large dataset (100 items). Show loading state during fetch. Handle sorting server-side.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----+-------+-----+
   | (o) loading spinner over rows  |  <- on each page/sort change
   +-----+-------+-----+
   Page 2 of 10   [<] [>]               <- re-fetches the slice
   ```

### Hard
7. `hard/p01-solve.vue` — Build a complete admin table: 100 users, search filter, sortable columns, pagination (10/page), row selection with bulk delete, custom cells (status badge, actions), and CSV export button. Include loading and empty states.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [search_______]                    [ Export CSV ]
   +---+-----+--------+--------+------+
   |[x]|Name v|Status  |Email v |Acts|
   +---+-----+--------+--------+------+
   |[x]|Alice |(Active)|a@x.com |[e d]|
   |... 10 rows ...                   |
   +---+-----+--------+--------+------+
   [Delete Selected]     1-10 of 100  [<][>]
   (no matches -> "No users found" message)
   ```
8. `hard/p02-solve.vue` — Build a table with virtual scrolling: 10,000 rows of generated data. Enable virtual scroll. Show smooth scrolling. Add a search filter that works with virtual scroll. Display row count.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [search_______]   Rows: 10,000         <- live count badge
   +================+|
   | Row 1          || <- only visible rows in DOM;
   | Row 2          ||    smooth scroll through 10k
   | ...            ||
   | Row 20         ||
   +================+|
   ```
9. `hard/p03-solve.vue` — Build an editable table: double-click a cell to edit it inline. Use QInput in edit mode. Save on Enter, cancel on Escape. Show a notification on save. Include add row and delete row buttons.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ + Add Row ]
   +-----------+---------------+-----+---+
   | Name      | Email         | Age |   |
   +-----------+---------------+-----+---+
   | Alice     | alice@x.com   | 30  |[d]|
   |[Bob______]| bob@x.com     | 25  |[d]|  <- dbl-click = input
   +-----------+---------------+-----+---+
   Enter saves + toast; Escape discards
   ```

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
