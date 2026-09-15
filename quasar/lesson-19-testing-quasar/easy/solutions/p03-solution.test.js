// Unit test for Pinia useCounterStore
// Run: vitest run easy/p03-solution.test.js
import { describe, it, expect, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { defineStore } from 'pinia'

// --- Counter store (inline for self-contained test) ---
const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 }),
  actions: {
    increment() { this.count++ },
  },
  getters: {
    double: (state) => state.count * 2,
  },
})

// --- Tests ---
describe('useCounterStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('initial state has count 0', () => {
    const store = useCounterStore()
    expect(store.count).toBe(0)
  })

  it('increment action increases count', () => {
    const store = useCounterStore()
    store.increment()
    expect(store.count).toBe(1)
    store.increment()
    expect(store.count).toBe(2)
  })

  it('double getter returns count * 2', () => {
    const store = useCounterStore()
    expect(store.double).toBe(0)
    store.increment()
    expect(store.double).toBe(2)
    store.increment()
    expect(store.double).toBe(4)
  })
})
