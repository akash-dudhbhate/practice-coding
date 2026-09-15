<template>
  <div class="q-pa-md">
    <q-btn label="Refetch" color="primary" @click="refetch" class="q-mb-md" />
    <q-linear-progress v-if="loading" indeterminate color="primary" />
    <q-banner v-if="error" class="bg-negative text-white">{{ error }}</q-banner>
    <q-list v-if="data && !loading" bordered separator>
      <q-item v-for="item in data" :key="item.id">
        <q-item-section>
          <q-item-label>{{ item.name || item.title }}</q-item-label>
          <q-item-label caption>{{ item.email || item.body }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script setup>
// useApi composable: accepts async function, returns { data, loading, error, refetch }
import { ref, onMounted, onActivated } from 'vue'

function useApi(asyncFn) {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  async function refetch() {
    loading.value = true
    error.value = null
    try {
      data.value = await asyncFn()
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  // Auto-refetch on mount and on component activation (e.g., returning to tab)
  onMounted(refetch)
  onActivated(refetch)

  // Auto-refetch on window focus
  if (typeof window !== 'undefined') {
    window.addEventListener('focus', refetch)
  }

  return { data, loading, error, refetch }
}

// Component using useApi to fetch users
const { data, loading, error, refetch } = useApi(async () => {
  const res = await fetch('https://jsonplaceholder.typicode.com/users')
  if (!res.ok) throw new Error(`HTTP ${res.status}`)
  return res.json()
})
</script>
