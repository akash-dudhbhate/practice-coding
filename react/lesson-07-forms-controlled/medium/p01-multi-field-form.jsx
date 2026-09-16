/*
LESSON 07 — Forms & Controlled Inputs
MEDIUM P01 — Multi-Field Form
============================================
CONCEPT: One state object + `[e.target.name]` handles any number of fields with a single onChange — then onSubmit locks the values in.
PROBLEM: Build a `MultiFieldForm` with `form` ({name, email, message}) and `submitted` state. Controlled inputs + a `<textarea>` share `handleChange`; `handleSubmit` preventDefaults and stores the form. Render submitted data in a `<pre>` via `JSON.stringify`.
TRY THIS: Render `<MultiFieldForm />`, fill all three fields, submit.
EXPECTED OUTPUT: The form values appear as formatted JSON below after submit.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
