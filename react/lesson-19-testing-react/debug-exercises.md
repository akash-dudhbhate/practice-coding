# Lesson 19 — Debug Exercises

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
