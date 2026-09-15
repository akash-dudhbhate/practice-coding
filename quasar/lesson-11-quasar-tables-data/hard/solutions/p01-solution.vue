<!--
  Lesson 11 - Hard - P01: Complete Admin Table
  100 users with: search filter, sortable columns, pagination (10/page),
  row selection with bulk delete, custom cells (status badge, actions),
  CSV export. Loading and empty states.
-->
<template>
  <q-page class="q-pa-md">
    <!-- Toolbar: search, export, bulk delete -->
    <div class="row q-mb-md items-center q-gutter-md">
      <q-input
        v-model="search"
        debounce="300"
        outlined
        dense
        placeholder="Search users..."
        class="col"
        clearable
      >
        <template #prepend>
          <q-icon name="search" />
        </template>
      </q-input>

      <q-btn
        color="primary"
        icon="download"
        label="Export CSV"
        no-caps
        @click="exportCSV"
      />

      <q-btn
        color="negative"
        icon="delete"
        :label="`Delete (${selected.length})`"
        no-caps
        :disable="selected.length === 0"
        @click="confirmBulkDelete"
      />
    </div>

    <q-table
      title="Admin - Users"
      :rows="filteredRows"
      :columns="columns"
      row-key="id"
      :loading="loading"
      :rows-per-page-options="[10, 20, 50]"
      selection="multiple"
      v-model:selected="selected"
      :filter="search"
    >
      <!-- Loading state -->
      <template #loading>
        <q-inner-loading showing color="primary" />
      </template>

      <!-- Empty state when no rows match -->
      <template #no-data>
        <div class="full-width row flex-center text-grey q-gutter-sm">
          <q-icon size="2em" name="sentiment_dissatisfied" />
          <span>No users found</span>
        </div>
      </template>

      <!-- Custom status cell: green badge for active, red for inactive -->
      <template #body-cell-status="props">
        <q-td :props="props">
          <q-badge
            :color="props.row.status === 'active' ? 'green' : 'red'"
            :label="props.row.status"
          />
        </q-td>
      </template>

      <!-- Custom actions cell: edit and delete buttons -->
      <template #body-cell-actions="props">
        <q-td :props="props" class="q-gutter-xs">
          <q-btn flat dense round icon="edit" color="primary" @click="editRow(props.row)" />
          <q-btn flat dense round icon="delete" color="negative" @click="deleteSingle(props.row)" />
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const search = ref('')
const selected = ref([])
const loading = ref(false)

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: true },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'age', label: 'Age', field: 'age', align: 'right', sortable: true },
  { name: 'status', label: 'Status', field: 'status', align: 'center', sortable: true },
  { name: 'actions', label: 'Actions', field: 'actions', align: 'center' },
])

// Generate 100 sample users
const firstNames = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
const lastNames = ['Smith', 'Jones', 'Brown', 'Davis', 'Wilson', 'Taylor', 'Clark', 'Hall', 'Lee', 'Young']

const rows = ref([])

// Filtered rows based on search term
const filteredRows = computed(() => {
  if (!search.value) return rows.value
  const term = search.value.toLowerCase()
  return rows.value.filter((r) =>
    r.name.toLowerCase().includes(term) ||
    r.email.toLowerCase().includes(term) ||
    r.status.toLowerCase().includes(term)
  )
})

// Simulate loading data on mount
onMounted(() => {
  loading.value = true
  setTimeout(() => {
    rows.value = Array.from({ length: 100 }, (_, i) => ({
      id: i + 1,
      name: `${firstNames[i % firstNames.length]} ${lastNames[i % lastNames.length]}`,
      email: `user${i + 1}@example.com`,
      age: 20 + (i % 50),
      status: i % 3 === 0 ? 'inactive' : 'active',
    }))
    loading.value = false
  }, 800)
})

// Export visible rows to CSV
function exportCSV() {
  const data = filteredRows.value
  const headers = columns.value.map((c) => c.label).join(',')
  const csvRows = data.map((row) =>
    columns.value.map((c) => {
      const val = row[c.field] || ''
      return `"${val}"`
    }).join(',')
  )
  const csv = [headers, ...csvRows].join('\n')
  const blob = new Blob([csv], { type: 'text/csv' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'users.csv'
  a.click()
  URL.revokeObjectURL(url)
  $q.notify({ type: 'positive', message: 'CSV exported' })
}

function confirmBulkDelete() {
  $q.dialog({
    title: 'Confirm Delete',
    message: `Delete ${selected.value.length} selected user(s)?`,
    cancel: true,
    persistent: true,
  }).onOk(() => {
    const ids = selected.value.map((r) => r.id)
    rows.value = rows.value.filter((r) => !ids.includes(r.id))
    selected.value = []
    $q.notify({ type: 'positive', message: 'Users deleted' })
  })
}

function editRow(row) {
  $q.notify({ type: 'info', message: `Editing ${row.name}` })
}

function deleteSingle(row) {
  rows.value = rows.value.filter((r) => r.id !== row.id)
  $q.notify({ type: 'negative', message: `Deleted ${row.name}` })
}
</script>

<style scoped>
</style>
