// Tests for LoginForm component with Quasar QForm
// Run: vitest run medium/p02-solution.test.js
import { describe, it, expect, beforeEach } from 'vitest'
import { mount, flushPromises } from '@vue/test-utils'
import { Quasar } from 'quasar'

// --- LoginForm component (inline for self-contained test) ---
const LoginForm = {
  emits: ['submit'],
  data() {
    return { email: '', password: '', error: '' }
  },
  computed: {
    isValid() {
      return this.email.includes('@') && this.password.length > 0
    },
  },
  template: `
    <q-form data-test="login-form" @submit.prevent="submit">
      <q-input data-test="email" v-model="email" label="Email" />
      <q-input data-test="password" v-model="password" label="Password" type="password" />
      <p v-if="error" data-test="error" class="text-negative">{{ error }}</p>
      <q-btn data-test="submit" type="submit" label="Login" :disable="!isValid" />
    </q-form>
  `,
  methods: {
    submit() {
      if (!this.email.includes('@')) {
        this.error = 'Invalid email'
        return
      }
      this.error = ''
      this.$emit('submit', { email: this.email, password: this.password })
    },
  },
}

// --- Helper to mount with Quasar ---
function mountWithQuasar(component, options = {}) {
  return mount(component, {
    global: { plugins: [[Quasar, {}]] },
    ...options,
  })
}

// --- Tests ---
describe('LoginForm', () => {
  let wrapper
  beforeEach(() => {
    wrapper = mountWithQuasar(LoginForm)
  })

  it('submit is disabled when fields are empty', () => {
    const submitBtn = wrapper.find('[data-test="submit"]')
    expect(submitBtn.attributes('disable')).toBeDefined()
  })

  it('valid submit emits submit with credentials', async () => {
    await wrapper.find('[data-test="email"]').setValue('test@example.com')
    await wrapper.find('[data-test="password"]').setValue('password123')
    await wrapper.find('[data-test="submit"]').trigger('click')
    expect(wrapper.emitted('submit')).toBeTruthy()
    expect(wrapper.emitted('submit')[0][0]).toEqual({
      email: 'test@example.com',
      password: 'password123',
    })
  })

  it('invalid email shows error', async () => {
    await wrapper.find('[data-test="email"]').setValue('invalidemail')
    await wrapper.find('[data-test="password"]').setValue('password123')
    await wrapper.find('[data-test="submit"]').trigger('click')
    await flushPromises()
    expect(wrapper.find('[data-test="error"]').exists()).toBe(true)
    expect(wrapper.find('[data-test="error"]').text()).toContain('Invalid email')
  })
})
