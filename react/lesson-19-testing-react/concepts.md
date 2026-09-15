# Lesson 19 — Concepts Explained (Testing React)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Testing Library Philosophy

**What:** React Testing Library (RTL) tests components the way users interact with them — by finding elements by text, role, or label, NOT by implementation details.

```jsx
// BAD: testing implementation details (enzyme style)
expect(wrapper.find('MyComponent').state('count')).toBe(5);

// GOOD: testing user-visible behavior (RTL style)
expect(screen.getByText('Count: 5')).toBeInTheDocument();
```

**Why it exists:** Implementation-detail tests break when you refactor (rename state, change component structure) even if behavior is unchanged → brittle. RTL tests behavior → survive refactoring → reliable.

**Where it's used:** Every React component test.

**What goes wrong without it:**
- Testing state instead of output → test passes but UI is broken (state is right but render is wrong).
- Querying by class name or test IDs when text/role would work → brittle, less accessible.
- Over-testing: testing every internal function → tests become a change-detector, not a correctness-checker.

---

## render and screen

**What:** `render` mounts a component in a virtual DOM. `screen` provides queries to find elements.

```jsx
import { render, screen } from '@testing-library/react';

test('displays greeting', () => {
    render(<Greeting name="Akash" />);
    expect(screen.getByText('Hello, Akash!')).toBeInTheDocument();
});
```

**Why it exists:** Without `render`, you can't test components in isolation. Without `screen`, you'd pass container around manually. `screen` is global → cleaner tests.

**Where it's used:** Every component test.

**What goes wrong without it:**
- Forgetting to `render` → `screen` queries return nothing → test fails.
- `render` multiple times in one test → duplicate elements → `getBy*` throws (multiple matches). Use `rerender` or separate tests.
- Not cleaning up → RTL auto-cleans up between tests (in Jest/Vitest), but if you're using a custom setup, you need `cleanup()`.

---

## Queries: getBy, queryBy, findBy

**What:** Three query variants with different behaviors:

| Query | Throws if not found | Throws if multiple | Returns | Async |
|-------|-------------------|-------------------|---------|-------|
| `getBy*` | Yes | Yes | Element | No |
| `queryBy*` | No (returns null) | Yes | Element/null | No |
| `findBy*` | Yes (after timeout) | Yes | Promise<Element> | Yes |

```jsx
// getBy: use when element SHOULD be there (throws if missing)
expect(screen.getByRole('button')).toBeInTheDocument();

// queryBy: use when element should NOT be there (returns null, no throw)
expect(screen.queryByText('Loading...')).not.toBeInTheDocument();

// findBy: use for async elements (waits for appearance)
const button = await screen.findByRole('button', { name: 'Submit' });
```

**Why it exists:** Different test scenarios need different behaviors. `getBy` for "must be there", `queryBy` for "must NOT be there", `findBy` for "will be there eventually" (async).

**Where it's used:** Every test — choose the right query for the scenario.

**What goes wrong without it:**
- Using `getByText` to check absence → throws (element not found) → test fails with wrong error. Use `queryByText` for absence checks.
- Using `getBy*` for async elements → element not there yet → throws. Use `findBy*` with `await`.
- `getBy*` with multiple matches → throws "Found multiple elements". Use `getAllBy*` for multiple.

---

## Querying by Role (Accessibility)

**What:** `getByRole` is the preferred query — it finds elements by their ARIA role, mirroring how screen readers navigate.

```jsx
// Button role
screen.getByRole('button', { name: 'Submit' });

// Heading role
screen.getByRole('heading', { name: 'Welcome', level: 1 });

// Textbox role (input, textarea)
screen.getByRole('textbox', { name: 'Email' });

// Link role
screen.getByRole('link', { name: 'About' });

// Navigation role
screen.getByRole('navigation');

// Dialog role (modal)
screen.getByRole('dialog');
```

**Why it exists:** Querying by role ensures your UI is accessible — if you can find it by role, a screen reader can too. It also survives refactoring (class names change, roles don't).

**Where it's used:** Prefer `getByRole` over `getByText`, `getByTestId`, or `getByClassName`.

**What goes wrong without it:**
- `name` option matches accessible name (aria-label, aria-labelledby, or text content). Not the `name` attribute on inputs.
- No `role` on a custom component → `getByRole` can't find it. Add `role` or use semantic HTML (`<button>` has role "button" automatically).
- Multiple elements with the same role → `getByRole` throws. Use `getAllByRole` or narrow with `name`.

---

## fireEvent vs userEvent

**What:** `fireEvent` dispatches a DOM event. `userEvent` simulates real user interaction (more realistic).

```jsx
import { fireEvent, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

// fireEvent: low-level, direct event dispatch
fireEvent.click(button);
fireEvent.change(input, { target: { value: 'hello' } });

// userEvent: high-level, simulates real user behavior
await userEvent.click(button);
await userEvent.type(input, 'hello');
await userEvent.tab();
await userEvent.keyboard('{Enter}');

// userEvent.type fires multiple events (keydown, input, keyup) for each char
// fireEvent.change fires one event
```

**Why it exists:** `fireEvent` is too simple — real users trigger multiple events per action (focus, keydown, input, keyup, blur). `userEvent` simulates the full sequence → tests match real behavior → fewer false positives.

**Where it's used:** Prefer `userEvent` for all interactions. Use `fireEvent` only when `userEvent` doesn't support the event.

**What goes wrong without it:**
- `fireEvent.change` doesn't trigger focus/blur → components relying on focus state → test passes but real usage fails.
- `userEvent` is async (returns a promise) → must `await`. Forgetting `await` → events fire in wrong order → flaky tests.
- `userEvent.setup()` in v14+ → create a user instance: `const user = userEvent.setup(); await user.click(button);`.

---

## Testing Events and State Changes

**What:** Test that user interactions produce the expected output.

```jsx
test('counter increments on click', async () => {
    const user = userEvent.setup();
    render(<Counter />);

    expect(screen.getByText('Count: 0')).toBeInTheDocument();

    await user.click(screen.getByRole('button', { name: /increment/i }));

    expect(screen.getByText('Count: 1')).toBeInTheDocument();
});

test('form submits with entered data', async () => {
    const user = userEvent.setup();
    const onSubmit = jest.fn();
    render(<ContactForm onSubmit={onSubmit} />);

    await user.type(screen.getByRole('textbox', { name: /name/i }), 'Akash');
    await user.type(screen.getByRole('textbox', { name: /email/i }), 'akash@test.com');
    await user.click(screen.getByRole('button', { name: /submit/i }));

    expect(onSubmit).toHaveBeenCalledWith({
        name: 'Akash',
        email: 'akash@test.com',
    });
});
```

**Why it exists:** Without testing interactions, you only test the initial render → miss bugs in event handling, state updates, and side effects.

**Where it's used:** Every interactive component — buttons, forms, toggles, dropdowns.

**What goes wrong without it:**
- Not awaiting `userEvent` calls → events fire but assertions run before state updates → test fails or is flaky.
- Testing the callback (`onSubmit`) instead of the output → tests integration but not the user experience. Test both.
- Forgetting to mock callbacks → `jest.fn()` creates a mock. Without it → `onSubmit is not a function`.

---

## Testing Async Components

**What:** Test components that fetch data or have delayed operations.

```jsx
import { waitFor, waitForElementToBeRemoved } from '@testing-library/react';

test('displays user data after fetch', async () => {
    // Mock the API
    jest.spyOn(global, 'fetch').mockResolvedValue({
        json: async () => ({ name: 'Akash' }),
    });

    render(<UserProfile userId={1} />);

    // Loading state
    expect(screen.getByText('Loading...')).toBeInTheDocument();

    // Wait for data to appear
    await waitFor(() => {
        expect(screen.getByText('Akash')).toBeInTheDocument();
    });

    // Loading is gone
    expect(screen.queryByText('Loading...')).not.toBeInTheDocument();

    global.fetch.mockRestore();
});

// Or use findBy (waits for element)
test('displays user data', async () => {
    render(<UserProfile userId={1} />);
    const userName = await screen.findByText('Akash');
    expect(userName).toBeInTheDocument();
});
```

**Why it exists:** Async components have loading → success/error states. Without `waitFor` or `findBy`, assertions run before the async operation completes → test fails.

**Where it's used:** Components with `useEffect` fetching, setTimeout, promises, async/await.

**What goes wrong without it:**
- Not mocking `fetch` → real network request → slow, flaky, depends on external API.
- `waitFor` timeout → default 1000ms. If your async is slower, increase: `waitFor(fn, { timeout: 5000 })`.
- Forgetting to restore mocks → `fetch` stays mocked for other tests → cascading failures.

---

## Mocking Components and Modules

**What:** Replace dependencies with controlled mocks.

```jsx
// Mock a child component
jest.mock('./ChildComponent', () => ({
    __esModule: true,
    default: ({ onClick }) => (
        <button data-testid="mock-child" onClick={onClick}>Mock Child</button>
    ),
}));

// Mock a module
jest.mock('axios', () => ({
    get: jest.fn(() => Promise.resolve({ data: { name: 'Akash' } })),
}));

// Mock a custom hook
jest.mock('./useAuth', () => ({
    useAuth: () => ({ user: { name: 'Akash' }, logout: jest.fn() }),
}));
```

**Why it exists:** Without mocking, tests depend on real implementations → slow, flaky, can't test edge cases (errors, loading). Mocks give you control → test specific scenarios.

**Where it's used:** Mocking API calls, child components, custom hooks, third-party libraries.

**What goes wrong without it:**
- Over-mocking → you're testing the mock, not the real component → tests pass but real component is broken.
- Mock at the right level: mock `fetch` or `axios`, not the entire API module (unless the module is complex).
- Forgetting to clear mocks between tests → `jest.clearAllMocks()` in `beforeEach` → mock call counts accumulate.

---

## Snapshot Testing

**What:** Capture the rendered output and compare it on future runs.

```jsx
test('button renders correctly', () => {
    const { container } = render(<Button label="Click me" />);
    expect(container.firstChild).toMatchSnapshot();
});
```

**Why it exists:** Quick way to detect unintended UI changes. If the snapshot differs → test fails → review the change → update if intentional.

**Where it's used:** Presentational components, static UI, regression testing.

**What goes wrong without it:**
- Snapshots are too broad → any change fails the test → "snapshot fatigue" → developers blindly update without reviewing.
- Snapshots don't test behavior → a button that renders correctly but doesn't click → snapshot passes.
- Use sparingly — prefer behavioral tests. Snapshots for visual regression only.
