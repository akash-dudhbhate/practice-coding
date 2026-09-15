<!--
  Lesson 11 - Hard - P03: Editable Table
  Double-click a cell to edit inline with QInput.
  Save on Enter, cancel on Escape. Notification on save.
  Add row and delete row buttons.
-->
<template>
  <q-page class="q-pa-md">
    <div class="q-mb-md">
      <q-btn color="primary" icon="add" label="Add Row" no-caps @click="addRow" />
    </div>

    <q-table
      title="Editable Users"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :rows-per-page-options="[0]"
    >
      <!-- Editable "name" cell -->
      <template #body-cell-name="props">
        <q-td :props="props" @dblclick="startEdit(props.row, 'name')">
          <q-input
            v-if="editing.rowId === props.row.id && editing.field === 'name'"
            v-model="editValue"
            dense
            autofocus
            @keyup.enter="saveEdit(props.row)"
            @keyup.escape="cancelEdit"
            @blur="saveEdit(props.row)"
          />
          <span v-else>{{ props.row.name }}</span>
        </q-td>
      </template>

      <!-- Editable "email" cell -->
      <template #body-cell-email="props">
        <q-td :props="props" @dblclick="startEdit(props.row, 'email')">
          <q-input
            v-if="editing.rowId === props.row.id && editing.field === 'email'"
            v-model="editValue"
            dense
            autofocus
            @keyup.enter="saveEdit(props.row)"
            @keyup.escape="cancelEdit"
            @blur="saveEdit(props.row)"
          />
          <span v-else>{{ props.row.email }}</span>
        </q-td>
      </template>

      <!-- Editable "age" cell -->
      <template #body-cell-age="props">
        <q-td :props="props" @dblclick="startEdit(props.row, 'age')">
          <q-input
            v-if="editing.rowId === props.row.id && editing.field === 'age'"
            v-model="editValue"
            type="number"
            dense
            autofocus
            @keyup.enter="saveEdit(props.row)"
            @keyup.escape="cancelEdit"
            @blur="saveEdit(props.row)"
          />
          <span v-else>{{ props.row.age }}</span>
        </q-td>
      </template>

      <!-- Delete action -->
      <template #body-cell-actions="props">
        <q-td :props="props">
          <q-btn flat dense round icon="delete" color="negative" @click="deleteRow(props.row)" />
        </q-td>
      </template>
    </q-table>

    <q-banner class="bg-blue-1 text-blue-8 q-mt-md">
      <template #avatar>
        <q-icon name="info" />
      </template>
      Double-click any cell to edit. Press Enter to save, Escape to cancel.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'name', label: 'Name (double-click to edit)', field: 'name', align: 'left' },
  { name: 'email', label: 'Email (double-click to edit)', field: 'email', align: 'left' },
  { name: 'age', label: 'Age (double-click to edit)', field: 'age', align: 'right' },
  { name: 'actions', label: 'Actions', field: 'actions', align: 'center' },
])

const rows = ref([
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', age: 28 },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', age: 34 },
  { id: 3, name: 'Carol White', email: 'carol@example.com', age: 22 },
  { id: 4, name: 'Dave Brown', email: 'dave@example.com', age: 45 },
  { id: 5, name: 'Eve Davis', email: 'eve@example.com', age: 31 },
])

// Track which cell is being edited
const editing = ref({ rowId: null, field: null })
const editValue = ref('')

// Start editing a cell
function startEdit(row, field) {
  editing.value = { rowId: row.id, field }
  editValue.value = row[field]
}

// Save the edited value
function saveEdit(row) {
  if (editing.value.rowId !== row.id) return
  const field = editing.value.field
  if (field) {
    row[field] = field === 'age' ? Number(editValue.value) : editValue.value
    $q.notify({ type: 'positive', message: `${field} updated for ${row.name}`, timeout: 2000 })
  }
  editing.value = { rowId: null, field: null }
}

// Cancel editing without saving
function cancelEdit() {
  editing.value = { rowId: null, field: null }
  editValue.value = ''
}

// Add a new row with default values
function addRow() {
  const newId = Math.max(0, ...rows.value.map((r) => r.id)) + 1
  rows.value.push({
    id: newId,
    name: `New User ${newId}`,
    email: `newuser${newId}@example.com`,
    age: 25,
  })
  $q.notify({ type: 'info', message: 'Row added' })
}

// Delete a row
function deleteRow(row) {
  rows.value = rows.value.filter((r) => r.id !== row.id)
  $q.notify({ type: 'negative', message: `Deleted ${row.name}` })
}
</script>

<style scoped>
</style>
