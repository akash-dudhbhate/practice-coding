<template>
  <div class="q-pa-md">
    <div class="q-mb-md">
      <q-btn label="Prev" :disable="page === 1" @click="prevPage" class="q-mr-sm" />
      <span class="q-mx-sm">Page {{ page }} of {{ totalPages }}</span>
      <q-btn label="Next" :disable="page === totalPages" @click="nextPage" />
    </div>
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
import { ref, onMounted, watch } from 'vue'

const API = 'https://jsonplaceholder.typicode.com/users'
const PER_PAGE = 3

const users = ref([])
const loading = ref(false)
const error = ref(null)
const page = ref(1)
const total = ref(0)
const totalPages = ref(1)

async function fetchPage() {
  loading.value = true
  error.value = null
  try {
    const res = await fetch(`${API}?_page=${page.value}&_limit=${PER_PAGE}`)
    total.value = parseInt(res.headers.get('x-total-count') || '0')
    totalPages.value = Math.ceil(total.value / PER_PAGE)
    users.value = await res.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

function prevPage() { if (page.value > 1) page.value-- }
function nextPage() { if (page.value < totalPages.value) page.value++ }

watch(page, fetchPage)
onMounted(fetchPage)
</script>
