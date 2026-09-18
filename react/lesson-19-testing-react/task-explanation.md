# Lesson 19 — Testing React

## What you'll learn
- React Testing Library philosophy (test behavior, not implementation)
- render and screen
- Queries: getBy, queryBy, findBy
- Querying by role (accessibility)
- fireEvent vs userEvent
- Testing events and state changes
- Testing async components (waitFor, findBy)
- Mocking components and modules
- Snapshot testing

## Lesson

### Basic test
```jsx
test('displays greeting', () => {
    render(<Greeting name="Akash" />);
    expect(screen.getByText('Hello, Akash!')).toBeInTheDocument();
});
```

### Interaction test
```jsx
test('submits form', async () => {
    const user = userEvent.setup();
    render(<Form />);
    await user.type(screen.getByRole('textbox', { name: /name/i }), 'Akash');
    await user.click(screen.getByRole('button', { name: /submit/i }));
});
```

### Async test
```jsx
test('loads data', async () => {
    render(<Profile />);
    expect(await screen.findByText('Akash')).toBeInTheDocument();
});
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.test.jsx` — Write a test for a `Greeting` component that displays "Hello, {name}!". Use `render` and `getByText`. Test with name="Akash".

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  Hello, Akash!              <- <h1>
   TEST RUN:
   PASS  easy/p01-solve.test.jsx
     ✓ renders greeting with name
   Tests: 1 passed, 1 total
   ```
2. `easy/p02-solve.test.jsx` — Write a test for a `Counter` component: initial count is 0. Use `getByRole('button')` to find the increment button. Click it and verify count becomes 1.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  [ Increment ]   Count: 0 -> 1 after click
   TEST RUN:
     ✓ shows initial count of 0
     ✓ increments count on click
   Tests: 2 passed, 2 total
   ```
3. `easy/p03-solve.test.jsx` — Write a test for a `Button` component with a `label` prop. Verify the button renders with the correct label text. Use `getByRole('button', { name: label })`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  [ Submit ]   /   [ Cancel ]
   TEST RUN:
     ✓ renders button with label Submit
     ✓ renders button with label Cancel
   Tests: 2 passed, 2 total
   ```

### Medium
4. `medium/p01-solve.test.jsx` — Write tests for a `TodoList` component: test that it renders the initial todos, test adding a new todo (type + click add), test toggling a todo (click toggles done class/text).

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  [ new todo___ ] [Add]
               * Learn React  * Task
   TEST RUN:
     ✓ renders initial todos
     ✓ adds a new todo
     ✓ toggles a todo to done
   Tests: 3 passed, 3 total
   ```
5. `medium/p02-solve.test.jsx` — Write tests for a `LoginForm`: test that submit is disabled when fields are empty, test that submitting with valid data calls the `onSubmit` callback, test error message for invalid email.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  Email [_______] Password [_______] [Login]
   TEST RUN:
     ✓ submit button disabled when empty
     ✓ calls onSubmit with credentials
     ✓ shows error for invalid email
   Tests: 3 passed, 3 total
   ```
6. `medium/p03-solve.test.jsx` — Write tests for an async `UserProfile` component: mock `fetch`, test loading state appears, test user data appears after fetch, test error state on fetch failure. Use `findBy` and `waitFor`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  loading... -> Alice / error
   TEST RUN:
     ✓ shows loading state
     ✓ displays user data after fetch
     ✓ shows error on failure
   Tests: 3 passed, 3 total
   ```

### Hard
7. `hard/p01-solve.test.jsx` — Write comprehensive tests for a `Modal` component: test it doesn't render when closed, test it renders when open, test close button works, test overlay click closes, test Escape key closes, test body scroll is locked.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  %%%% +------------------+ %%%%
               %%%% | Modal  [ Close ] | %%%%
               %%%% +------------------+ %%%%
   TEST RUN:
     ✓ renders nothing when closed
     ✓ renders content when open
     ✓ closes on button click
     ✓ closes on overlay click
     ✓ closes on Escape key
     ✓ locks body scroll while open
   Tests: 6 passed, 6 total
   ```
8. `hard/p02-solve.test.jsx` — Write tests for a `useFetch` custom hook using `renderHook`: test initial loading state, test data is set after fetch, test error state, test refetch works, test cleanup on unmount.

   WHAT IT SHOULD LOOK LIKE:
   ```
   TEST RUN (hook):
     ✓ starts in loading state
     ✓ sets data after successful fetch
     ✓ sets error on failure
     ✓ refetches when url changes
   Tests: 4 passed, 4 total
   ```
9. `hard/p03-solve.test.jsx` — Write tests for a `ShoppingCart` component with Context: test adding items, test removing items, test updating quantity, test total calculation, test empty cart message, test cart count in navbar.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Component:  Cart (2) | Apple x3 [Remove] | Total: $1.50
   TEST RUN:
     ✓ starts with empty cart
     ✓ adds items to cart
     ✓ removes item from cart
     ✓ updates item quantity
     ✓ calculates correct total
   Tests: 5 passed, 5 total
   ```

### How to work
- Write your complete test file solution.
- Remove the TODO comment when done.
- Tests should use React Testing Library and (if needed) Jest/Vitest.
