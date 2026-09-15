/**
 * Two stores: useUserStore and useProductStore.
 * Also includes a component using both stores.
 */
import { ref } from 'vue'
import { defineStore } from 'pinia'

// ===== User Store =====
export const useUserStore = defineStore('user', () => {
  const user = ref(null)

  // Action: login (mock)
  function login(userData) {
    user.value = { ...userData, id: Date.now() }
  }

  // Action: logout
  function logout() {
    user.value = null
  }

  return { user, login, logout }
})

// ===== Product Store =====
export const useProductStore = defineStore('product', () => {
  const products = ref([])

  // Action: fetch products (mock API)
  async function fetchProducts() {
    // Simulate API call
    products.value = [
      { id: 1, name: 'Laptop', price: 999 },
      { id: 2, name: 'Phone', price: 599 },
      { id: 3, name: 'Tablet', price: 399 },
    ]
  }

  return { products, fetchProducts }
})

/*
 * Component using both stores:
 *
 * <template>
 *   <div class="q-pa-md">
 *     <div v-if="user">
 *       <p>Welcome, {{ user.name }}!</p>
 *       <q-btn label="Logout" color="negative" @click="logout" />
 *     </div>
 *     <div v-else>
 *       <q-btn label="Login" color="primary" @click="login({ name: 'Guest' })" />
 *     </div>
 *
 *     <q-btn label="Load Products" color="secondary" class="q-mt-md" @click="fetchProducts" />
 *     <q-list bordered separator class="q-mt-md">
 *       <q-item v-for="product in products" :key="product.id">
 *         <q-item-section>{{ product.name }}</q-item-section>
 *         <q-item-section side>${{ product.price }}</q-item-section>
 *       </q-item>
 *     </q-list>
 *   </div>
 * </template>
 *
 * <script setup>
 * import { onMounted } from 'vue'
 * import { useUserStore, useProductStore } from './p02-solution.js'
 * import { storeToRefs } from 'pinia'
 *
 * const userStore = useUserStore()
 * const productStore = useProductStore()
 *
 * const { user } = storeToRefs(userStore)
 * const { products } = storeToRefs(productStore)
 *
 * const { login, logout } = userStore
 * const { fetchProducts } = productStore
 *
 * onMounted(() => {
 *   fetchProducts()
 * })
 * </script>
 */
