/**
 * useCartStore: shopping cart with items, getters, and actions.
 * Also includes a cart component displaying items and totals.
 */
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart', () => {
  // State: array of cart items { id, name, price, quantity }
  const items = ref([])

  // Getter: total number of items (sum of quantities)
  const totalItems = computed(() =>
    items.value.reduce((sum, item) => sum + item.quantity, 0)
  )

  // Getter: total price of all items
  const totalPrice = computed(() =>
    items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  )

  // Action: add item to cart (increment quantity if already exists)
  function addItem(product) {
    const existing = items.value.find((item) => item.id === product.id)
    if (existing) {
      existing.quantity++
    } else {
      items.value.push({ ...product, quantity: 1 })
    }
  }

  // Action: remove item from cart by id
  function removeItem(id) {
    items.value = items.value.filter((item) => item.id !== id)
  }

  // Action: clear all items from cart
  function clearCart() {
    items.value = []
  }

  return {
    items,
    totalItems,
    totalPrice,
    addItem,
    removeItem,
    clearCart,
  }
})

/*
 * Cart component displaying items and totals:
 *
 * <template>
 *   <div class="q-pa-md">
 *     <div class="text-h5 q-mb-md">Shopping Cart</div>
 *     <q-list bordered separator>
 *       <q-item v-for="item in items" :key="item.id">
 *         <q-item-section>
 *           <q-item-label>{{ item.name }}</q-item-label>
 *           <q-item-label caption>Qty: {{ item.quantity }} x ${{ item.price }}</q-item-label>
 *         </q-item-section>
 *         <q-item-section side>
 *           ${{ item.price * item.quantity }}
 *           <q-btn label="Remove" size="sm" color="negative" @click="removeItem(item.id)" />
 *         </q-item-section>
 *       </q-item>
 *     </q-list>
 *     <div class="q-mt-md">
 *       <p>Total Items: {{ totalItems }}</p>
 *       <p>Total Price: ${{ totalPrice }}</p>
 *       <q-btn label="Clear Cart" color="negative" @click="clearCart" />
 *     </div>
 *   </div>
 * </template>
 *
 * <script setup>
 * import { useCartStore } from './p01-solution.js'
 * import { storeToRefs } from 'pinia'
 *
 * const cartStore = useCartStore()
 * const { items, totalItems, totalPrice } = storeToRefs(cartStore)
 * const { removeItem, clearCart } = cartStore
 * </script>
 */
