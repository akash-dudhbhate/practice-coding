// Comprehensive tests for ShoppingCart with Pinia (store + component together)
// Run: vitest run hard/p01-solution.test.js
import { describe, it, expect, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { defineStore } from 'pinia'
import { mount } from '@vue/test-utils'

// --- ShoppingCart store ---
const useCartStore = defineStore('cart', {
  state: () => ({
    items: [],
  }),
  actions: {
    addItem(item) {
      const existing = this.items.find(i => i.id === item.id)
      if (existing) existing.quantity++
      else this.items.push({ ...item, quantity: 1 })
    },
    removeItem(id) {
      this.items = this.items.filter(i => i.id !== id)
    },
    updateQuantity(id, qty) {
      const item = this.items.find(i => i.id === id)
      if (item) item.quantity = qty
    },
    clear() {
      this.items = []
    },
  },
  getters: {
    total: (state) => state.items.reduce((sum, i) => sum + i.price * i.quantity, 0),
    count: (state) => state.items.reduce((sum, i) => sum + i.quantity, 0),
    isEmpty: (state) => state.items.length === 0,
  },
})

// --- ShoppingCart component ---
const ShoppingCart = {
  setup() {
    const store = useCartStore()
    return { store }
  },
  template: `
    <div data-test="cart">
      <p data-test="count">Items: {{ store.count }}</p>
      <p data-test="total">Total: {{ store.total }}</p>
      <p v-if="store.isEmpty" data-test="empty">Cart is empty</p>
      <div v-for="item in store.items" :key="item.id" data-test="cart-item">
        <span data-test="item-name">{{ item.name }} ({{ item.quantity }})</span>
        <button data-test="remove" @click="store.removeItem(item.id)">Remove</button>
      </div>
    </div>
  `,
}

// --- Tests ---
describe('ShoppingCart (store + component)', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  describe('Store', () => {
    it('starts empty', () => {
      const store = useCartStore()
      expect(store.isEmpty).toBe(true)
      expect(store.count).toBe(0)
      expect(store.total).toBe(0)
    })

    it('adds items', () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      expect(store.items).toHaveLength(1)
      expect(store.count).toBe(1)
    })

    it('increments quantity for existing items', () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      expect(store.items).toHaveLength(1)
      expect(store.items[0].quantity).toBe(2)
      expect(store.count).toBe(2)
    })

    it('removes items', () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      store.removeItem(1)
      expect(store.items).toHaveLength(0)
      expect(store.isEmpty).toBe(true)
    })

    it('updates quantity', () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      store.updateQuantity(1, 5)
      expect(store.items[0].quantity).toBe(5)
    })

    it('calculates total correctly', () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      store.addItem({ id: 2, name: 'Banana', price: 3 })
      store.updateQuantity(1, 3)
      // 3*2 + 1*3 = 9
      expect(store.total).toBe(9)
    })
  })

  describe('Component', () => {
    it('shows empty message when cart is empty', () => {
      const wrapper = mount(ShoppingCart)
      expect(wrapper.find('[data-test="empty"]').exists()).toBe(true)
    })

    it('displays item count and total', async () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      const wrapper = mount(ShoppingCart)
      expect(wrapper.find('[data-test="count"]').text()).toContain('Items: 1')
      expect(wrapper.find('[data-test="total"]').text()).toContain('Total: 2')
    })

    it('removes item on button click', async () => {
      const store = useCartStore()
      store.addItem({ id: 1, name: 'Apple', price: 2 })
      const wrapper = mount(ShoppingCart)
      await wrapper.find('[data-test="remove"]').trigger('click')
      expect(store.items).toHaveLength(0)
    })
  })
})
