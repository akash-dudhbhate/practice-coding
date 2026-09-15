# Lesson 18 — Intuition Checks

## Check 01: Utility classes
Why use utility classes instead of custom CSS?
<details><summary>Answer</summary>
Faster development, consistent design system, smaller CSS bundle (only used classes), no naming (BEM) needed, responsive variants built in.
</details>

## Check 02: Responsive prefixes
```jsx
<div className="text-sm md:text-base lg:text-lg">
```
<details><summary>Answer</summary>
Mobile-first: `text-sm` by default, `text-base` at md (768px+), `text-lg` at lg (1024px+).
</details>

## Check 03: State variants
```jsx
<button className="bg-blue-500 hover:bg-blue-600 active:bg-blue-700">
```
<details><summary>Answer</summary>
`hover:` applies on hover, `active:` on click. Also `focus:`, `disabled:`, `group-hover:`, `dark:`.
</details>

## Check 04: Configuration
```jsx
// tailwind.config.js
module.exports = {
  theme: { extend: { colors: { brand: "#007bff" } } }
};
```
<details><summary>Answer</summary>
Extend theme with custom values. `extend` adds to defaults (doesn't replace). Use as `bg-brand`, `text-brand`.
</details>

## Check 05: @apply
```css
.btn { @apply bg-blue-500 text-white px-4 py-2 rounded; }
```
<details><summary>Answer</summary>
Use Tailwind utilities in custom CSS. Useful for reusable component classes. But prefer composing utilities directly in JSX.
</details>
