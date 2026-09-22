/*
LESSON 02 — State & useState
MEDIUM P03 — Form with Multiple Fields
============================================
CONCEPT: One state object can hold a whole form. The `[e.target.name]: e.target.value` computed-key pattern lets a single handler update any field.
PROBLEM: Build a `Form` component with state `{ name: "", email: "" }`. One `handleChange` does `setForm({ ...form, [e.target.name]: e.target.value })`. Render two inputs with `name` attributes plus `<p>` lines echoing both values.
TRY THIS: Render `<Form />`, type "Ada" in Name and "ada@x.com" in Email.
EXPECTED OUTPUT: "Name: Ada" and "Email: ada@x.com" update live below the inputs.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
