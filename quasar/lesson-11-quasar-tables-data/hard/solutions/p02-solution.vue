<!--
  Lesson 11 - Hard - P02: Virtual Scroll Table
  10,000 rows of generated data with virtual scrolling enabled.
  Smooth scrolling, search filter compatible with virtual scroll,
  and a row count display.
-->
<template>
  <q-page class="q-pa-md">
    <!-- Row count and search filter -->
    <div class="row q-mb-md items-center q-gutter-md">
      <q-input
        v-model="search"
        debounce="300"
        outlined
        dense
        placeholder="Search 10,000 rows..."
        class="col"
        clearable
      >
        <template #prepend>
          <q-icon name="search" />
        </template>
      </q-input>
      <q-badge color="primary" class="text-subtitle2 q-pa-sm">
        {{ filteredRows.length.toLocaleString() }} rows
      </q-badge>
    </div>

    <!-- Virtual scroll table: only renders visible rows for performance -->
    <q-table
      title="Virtual Scroll - 10,000 Rows"
      :rows="filteredRows"
      :columns="columns"
      row-key="id"
      virtual-scroll
      :virtual-scroll-item-size="48"
      :rows-per-page-options="[0]"
      style="height: 500px"
    />
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'

const search = ref('')

const columns = ref([
  { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: true },
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'value', label: 'Value', field: 'value', align: 'right', sortable: true },
  { name: 'category', label: 'Category', field: 'category', align: 'left' },
])

// Generate 10,000 rows of sample data
const categories = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
const rows = ref(
  Array.from({ length: 10000 }, (_, i) => ({
    id: i + 1,
    name: `Item ${i + 1}`,
    value: Math.round(Math.random() * 10000),
    category: categories[i % categories.length],
  }))
)

// Filtered rows for search — works with virtual scroll
const filteredRows = computed(() => {
  if (!search.value) return rows.value
  const term = search.value.toLowerCase()
  return rows.value.filter((r) =>
    r.name.toLowerCase().includes(term) ||
    r.category.toLowerCase().includes(term) ||
    String(r.id).includes(term)
  )
})
</script>

<style scoped>
</style>
