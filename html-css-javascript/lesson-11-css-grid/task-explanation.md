# Lesson 11 — CSS Grid

## What you'll learn
- display: grid and 2D layouts
- grid-template-columns and grid-template-rows
- gap (row-gap, column-gap)
- grid-column / grid-row (item placement)
- grid-template-areas (named layout regions)
- repeat() and minmax()
- auto-fit vs auto-fill (responsive grids)
- Grid alignment (justify-items, align-items)
- Grid vs Flexbox — when to use which

## Lesson

### Basic grid
```css
.grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }
```

### Named areas
```css
grid-template-areas:
    "header header"
    "sidebar content"
    "footer footer";
```

### Responsive auto-grid
```css
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a 3-column grid with equal-width columns and 20px gap. Place 6 items in it.
2. `easy/p02-solve.html` — Create a 2x3 grid (2 columns, 3 rows) with different row heights (100px, 200px, 100px). Place 6 items.
3. `easy/p03-solve.html` — Create a responsive card grid using `repeat(auto-fit, minmax(250px, 1fr))`. Add 8 cards. Resize browser to see them reflow.

### Medium
4. `medium/p01-solve.html` — Create a page layout using `grid-template-areas`: header (full width), sidebar (left), content (right), footer (full width). Use named grid areas.
5. `medium/p02-solve.html` — Create a photo gallery: 4 columns on desktop, 2 on tablet, 1 on mobile. Use `grid-template-columns` with media queries. Photos span different sizes (some 1x1, some 2x1).
6. `medium/p03-solve.html` — Create a dashboard layout: header on top, sidebar on left, 4 widget cards in the content area (2x2 grid). Use nested grid (outer grid for layout, inner grid for widgets).

### Hard
7. `hard/p01-solve.html` — Build a magazine-style layout: featured article spanning 2 columns and 2 rows, then 4 smaller articles in a 2x2 grid next to it. Use `grid-column` and `grid-row` for placement.
8. `hard/p02-solve.html` — Build a responsive dashboard: sidebar + header + content grid. Content has 4 widgets that rearrange based on screen size (4 columns desktop, 2 tablet, 1 mobile). Sidebar collapses on mobile.
9. `hard/p03-solve.html` — Build a calendar grid: 7 columns (days of week), 5-6 rows (weeks). Include day names header. Some days have events (colored cells). Use grid placement for events spanning multiple days.

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Open in browser to test visually.
