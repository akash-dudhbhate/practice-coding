/*
LESSON 07 — Forms & Controlled Inputs
EASY P02 — Checkbox Toggle
============================================
CONCEPT: Checkboxes use `checked` (not `value`) and `e.target.checked` (a boolean) in onChange.
PROBLEM: Build a `SubscribeCheckbox` with `subscribed` boolean state. Render a `<label>` wrapping `<input type="checkbox" checked={subscribed} onChange={e => setSubscribed(e.target.checked)} />` plus "Subscribe to newsletter", and a `<p>` showing the state.
TRY THIS: Render `<SubscribeCheckbox />` and tick the box.
EXPECTED OUTPUT: Text flips between "Not subscribed" and "Subscribed!".
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
