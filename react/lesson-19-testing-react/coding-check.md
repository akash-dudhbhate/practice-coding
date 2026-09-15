# Lesson 19 — Coding Check

## Easy

### p01-solve.test.jsx — Greeting test
- [ ] `render` used to mount the component
- [ ] `screen.getByText` finds the greeting
- [ ] Tests with name="Akash"
- [ ] Assertion: "Hello, Akash!" is in the document
- [ ] Test passes

### p02-solve.test.jsx — Counter test
- [ ] Initial count (0) is tested
- [ ] `getByRole('button')` finds the increment button
- [ ] `userEvent.click()` or `fireEvent.click()` used
- [ ] Count updates to 1 after click
- [ ] Assertion verifies the new count

### p03-solve.test.jsx — Button test
- [ ] Button rendered with label prop
- [ ] `getByRole('button', { name: label })` used
- [ ] Label text is correct
- [ ] Test passes for different label values

## Medium

### p01-solve.test.jsx — TodoList tests
- [ ] Initial todos are rendered
- [ ] Typing in input and clicking add creates a new todo
- [ ] Clicking a todo toggles its done state
- [ ] `userEvent.type` and `userEvent.click` used
- [ ] Multiple test cases (initial, add, toggle)

### p02-solve.test.jsx — LoginForm tests
- [ ] Submit button is disabled when fields are empty
- [ ] Typing in fields enables the button
- [ ] Submitting with valid data calls `onSubmit`
- [ ] `jest.fn()` used to mock callback
- [ ] Invalid email shows error message
- [ ] `expect(onSubmit).toHaveBeenCalledWith(...)` used

### p03-solve.test.jsx — Async UserProfile tests
- [ ] `fetch` is mocked with `jest.spyOn` or `jest.fn()`
- [ ] Loading state ("Loading...") appears initially
- [ ] User data appears after fetch (using `findBy` or `waitFor`)
- [ ] Error state tested (mock fetch to reject)
- [ ] Mock is restored after tests
- [ ] Async/await used correctly

## Hard

### p01-solve.test.jsx — Modal tests
- [ ] Modal doesn't render when `isOpen` is false
- [ ] Modal renders when `isOpen` is true
- [ ] Close button (×) closes the modal
- [ ] Clicking overlay closes the modal
- [ ] Pressing Escape closes the modal
- [ ] Body scroll is locked when modal is open
- [ ] Body scroll is restored when modal closes
- [ ] `userEvent.keyboard('{Escape}')` used

### p02-solve.test.jsx — useFetch hook tests
- [ ] `renderHook` used from `@testing-library/react`
- [ ] Initial state: loading is true, data is null
- [ ] After fetch: data is set, loading is false
- [ ] Error state: error is set on fetch failure
- [ ] Refetch: calling refetch triggers a new fetch
- [ ] Cleanup: unmount prevents state updates
- [ ] `waitFor` used for async assertions

### p03-solve.test.jsx — ShoppingCart tests
- [ ] Cart provider wraps the component in tests
- [ ] Adding items updates the cart
- [ ] Removing items updates the cart
- [ ] Updating quantity changes the item count
- [ ] Total is calculated correctly
- [ ] Empty cart shows a message
- [ ] Cart count in navbar updates
- [ ] Multiple components (navbar, cart) tested together
