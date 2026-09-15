# Lesson 06 — Intuition Checks

## Check 01: Specificity
Rank these by specificity (lowest to highest):
- `div`
- `.class`
- `#id`
- `div.class`
<details><summary>Answer</summary>
`div` (0,0,1) < `.class` (0,1,0) < `div.class` (0,1,1) < `#id` (1,0,0).
</details>

## Check 02: Combinators
What do ` `, `>`, `+`, `~` mean?
<details><summary>Answer</summary>
- ` ` (space) — descendant (any depth)
- `>` — direct child only
- `+` — adjacent sibling (immediately after)
- `~` — general sibling (any sibling after)
</details>

## Check 03: Pseudo-class vs pseudo-element
What's the difference between `:hover` and `::before`?
<details><summary>Answer</summary>
`:hover` is a pseudo-class (selects an element in a specific state). `::before` is a pseudo-element (creates a new virtual element). Single colon vs double colon (though `:` works for both in older CSS).
</details>

## Check 04: Universal selector
```css
* { margin: 0; }
```
What does `*` do?
<details><summary>Answer</summary>
Selects ALL elements. Common in CSS resets. Can be slow — use sparingly.
</details>

## Check 05: :not()
```css
.button:not(.disabled) { cursor: pointer; }
```
<details><summary>Answer</summary>
Selects `.button` elements that do NOT have `.disabled` class. Useful for excluding specific cases.
</details>
