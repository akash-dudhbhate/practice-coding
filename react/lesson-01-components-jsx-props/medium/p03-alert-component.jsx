/*
LESSON 01 — Components, JSX & Props
MEDIUM P03 — Alert Component
============================================
CONCEPT: A component can render nothing by returning `null`. Check a boolean prop early in the function body and bail out before the main JSX.
PROBLEM: Build an `Alert` component taking `message`, `type`, and `show` props. If `show` is false, `return null` so nothing renders. Otherwise map `type` ("success", "error", "warning", "info") to a background color — fall back to "#999" — and render a styled `<div>` displaying `message`.
TRY THIS: Render `<Alert message="Saved!" type="success" show={true} />`, then again with `show={false}`.
EXPECTED OUTPUT: A colored banner reading "Saved!" — and nothing at all when `show` is false.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
