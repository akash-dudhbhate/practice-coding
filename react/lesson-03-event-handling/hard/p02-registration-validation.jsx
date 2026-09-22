/*
LESSON 03 — Event Handling
HARD P02 — Multi-Input Form with Validation
============================================
CONCEPT: Collect errors into an object keyed by field name, store it in state, and render each message next to its input — all inside `onSubmit`.
PROBLEM: Build a `RegistrationForm` with `form` ({name, email, password}) and `errors` state. On submit: preventDefault, require all fields, email must include "@", show each error in a red `<span>` under its input, and `alert("Registration successful!")` when clean.
TRY THIS: Render `<RegistrationForm />`, submit empty, then fill correctly and submit again.
EXPECTED OUTPUT: First submit shows three red errors; valid submit shows the alert.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
