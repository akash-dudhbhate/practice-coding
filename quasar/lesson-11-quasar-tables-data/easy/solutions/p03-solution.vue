<!--
  Lesson 11 - Easy - P03: Custom Cell Rendering
  "status" column shows a green badge for "active", red for "inactive".
  "actions" column has edit and delete buttons using body-cell slots.
-->
<template>
  <q-page class="q-pa-md">
    <q-table
      title="Users"
      :rows="rows"
      :columns="columns"
      row-key="id"
    >
      <!-- Custom cell for the "status" column -->
      <template #body-cell-status="props">
        <q-td :props="props">
          <q-badge
            :color="props.row.status === 'active' ? 'green' : 'red'"
            :label="props.row.status"
          />
        </q-td>
      </template>

      <!-- Custom cell for the "actions" column -->
      <template #body-cell-actions="props">
        <q-td :props="props" class="q-gutter-xs">
          <q-btn
            flat
            dense
            round
            icon="edit"
            color="primary"
            @click="editRow(props.row)"
          />
          <q-btn
            flat
            dense
            round
            icon="delete"
            color="negative"
            @click="deleteRow(props.row)"
          />
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'name', label: 'Name', field: 'name', align: 'left' },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'status', label: 'Status', field: 'status', align: 'center' },
  { name: 'actions', label: 'Actions', field: 'actions', align: 'center' },
])

const rows = ref([
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', status: 'active' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', status: 'inactive' },
  { id: 3, name: 'Carol White', email: 'carol@example.com', status: 'active' },
  { id: 4, name: 'Dave Brown', email: 'dave@example.com', status: 'inactive' },
  { id: 5, name: 'Eve Davis', email: 'eve@example.com', status: 'active' },
])

function editRow(row) {
  $q.notify({ type: 'info', message: `Editing ${row.name}` })
}

function deleteRow(row) {
  $q.notify({ type: 'negative', message: `Deleted ${row.name}` })
  rows.value = rows.value.filter((r) => r.id !== row.id)
}
</script>

<style scoped>
</style>
