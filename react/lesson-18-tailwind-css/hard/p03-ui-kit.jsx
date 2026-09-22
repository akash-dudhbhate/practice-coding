/*
LESSON 18 — Tailwind CSS
HARD P03 — Reusable UI Kit + Demo Page
============================================
CONCEPT: A UI kit is a set of small components, each merging its own Tailwind defaults with a caller-supplied `className` via `clsx`. Consistency comes from shared class recipes, flexibility from the escape hatch.
PROBLEM: Build `Button` (5 `btnVariants`: primary/secondary/danger/success/outline), `Input` (label + error border), `Select` (label + options), `Card`, `Badge`, `Alert` (info/success/error colors), `Modal` (open + onClose + stopPropagation), `Tabs` (tabs/active/onChange), `Accordion` (sections with useState). Then `UIKitDemo` showcasing every component with working state for Tabs, Accordion, and Modal.
TRY THIS: Render `<UIKitDemo />` — click through the tabs, accordion, and open the modal.
EXPECTED OUTPUT: A demo page exercising all 9 kit components; every component accepts className.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
