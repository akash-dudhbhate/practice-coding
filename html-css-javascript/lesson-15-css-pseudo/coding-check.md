# Lesson 15 — Coding Check

## Easy

### p01-solve.html — Hover effects
- [ ] 3 links with different hover effects
- [ ] Link 1: changes color on hover
- [ ] Link 2: shows underline on hover
- [ ] Link 3: scales up on hover
- [ ] All use `:hover` with `transition`

### p02-solve.html — Zebra-striped list
- [ ] Even items have one background color
- [ ] Odd items have another background color
- [ ] Uses `:nth-child(even)` and `:nth-child(odd)`
- [ ] First child has distinct style
- [ ] Last child has distinct style

### p03-solve.html — Decorative bullets
- [ ] Each `<li>` has a decorative arrow before it
- [ ] Uses `::before` with `content: "→ "`
- [ ] Default bullet removed (`list-style: none`)
- [ ] Content is visible and properly positioned

## Medium

### p01-solve.html — CSS tooltip
- [ ] Element has `data-tooltip` attribute
- [ ] `::after` uses `content: attr(data-tooltip)`
- [ ] Tooltip hidden by default (opacity: 0)
- [ ] Tooltip appears on hover (`:hover::after`)
- [ ] Tooltip is positioned above or below the element
- [ ] Smooth transition

### p02-solve.html — Styled form states
- [ ] `:focus` adds a highlight (border or outline)
- [ ] `:invalid` shows red border (with `required` and `type="email"`)
- [ ] `:valid` shows green border
- [ ] `:disabled` input is greyed out
- [ ] `:checked` checkbox label is styled differently

### p03-solve.html — Magazine article
- [ ] `::first-letter` creates a drop cap (large, floated)
- [ ] Drop cap is 2-3x the normal font size
- [ ] `::first-line` is uppercase
- [ ] First line has letter-spacing
- [ ] Article looks like a magazine layout

## Hard

### p01-solve.html — CSS accordion
- [ ] Multiple FAQ items with question links
- [ ] Answers hidden by default
- [ ] Clicking a question shows the answer (using `:target`)
- [ ] Only one answer visible at a time
- [ ] No JavaScript used
- [ ] Smooth transition or animation

### p02-solve.html — Custom checkbox/radio
- [ ] Default input hidden (`appearance: none` or opacity: 0)
- [ ] Custom visual using `::before` or `::after` on label
- [ ] `:checked` state shows selected visual (checkmark or fill)
- [ ] `:hover` state on the custom control
- [ ] `:focus-visible` state for keyboard navigation
- [ ] Both checkbox AND radio button styled

### p03-solve.html — Animated navigation
- [ ] Nav links with underline animation on hover
- [ ] Underline uses `::after` with `transform: scaleX(0)` → `scaleX(1)`
- [ ] Underline animates smoothly (transition)
- [ ] One item has a badge using `::after` with `content`
- [ ] Active item has a visual indicator
- [ ] All effects are CSS-only (no JS)
