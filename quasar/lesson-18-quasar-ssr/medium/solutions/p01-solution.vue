<template>
  <div class="q-pa-md">
    <q-linear-progress v-if="loading" indeterminate color="primary" />
    <q-banner v-if="error" class="bg-negative text-white">{{ error }}</q-banner>
    <div v-if="product">
      <h4>{{ product.name }}</h4>
      <p>{{ product.description }}</p>
      <p class="text-h6 text-primary">{{ product.price }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Define preFetch for SSR data fetching
// This runs on both server and client before component creation
const preFetch = async ({ store, currentRoute }) => {
  const productId = currentRoute.params.id
  // Simulate API call with a promise
  const fetchProduct = (id) => new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id === 'missing') reject(new Error('Product not found'))
      else resolve({ id, name: `Product ${id}`, description: 'A great product', price: '$99.99' })
    }, 100)
  })
  // Store data in Pinia (simplified — in real app, use a Pinia store)
  const product = await fetchProduct(productId)
  store.product = product
}

const product = ref(null)
const loading = ref(false)
const error = ref(null)

// In real usage, read from Pinia store after preFetch
// For this example, we simulate reading the prefetched data
if (typeof window !== 'undefined' && window.__INITIAL_STATE__?.product) {
  product.value = window.__INITIAL_STATE__.product
}

export { preFetch }
</script>
