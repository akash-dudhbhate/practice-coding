<template>
  <div class="q-pa-md">
    <q-input v-model="filter" label="Filter" />
    <p>Computed calls: {{ computedCalls }}</p>
    <p>Function calls: {{ functionCalls }}</p>
    <h6>Computed filtered:</h6>
    <q-list dense>
      <q-item v-for="item in computedFiltered" :key="item">
        <q-item-section>{{ item }}</q-item-section>
      </q-item>
    </q-list>
    <h6>Function filtered:</h6>
    <q-list dense>
      <q-item v-for="item in functionFiltered" :key="item">
        <q-item-section>{{ item }}</q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const filter = ref('')
const computedCalls = ref(0)
const functionCalls = ref(0)

const items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape']

// Computed: cached, only re-runs when filter changes
const computedFiltered = computed(() => {
  computedCalls.value++
  return items.filter(i => i.toLowerCase().includes(filter.value.toLowerCase()))
})

// Function: runs on every render (not cached)
const functionFiltered = items.filter(i => {
  functionCalls.value++
  return i.toLowerCase().includes(filter.value.toLowerCase())
})
</script>
