# Lesson 11 — Concepts Explained (CSS Grid)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## display: grid

**What:** `display: grid` creates a 2D layout system — you control both rows AND columns simultaneously.

```css
.container {
    display: grid;
    grid-template-columns: 200px 1fr 200px;  /* 3 columns: fixed, flexible, fixed */
    grid-template-rows: 100px 1fr 50px;       /* 3 rows */
}
```

**Why it exists:** Flexbox is 1D (row OR column). Grid is 2D (rows AND columns). For complex layouts with both dimensions, Grid is the right tool. You can place items in specific cells, span multiple rows/columns.

**Where it's used:** Page layouts, dashboards, photo galleries, calendars, complex card arrangements, form layouts.

**What goes wrong without it:**
- Using flexbox for 2D layouts → nested flex containers → complex, fragile. Grid handles 2D natively.
- Grid for simple 1D layouts (just a row of items) → overkill. Use flexbox for 1D, grid for 2D.
- Forgetting that grid items don't wrap like flex items → grid is explicitly defined by rows/columns.

---

## grid-template-columns

**What:** Defines the number and size of columns.

```css
/* Fixed sizes */
grid-template-columns: 200px 200px 200px;     /* 3 columns, 200px each */

/* Fractional units (fr) — share remaining space */
grid-template-columns: 1fr 2fr 1fr;           /* 25% 50% 25% */

/* Mix of fixed and flexible */
grid-template-columns: 250px 1fr;             /* sidebar + content */

/* repeat() function */
grid-template-columns: repeat(3, 1fr);        /* 3 equal columns */
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  /* responsive! */

/* auto — size based on content */
grid-template-columns: auto 1fr auto;         /* content-sized, flexible, content-sized */
```

**Why it exists:** Without grid-template-columns, you can't create column layouts. `fr` units are the key innovation — they distribute space proportionally, like flex-grow but for grid.

**Where it's used:** Every grid layout — the most important grid property.

**What goes wrong without it:**
- `1fr` vs `%`: `1fr` distributes FREE space (after fixed sizes). `%` is based on container width. Different behavior when mixed with fixed columns.
- `repeat(auto-fit, minmax(300px, 1fr))` → responsive grid without media queries! But items can be wider than 300px if there's extra space. Understand `auto-fit` vs `auto-fill`.
- Too many columns → items become very narrow on small screens → use `minmax()` with a minimum.

---

## grid-template-rows

**What:** Defines the number and size of rows.

```css
grid-template-rows: 100px 1fr 50px;     /* header, content, footer */
grid-template-rows: repeat(3, 200px);   /* 3 rows, 200px each */
grid-template-rows: auto 1fr auto;      /* content-sized, flexible, content-sized */
```

**Why it exists:** Without explicit rows, grid creates implicit rows as needed (auto-sized). Defining rows gives you control over row heights — essential for full-height layouts.

**Where it's used:** Full-page layouts (header/content/footer), dashboards with fixed-height sections.

**What goes wrong without it:**
- No `grid-template-rows` → rows are auto-sized (based on content) → no control over heights.
- `1fr` in rows → fills remaining vertical space. Without `min-height: 100vh` on container, there's no "remaining" space → `1fr` has no effect.
- Too many fixed rows → content overflow on small screens → use `auto` or `minmax()` for flexible rows.

---

## grid-gap (gap)

**What:** Sets spacing between grid cells (rows and columns).

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;              /* 20px between all cells */
    gap: 10px 20px;         /* row-gap column-gap */
    row-gap: 10px;          /* vertical gap only */
    column-gap: 20px;       /* horizontal gap only */
}
```

**Why it exists:** Without gap, you'd use padding/margins on items → uneven spacing at edges. `gap` applies only BETWEEN cells → clean, consistent spacing.

**Where it's used:** Every grid layout that needs spacing.

**What goes wrong without it:**
- `gap` is not supported in very old browsers → fallback to margins.
- `gap` doesn't add space at the outer edges → only between cells. If you need outer spacing, add padding to the container.
- Confusing `gap` with padding → padding is inside the container edge; gap is between cells.

---

## grid-column / grid-row (Placement)

**What:** Place items in specific cells or span multiple cells.

```css
.item {
    grid-column: 1 / 3;      /* span from line 1 to line 3 (2 columns) */
    grid-column: 1 / span 2; /* span 2 columns starting from line 1 */
    grid-row: 1 / 2;         /* row 1 only */
}

/* Shorthand for both */
.item {
    grid-area: 1 / 1 / 2 / 3;  /* row-start / col-start / row-end / col-end */
}
```

Grid lines are numbered starting from 1. A 3-column grid has 4 vertical lines (1, 2, 3, 4).

**Why it exists:** Without explicit placement, items flow into cells automatically. Explicit placement lets you position items precisely — a sidebar spanning 2 rows, a header spanning all columns.

**Where it's used:** Magazine layouts, dashboards, any layout where items need specific positions.

**What goes wrong without it:**
- Line numbers start at 1, not 0. `grid-column: 0 / 2` → invalid.
- `grid-column: 1 / 3` → spans columns 1 and 2 (between lines 1 and 3). Not 3 columns. The number is the LINE, not the column.
- Overlapping items → two items in the same cell → they overlap (can be intentional for layering, but usually a mistake).

---

## grid-template-areas

**What:** Name grid cells and place items by name — the most readable grid layout method.

```css
.container {
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-rows: 80px 1fr 50px;
    grid-template-areas:
        "header header"
        "sidebar content"
        "footer footer";
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }
.footer  { grid-area: footer; }
```

**Why it exists:** Without grid-areas, you use line numbers (`grid-column: 1 / 3`) → hard to visualize. Grid-areas show the layout visually in the CSS — you can see the structure at a glance.

**Where it's used:** Page layouts, dashboards — any layout with named sections.

**What goes wrong without it:**
- Area names must match exactly: `grid-area: header` ↔ `"header header"` in template. Typos → item doesn't place.
- Each row in `grid-template-areas` must have the same number of cells. Missing a name → invalid.
- `.` (dot) = empty cell. `"header header" "sidebar ."` → bottom-right cell is empty.

---

## repeat() and minmax()

**What:** `repeat()` creates multiple tracks. `minmax()` sets a size range.

```css
/* 3 equal columns */
grid-template-columns: repeat(3, 1fr);

/* Responsive: auto-fit columns, min 300px, max 1fr */
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));

/* auto-fill vs auto-fit:
   auto-fill: creates empty tracks to fill the row
   auto-fit: stretches existing items to fill the row */
```

**Why it exists:** Without `repeat()`, you'd write `1fr 1fr 1fr 1fr 1fr` for 5 columns → tedious. Without `minmax()`, columns can shrink to 0 → unusable. `minmax(300px, 1fr)` ensures columns are at least 300px.

**Where it's used:** Responsive card grids, photo galleries, any layout with dynamic column counts.

**What goes wrong without it:**
- `auto-fill` vs `auto-fit`: with 3 items and 5 columns: `auto-fill` → 5 columns, 2 empty. `auto-fit` → 3 columns stretched to fill. Usually you want `auto-fit`.
- `minmax(300px, 1fr)` → on a 900px container, 3 columns. On 600px, 2 columns. On 300px, 1 column. Automatic responsiveness!
- Forgetting `minmax` → columns shrink to content width → tiny columns on large screens.

---

## Implicit vs Explicit Grid

**What:**
- **Explicit grid:** rows/columns you define with `grid-template-*`.
- **Implicit grid:** rows/columns created automatically when items exceed the explicit grid.

```css
.container {
    grid-template-columns: repeat(3, 1fr);   /* 3 explicit columns */
    grid-template-rows: 100px;                /* 1 explicit row */
    grid-auto-rows: 150px;                    /* implicit rows are 150px */
}
/* If you have 7 items: 3 in row 1, 3 in row 2 (implicit, 150px), 1 in row 3 */
```

**Why it exists:** Without implicit grid, you'd need to define every row → impractical for dynamic content. Implicit grid handles overflow automatically.

**Where it's used:** Dynamic content (blog posts, search results) where the number of items is unknown.

**What goes wrong without it:**
- No `grid-auto-rows` → implicit rows are `auto` (content-sized) → inconsistent row heights.
- `grid-auto-flow: column` → items flow into columns instead of rows → changes the entire layout.
- Forgetting that items beyond the explicit grid go into implicit rows → unexpected layout.

---

## Grid Alignment

**What:** Align items within the grid (similar to flexbox alignment).

```css
/* Align all items */
.container {
    justify-items: start;    /* default: stretch. start/end/center/stretch */
    align-items: center;     /* cross-axis (vertical) alignment */
}

/* Align the entire grid within the container */
.container {
    justify-content: center;   /* grid horizontally centered in container */
    align-content: center;     /* grid vertically centered */
}

/* Align a single item */
.item {
    justify-self: center;   /* override justify-items for one item */
    align-self: end;        /* override align-items for one item */
}
```

**Why it exists:** Without alignment, items stretch to fill their cells → can't center or position within cells. Grid alignment gives the same control as flexbox but for 2D.

**Where it's used:** Centering content in cells, aligning items of different sizes, positioning grid within a larger container.

**What goes wrong without it:**
- `justify-items` vs `justify-content`: `justify-items` aligns items WITHIN cells. `justify-content` aligns the ENTIRE GRID within the container. Different things!
- Default is `stretch` → items fill their cells. If you set a fixed size, stretch has no effect.
- Confusing grid alignment with flexbox alignment → similar names, slightly different behavior.

---

## Grid vs Flexbox — When to Use Which

**What:** Decision framework:

| Use Grid when... | Use Flexbox when... |
|---|---|
| 2D layout (rows AND columns) | 1D layout (row OR column) |
| Complex page structure | Navigation bars |
| Items need specific cell placement | Simple alignment |
| Fixed number of rows/columns | Dynamic/wrapping items |
| Magazine/newspaper layout | Card rows that wrap |

**Why it exists:** Both tools are powerful. Using the wrong one → more complex code, fragile layouts. Understanding when to use each is a core CSS skill.

**Where it's used:** Every layout decision. Many layouts use BOTH — Grid for page structure, Flexbox for component internals.

**What goes wrong without it:**
- Grid for a simple navbar → overkill, more code than flexbox.
- Flexbox for a 3x3 dashboard → nested flex containers → complex, hard to maintain. Grid is simpler.
- Mixing them incorrectly → Grid container with flex items (fine), but flex container with grid items (also fine) → understand the nesting.
