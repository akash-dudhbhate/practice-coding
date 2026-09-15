# Lesson 18 — Tailwind CSS with React

## What you'll learn
- Tailwind basics (utility-first CSS in JSX)
- Common utility classes (spacing, colors, flex, grid)
- Responsive design (mobile-first breakpoints)
- State variants (hover, focus, active, group)
- Conditional classes (cn utility with clsx + tailwind-merge)
- Tailwind config (custom colors, fonts, animations)
- Dark mode (dark: prefix)
- Reusable component patterns (Card, Badge, Input)

## Lesson

### Utilities
```jsx
<div className="p-4 bg-blue-500 text-white rounded-lg shadow-md flex items-center gap-4">
```

### Responsive
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
```

### Conditional
```jsx
<button className={cn('base-classes', { 'active-class': isActive })}>
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a card component using Tailwind: white background, rounded corners, shadow, padding. Include a title, description, and a button.
2. `easy/p02-solve.jsx` — Create a responsive grid: 1 column on mobile, 2 on tablet, 3 on desktop. Each cell is a colored box with text. Use `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`.
3. `easy/p03-solve.jsx` — Create a button with hover and focus states using Tailwind: changes color on hover, shows a ring on focus, scales down on active. Add `transition-colors`.

### Medium
4. `medium/p01-solve.jsx` — Create a reusable `Button` component with variants (primary, secondary, danger) and sizes (sm, md, lg) using the `cn()` utility. Allow a `className` prop for customization.
5. `medium/p02-solve.jsx` — Create a responsive navbar: logo on left, links on right (hidden on mobile, shown on tablet+), hamburger menu on mobile. Use `hidden md:flex` and `md:hidden`.
6. `medium/p03-solve.jsx` — Create a form with styled inputs using Tailwind: text input, email input, password input, select, checkbox. Include focus states, error states (red border), and labels.

### Hard
7. `hard/p01-solve.jsx` — Build a complete dashboard layout with Tailwind: sidebar (collapsible), header with search, main content area with stat cards, table, and chart placeholder. Fully responsive.
8. `hard/p02-solve.jsx` — Build a dark mode toggle: button switches between light and dark themes. All components use `dark:` variants. Store preference in localStorage. Apply `dark` class to `<html>` element.
9. `hard/p03-solve.jsx` — Build a reusable UI kit with Tailwind: Button (5 variants), Input, Select, Card, Badge, Alert, Modal, Tabs, Accordion. All components accept `className` for customization. Include a demo page showcasing all components.

### How to work
- Write your complete React + Tailwind solution.
- Remove the TODO comment when done.
- Test by importing into a React app with Tailwind configured.
