/*
LESSON 18 — Tailwind CSS
MEDIUM P03 — Styled Form with Error States
============================================
CONCEPT: Forms combine controlled inputs (React state) with Tailwind's `focus:` ring and conditional error classes — `border-red-500` when `errors[name]` is set, `border-gray-300` otherwise.
PROBLEM: Build `StyledForm`: `form` state {name, email, password, role, agree} + `errors` state, a `handleChange` reading `e.target` (checkbox uses `checked`), clearing that field's error. Render labeled fields — text, email, password inputs, a `<select>` for role, and an `agree` checkbox — each input getting `w-full px-3 py-2 border rounded focus:outline-none focus:ring-2` plus the conditional error border.
TRY THIS: Render `<StyledForm />`, set `errors` for email — its border turns red until you type.
EXPECTED OUTPUT: Uniform styled fields; focus ring on all; red borders while a field has an error.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
