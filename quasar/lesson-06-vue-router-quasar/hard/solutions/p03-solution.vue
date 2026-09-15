<template>
  <!-- Product detail page reading route.params.id, fetches mock data, watches param changes -->
  <q-page class="q-pa-md">
    <div v-if="loading" class="text-center q-pa-xl">
      <q-spinner-dots size="40px" color="primary" />
      <div class="q-mt-sm">Loading product...</div>
    </div>

    <div v-else-if="error" class="text-center q-pa-xl">
      <q-icon name="error" size="40px" color="negative" />
      <div class="q-mt-sm text-negative">{{ error }}</div>
    </div>

    <q-card v-else-if="product" class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">{{ product.name }}</div>
        <div class="text-subtitle1 q-mt-sm">Price: ${{ product.price }}</div>
        <div class="text-body1 q-mt-md">{{ product.description }}</div>
      </q-card-section>
      <q-card-actions>
        <q-btn label="View Product 1" color="primary" @click="navigateTo(1)" />
        <q-btn label="View Product 2" color="primary" @click="navigateTo(2)" />
        <q-btn label="View Product 3" color="primary" @click="navigateTo(3)" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const product = ref(null)
const loading = ref(false)
const error = ref(null)

// Mock product data array
const mockProducts = [
  { id: 1, name: 'Laptop', price: 999, description: 'A powerful laptop.' },
  { id: 2, name: 'Phone', price: 599, description: 'A sleek smartphone.' },
  { id: 3, name: 'Tablet', price: 399, description: 'A versatile tablet.' },
]

// Fetch product by id from mock array
function fetchProduct(id) {
  loading.value = true
  error.value = null
  product.value = null

  // Simulate async fetch
  setTimeout(() => {
    const found = mockProducts.find((p) => p.id === Number(id))
    if (found) {
      product.value = found
    } else {
      error.value = 'Product not found'
    }
    loading.value = false
  }, 300)
}

// Watch for param changes so navigating /products/1 -> /products/2
// updates the data without remounting the component
watch(
  () => route.params.id,
  (newId) => {
    if (newId) fetchProduct(newId)
  },
  { immediate: true }
)

// Navigate to a different product
function navigateTo(id) {
  router.push({ name: 'ProductDetail', params: { id } })
}
</script>

<style scoped>
.q-card {
  max-width: 500px;
  margin: 0 auto;
}
</style>
