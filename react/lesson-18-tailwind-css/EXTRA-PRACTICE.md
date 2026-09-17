# lesson-18-tailwind-css — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Wrong Class Name
```jsx
<div className="bg-blue">Box</div>
```
<details><summary>Answer</summary>
**Bug:** `bg-blue` is not valid. Tailwind needs shade: `bg-blue-500`.
**Fix:** `className="bg-blue-500"`.
</details>

## Debug 02 (Medium): Arbitrary Value Syntax
```jsx
<div className="w-[500]">Box</div>
```
<details><summary>Answer</summary>
**Bug:** Arbitrary values need units: `w-[500px]`.
**Fix:** `className="w-[500px]"`.
</details>

## Debug 03 (Hard): Responsive Prefix Order
```jsx
<div className="md:sm:flex">Box</div>
```
<details><summary>Answer</summary>
**Bug:** Can't stack responsive prefixes. Only one per property.
**Fix:** `className="sm:flex md:block"` — different breakpoints for different properties.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Missing shade numbers
```jsx
// WRONG
<div className="bg-blue text-white">
// CORRECT
<div className="bg-blue-500 text-white">
```

## Mistake 02: Too many classes
```jsx
// HARD TO READ
<div className="flex flex-col items-center justify-center gap-4 p-4 md:p-8 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
// EXTRACT to component or @apply
```

## Mistake 03: Not using config
```jsx
// WRONG — hardcoded colors
<div className="bg-[#007bff]">
// CORRECT — use config
<div className="bg-brand">
```

## Mistake 04: Fighting the framework
```jsx
// WRONG — custom CSS to override Tailwind
// CORRECT — use Tailwind's configuration
```

## Mistake 05: Not purging
```jsx
// Ensure content paths are set in config
// Otherwise CSS includes all utilities (huge file)
module.exports = { content: ["./src/**/*.{js,jsx}"] };
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Inline Styles
### Before
```jsx
<div style={{ padding: '16px', margin: '8px', backgroundColor: 'red' }}>
```
### After
```jsx
<div className="p-4 m-2 bg-red-500">
```

## Refactor 02 (Medium): Repeated Class Strings
### Before
```jsx
<button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">A</button>
<button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">B</button>
```
### After
```jsx
const btnClass = "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600";
<button className={btnClass}>A</button>
```

## Refactor 03 (Hard): Long Class Lists
### Before
```jsx
<div className="flex flex-col items-center justify-between p-4 m-2 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer">
```
### After
```jsx
// Extract to component or @apply in CSS
.card { @apply flex flex-col items-center justify-between p-4 m-2 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer; }
<div className="card">
```

---

## Approach Comparison — different ways to solve it

## Problem: Button Styles

### Approach 1: Utility classes
```jsx
<button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
```

### Approach 2: @apply in CSS
```css
.btn { @apply bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600; }
```
```jsx
<button className="btn">
```

### Approach 3: Component
```jsx
function Button({ children }) {
  return <button className="bg-blue-500 ...">{children}</button>;
}
```

**Winner:** Approach 3 for reusable buttons. Approach 1 for one-off styling.

---

## Problem: Responsive Design

### Approach 1: Tailwind responsive prefixes
```jsx
<div className="grid grid-cols-1 md:grid-cols-3">
```

### Approach 2: Custom CSS media queries
```css
@media (min-width: 768px) { .grid { grid-template-columns: repeat(3, 1fr); } }
```

**Winner:** Approach 1 — faster, consistent.
