# Lesson 07 — Coding Check

Use this to verify your solutions before asking me to review. Link your CSS to an HTML file and use DevTools to inspect the box model.

## Easy

### p01-solve.css (Four layers of the box model)
- [ ] `.box` has `width` set (e.g. 200px).
- [ ] `.box` has `padding` (e.g. 20px) — visible as space inside the border.
- [ ] `.box` has `border` (e.g. 2px solid) — visible line around the element.
- [ ] `.box` has `margin` (e.g. 20px) — visible gap between this and other elements.
- [ ] Background color is set so padding area is visible (padding has the background).
- [ ] DevTools box model diagram shows all four layers with correct values.

### p02-solve.css (border-box reset)
- [ ] Universal selector `*` (with `::before` and `::after`) has `box-sizing: border-box`.
- [ ] Two boxes with the same `width` (e.g. 200px) and padding are the SAME total width.
- [ ] Without the reset, boxes would be wider than 200px; with it, they're exactly 200px.
- [ ] Test: inspect both boxes in DevTools — total width equals the set width.

### p03-solve.css (Button styling)
- [ ] `.button` has `padding: 10px 20px` (vertical, horizontal).
- [ ] `.button` has a `border` (e.g. 1px solid).
- [ ] `.button` has `border-radius` (rounded corners).
- [ ] Multiple buttons have `margin` between them (e.g. `margin-right: 10px`).
- [ ] Text inside buttons doesn't touch the border (padding creates space).

## Medium

### p01-solve.css (Card with margin vs padding)
- [ ] `.card` has `padding` (e.g. 20px) — content doesn't touch card edge.
- [ ] `.card` has `margin-bottom` (e.g. 20px) — gap between cards.
- [ ] Background color on `.card` fills the padding area (proves padding is inside).
- [ ] Margin area has NO background (proves margin is outside the background).
- [ ] Test: visually, the background extends to the border, not into the margin gap.

### p02-solve.css (Margin collapsing)
- [ ] Two stacked block elements with different vertical margins (e.g. 30px and 20px).
- [ ] Comment states the actual gap is 30px (the larger margin, not 50px).
- [ ] Test: measure the gap in DevTools — it's 30px, not 50px.
- [ ] Comment explains: vertical margins collapse, larger wins.
- [ ] Horizontal margins (if shown) do NOT collapse — they add up.

### p03-solve.css (Display types)
- [ ] A `display: block` element respects `width` and `height`.
- [ ] A `display: inline` element ignores `width` and `height` (no effect).
- [ ] A `display: inline-block` element respects `width`/`height` but flows inline.
- [ ] Inline element ignores `margin-top`/`margin-bottom` (no vertical margin effect).
- [ ] Test: inspect each element — block and inline-block have set dimensions, inline does not.

## Hard

### p01-solve.css (Complete card layout)
- [ ] `border-box` reset applied to `*`.
- [ ] `.container` has `max-width` (e.g. 800px) and `margin: 0 auto` (centered).
- [ ] `.card` has padding, border, margin-bottom, and background.
- [ ] Images have `max-width: 100%` and `height: auto` (responsive, no overflow).
- [ ] No element overflows the container width.
- [ ] Test: resize browser — cards stay within container, images scale down.

### p02-solve.css (Button group with inline-block)
- [ ] Buttons use `display: inline-block`.
- [ ] Each button has padding, border, border-radius.
- [ ] `margin` between buttons creates spacing.
- [ ] `:hover` state changes background or border color.
- [ ] No flexbox used — only box model properties.
- [ ] Test: buttons sit side by side with consistent gaps; hover changes appearance.

### p03-solve.css (Page layout with box model)
- [ ] `header` has padding and a bottom border.
- [ ] `sidebar` has padding, border, and a fixed/min width.
- [ ] `content` section has padding and `min-height`.
- [ ] Container has `max-width` and is centered with `margin: 0 auto`.
- [ ] `border-box` reset applied.
- [ ] Comments describe the box model of each section (padding, margin, border values).
- [ ] Test: layout has visible spacing, borders, and no overflow on resize.

## How to verify

Create a test HTML file that links your CSS:
```html
<link rel="stylesheet" href="easy/p01-solve.css" />
```
- Open in a browser, then open DevTools (F12).
- Click any element → look at the box model diagram (bottom of Styles/Computed tab) — it shows content, padding, border, margin values visually.
- For margin collapse: measure the gap between two stacked elements — confirm it's the larger margin, not the sum.
- For border-box: confirm total width equals the set `width` (not width + padding + border).
- For responsive: resize the browser narrow — confirm nothing overflows and images scale.
