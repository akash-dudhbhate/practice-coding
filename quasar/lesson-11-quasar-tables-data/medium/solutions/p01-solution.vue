<!--
  Lesson 11 - Medium - P01: Table with Pagination
  50 sample rows with pagination (10 rows/page default).
  Page navigation and ability to change rows per page (5, 10, 20, 50).
-->
<template>
  <q-page class="q-pa-md">
    <q-table
      title="Users (50 rows)"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :rows-per-page-options="[5, 10, 20, 50]"
      :rows-per-page-label="'Rows per page'"
    >
      <!-- Custom pagination label showing current range -->
      <template #pagination="scope">
        <span class="q-mr-md">
          {{ scope.paginationStartRow + 1 }}–{{ scope.paginationEndRow }}
          of {{ scope.paginationRowsNumber }}
        </span>
        <q-btn
          dense
          flat
          round
          icon="first_page"
          :disable="scope.isFirstPage"
          @click="scope.firstPage"
        />
        <q-btn
          dense
          flat
          round
          icon="chevron_left"
          :disable="scope.isFirstPage"
          @click="scope.prevPage"
        />
        <span class="q-mx-sm">{{ scope.paginationPage }}</span>
        <q-btn
          dense
          flat
          round
          icon="chevron_right"
          :disable="scope.isLastPage"
          @click="scope.nextPage"
        />
        <q-btn
          dense
          flat
          round
          icon="last_page"
          :disable="scope.isLastPage"
          @click="scope.lastPage"
        />
      </template>
    </q-table>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: true },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'age', label: 'Age', field: 'age', align: 'right', sortable: true },
])

// Generate 50 sample rows programmatically
const firstNames = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Henry']
const lastNames = ['Smith', 'Jones', 'Brown', 'Davis', 'Wilson', 'Taylor', 'Clark', 'Hall']

const rows = ref(
  Array.from({ length: 50 }, (_, i) => ({
    id: i + 1,
    name: `${firstNames[i % firstNames.length]} ${lastNames[i % lastNames.length]}`,
    email: `user${i + 1}@example.com`,
    age: 20 + (i % 40),
  }))
)
</script>

<style scoped>
</style>
