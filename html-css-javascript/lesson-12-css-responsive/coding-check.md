# Lesson 12 — Coding Check

## Easy

### p01-solve.html — Viewport + font-size breakpoint
- [ ] `<meta name="viewport">` tag present in `<head>`
- [ ] Body font-size is 16px on mobile (default)
- [ ] Font-size changes to 18px at min-width: 768px
- [ ] Uses `@media (min-width: 768px)`

### p02-solve.html — Responsive container
- [ ] Container is full-width on mobile
- [ ] Container is max-width 1200px on desktop
- [ ] Container is centered on desktop (`margin: 0 auto`)
- [ ] Uses media query for desktop styles

### p03-solve.html — Fluid heading with clamp
- [ ] Uses `font-size: clamp(1.5rem, 5vw, 3rem)`
- [ ] Heading is at least 1.5rem on small screens
- [ ] Heading is at most 3rem on large screens
- [ ] Heading scales smoothly between min and max

## Medium

### p01-solve.html — Responsive card grid
- [ ] 1 column on mobile (default)
- [ ] 2 columns at 768px
- [ ] 3 columns at 1024px
- [ ] Uses media queries with `grid-template-columns` or flex
- [ ] Gap between cards

### p02-solve.html — Responsive navigation
- [ ] Horizontal nav links on desktop
- [ ] Hamburger menu button on mobile
- [ ] Nav links hidden on mobile, shown when toggled
- [ ] Toggle works (CSS checkbox hack or JS)
- [ ] Smooth transition or animation

### p03-solve.html — Responsive hero
- [ ] Full viewport height (`min-height: 100vh`)
- [ ] Title uses `clamp()` for fluid sizing
- [ ] Background image with `background-size: cover`
- [ ] CTA button is full-width on mobile
- [ ] CTA button is auto-width on desktop

## Hard

### p01-solve.html — Full responsive landing page
- [ ] Header with responsive nav
- [ ] Hero section adapts to screen size
- [ ] Features grid: 1/2/3 columns (mobile/tablet/desktop)
- [ ] Testimonials section
- [ ] Footer
- [ ] All sections look correct at 375px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile

### p02-solve.html — Responsive dashboard
- [ ] Sidebar visible on desktop (full width)
- [ ] Sidebar collapses to icons on tablet
- [ ] Sidebar hidden on mobile with toggle button
- [ ] Widget grid reflows (1/2/3/4 columns)
- [ ] CSS transitions for smooth changes
- [ ] Toggle button works

### p03-solve.html — Responsive image gallery
- [ ] Uses `<picture>` with `<source>` for different images
- [ ] At least 2 different images per breakpoint
- [ ] Grid layout with `auto-fit` and `minmax`
- [ ] Lightbox effect on image click
- [ ] Images have `loading="lazy"`
- [ ] Images have `alt` text
- [ ] No horizontal scroll on mobile
