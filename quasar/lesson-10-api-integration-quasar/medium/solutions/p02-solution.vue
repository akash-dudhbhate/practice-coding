<template>
  <div class="q-pa-md">
    <q-input
      v-model="search"
      label="Search users by name"
      debounce="400"
      @update:model-value="onSearch"
    />
    <q-linear-progress v-if="loading" indeterminate color="primary" class="q-mt-sm" />
    <q-banner v-if="error" class="bg-negative text-white q-mt-sm">{{ error }}</q-banner>
    <q-list v-if="results.length" bordered separator class="q-mt-sm">
      <q-item v-for="user in results" :key="user.id" clickable>
        <q-item-section>
          <q-item-label>{{ user.name }}</q-item-label>
          <q-item-label caption>{{ user.email }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
    <q-banner v-if="search && !loading && !results.length" class="bg-grey-2 q-mt-sm">
      No results found.
    </q-banner>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const search = ref('')
const results = ref([])
const loading = ref(false)
const error = ref(null)
let currentController = null

async function onSearch() {
  if (!search.value.trim()) {
    results.value = []
    return
  }
  // Cancel previous request
  if (currentController) currentController.abort()
  currentController = new AbortController()

  loading.value = true
  error.value = null
  try {
    const res = await fetch(
      `https://jsonplaceholder.typicode.com/users?name_like=${encodeURIComponent(search.value)}`,
      { signal: currentController.signal }
    )
    results.value = await res.json()
  } catch (e) {
    if (e.name !== 'AbortError') error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>
