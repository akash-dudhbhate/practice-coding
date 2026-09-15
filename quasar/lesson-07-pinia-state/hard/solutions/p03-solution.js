/**
 * Cross-store dependencies: useCartStore depends on useAuthStore.
 * - Only logged-in users can add items
 * - Computed showing cart only if authenticated
 * - Action redirecting to login if not authenticated
 * - Watcher clearing cart on logout
 */
import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'

// ===== Auth Store =====
export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(null)

  const isAuthenticated = computed(() => !!token.value)

  function login(credentials) {
    user.value = { name: credentials.name || 'User', email: credentials.email }
    token.value = 'mock-token-' + Date.now()
  }

  function logout() {
    user.value = null
    token.value = null
  }

  return { user, token, isAuthenticated, login, logout }
})

// ===== Cart Store (depends on Auth Store) =====
export const useCartStore = defineStore('cart', () => {
  const items = ref([])

  // Import auth store inside the cart store to create cross-store dependency
  const authStore = useAuthStore()

  // Getter: total items
  const totalItems = computed(() =>
    items.value.reduce((sum, item) => sum + item.quantity, 0)
  )

  // Getter: total price
  const totalPrice = computed(() =>
    items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  )

  // Computed: cart is only visible/usable if authenticated
  const visibleCart = computed(() => {
    if (!authStore.isAuthenticated) return []
    return items.value
  })

  // Action: add item - only if authenticated, otherwise redirect to login
  function addItem(product) {
    if (!authStore.isAuthenticated) {
      // Signal that login is required (component handles redirect)
      return { success: false, reason: 'login_required' }
    }
    const existing = items.value.find((item) => item.id === product.id)
    if (existing) {
      existing.quantity++
    } else {
      items.value.push({ ...product, quantity: 1 })
    }
    return { success: true }
  }

  function removeItem(id) {
    items.value = items.value.filter((item) => item.id !== id)
  }

  function clearCart() {
    items.value = []
  }

  // Watcher: clear cart when user logs out
  watch(
    () => authStore.isAuthenticated,
    (isAuthed) => {
      if (!isAuthed) {
        clearCart()
      }
    }
  )

  return {
    items,
    totalItems,
    totalPrice,
    visibleCart,
    addItem,
    removeItem,
    clearCart,
  }
})

/*
 * Component using both stores with login redirect:
 *
 * <template>
 *   <div class="q-pa-md">
 *     <!-- Auth status -->
 *     <div v-if="isAuthenticated">
 *       <p>Welcome, {{ user.name }}</p>
 *       <q-btn label="Logout" color="negative" @click="logout" />
 *     </div>
 *     <div v-else>
 *       <q-btn label="Login" color="primary" @click="login({ name: 'Demo', email: 'demo@test.com' })" />
 *     </div>
 *
 *     <!-- Cart -->
 *     <div class="q-mt-md">
 *       <div class="text-h6">Cart ({{ totalItems }} items)</div>
 *       <q-btn label="Add Item" color="secondary" @click="handleAdd" />
 *       <q-list bordered separator class="q-mt-sm" v-if="visibleCart.length">
 *         <q-item v-for="item in visibleCart" :key="item.id">
 *           {{ item.name }} - {{ item.quantity }}
 *         </q-item>
 *       </q-list>
 *       <p v-else-if="isAuthenticated" class="text-grey">Cart is empty</p>
 *       <p v-else class="text-grey">Login to view cart</p>
 *     </div>
 *   </div>
 * </template>
 *
 * <script setup>
 * import { useRouter } from 'vue-router'
 * import { useAuthStore, useCartStore } from './p03-solution.js'
 * import { storeToRefs } from 'pinia'
 * import { useQuasar } from 'quasar'
 *
 * const $q = useQuasar()
 * const router = useRouter()
 * const authStore = useAuthStore()
 * const cartStore = useCartStore()
 *
 * const { user, isAuthenticated } = storeToRefs(authStore)
 * const { totalItems, visibleCart } = storeToRefs(cartStore)
 * const { login, logout } = authStore
 * const { addItem } = cartStore
 *
 * function handleAdd() {
 *   const result = addItem({ id: 1, name: 'Product 1', price: 100 })
 *   if (!result.success && result.reason === 'login_required') {
 *     $q.notify({ type: 'warning', message: 'Please login first' })
 *     router.push('/login')
 *   }
 * }
 * </script>
 */
