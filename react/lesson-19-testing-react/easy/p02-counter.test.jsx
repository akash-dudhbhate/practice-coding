/*
LESSON 19 — Testing React
EASY P02 — Test a Counter (Initial State + Click)
============================================
CONCEPT: `getByRole("button", {name: /.../})` queries by accessible role+name (like a screen reader sees it), and `fireEvent.click` simulates the user clicking — test behavior, not implementation.
PROBLEM: For a `Counter` component (import "../Counter") showing "Count: N" and an Increment button, write TWO tests: (1) initial render shows "count: 0"; (2) after `fireEvent.click` on the button found via `getByRole("button", {name: /increment/i})`, text shows "count: 1".
TRY THIS: Run the suite — both tests pass if the counter really increments.
EXPECTED OUTPUT: 2 passing tests covering initial state and the click interaction.
CHECK: python3 check.py easy/p02
*/
// TODO: write your test from scratch
