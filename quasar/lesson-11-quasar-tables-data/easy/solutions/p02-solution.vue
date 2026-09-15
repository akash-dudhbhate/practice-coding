<!--
  Lesson 11 - Easy - P02: QTable with Search Filter
  A QInput with debounce filters table rows by search term.
  The filter input is displayed above the table.
-->
<template>
  <q-page class="q-pa-md">
    <!-- Search filter input with debounce to limit filter recalculations -->
    <q-input
      v-model="search"
      debounce="300"
      outlined
      dense
      placeholder="Search users..."
      class="q-mb-md"
    >
      <template #prepend>
        <q-icon name="search" />
      </template>
    </q-input>

    <q-table
      title="Users"
      :rows="filteredRows"
      :columns="columns"
      row-key="id"
      :filter="search"
    />
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'

const search = ref('')

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'age', label: 'Age', field: 'age', align: 'right', sortable: true },
])

const rows = ref([
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', age: 28 },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', age: 34 },
  { id: 3, name: 'Carol White', email: 'carol@example.com', age: 22 },
  { id: 4, name: 'Dave Brown', email: 'dave@example.com', age: 45 },
  { id: 5, name: 'Eve Davis', email: 'eve@example.com', age: 31 },
])

// Computed filtered rows: matches search term against name, email, or age
const filteredRows = computed(() => {
  if (!search.value) return rows.value
  const term = search.value.toLowerCase()
  return rows.value.filter((row) =>
    String(row.name).toLowerCase().includes(term) ||
    String(row.email).toLowerCase().includes(term) ||
    String(row.age).includes(term)
  )
})
</script>

<style scoped>
</style>
