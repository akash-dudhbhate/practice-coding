<!--
  Lesson 11 - Medium - P03: Server-Side Pagination
  Simulates an API call (setTimeout) returning 10 items per page from 100 items.
  Shows loading state during fetch. Supports server-side sorting.
-->
<template>
  <q-page class="q-pa-md">
    <q-table
      title="Server-Side Data (100 items)"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :loading="loading"
      :rows-per-page-options="[10]"
      :pagination="pagination"
      @request="onRequest"
    >
      <!-- Loading spinner overlay handled by :loading prop -->
      <template #loading>
        <q-inner-loading showing color="primary" />
      </template>
    </q-table>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const loading = ref(false)
const rows = ref([])

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: true },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'age', label: 'Age', field: 'age', align: 'right', sortable: true },
])

// Pagination state: page, rowsPerPage, sortBy, descending, rowsNumber
const pagination = ref({
  page: 1,
  rowsPerPage: 10,
  sortBy: 'id',
  descending: false,
  rowsNumber: 100,
})

// Simulated full dataset of 100 items
const allData = Array.from({ length: 100 }, (_, i) => ({
  id: i + 1,
  name: `User ${i + 1}`,
  email: `user${i + 1}@example.com`,
  age: 20 + (i % 50),
}))

// Simulate API request with setTimeout
function fetchFromServer({ page, rowsPerPage, sortBy, descending }) {
  loading.value = true
  return new Promise((resolve) => {
    setTimeout(() => {
      let data = [...allData]

      // Server-side sorting
      if (sortBy) {
        data.sort((a, b) => {
          const valA = a[sortBy]
          const valB = b[sortBy]
          if (typeof valA === 'number') return valA - valB
          return String(valA).localeCompare(String(valB))
        })
        if (descending) data.reverse()
      }

      // Pagination slice
      const start = (page - 1) * rowsPerPage
      const end = start + rowsPerPage
      resolve(data.slice(start, end))
      loading.value = false
    }, 500) // Simulate network delay
  })
}

// Handle QTable request event (page change, sort change)
async function onRequest(props) {
  const { page, rowsPerPage, sortBy, descending } = props.pagination
  pagination.value = { ...props.pagination, rowsNumber: 100 }
  const data = await fetchFromServer({ page, rowsPerPage, sortBy, descending })
  rows.value = data
}

// Load initial data on mount
onMounted(async () => {
  const data = await fetchFromServer({
    page: pagination.value.page,
    rowsPerPage: pagination.value.rowsPerPage,
    sortBy: pagination.value.sortBy,
    descending: pagination.value.descending,
  })
  rows.value = data
})
</script>

<style scoped>
</style>
