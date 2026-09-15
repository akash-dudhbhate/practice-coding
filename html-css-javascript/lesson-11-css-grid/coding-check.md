# Lesson 11 — Coding Check

## Easy

### p01-solve.html — 3-column grid
- [ ] 3 equal-width columns (`1fr 1fr 1fr` or `repeat(3, 1fr)`)
- [ ] 20px gap between items
- [ ] 6 items placed in the grid
- [ ] Uses `display: grid`

### p02-solve.html — 2x3 grid with row heights
- [ ] 2 columns
- [ ] 3 rows with heights: 100px, 200px, 100px
- [ ] 6 items placed
- [ ] Row heights are visibly different

### p03-solve.html — Responsive auto-fit grid
- [ ] Uses `repeat(auto-fit, minmax(250px, 1fr))`
- [ ] 8 cards in the grid
- [ ] Cards reflow when browser is resized
- [ ] Cards are minimum 250px wide
- [ ] No media queries needed

## Medium

### p01-solve.html — Named grid areas
- [ ] Header spans full width
- [ ] Sidebar on left, content on right
- [ ] Footer spans full width
- [ ] Uses `grid-template-areas` with named regions
- [ ] Each section has `grid-area: <name>`

### p02-solve.html — Photo gallery
- [ ] 4 columns on desktop
- [ ] 2 columns on tablet (media query)
- [ ] 1 column on mobile (media query)
- [ ] Some photos span 2 columns (`grid-column: span 2`)
- [ ] Gap between photos

### p03-solve.html — Nested grid dashboard
- [ ] Outer grid: header, sidebar, content area
- [ ] Inner grid: 2x2 widget layout in content area
- [ ] 4 widget cards visible
- [ ] Sidebar has fixed width
- [ ] Both grids use `display: grid`

## Hard

### p01-solve.html — Magazine layout
- [ ] Featured article spans 2 columns and 2 rows
- [ ] 4 smaller articles in remaining space
- [ ] Uses `grid-column: 1 / 3` and `grid-row: 1 / 3` for featured
- [ ] All items fit together without gaps
- [ ] Visually distinct featured article

### p02-solve.html — Responsive dashboard
- [ ] Sidebar + header + content layout
- [ ] 4 widgets in content area
- [ ] 4 columns on desktop
- [ ] 2 columns on tablet
- [ ] 1 column on mobile
- [ ] Sidebar collapses or hides on mobile
- [ ] Uses both grid and media queries

### p03-solve.html — Calendar grid
- [ ] 7 columns (days of week: Sun-Sat)
- [ ] 5-6 rows (weeks)
- [ ] Day names header row
- [ ] Some days have colored event cells
- [ ] At least one event spans multiple days (`grid-column: span N`)
- [ ] Cells have consistent size
- [ ] Gap between cells is small (1-2px)
