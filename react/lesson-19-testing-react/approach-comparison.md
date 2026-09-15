# Lesson 19 — Approach Comparison

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
