# Lesson 19 — Coding Check

## Easy

### p01-solve.test.js — Counter component tests
- [ ] Initial count (0) tested
- [ ] Increment button tested
- [ ] Decrement button tested
- [ ] `mount` from @vue/test-utils used
- [ ] `trigger('click')` awaited
- [ ] Assertions on rendered text

### p02-solve.test.js — UserCard tests
- [ ] Name from prop displayed
- [ ] Email from prop displayed
- [ ] Delete button emits 'delete'
- [ ] Emitted event contains user id
- [ ] `data-test` attributes used
- [ ] `trigger('click')` awaited

### p03-solve.test.js — Counter store tests
- [ ] `setActivePinia(createPinia())` in beforeEach
- [ ] Initial state tested (count = 0)
- [ ] Increment action tested
- [ ] Double getter tested
- [ ] Store reset between tests

## Medium

### p01-solve.test.js — TodoList tests
- [ ] Initial todos rendered
- [ ] Adding todo tested (type + click)
- [ ] Toggling todo tested
- [ ] Deleting todo tested
- [ ] Store mocked or used
- [ ] Multiple test cases

### p02-solve.test.js — LoginForm tests
- [ ] Quasar plugin installed for tests
- [ ] Submit disabled when empty
- [ ] Valid submit emits credentials
- [ ] Invalid email shows error
- [ ] QForm validation tested
- [ ] `data-test` attributes used

### p03-solve.test.js — API service tests
- [ ] fetch/axios mocked
- [ ] getUsers returns data
- [ ] createUser sends correct payload
- [ ] Error handling on 500
- [ ] Mock called with correct arguments
- [ ] Mock restored after tests

## Hard

### p01-solve.test.js — ShoppingCart tests
- [ ] Adding items tested
- [ ] Removing items tested
- [ ] Updating quantity tested
- [ ] Total calculation tested
- [ ] Empty cart state tested
- [ ] Cart count tested
- [ ] Store and component tested together
- [ ] Pinia setup in beforeEach

### p02-solve.cy.js — Cypress E2E tests
- [ ] Login page visited
- [ ] Credentials typed
- [ ] Submit clicked
- [ ] Redirect to dashboard verified
- [ ] Invalid credentials show error
- [ ] Logout redirects to login
- [ ] `data-test` attributes used
- [ ] `cy.contains` for waits

### p03-solve.test.js — Async component tests
- [ ] Loading state appears
- [ ] Data renders after fetch
- [ ] fetch mocked
- [ ] `flushPromises` used for async
- [ ] Error state on fetch failure
- [ ] Refetch button works
- [ ] Mock call verified
- [ ] Error handling tested
