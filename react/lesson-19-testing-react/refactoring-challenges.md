# Lesson 19 — Refactoring Challenges

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
