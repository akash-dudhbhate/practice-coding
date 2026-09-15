# Lesson 19 — Concepts Explained (Testing Quasar Apps)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Testing Overview

**What:** Quasar supports unit testing (Jest/Vitest) and end-to-end testing (Cypress/Playwright).

```bash
# Add testing to Quasar
quasar ext add @quasar/testing-unit-jest
# or
quasar ext add @quasar/testing-unit-vitest
quasar ext add @quasar/testing-e2e-cypress
```

**Why it exists:** Without tests, changes break things silently → users find bugs → bad experience. Tests catch regressions → confidence to refactor → reliable code.

**Where it's used:** Every production app — unit tests for components, e2e for user flows.

**What goes wrong without it:**
- No tests → every change is a risk → slow development → fear of refactoring.
- Only e2e tests → slow, flaky → don't pinpoint the issue. Add unit tests.
- Only unit tests → components work individually but integration fails. Add e2e.

---

## Unit Testing Components with Vitest

**What:** Test individual components in isolation.

```js
// test/components/MyComponent.test.js
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import MyComponent from 'src/components/MyComponent.vue'

describe('MyComponent', () => {
    it('renders a message', () => {
        const wrapper = mount(MyComponent, {
            props: { msg: 'Hello' }
        })
        expect(wrapper.text()).toContain('Hello')
    })

    it('emits click event', async () => {
        const wrapper = mount(MyComponent)
        await wrapper.find('button').trigger('click')
        expect(wrapper.emitted('click')).toHaveLength(1)
    })
})
```

**Why it exists:** Without unit tests, you test manually → slow, incomplete. Unit tests → fast, automated, isolated → catch bugs early in development.

**Where it's used:** Every component — especially those with logic, props, events.

**What goes wrong without it:**
- Not mounting with props → component uses defaults → test doesn't cover real usage.
- Not awaiting `trigger('click')` → event fires but assertions run before → flaky.
- Testing implementation details (internal state) → breaks on refactor. Test behavior (output, events).

---

## Testing Quasar Components

**What:** Quasar components need special setup for testing.

```js
import { config } from '@vue/test-utils'
import { Quasar, QuasarPlugin } from 'quasar'

// Global setup: install Quasar for all tests
config.global.plugins = [[Quasar, QuasarPlugin]]

// Or per-test:
const wrapper = mount(MyComponent, {
    global: {
        plugins: [[Quasar, QuasarPlugin]]
    }
})
```

**Why it exists:** Quasar components (QBtn, QInput) need the Quasar plugin → without it, they don't render → tests fail. Installing Quasar in test setup → components work → tests pass.

**Where it's used:** Every test that renders Quasar components.

**What goes wrong without it:**
- Not installing Quasar → `<q-btn>` renders as empty → test fails.
- Installing all Quasar plugins → slow tests. Install only what's needed.
- Quasar CSS not loaded → visual tests fail (but most unit tests don't need CSS).

---

## Testing Props and Events

**What:** Test that components receive props and emit events correctly.

```js
describe('UserCard', () => {
    it('displays user name from prop', () => {
        const wrapper = mount(UserCard, {
            props: { user: { name: 'Akash', age: 25 } }
        })
        expect(wrapper.text()).toContain('Akash')
        expect(wrapper.text()).toContain('25')
    })

    it('emits delete event with user id', async () => {
        const wrapper = mount(UserCard, {
            props: { user: { id: 1, name: 'Akash' } }
        })
        await wrapper.find('[data-test="delete-btn"]').trigger('click')
        expect(wrapper.emitted('delete')).toBeTruthy()
        expect(wrapper.emitted('delete')[0]).toEqual([1])  // user id
    })
})
```

**Why it exists:** Props and events are the component's API. Testing them → ensures the contract is met → components integrate correctly.

**Where it's used:** Every component with props or events.

**What goes wrong without it:**
- `wrapper.emitted('delete')` → returns undefined if event wasn't emitted → `toBeTruthy()` catches it.
- Not awaiting `trigger('click')` → event hasn't fired yet → emitted is undefined → flaky.
- Testing with `data-test` attributes → stable selectors → don't break on CSS/class changes.

---

## Testing Pinia Stores

**What:** Test Pinia stores in isolation.

```js
// test/stores/counter.test.js
import { describe, it, expect, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useCounterStore } from 'src/stores/counter'

describe('Counter Store', () => {
    beforeEach(() => {
        setActivePinia(createPinia())
    })

    it('starts with count 0', () => {
        const store = useCounterStore()
        expect(store.count).toBe(0)
    })

    it('increments', () => {
        const store = useCounterStore()
        store.increment()
        expect(store.count).toBe(1)
    })

    it('double getter works', () => {
        const store = useCounterStore()
        store.count = 5
        expect(store.double).toBe(10)
    })
})
```

**Why it exists:** Stores hold business logic → bugs here affect the whole app. Testing stores → logic is correct → components that use them work.

**Where it's used:** Every Pinia store.

**What goes wrong without it:**
- Not calling `setActivePinia` → store uses the global pinia → state leaks between tests.
- Not resetting in `beforeEach` → previous test's state affects the next → flaky.
- Testing getters → they're computed → set state, then check the getter.

---

## Mocking API Calls

**What:** Replace API calls with controlled mocks.

```js
import { vi } from 'vitest'

// Mock fetch
global.fetch = vi.fn(() =>
    Promise.resolve({
        json: () => Promise.resolve({ name: 'Akash' })
    })
)

// Mock axios
vi.mock('axios', () => ({
    default: {
        get: vi.fn(() => Promise.resolve({ data: { name: 'Akash' } })),
        post: vi.fn(() => Promise.resolve({ data: { id: 1 } })),
    }
}))

// In a test:
it('fetches user', async () => {
    const wrapper = mount(UserProfile)
    await flushPromises()  // wait for async
    expect(wrapper.text()).toContain('Akash')
    expect(fetch).toHaveBeenCalledWith('/api/user/1')
})
```

**Why it exists:** Without mocking, tests make real API calls → slow, flaky, depend on network. Mocks → fast, deterministic, test edge cases (errors, loading).

**Where it's used:** Every test that involves API calls.

**What goes wrong without it:**
- Not calling `flushPromises()` → assertions run before the async resolves → flaky.
- Not restoring mocks → other tests use the mock → cascade failures.
- Mocking too much → you test the mock, not the code. Mock the boundary (fetch/axios), not the logic.

---

## E2E Testing with Cypress

**What:** Test the full app as a user would (click, type, navigate).

```js
// test/cypress/e2e/login.cy.js
describe('Login Flow', () => {
    it('logs in successfully', () => {
        cy.visit('/login')
        cy.get('[data-test="email"]').type('user@test.com')
        cy.get('[data-test="password"]').type('password123')
        cy.get('[data-test="submit"]').click()
        cy.url().should('include', '/dashboard')
        cy.contains('Welcome, User')
    })

    it('shows error on invalid credentials', () => {
        cy.visit('/login')
        cy.get('[data-test="email"]').type('wrong@test.com')
        cy.get('[data-test="password"]').type('wrongpass')
        cy.get('[data-test="submit"]').click()
        cy.contains('Invalid credentials')
    })
})
```

**Why it exists:** Unit tests check parts → integration might fail. E2E tests check the whole flow → catches integration bugs → confidence the app works for users.

**Where it's used:** Critical user flows — login, checkout, registration, core features.

**What goes wrong without it:**
- E2E tests are slow → don't run on every save. Run on CI/PR.
- Flaky tests (timing issues) → use `cy.contains()` (waits) instead of `cy.get()` (instant).
- Not using `data-test` attributes → selectors break on UI changes. Use `data-test` for stability.

---

## Testing Best Practices

**What:** Guidelines for effective tests.

1. **Test behavior, not implementation** → test what the component does, not how.
2. **Use `data-test` attributes** → stable selectors → don't break on styling changes.
3. **One assertion per test** → clear what failed. (Or group related assertions.)
4. **Name tests descriptively** → "shows error when email is invalid" not "test1".
5. **Arrange-Act-Assert** → setup, action, verify → clear structure.
6. **Don't test Quasar** → Quasar is already tested. Test your code.
7. **Mock at the boundaries** → mock API calls, not internal logic.

**Why it exists:** Without guidelines, tests are messy → hard to maintain → people stop writing them. Guidelines → consistent, useful tests → maintainable.

**Where it's used:** Every testing codebase.

**What goes wrong without it:**
- Testing implementation → tests break on every refactor → people delete tests → no coverage.
- Testing Quasar components (does QBtn render?) → waste of time. Test your components.
- No naming convention → "test1, test2" → can't find what failed → debugging nightmare.
