/*
LESSON 19 — Testing React
EASY P01 — Test a Greeting Component
============================================
CONCEPT: React Testing Library renders a component into a fake DOM and queries it the way a USER would — `screen.getByText("...")` finds visible text, `expect(...).toBeInTheDocument()` asserts it exists.
PROBLEM: Assuming a `Greeting` component (import from "../Greeting") that renders "Hello, {name}!", write a `test("renders greeting with name", ...)` that `render(<Greeting name="Akash" />)` and asserts `screen.getByText("Hello, Akash!")` is in the document.
TRY THIS: Run with `npx jest` or `npx vitest` in a project that has @testing-library/react.
EXPECTED OUTPUT: One passing test — the rendered text is found exactly as a user sees it.
CHECK: python3 check.py easy/p01
*/
// TODO: write your test from scratch
