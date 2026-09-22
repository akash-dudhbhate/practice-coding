/*
LESSON 04 — Conditional Rendering
MEDIUM P03 — Conditional CSS Classes
============================================
CONCEPT: className is just a string — build it with a template literal so state picks the class: `btn ${state === "active" ? "btn-active" : ...}`.
PROBLEM: Build a `ConditionalButton` component with `state` ("active"/"inactive"/"disabled"). Compose a `className` template literal from state, disable the button when state is "disabled", and let clicks cycle active/inactive. Add a "Disable" button that sets state to "disabled".
TRY THIS: Render `<ConditionalButton />`, click the state button, then "Disable".
EXPECTED OUTPUT: className changes each click; after Disable the button is `disabled` and classed btn-disabled.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
