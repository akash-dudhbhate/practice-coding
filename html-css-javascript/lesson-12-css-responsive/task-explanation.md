# Lesson 12 — CSS Responsive Design

## What you'll learn
- Viewport meta tag
- Media queries (min-width, max-width)
- Mobile-first design approach
- Common breakpoints
- Relative units (rem, em, %, vw, vh)
- clamp() for fluid typography
- Responsive images (srcset, picture)
- Flexbox/Grid responsive patterns
- Hide/show elements per breakpoint
- Mobile navigation (hamburger menu)

## Lesson

### Media query
```css
@media (min-width: 768px) {
    .container { flex-direction: row; }
}
```

### Fluid typography
```css
font-size: clamp(1rem, 5vw, 3rem);
```

### Responsive grid
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a page with viewport meta tag. Make the body font-size change at 768px breakpoint (16px mobile, 18px desktop).
2. `easy/p02-solve.html` — Create a container that is full-width on mobile, max-width 1200px centered on desktop. Use media queries.
3. `easy/p03-solve.html` — Create a responsive heading using `clamp()`: minimum 1.5rem, preferred 5vw, maximum 3rem.

### Medium
4. `medium/p01-solve.html` — Create a responsive card grid: 1 column on mobile, 2 on tablet (768px), 3 on desktop (1024px). Use media queries.
5. `medium/p02-solve.html` — Create a responsive navigation: horizontal links on desktop, hamburger menu on mobile. Use CSS-only toggle (checkbox hack) or simple JS.
6. `medium/p03-solve.html` — Create a responsive hero section: full viewport height, fluid title with clamp(), background image that changes size with `background-size: cover`. Add a CTA button that's full-width on mobile, auto-width on desktop.

### Hard
7. `hard/p01-solve.html` — Build a full responsive landing page: header with nav, hero section, features grid (1/2/3 columns), testimonials, footer. All sections adapt to mobile/tablet/desktop.
8. `hard/p02-solve.html` — Build a responsive dashboard: sidebar collapses to icons on tablet, hidden on mobile (toggle button). Content area has a widget grid that reflows. Use CSS transitions for smooth changes.
9. `hard/p03-solve.html` — Build a responsive image gallery: uses `<picture>` with different images per breakpoint. Grid layout with `auto-fit` and `minmax`. Lightbox effect on click (CSS-only or minimal JS). Images have `loading="lazy"`.

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Test in browser: resize window, use DevTools mobile emulation.
