<!--
  Lesson 04 - Vue Composition API - Medium - Problem 02
  Search filter: searchQuery ref, items ref (strings).
  Computed filtered list. Watch searchQuery, log changes.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md" style="max-width: 400px; margin: 0 auto;">
    <h2 class="text-h6">Search Filter</h2>

    <!-- Search input bound to searchQuery -->
    <q-input v-model="searchQuery" label="Search..." outlined clearable />

    <!-- Filtered list (computed) -->
    <q-list bordered separator class="full-width">
      <q-item v-for="(item, index) in filteredItems" :key="index">
        <q-item-section>{{ item }}</q-item-section>
      </q-item>
    </q-list>

    <p v-if="filteredItems.length === 0" class="text-grey-7">No results found.</p>
  </q-page>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

// Search query string
const searchQuery = ref('')

// List of items to filter
const items = ref([
  'Apple',
  'Banana',
  'Cherry',
  'Date',
  'Elderberry',
  'Fig',
  'Grape',
])

// Computed filtered list: only items containing the search query (case-insensitive)
const filteredItems = computed(() => {
  const query = searchQuery.value.trim().toLowerCase()
  if (!query) return items.value
  return items.value.filter(item => item.toLowerCase().includes(query))
})

// Watch searchQuery and log every change (old and new value)
watch(searchQuery, (newVal, oldVal) => {
  console.log(`Search changed from "${oldVal}" to "${newVal}"`)
})
</script>

<style scoped>
</style>
