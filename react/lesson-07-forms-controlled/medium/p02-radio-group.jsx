/*
LESSON 07 — Forms & Controlled Inputs
MEDIUM P02 — Radio Button Group
============================================
CONCEPT: Radio buttons are controlled by `checked={state === "value"}` — each option compares itself to the shared state.
PROBLEM: Build a `SizeSelector` with `size` state (start "medium"). Map `["small","medium","large"]` to `<label>`s, each with `<input type="radio" name="size" value={s} checked={size === s} onChange={...}>`. Show the selection in a `<p>`.
TRY THIS: Render `<SizeSelector />` and pick Large.
EXPECTED OUTPUT: "Selected size: large" shows; only one radio is checked at a time.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
