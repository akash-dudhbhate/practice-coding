/*
LESSON 07 — Forms & Controlled Inputs
HARD P03 — Dynamic Form Fields
============================================
CONCEPT: Form fields can come from array state: `.map` over `{id, value}` rows, update with map, remove with filter, add with spread.
PROBLEM: Build a `DynamicEmails` with `emails` state ([{id, value}]). Implement `addEmail`, `removeEmail(id)`, `updateEmail(id, value)` — all immutable. Each row is a keyed `<div>` with a controlled input + Remove button. Submit alerts the list of emails containing "@".
TRY THIS: Render `<DynamicEmails />`, add two rows, type addresses, remove one, submit.
EXPECTED OUTPUT: Rows appear/disappear; submit alerts only the valid emails.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
