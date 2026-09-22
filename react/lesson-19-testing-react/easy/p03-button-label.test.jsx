/*
LESSON 19 — Testing React
EASY P03 — Test a Button's label Prop
============================================
CONCEPT: Props tests render the same component with different inputs and assert each output — proving the component is driven by its props, not hard-coded text.
PROBLEM: For a `Button` component (import "../Button") taking a `label` prop, write TWO tests: `render(<Button label="Submit" />)` finds a button named "Submit" via `getByRole("button", {name: "Submit"})`, and `render(<Button label="Cancel" />)` finds "Cancel".
TRY THIS: Run the suite; then change the component to ignore `label` — tests should fail.
EXPECTED OUTPUT: 2 passing tests, one per label value.
CHECK: python3 check.py easy/p03
*/
// TODO: write your test from scratch
