// Unit test for UserCard component
// Run: vitest run easy/p02-solution.test.js
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'

// --- UserCard component (inline for self-contained test) ---
const UserCard = {
  props: { user: { type: Object, required: true } },
  emits: ['delete'],
  template: `
    <div data-test="user-card">
      <p data-test="name">{{ user.name }}</p>
      <p data-test="email">{{ user.email }}</p>
      <button data-test="delete" @click="$emit('delete', user.id)">Delete</button>
    </div>
  `,
}

// --- Tests ---
describe('UserCard', () => {
  const mockUser = { id: 1, name: 'Alice', email: 'alice@test.com' }

  it('displays name and email from props', () => {
    const wrapper = mount(UserCard, { props: { user: mockUser } })
    expect(wrapper.find('[data-test="name"]').text()).toBe('Alice')
    expect(wrapper.find('[data-test="email"]').text()).toBe('alice@test.com')
  })

  it('delete button emits delete event with user id', async () => {
    const wrapper = mount(UserCard, { props: { user: mockUser } })
    await wrapper.find('[data-test="delete"]').trigger('click')
    expect(wrapper.emitted('delete')).toBeTruthy()
    expect(wrapper.emitted('delete')[0]).toEqual([1])
  })
})
