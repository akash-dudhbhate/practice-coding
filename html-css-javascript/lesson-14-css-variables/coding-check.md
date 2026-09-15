# Lesson 14 — Coding Check

## Easy

### p01-solve.html — Basic variables
- [ ] 3 CSS variables defined in `:root` (--primary, --spacing, --radius)
- [ ] Button uses var(--primary) and var(--spacing)
- [ ] Card uses var(--spacing) and var(--radius)
- [ ] Input uses var(--primary) and var(--radius)
- [ ] Changing a variable value updates all elements

### p02-solve.html — Fallback values
- [ ] Uses `var(--btn-bg, #ccc)` with fallback
- [ ] Variable is defined → custom color is used
- [ ] If variable is removed/undefined → falls back to #ccc
- [ ] Demonstrates both cases (defined and undefined)

### p03-solve.html — Scoped variables
- [ ] `--card-color` defined on `.card` element (not :root)
- [ ] Used for card background
- [ ] Used for card border
- [ ] Variable is NOT available outside the card (scoped)

## Medium

### p01-solve.html — Theme toggle
- [ ] Light theme variables in `:root`
- [ ] Dark theme variables in `[data-theme="dark"]`
- [ ] Toggle button switches `data-theme` attribute
- [ ] All elements update when theme changes
- [ ] Uses JavaScript to toggle attribute

### p02-solve.html — System theme
- [ ] Uses `@media (prefers-color-scheme: dark)`
- [ ] Dark variables defined inside the media query
- [ ] Page automatically matches OS theme
- [ ] No manual toggle needed
- [ ] Testable via DevTools emulation

### p03-solve.html — Design system
- [ ] 5 color variables (primary, secondary, success, warning, danger)
- [ ] 5 spacing variables (xs, sm, md, lg, xl)
- [ ] 4 font-size variables (sm, base, lg, xl)
- [ ] 3 border-radius variables (sm, md, lg)
- [ ] Sample card uses variables from all categories
- [ ] Sample button uses variables from all categories

## Hard

### p01-solve.html — Theme customizer
- [ ] 3 color picker inputs (primary, secondary, accent)
- [ ] JavaScript reads color values and sets CSS variables
- [ ] All elements update in real-time when color changes
- [ ] Reset button restores default values
- [ ] Variables are set on `:root` (document.documentElement)

### p02-solve.html — Responsive design system
- [ ] Variables for spacing, font-size, container width
- [ ] Variables change at 3 breakpoints (mobile, tablet, desktop)
- [ ] Sample page with header, cards, footer
- [ ] ALL values use CSS variables (no hardcoded px/rem)
- [ ] Resizing browser smoothly adapts all values

### hard/p03-solve.html — Multi-theme system
- [ ] 3 themes: light, dark, high-contrast
- [ ] Each theme redefines all color variables
- [ ] Theme switcher with 3 buttons
- [ ] Choice persists in localStorage
- [ ] On page load, saved theme is applied
- [ ] Smooth transitions between themes (`transition: background 0.3s, color 0.3s`)
- [ ] High-contrast theme has maximum contrast ratios
