<!--
  Lesson 03 - Quasar Components - Medium - Problem 01
  q-table with 3 columns (Name, Email, Role) and 5 sample rows.
  Enable sorting on Name and Email.
-->
<template>
  <q-page class="q-pa-md">
    <!--
      columns: define each column with name, label, field, sortable.
      sortable: true enables click-to-sort on that column.
    -->
    <q-table
      title="Users"
      :rows="rows"
      :columns="columns"
      row-key="id"
      flat
      bordered
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Column definitions; sortable enabled on Name and Email
const columns = ref([
  { name: 'name', label: 'Name', field: 'name', sortable: true, align: 'left' },
  { name: 'email', label: 'Email', field: 'email', sortable: true, align: 'left' },
  { name: 'role', label: 'Role', field: 'role', sortable: false, align: 'left' },
])

// 5 sample rows
const rows = ref([
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', role: 'Admin' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', role: 'Editor' },
  { id: 3, name: 'Carol White', email: 'carol@example.com', role: 'Viewer' },
  { id: 4, name: 'Dave Brown', email: 'dave@example.com', role: 'Editor' },
  { id: 5, name: 'Eve Green', email: 'eve@example.com', role: 'Admin' },
])
</script>

<style scoped>
</style>
