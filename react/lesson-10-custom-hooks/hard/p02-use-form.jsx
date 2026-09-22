/*
LESSON 10 — Custom Hooks
HARD P02 — useForm Hook
============================================
CONCEPT: useForm lifts values/errors/handleChange/handleSubmit out of the component — validation stays a plain function passed in, so any form can reuse it.
PROBLEM: Build `useForm(initialValues, validate)` with `values`/`errors` state, a `useCallback` `handleChange` (updates field + clears its error) and `handleSubmit(onSubmit)` returning a handler that preventDefaults, runs validate, sets errors, calls onSubmit when clean. Then `RegistrationForm` uses it with name/email/password/confirm rules. Export `RegistrationForm` default.
TRY THIS: Render `<RegistrationForm />`, submit empty, then valid.
EXPECTED OUTPUT: Inline red errors on bad submit; "Registered: <name>" alert when valid.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
