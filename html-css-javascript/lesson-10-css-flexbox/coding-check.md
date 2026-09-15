# Lesson 10 — Coding Check

## Easy

### p01-solve.html — Centered box
- [ ] 200x200 box is centered horizontally
- [ ] Box is centered vertically
- [ ] Uses `display: flex`, `justify-content: center`, `align-items: center`
- [ ] Container is at least viewport height (`min-height: 100vh`)

### p02-solve.html — Navbar
- [ ] Logo on the left side
- [ ] 3 nav links on the right side
- [ ] Uses `justify-content: space-between`
- [ ] Vertically aligned (`align-items: center`)

### p03-solve.html — Equal-width cards
- [ ] 4 cards in a row
- [ ] All cards are equal width (`flex: 1`)
- [ ] 16px gap between cards
- [ ] Uses `display: flex` and `gap`

## Medium

### p01-solve.html — Sidebar + content
- [ ] Header spans full width on top
- [ ] Sidebar is fixed 250px width (`flex: 0 0 250px`)
- [ ] Content fills remaining space (`flex: 1`)
- [ ] Sidebar and content are side by side

### p02-solve.html — Wrapping card grid
- [ ] Cards have minimum width of 300px (`flex: 1 1 300px`)
- [ ] Cards wrap to next line on narrow screens (`flex-wrap: wrap`)
- [ ] 20px gap between cards (both horizontal and vertical)
- [ ] At least 4 cards visible

### p03-solve.html — Product card responsive
- [ ] Image on left, details on right (desktop)
- [ ] Uses flexbox for internal layout
- [ ] On mobile (max-width: 600px): switches to column (`flex-direction: column`)
- [ ] Image and details stack vertically on mobile

## Hard

### p01-solve.html — Complete page layout
- [ ] Sticky header at top
- [ ] Fixed sidebar on left
- [ ] Main content area fills remaining space
- [ ] Sticky footer at bottom
- [ ] Content area scrolls independently (`overflow: auto`)
- [ ] Page uses `min-height: 100vh` with `flex-direction: column`

### p02-solve.html — Responsive feature section
- [ ] 3 columns on desktop (flex-basis ~33%)
- [ ] 2 columns on tablet (max-width: 768px, flex-basis ~50%)
- [ ] 1 column on mobile (max-width: 480px, flex-basis 100%)
- [ ] Each column has icon, title, description
- [ ] Uses flex-wrap

### p03-solve.html — Pricing table
- [ ] 3 pricing tiers side by side
- [ ] Middle tier is visually highlighted (different color/border)
- [ ] Middle tier has "Popular" badge
- [ ] Middle tier is slightly larger or elevated
- [ ] All tiers are equal height (`align-self: stretch`)
- [ ] Uses `order` to control visual arrangement
- [ ] Responsive: stacks vertically on mobile
