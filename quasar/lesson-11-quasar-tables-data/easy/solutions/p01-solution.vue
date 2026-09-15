<!--
  Lesson 11 - Easy - P01: Basic QTable with Sorting
  Displays 5 users in a table with columns for id, name, email, age.
  Sorting enabled on name and age columns.
-->
<template>
  <q-page class="q-pa-md">
    <q-table
      title="Users"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :sort-method="customSort"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Column definitions: name, label, field, sortable, align
// sortable: true on name and age enables clicking column headers to sort
const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: false },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left', sortable: false },
  { name: 'age', label: 'Age', field: 'age', align: 'right', sortable: true },
])

// 5 sample user rows
const rows = ref([
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', age: 28 },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', age: 34 },
  { id: 3, name: 'Carol White', email: 'carol@example.com', age: 22 },
  { id: 4, name: 'Dave Brown', email: 'dave@example.com', age: 45 },
  { id: 5, name: 'Eve Davis', email: 'eve@example.com', age: 31 },
])

// Custom sort method to handle string and number sorting
function customSort(rows, sortBy, descending) {
  if (!sortBy) return rows
  const sorted = [...rows].sort((a, b) => {
    const valA = a[sortBy]
    const valB = b[sortBy]
    if (typeof valA === 'number' && typeof valB === 'number') {
      return valA - valB
    }
    return String(valA).localeCompare(String(valB))
  })
  return descending ? sorted.reverse() : sorted
}
</script>

<style scoped>
/* Table styling handled by Quasar defaults */
</style>
