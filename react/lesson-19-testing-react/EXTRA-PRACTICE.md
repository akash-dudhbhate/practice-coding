# lesson-19-testing-react — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Testing Library philosophy
What should you test?
<details><summary>Answer</summary>
Test behavior, not implementation. Test what the user sees and does. "The more your tests resemble the way your software is used, the more confidence they give you."
</details>

## Check 02: getBy vs queryBy vs findBy
```jsx
screen.getByText("Hello");    // throws if not found
screen.queryByText("Hello");  // returns null if not found
screen.findByText("Hello");   // waits (async) — returns promise
```
<details><summary>Answer</summary>
getBy — must exist (throws if not). queryBy — check existence (null if not). findBy — async, waits for element.
</details>

## Check 03: userEvent vs fireEvent
```jsx
fireEvent.click(button);    // low-level
userEvent.click(button);    // high-level, simulates real user
```
<details><summary>Answer</summary>
userEvent simulates real browser behavior (focus, blur, events chain). fireEvent is lower-level. Prefer userEvent.
</details>

## Check 04: render cleanup
Do you need to cleanup after render?
<details><summary>Answer</summary>
No — Testing Library auto-cleans up after each test (in most test runners). DOM is reset between tests.
</details>

## Check 05: data-testid
```jsx
<button data-testid="submit">Submit</button>
```
<details><summary>Answer</summary>
Last resort for querying. Prefer text, role, label. Use testid only when text/role aren't unique or available.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Testing Implementation Details
```jsx
expect(button.state().isClicked).toBe(true);
```
<details><summary>Answer</summary>
**Bug:** Testing internal state, not behavior. Breaks on refactor.
**Fix:** `expect(button).toHaveTextContent("Clicked")` or `userEvent.click(button)`.
</details>

## Debug 02 (Medium): Not Using screen
```jsx
const { getByText } = render(<App />);
expect(getByText("Hello")).toBeInTheDocument();
```
<details><summary>Answer</summary>
**Issue:** Not using `screen`. Harder to maintain, more verbose.
**Fix:** `render(<App />); expect(screen.getByText("Hello")).toBeInTheDocument();`.
</details>

## Debug 03 (Hard): Async Test Without await
```jsx
test("loads data", () => {
  render(<App />);
  expect(screen.getByText("Data")).toBeInTheDocument(); // fails — not loaded yet
});
```
<details><summary>Answer</summary>
**Bug:** Async data not awaited. Test runs before data loads.
**Fix:** `await screen.findByText("Data")` — findBy waits for element.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Testing implementation details
```jsx
// WRONG — breaks on refactor
expect(component.state().isOpen).toBe(true);
// CORRECT — test behavior
expect(screen.getByText("Open")).toBeInTheDocument();
```

## Mistake 02: Not using screen
```jsx
// VERBOSE
const { getByText } = render(<App />);
// BETTER
render(<App />);
screen.getByText("Hello");
```

## Mistake 03: Not awaiting async
```jsx
// WRONG — race condition
expect(screen.getByText("Data")).toBeInTheDocument();
// CORRECT
expect(await screen.findByText("Data")).toBeInTheDocument();
```

## Mistake 04: Using fireEvent over userEvent
```jsx
// LESS REALISTIC
fireEvent.change(input, { target: { value: "test" } });
// MORE REALISTIC
await userEvent.type(input, "test");
```

## Mistake 05: Testing too much in one test
```jsx
// WRONG — one test does everything
test("everything", () => { render; click; type; submit; verify; });
// CORRECT — one assertion concept per test
test("shows error on invalid input", () => { ... });
test("submits on valid input", () => { ... });
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Testing Implementation
### Before
```jsx
expect(wrapper.instance().state.count).toBe(1);
```
### After
```jsx
expect(screen.getByText("Count: 1")).toBeInTheDocument();
```

## Refactor 02 (Medium): Testing Library Details
### Before
```jsx
const btn = container.querySelector(".submit-btn");
```
### After
```jsx
const btn = screen.getByRole("button", { name: /submit/i });
```

## Refactor 03 (Hard): No async Await
### Before
```jsx
test("loads", () => {
  render(<Comp />);
  expect(screen.getByText("Data")).toBeInTheDocument(); // not loaded yet
});
```
### After
```jsx
test("loads", async () => {
  render(<Comp />);
  expect(await screen.findByText("Data")).toBeInTheDocument();
});
```

---

## Approach Comparison — different ways to solve it

## Problem: Query Elements

### Approach 1: data-testid
```jsx
<button data-testid="submit">Submit</button>
screen.getByTestId("submit");
```

### Approach 2: Role
```jsx
<button>Submit</button>
screen.getByRole("button", { name: "Submit" });
```

**Winner:** Approach 2 — tests accessibility too. If you can query by role, a screen reader can find it.

---

## Problem: Async Testing

### Approach 1: findBy (wait)
```jsx
expect(await screen.findByText("Data")).toBeInTheDocument();
```

### Approach 2: waitFor + getBy
```jsx
await waitFor(() => {
  expect(screen.getByText("Data")).toBeInTheDocument();
});
```

**Winner:** Approach 1 — simpler for single assertion. Approach 2 for multiple assertions.
