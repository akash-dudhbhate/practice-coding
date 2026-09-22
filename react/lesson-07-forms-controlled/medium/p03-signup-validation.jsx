/*
LESSON 07 — Forms & Controlled Inputs
MEDIUM P03 — Form with Validation
============================================
CONCEPT: Validate in onSubmit, store an `errors` object keyed by field, render messages inline — and clear a field's error as soon as the user edits it.
PROBLEM: Build a `SignupForm` with `form` ({email, password}) and `errors` state. `handleChange` updates the field AND clears its error. On submit: email needs "@", password needs 8+ chars; show errors in red spans; alert on success.
TRY THIS: Render `<SignupForm />`, submit with a bad email + short password, fix them.
EXPECTED OUTPUT: Red errors appear on bad submit and clear as you correct each field.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
