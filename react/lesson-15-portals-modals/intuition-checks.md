# Lesson 15 — Intuition Checks

## Check 01: What is a Portal?
<details><summary>Answer</summary>
Portal renders children into a DOM node outside the parent component's DOM hierarchy. Visually escapes parent constraints (z-index, overflow).
</details>

## Check 02: createPortal
```jsx
ReactDOM.createPortal(children, container)
```
<details><summary>Answer</summary>
`children` — React elements to render. `container` — DOM node to render into. Returns React element.
</details>

## Check 03: Portal event bubbling
Do events bubble through portals?
<details><summary>Answer</summary>
Yes — in React's synthetic event system, events bubble through the React component tree, not the DOM tree. A portal's events still reach parent components in React.
</details>

## Check 04: Modal use case
Why use portals for modals?
<details><summary>Answer</summary>
Modals need to: escape parent overflow/z-index, be on top of everything, be accessible. Portals render at body level, avoiding parent clipping.
</details>

## Check 05: Accessibility
What accessibility concerns do modals have?
<details><summary>Answer</summary>
Focus trap (Tab stays in modal), escape key to close, aria-modal="true", return focus to trigger on close, screen reader announcement.
</details>
