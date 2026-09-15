# Lesson 11 — Concepts Explained (Quasar Tables & Data)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## QTable Basics

**What:** Quasar's data table component with sorting, pagination, and selection.

```vue
<template>
    <q-table
        :rows="rows"
        :columns="columns"
        row-key="id"
        title="Users"
    />
</template>

<script setup>
const columns = [
    { name: 'name', label: 'Name', field: 'name', sortable: true, align: 'left' },
    { name: 'email', label: 'Email', field: 'email', sortable: true },
    { name: 'age', label: 'Age', field: 'age', sortable: true, sort: (a, b) => a - b },
]

const rows = [
    { id: 1, name: 'Akash', email: 'akash@test.com', age: 25 },
    { id: 2, name: 'Dev', email: 'dev@test.com', age: 30 },
]
</script>
```

**Why it exists:** Tables are essential for displaying tabular data (users, orders, products). Building from scratch → sorting, pagination, filtering → complex. QTable handles all of it → production-ready.

**Where it's used:** Admin panels, dashboards, data lists, any tabular data display.

**What goes wrong without it:**
- `row-key` missing → selection and row operations don't work. Always set a unique `row-key`.
- `field` as a string → accesses `row[field]`. For nested: `field: row => row.user.name`.
- `sortable: true` without `sort` → string sort (alphabetical). For numbers, provide a custom `sort`.

---

## Sorting and Pagination

**What:** QTable has built-in sorting and pagination.

```vue
<q-table
    :rows="rows"
    :columns="columns"
    row-key="id"
    :pagination="pagination"
    @update:pagination="pagination = $event"
/>

<script setup>
const pagination = ref({
    sortBy: 'name',     // initial sort column
    descending: false,  // ascending
    page: 1,
    rowsPerPage: 10,
})
</script>
```

**Why it exists:** Large datasets need sorting (find the oldest user) and pagination (don't show 1000 rows at once). QTable handles both → usable tables.

**Where it's used:** Every table with more than a few rows.

**What goes wrong without it:**
- `rowsPerPage: 0` → shows all rows → no pagination. Use a number (5, 10, 20).
- Sorting numbers as strings → "10" < "2" (alphabetical). Provide `sort: (a, b) => a - b`.
- Not setting initial `sortBy` → table starts unsorted → user doesn't know the order.

---

## Filtering

**What:** Add search/filter functionality to the table.

```vue
<template>
    <q-input v-model="filter" label="Search..." debounce="300">
        <template #prepend><q-icon name="search" /></template>
    </q-input>

    <q-table
        :rows="rows"
        :columns="columns"
        :filter="filter"
        row-key="id"
    />
</template>

<script setup>
import { ref } from 'vue'
const filter = ref('')
</script>
```

**Why it exists:** Without filtering, users scroll through hundreds of rows to find one. Filter narrows the view → fast lookup → better UX.

**Where it's used:** Every table with searchable data.

**What goes wrong without it:**
- `filter` checks all columns → might match unwanted fields. Use `filter-method` for custom filtering.
- Not debouncing the filter input → filters on every keystroke → slow with large data. Use `debounce`.
- Filter is case-insensitive by default → good. But for exact match, use `filter-method`.

---

## Custom Cell Rendering

**What:** Customize how cells are displayed using `body-cell` slots.

```vue
<q-table :rows="rows" :columns="columns" row-key="id">
    <!-- Custom cell for 'status' column -->
    <template #body-cell-status="props">
        <q-td :props="props">
            <q-badge :color="props.row.status === 'active' ? 'green' : 'red'">
                {{ props.row.status }}
            </q-badge>
        </q-td>
    </template>

    <!-- Custom cell for 'actions' column -->
    <template #body-cell-actions="props">
        <q-td :props="props">
            <q-btn flat icon="edit" @click="editUser(props.row)" />
            <q-btn flat icon="delete" color="negative" @click="deleteUser(props.row)" />
        </q-td>
    </template>
</q-table>
```

**Why it exists:** Raw data isn't always user-friendly. Status as "1/0" → show a badge. Actions → show buttons. Custom cells make tables interactive and readable.

**Where it's used:** Status badges, action buttons, images, links, formatted dates.

**What goes wrong without it:**
- Slot name must match column name: `body-cell-status` for column `name: 'status'`. Mismatch → slot not used.
- Forgetting `:props="props"` on `q-td` → loses alignment and styling. Always pass props.
- Heavy custom cells (images, components) → slow rendering with many rows. Use virtual scrolling.

---

## Row Selection

**What:** Select single or multiple rows.

```vue
<q-table
    :rows="rows"
    :columns="columns"
    row-key="id"
    selection="multiple"
    :selected="selected"
    @update:selected="selected = $event"
/>

<script setup>
const selected = ref([])
// selected is an array of row objects
function deleteSelected() {
    const ids = selected.value.map(row => row.id)
    // delete by ids
}
</script>
```

**Why it exists:** Bulk operations (delete selected, export selected) need row selection. QTable handles single and multiple selection → checkbox UI → clean.

**Where it's used:** Bulk delete, bulk export, selecting items for an order.

**What goes wrong without it:**
- `selection="single"` → radio buttons. `selection="multiple"` → checkboxes. Choose the right one.
- `selected` contains full row objects, not just IDs. Map to IDs: `selected.map(r => r.id)`.
- Not clearing selection after bulk operation → selected rows still highlighted → confusing. Clear `selected.value = []`.

---

## Server-Side Pagination

**What:** Fetch data from the server page by page (for large datasets).

```vue
<q-table
    :rows="rows"
    :columns="columns"
    row-key="id"
    :loading="loading"
    :rows-number="totalRows"
    v-model:pagination="pagination"
    @request="onRequest"
/>

<script setup>
const loading = ref(false)
const rows = ref([])
const totalRows = ref(0)
const pagination = ref({ page: 1, rowsPerPage: 10, sortBy: 'name', descending: false })

async function onRequest(props) {
    const { page, rowsPerPage, sortBy, descending } = props.pagination
    loading.value = true
    const { data } = await api.get('/users', {
        params: { page, per_page: rowsPerPage, sort_by: sortBy, order: descending ? 'desc' : 'asc' }
    })
    rows.value = data.items
    totalRows.value = data.total
    pagination.value = { page, rowsPerPage, sortBy, descending }
    loading.value = false
}
</script>
```

**Why it exists:** Loading 10,000 rows to the client → slow, memory-heavy. Server-side pagination fetches only the current page → fast, scalable.

**Where it's used:** Large datasets, admin panels, any table with 1000+ rows.

**What goes wrong without it:**
- Not updating `pagination` after fetch → table shows wrong page info. Update in `onRequest`.
- Not setting `rows-number` → pagination doesn't know the total → wrong page count.
- `@request` fires on sort, page change, and rows-per-page change → all handled in one function.

---

## Exporting Data

**What:** Export table data to CSV or other formats.

```js
function exportToCSV() {
    const headers = columns.map(c => c.label).join(',')
    const rows = rows.value.map(row =>
        columns.map(c => row[c.field]).join(',')
    )
    const csv = [headers, ...rows].join('\n')

    const blob = new Blob([csv], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'export.csv'
    a.click()
    URL.revokeObjectURL(url)
}
```

**Why it exists:** Users often need data in Excel/CSV for reports or offline analysis. Export functionality → data is portable → more useful.

**Where it's used:** Admin panels, reports, any data table users might want to export.

**What goes wrong without it:**
- Not escaping commas in CSV → breaks formatting. Wrap values in quotes: `"value, with comma"`.
- Not including filtered/sorted data → export shows raw data, not what the user sees. Export the filtered rows.
- Large exports → browser freezes. Generate on the server for large datasets.

---

## Virtual Scrolling

**What:** Render only visible rows → handle thousands of rows smoothly.

```vue
<q-table
    :rows="thousandRows"
    :columns="columns"
    row-key="id"
    virtual-scroll
    :virtual-scroll-item-size="48"
    :rows-per-page-options="[0]"
/>
```

**Why it exists:** Without virtual scrolling, 10,000 rows → 10,000 DOM elements → browser freezes. Virtual scroll renders only visible rows (~20) → smooth scrolling with any dataset size.

**Where it's used:** Large datasets that can't be paginated server-side, or when users want to scroll through everything.

**What goes wrong without it:**
- `rows-per-page-options="[0]"` → shows all rows (required for virtual scroll).
- `virtual-scroll-item-size` → must match row height. Wrong value → scroll jumps.
- Custom cells with virtual scroll → still works but keep cells simple for performance.
