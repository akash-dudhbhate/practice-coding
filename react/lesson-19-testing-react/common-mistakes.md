# Lesson 19 — Common Mistakes

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
