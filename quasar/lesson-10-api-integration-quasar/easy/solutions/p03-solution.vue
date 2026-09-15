<template>
  <div class="q-pa-md">
    <q-linear-progress v-if="loading" indeterminate color="primary" />
    <q-banner v-if="error" class="bg-negative text-white">{{ error }}</q-banner>
    <q-list v-if="!loading && !error" bordered separator>
      <q-item v-for="user in users" :key="user.id">
        <q-item-section>
          <q-item-label>{{ user.name }}</q-item-label>
          <q-item-label caption>{{ user.email }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// User service with CRUD operations
const userService = {
  baseURL: 'https://jsonplaceholder.typicode.com/users',
  async getAll() {
    const res = await fetch(this.baseURL)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },
  async getById(id) {
    const res = await fetch(`${this.baseURL}/${id}`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },
  async create(data) {
    const res = await fetch(this.baseURL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },
  async update(id, data) {
    const res = await fetch(`${this.baseURL}/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },
  async remove(id) {
    const res = await fetch(`${this.baseURL}/${id}`, { method: 'DELETE' })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },
}

const users = ref([])
const loading = ref(false)
const error = ref(null)

async function loadUsers() {
  loading.value = true
  error.value = null
  try {
    users.value = await userService.getAll()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

onMounted(loadUsers)
</script>
