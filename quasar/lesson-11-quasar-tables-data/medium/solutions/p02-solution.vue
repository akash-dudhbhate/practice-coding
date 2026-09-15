<!--
  Lesson 11 - Medium - P02: Table with Multiple Row Selection
  Checkbox selection of rows. "Delete Selected" button shows count.
  Confirm dialog on delete. Selection cleared after deletion.
-->
<template>
  <q-page class="q-pa-md">
    <!-- Delete Selected button - shows count of selected rows -->
    <div class="q-mb-md">
      <q-btn
        color="negative"
        icon="delete"
        :label="`Delete Selected (${selected.length})`"
        :disable="selected.length === 0"
        @click="confirmDelete"
      />
    </div>

    <q-table
      title="Users"
      :rows="rows"
      :columns="columns"
      row-key="id"
      selection="multiple"
      v-model:selected="selected"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Track selected rows via v-model:selected
const selected = ref([])

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'age', label: 'Age', field: 'age', align: 'right', sortable: true },
])

const rows = ref(
  Array.from({ length: 20 }, (_, i) => ({
    id: i + 1,
    name: `User ${i + 1}`,
    email: `user${i + 1}@example.com`,
    age: 20 + (i % 40),
  }))
)

// Confirm dialog before deleting selected rows
function confirmDelete() {
  $q.dialog({
    title: 'Confirm Delete',
    message: `Delete ${selected.value.length} selected user(s)?`,
    cancel: true,
    persistent: true,
  }).onOk(() => {
    const selectedIds = selected.value.map((r) => r.id)
    rows.value = rows.value.filter((r) => !selectedIds.includes(r.id))
    selected.value = [] // Clear selection after delete
    $q.notify({ type: 'positive', message: 'Selected users deleted' })
  })
}
</script>

<style scoped>
</style>
