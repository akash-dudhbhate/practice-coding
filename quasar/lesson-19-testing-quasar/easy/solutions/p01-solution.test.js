// Unit test for Counter component
// Run: vitest run easy/p01-solution.test.js
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'

// --- Counter component (inline for self-contained test) ---
const Counter = {
  template: `
    <div data-test="counter">
      <p data-test="count">{{ count }}</p>
      <button data-test="increment" @click="count++">+</button>
      <button data-test="decrement" @click="count--">-</button>
    </div>
  `,
  data() {
    return { count: 0 }
  },
}

// --- Tests ---
describe('Counter', () => {
  it('initial count is 0', () => {
    const wrapper = mount(Counter)
    expect(wrapper.find('[data-test="count"]').text()).toBe('0')
  })

  it('increment button increases count', async () => {
    const wrapper = mount(Counter)
    await wrapper.find('[data-test="increment"]').trigger('click')
    expect(wrapper.find('[data-test="count"]').text()).toBe('1')
  })

  it('decrement button decreases count', async () => {
    const wrapper = mount(Counter)
    await wrapper.find('[data-test="decrement"]').trigger('click')
    expect(wrapper.find('[data-test="count"]').text()).toBe('-1')
  })
})
