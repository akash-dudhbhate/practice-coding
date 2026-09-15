/**
 * Multi-store app: useUserStore, useCartStore, useOrderStore.
 * - Cart creates orders (moves items to order)
 * - Orders reference the user
 * Components interacting with all three stores.
 */
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

// ===== User Store =====
export const useUserStore = defineStore('user', () => {
  const user = ref(null)

  function login(userData) {
    user.value = { ...userData, id: Date.now() }
  }

  function logout() {
    user.value = null
  }

  return { user, login, logout }
})

// ===== Cart Store =====
export const useCartStore = defineStore('cart', () => {
  const items = ref([])

  const totalItems = computed(() =>
    items.value.reduce((sum, item) => sum + item.quantity, 0)
  )

  const totalPrice = computed(() =>
    items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  )

  function addItem(product) {
    const existing = items.value.find((item) => item.id === product.id)
    if (existing) {
      existing.quantity++
    } else {
      items.value.push({ ...product, quantity: 1 })
    }
  }

  function removeItem(id) {
    items.value = items.value.filter((item) => item.id !== id)
  }

  function clearCart() {
    items.value = []
  }

  return { items, totalItems, totalPrice, addItem, removeItem, clearCart }
})

// ===== Order Store =====
export const useOrderStore = defineStore('order', () => {
  const orders = ref([])

  // Create order from cart items, referencing the current user
  function createOrder(cartItems, user) {
    const order = {
      id: Date.now(),
      items: [...cartItems],
      userId: user ? user.id : null,
      userName: user ? user.name : 'Guest',
      total: cartItems.reduce((sum, item) => sum + item.price * item.quantity, 0),
      date: new Date().toISOString(),
    }
    orders.value.push(order)
    return order
  }

  return { orders, createOrder }
})

/*
 * Component using all three stores (checkout flow):
 *
 * <template>
 *   <div class="q-pa-md">
 *     <!-- User section -->
 *     <div v-if="user">
 *       <p>Welcome, {{ user.name }}</p>
 *       <q-btn label="Logout" color="negative" @click="logout" />
 *     </div>
 *     <div v-else>
 *       <q-btn label="Login as Guest" color="primary" @click="login({ name: 'Guest' })" />
 *     </div>
 *
 *     <!-- Cart section -->
 *     <div class="q-mt-md">
 *       <div class="text-h6">Cart ({{ totalItems }} items - ${{ totalPrice }})</div>
 *       <q-btn label="Add Laptop" color="secondary" @click="addItem({ id: 1, name: 'Laptop', price: 999 })" />
 *       <q-btn label="Add Phone" color="secondary" @click="addItem({ id: 2, name: 'Phone', price: 599 })" />
 *       <q-btn label="Checkout" color="positive" @click="checkout" :disable="totalItems === 0" />
 *     </div>
 *
 *     <!-- Orders section -->
 *     <div class="q-mt-md">
 *       <div class="text-h6">Orders</div>
 *       <q-list bordered separator>
 *         <q-item v-for="order in orders" :key="order.id">
 *           <q-item-section>
 *             Order #{{ order.id }} - {{ order.userName }} - ${{ order.total }}
 *           </q-item-section>
 *         </q-item>
 *       </q-list>
 *     </div>
 *   </div>
 * </template>
 *
 * <script setup>
 * import { useUserStore, useCartStore, useOrderStore } from './p02-solution.js'
 * import { storeToRefs } from 'pinia'
 * import { useQuasar } from 'quasar'
 *
 * const $q = useQuasar()
 * const userStore = useUserStore()
 * const cartStore = useCartStore()
 * const orderStore = useOrderStore()
 *
 * const { user } = storeToRefs(userStore)
 * const { items, totalItems, totalPrice } = storeToRefs(cartStore)
 * const { orders } = storeToRefs(orderStore)
 *
 * const { login, logout } = userStore
 * const { addItem, clearCart } = cartStore
 * const { createOrder } = orderStore
 *
 * function checkout() {
 *   const order = createOrder(items.value, user.value)
 *   clearCart()
 *   $q.notify({ type: 'positive', message: 'Order created!' })
 * }
 * </script>
 */
