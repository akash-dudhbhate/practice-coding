# Lesson 10 — Concepts Explained (CSS Flexbox)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## display: flex

**What:** `display: flex` turns an element into a flex container. Its children become flex items that can be aligned, distributed, and reordered in one dimension (row or column).

```css
.container {
    display: flex;        /* children align in a row by default */
}
```

**Why it exists:** Before flexbox, centering elements vertically was a nightmare (tables, `position: absolute` hacks, `line-height` tricks). Flexbox makes alignment, distribution, and reordering trivial — one line of CSS.

**Where it's used:** Navigation bars, card rows, button groups, centering content, toolbars, footers, any 1D layout.

**What goes wrong without it:**
- Using `float` for layout → floats were never designed for layout → clearfix hacks, collapsing containers, unpredictable behavior.
- `inline-block` → whitespace gaps between items → annoying.
- Flexbox only does 1D (row OR column). For 2D layouts (rows AND columns), use CSS Grid.

---

## flex-direction

**What:** Controls the main axis direction of flex items.

```css
.container {
    display: flex;
    flex-direction: row;             /* default: left to right */
    flex-direction: row-reverse;     /* right to left */
    flex-direction: column;          /* top to bottom */
    flex-direction: column-reverse;  /* bottom to top */
}
```

**Why it exists:** Without `flex-direction`, you can only lay items in a row. `column` is essential for stacking items vertically with flex alignment (centered, distributed).

**Where it's used:** Vertical menus, stacked cards, sidebars, responsive layouts (row on desktop, column on mobile).

**What goes wrong without it:**
- Forgetting `flex-direction: column` → items stay in a row when you want them stacked → alignment looks wrong.
- `row-reverse` → items are in reverse order but DOM order stays the same → accessibility issues (screen readers read DOM order, not visual order).
- Switching from row to column for responsive → `flex-direction: column` in a media query is the simplest responsive pattern.

---

## justify-content (Main Axis)

**What:** Aligns items along the main axis (the direction of `flex-direction`).

```css
.container {
    display: flex;
    justify-content: flex-start;     /* default: packed at start */
    justify-content: flex-end;       /* packed at end */
    justify-content: center;         /* centered */
    justify-content: space-between;  /* first at start, last at end, equal space between */
    justify-content: space-around;   /* equal space around each item */
    justify-content: space-evenly;   /* equal space between and at edges */
}
```

**Why it exists:** Without `justify-content`, you'd use margins (`margin-left: auto`) to push items → fragile, doesn't adapt to content changes. `justify-content` distributes items dynamically.

**Where it's used:** Navigation bars (logo left, links right with `space-between`), centered content, card distributions, button groups.

**What goes wrong without it:**
- `space-between` vs `space-around`: `space-between` has no space at edges; `space-around` has half-space at edges. Choose based on design.
- `justify-content` works on the MAIN axis. If `flex-direction: column`, it controls vertical alignment, not horizontal. This is the #1 flexbox confusion.
- Overflow: too many items → `justify-content` has no effect (items overflow).

---

## align-items (Cross Axis)

**What:** Aligns items along the cross axis (perpendicular to `flex-direction`).

```css
.container {
    display: flex;
    align-items: stretch;       /* default: fill container height */
    align-items: flex-start;    /* top of cross axis */
    align-items: flex-end;      /* bottom of cross axis */
    align-items: center;        /* centered on cross axis */
    align-items: baseline;      /* aligned by text baseline */
}
```

**Why it exists:** Without `align-items`, items of different heights align to the top by default → looks ragged. `align-items: center` vertically centers them — the most common use case.

**Where it's used:** Vertically centering content (the classic flexbox use case), aligning items of different heights, baseline alignment for text.

**What goes wrong without it:**
- `align-items` works on the CROSS axis. If `flex-direction: row`, it controls VERTICAL alignment. If `flex-direction: column`, it controls HORIZONTAL alignment. Opposite of what you'd expect.
- `stretch` (default) → items fill the container height. If you set a fixed height on items, stretch has no effect.
- Forgetting `align-items: center` → items align to top → "why isn't my content centered?"

---

## flex-wrap

**What:** Controls whether flex items wrap to the next line when they overflow.

```css
.container {
    display: flex;
    flex-wrap: nowrap;      /* default: shrink to fit, no wrapping */
    flex-wrap: wrap;        /* wrap to next line */
    flex-wrap: wrap-reverse;/* wrap in reverse order */
}
```

**Why it exists:** Without `flex-wrap`, all items squeeze into one line → tiny, unreadable items. `wrap` lets items flow to the next line → responsive without media queries.

**Where it's used:** Card grids, tag clouds, navigation that wraps on mobile, image galleries.

**What goes wrong without it:**
- `nowrap` (default) → 10 items in 300px → each item is 30px → unusable. Always use `wrap` for dynamic content.
- Wrapped items don't align by default → use `align-content` to control spacing between wrapped lines.
- `wrap` + `justify-content: space-between` → last row may have large gaps if items don't fill it evenly.

---

## flex: 1 (grow, shrink, basis)

**What:** `flex` is shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`.

```css
.item {
    flex: 1;                    /* grow to fill available space */
    /* = flex-grow: 1, flex-shrink: 1, flex-basis: 0% */

    flex: 0 1 auto;             /* default: don't grow, can shrink, natural size */

    flex: 2;                    /* grow twice as much as flex: 1 items */

    flex: 0 0 200px;            /* fixed: don't grow, don't shrink, 200px */
}
```

**Why it exists:** Without `flex`, items are their natural size. `flex: 1` makes an item fill available space — essential for sidebars (fixed width) + content (fills rest) layouts.

**Where it's used:** Sidebar + content layouts, equal-width columns, one item that grows while others stay fixed.

**What goes wrong without it:**
- `flex: 1` on all items → equal widths. `flex: 2` on one → it's twice as wide. Forgetting to set flex → items are natural width → uneven.
- `flex-basis: 0` vs `auto`: `0` means "ignore content size, distribute purely by grow ratio". `auto` means "start from content size, then grow". Different results.
- `flex: 1` doesn't mean "100% width" — it means "grow to fill remaining space after other items take their share".

---

## align-self

**What:** Override `align-items` for a single item.

```css
.container { display: flex; align-items: center; }
.item.special { align-self: flex-start; }  /* this one aligns to top */
```

**Why it exists:** Without `align-self`, all items follow the container's `align-items`. `align-self` lets one item break the rule — useful for a taller item or a special-positioned element.

**Where it's used:** One item that needs different alignment (e.g., a badge in a card row that sticks to the top).

**What goes wrong without it:**
- Forgetting that `align-self` overrides `align-items` → confused why one item is different.
- `align-self` only affects the cross axis → if you want main-axis override, use `margin: auto` instead.

---

## gap

**What:** `gap` adds space between flex items without needing margins.

```css
.container {
    display: flex;
    gap: 16px;          /* 16px between each item */
    gap: 10px 20px;     /* row-gap column-gap */
}
```

**Why it exists:** Before `gap`, you'd use `margin-right` on each item and remove it from the last (`:last-child { margin-right: 0 }`). `gap` is cleaner — no margin hacks, works perfectly with `flex-wrap`.

**Where it's used:** Every flex layout that needs spacing between items.

**What goes wrong without it:**
- Using margins instead → extra space at the end, or `:last-child` hacks → fragile.
- `gap` doesn't work in very old browsers → fallback to margins if you need to support them.
- `gap` with `flex-wrap` → applies between rows too → consistent spacing in wrapped layouts.

---

## order

**What:** Change the visual order of flex items without changing the DOM.

```css
.item { order: 1; }    /* default is 0 */
.item-first { order: -1; }   /* appears before others */
.item-last { order: 99; }    /* appears after others */
```

**Why it exists:** Without `order`, visual order = DOM order. `order` lets you rearrange visually — useful for responsive layouts (sidebar on left desktop, on top mobile).

**Where it's used:** Responsive layouts, reordering elements per breakpoint, visual emphasis.

**What goes wrong without it:**
- Screen readers read DOM order, not visual order → `order` creates a mismatch → accessibility issue. Don't use `order` for important content sequence.
- `order: 99` → if another item has `order: 100`, it comes after. Use large numbers carefully.
- Overusing `order` → confusing code. If you need to reorder significantly, change the DOM.

---

## Common Flexbox Patterns

**What:** Real-world patterns you'll use constantly:

```css
/* 1. Perfect centering */
.center { display: flex; justify-content: center; align-items: center; }

/* 2. Navbar: logo left, links right */
.nav { display: flex; justify-content: space-between; align-items: center; }

/* 3. Sidebar + content */
.layout { display: flex; }
.sidebar { flex: 0 0 250px; }  /* fixed width */
.content { flex: 1; }           /* fills remaining */

/* 4. Card grid that wraps */
.cards { display: flex; flex-wrap: wrap; gap: 20px; }
.card { flex: 1 1 300px; }     /* grow, shrink, min 300px */

/* 5. Sticky footer */
.page { display: flex; flex-direction: column; min-height: 100vh; }
.content { flex: 1; }           /* fills space, pushes footer down */
```

**Why it exists:** These patterns solve the most common layout problems. Memorizing them covers 90% of flexbox use cases.

**Where it's used:** Every web page — navigation, layouts, cards, centering, sticky footers.

**What goes wrong without it:**
- `min-height: 100vh` on the page → without it, `flex: 1` on content doesn't push the footer down (no space to fill).
- `flex: 1 1 300px` → `300px` is `flex-basis` (min size before growing). Without it, cards can shrink too small.
- Forgetting `flex-direction: column` for the sticky footer → flex works horizontally by default.
