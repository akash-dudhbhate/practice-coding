# Lesson 19 — Testing Quasar Apps

## What you'll learn
- Testing overview (unit, e2e)
- Unit testing components with Vitest
- Testing Quasar components (Quasar plugin setup)
- Testing props and events
- Testing Pinia stores
- Mocking API calls
- E2E testing with Cypress
- Testing best practices

## Lesson

### Unit test
```js
import { mount } from '@vue/test-utils'
it('renders', () => {
    const wrapper = mount(MyComp, { props: { msg: 'Hi' } })
    expect(wrapper.text()).toContain('Hi')
})
```

### Store test
```js
beforeEach(() => setActivePinia(createPinia()))
it('increments', () => {
    const store = useStore()
    store.increment()
    expect(store.count).toBe(1)
})
```

### E2E test
```js
cy.visit('/login')
cy.get('[data-test="email"]').type('user@test.com')
cy.get('[data-test="submit"]').click()
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.test.js` — Write a unit test for a simple `Counter` component: test initial count (0), test increment button increases count, test decrement button decreases count. Use Vitest and @vue/test-utils.
2. `easy/p02-solve.test.js` — Write a unit test for a `UserCard` component: test that it displays name and email from props, test that the delete button emits a 'delete' event with the user id. Use `data-test` attributes.
3. `easy/p03-solve.test.js` — Write a unit test for a Pinia `useCounterStore`: test initial state, test increment action, test double getter. Use `setActivePinia(createPinia())` in beforeEach.

### Medium
4. `medium/p01-solve.test.js` — Write tests for a `TodoList` component: test rendering initial todos, test adding a todo (type + click), test toggling a todo (click changes done state), test deleting a todo. Mock the store if needed.
5. `medium/p02-solve.test.js` — Write tests for a `LoginForm` component with Quasar QForm: test that submit is disabled when fields are empty, test that valid submit emits 'submit' with credentials, test that invalid email shows error. Install Quasar plugin for tests.
6. `medium/p03-solve.test.js` — Write tests for an API service: mock `fetch` or axios, test `getUsers` returns data, test `createUser` sends correct payload, test error handling on 500 response. Verify mock was called with correct arguments.

### Hard
7. `hard/p01-solve.test.js` — Write comprehensive tests for a `ShoppingCart` component with Pinia: test adding items, removing items, updating quantity, total calculation, empty cart state, and cart count. Test the store and the component together.
8. `hard/p02-solve.cy.js` — Write Cypress E2E tests for a login flow: visit login page, type credentials, submit, verify redirect to dashboard. Test invalid credentials show error. Test logout redirects to login. Use `data-test` attributes.
9. `hard/p03-solve.test.js` — Write tests for an async component that fetches data: test loading state appears, test data renders after fetch (mock fetch), test error state on fetch failure, test refetch button works. Use `flushPromises` for async.

### How to work
- Write your complete test file solution.
- Remove the TODO comment when done.
- Tests should use Vitest and @vue/test-utils (or Cypress for e2e).
