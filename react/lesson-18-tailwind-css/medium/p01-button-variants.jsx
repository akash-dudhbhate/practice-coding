/*
LESSON 18 — Tailwind CSS
MEDIUM P01 — Reusable Button: Variants + Sizes
============================================
CONCEPT: Real design systems map prop values to class strings: look up `variants[variant]` and `sizes[size]`, then merge with `clsx`/`cn` so a caller's `className` can still customize.
PROBLEM: Define `variants` = {primary: blue, secondary: gray, danger: red} (each with hover state) and `sizes` = {sm, md, lg} padding/text classes. Build `Button({variant = "primary", size = "md", className, children, ...props})` merging base classes + `variants[variant]` + `sizes[size]` + `className` via `clsx` (or `cn`), spreading `...props` onto the `<button>`.
TRY THIS: Render `<Button variant="danger" size="lg">Delete</Button>` and `<Button variant="secondary" className="underline">Edit</Button>`.
EXPECTED OUTPUT: Three color variants × three sizes; className overrides merge in.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
