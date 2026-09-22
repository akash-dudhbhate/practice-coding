/*
LESSON 07 — Forms & Controlled Inputs
HARD P01 — Registration Form with Validation
============================================
CONCEPT: Same pattern, more rules: a separate `validate()` returns the whole errors object so submit stays readable and every field gets checked.
PROBLEM: Build a `RegistrationForm` with `form` ({name, email, password, confirm}) and `errors`. `validate()` checks: name required, email contains "@", password 8+ chars, password === confirm. `handleChange` clears the touched field's error; submit shows inline red errors or alerts success.
TRY THIS: Render `<RegistrationForm />`, use mismatched passwords, then fix.
EXPECTED OUTPUT: Each bad field shows its own message; matching valid fields alert "Registered!".
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
