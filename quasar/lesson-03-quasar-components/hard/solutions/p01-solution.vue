<!--
  Lesson 03 - Quasar Components - Hard - Problem 01
  q-table with custom body-cell slot for Status column —
  q-badge (green "Active" or red "Inactive"). 5 rows with mixed statuses.
-->
<template>
  <q-page class="q-pa-md">
    <!--
      The body-cell-status slot lets us customize rendering of the
      Status column. The slot name follows the pattern: body-cell-<column-name>
    -->
    <q-table
      title="User Status"
      :rows="rows"
      :columns="columns"
      row-key="id"
      flat
      bordered
    >
      <!-- Custom body cell for the 'status' column -->
      <template #body-cell-status="props">
        <q-td :props="props">
          <q-badge
            :color="props.value === 'Active' ? 'green' : 'red'"
            :label="props.value"
            class="q-pa-sm"
          />
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Column definitions
const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'status', label: 'Status', field: 'status', align: 'left' },
])

// 5 rows with mixed Active/Inactive statuses
const rows = ref([
  { id: 1, name: 'Alice Johnson', status: 'Active' },
  { id: 2, name: 'Bob Smith', status: 'Inactive' },
  { id: 3, name: 'Carol White', status: 'Active' },
  { id: 4, name: 'Dave Brown', status: 'Inactive' },
  { id: 5, name: 'Eve Green', status: 'Active' },
])
</script>

<style scoped>
</style>
