# Lesson 10 — CSS Flexbox

## What you'll learn
- display: flex and flex-direction
- justify-content (main axis alignment)
- align-items (cross axis alignment)
- flex-wrap for wrapping items
- flex: grow / shrink / basis
- align-self for individual items
- gap for spacing
- order for visual reordering
- Common flexbox patterns

## Lesson

### Centering
```css
.center { display: flex; justify-content: center; align-items: center; }
```

### Navbar
```css
.nav { display: flex; justify-content: space-between; align-items: center; }
```

### Sidebar + content
```css
.layout { display: flex; }
.sidebar { flex: 0 0 250px; }
.content { flex: 1; }
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Center a box (200x200) both horizontally and vertically in the viewport using flexbox.
2. `easy/p02-solve.html` — Create a navbar with logo on the left and 3 nav links on the right using `justify-content: space-between`.
3. `easy/p03-solve.html` — Create a row of 4 equal-width cards using `flex: 1` and `gap: 16px`.

### Medium
4. `medium/p01-solve.html` — Create a sidebar + content layout: fixed 250px sidebar, content fills remaining space. Add a header spanning full width on top.
5. `medium/p02-solve.html` — Create a wrapping card grid: cards are minimum 300px wide, wrap to next line on smaller screens. Use `flex-wrap` and `gap`.
6. `medium/p03-solve.html` — Create a product card with image on left, details on right. Use flexbox for the internal layout. On mobile (max-width 600px), switch to column layout.

### Hard
7. `hard/p01-solve.html` — Build a complete page layout: sticky header, sidebar, main content area, and sticky footer. All using flexbox. Content area scrolls independently.
8. `hard/p02-solve.html` — Build a feature section: 3 columns on desktop, 2 on tablet, 1 on mobile. Each column has an icon, title, and description. Use flex-wrap with appropriate flex-basis.
9. `hard/p03-solve.html` — Build a pricing table with 3 tiers side by side. Middle tier is highlighted (larger, different color, "Popular" badge). Use flexbox for alignment, `order` to control visual order, and `align-self: stretch` for equal heights.

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Open in browser to test visually.
