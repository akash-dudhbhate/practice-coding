/*
LESSON 19 — Testing React
MEDIUM P02 — Test a LoginForm (Disabled, Callback, Error)
============================================
CONCEPT: `jest.fn()` creates a spy — pass it as `onSubmit` and assert `toHaveBeenCalledWith({...})` to verify the form reports exactly the data the user typed.
PROBLEM: For `LoginForm` (import "../LoginForm") with Email/Password placeholder inputs, a submit button, and an `onSubmit` prop, write THREE tests: (1) button `toBeDisabled()` when fields are empty; (2) filling valid email+password and clicking submit calls `onSubmit` with `{email: "test@test.com", password: "password123"}`; (3) an invalid email shows text matching /invalid email/i.
TRY THIS: Run the suite — each test isolates one behavior (disabled, callback payload, validation).
EXPECTED OUTPUT: 3 passing tests covering the form's contract.
CHECK: python3 check.py medium/p02
*/
// TODO: write your test from scratch
