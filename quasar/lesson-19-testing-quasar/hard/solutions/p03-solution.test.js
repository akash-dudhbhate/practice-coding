// Tests for async component that fetches data
// Run: vitest run hard/p03-solution.test.js
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'
import { mount, flushPromises } from '@vue/test-utils'

// --- AsyncDataComponent (inline for self-contained test) ---
const AsyncDataComponent = {
  data() {
    return { data: null, loading: false, error: null }
  },
  template: `
    <div data-test="async-component">
      <div v-if="loading" data-test="loading">Loading...</div>
      <div v-if="error" data-test="error">{{ error }}</div>
      <div v-if="data" data-test="data">
        <p v-for="item in data" :key="item.id">{{ item.name }}</p>
      </div>
      <button data-test="refetch" @click="fetchData">Refetch</button>
    </div>
  `,
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.loading = true
      this.error = null
      try {
        const res = await fetch('https://api.example.com/data')
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        this.data = await res.json()
      } catch (e) {
        this.error = e.message
      } finally {
        this.loading = false
      }
    },
  },
}

// --- Tests ---
describe('AsyncDataComponent', () => {
  const mockData = [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]

  beforeEach(() => {
    global.fetch = vi.fn()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('shows loading state on mount', () => {
    global.fetch.mockReturnValueOnce(new Promise(() => {})) // never resolves
    const wrapper = mount(AsyncDataComponent)
    expect(wrapper.find('[data-test="loading"]').exists()).toBe(true)
  })

  it('renders data after fetch succeeds', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockData,
    })
    const wrapper = mount(AsyncDataComponent)
    await flushPromises()
    expect(wrapper.find('[data-test="loading"]').exists()).toBe(false)
    expect(wrapper.find('[data-test="data"]').exists()).toBe(true)
    expect(wrapper.findAll('[data-test="data"] p')).toHaveLength(2)
  })

  it('shows error state on fetch failure', async () => {
    global.fetch.mockResolvedValueOnce({ ok: false, status: 500 })
    const wrapper = mount(AsyncDataComponent)
    await flushPromises()
    expect(wrapper.find('[data-test="error"]').exists()).toBe(true)
    expect(wrapper.find('[data-test="error"]').text()).toContain('HTTP 500')
  })

  it('refetch button triggers new fetch', async () => {
    global.fetch.mockResolvedValueOnce({ ok: true, json: async () => mockData })
    const wrapper = mount(AsyncDataComponent)
    await flushPromises()

    global.fetch.mockResolvedValueOnce({ ok: true, json: async () => [{ id: 3, name: 'Charlie' }] })
    await wrapper.find('[data-test="refetch"]').trigger('click')
    await flushPromises()

    expect(global.fetch).toHaveBeenCalledTimes(2)
    expect(wrapper.findAll('[data-test="data"] p')).toHaveLength(1)
    expect(wrapper.findAll('[data-test="data"] p')[0].text()).toBe('Charlie')
  })
})
