# Lesson 07 — Box Model & Spacing

## What you'll learn
- The four layers of the box model: content, padding, border, margin.
- How `box-sizing: border-box` fixes sizing confusion.
- When to use margin vs padding.
- How display types (block, inline, inline-block) affect the box model.

## Lesson

Every HTML element is a rectangular box. Understanding the box model is the foundation of CSS layout.

### The four layers
```
content → padding → border → margin
(inside out)
```
- **Content:** the text/image.
- **Padding:** space inside, between content and border (has the background).
- **Border:** the line around the element.
- **Margin:** space outside, between this element and neighbors.

### box-sizing
```css
*, *::before, *::after {
  box-sizing: border-box;  /* width INCLUDES padding + border */
}
```
Without this, `width: 200px` + `padding: 20px` = 244px total. With it, total = 200px.

### Shorthand syntax
```css
margin: 10px 20px 30px 40px;  /* top, right, bottom, left (clockwise) */
margin: 10px 20px;            /* top/bottom, left/right */
padding: 20px;                /* all sides */
```

### Margin collapsing
Vertical margins between block elements collapse — the larger margin wins, they don't add up.

### Display types
- `block`: full width, new line, respects width/height.
- `inline`: content-width, same line, ignores width/height/vertical margin.
- `inline-block`: inline flow, but respects width/height.

### Key rules
- Always use the `border-box` reset.
- Margin = between elements. Padding = inside an element.
- Use `max-width: 100%` on images and responsive containers.
- Avoid fixed heights on growing content.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete CSS from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.css` — Style a `.box` with width, padding, border, and margin. Show the four layers visually with different background/border colors.

   ```
   WHAT IT SHOULD LOOK LIKE:
   . . . margin 30px (transparent) . . .
   . +=============================+ .
   . | border 5px                  | .
   . |  +----------------------+   | .
   . |  | padding 20px (bg)    |   | .
   . |  |   [ content 200px ]  |   | .
   . |  +----------------------+   | .
   . +=============================+ .
   (total footprint is much wider than 200px)
   ```
2. `easy/p02-solve.css` — Apply the `border-box` reset (`*`) and style two boxes side by side with consistent widths.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +--------------------+--------------------+
   |       .box1        |       .box2        |   <- each exactly 50%
   | padding + border   | padding + border   |      wide; padding and
   +--------------------+--------------------+      border are INSIDE
                                                   (border-box)
   ```
3. `easy/p03-solve.css` — Style a `.button` with padding (10px 20px), border, border-radius, and margin between buttons.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [  Button 1  ]   [  Button 2  ]   [  Button 3  ]
       ^-- padded, rounded 6px corners,
           margin space between neighbors
   ```

### Medium
4. `medium/p01-solve.css` — Style a `.card` with padding for internal spacing and margin between cards. Demonstrate margin vs padding with background colors.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-----------------+
   |   (padding 20)  |   <- space INSIDE border, tinted by background
   |   card content  |
   +-----------------+
       < 16px gap >      <- margin: transparent space BETWEEN cards
   +-----------------+
   |   next card     |
   +-----------------+
   ```
5. `medium/p02-solve.css` — Demonstrate margin collapsing: two stacked boxes with different vertical margins. Comment what the actual gap is.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +---------+
   | box A   |   margin-bottom: 30px
   +---------+
       ~ ~ ~      <- gap is 30px (the LARGER margin wins)
   +---------+        NOT 30+20 = 50px -- margins collapse
   | box B   |   margin-top: 20px
   +---------+
   ```
6. `medium/p03-solve.css` — Style elements with `display: block`, `inline`, and `inline-block`. Show which respects width/height and which doesn't.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------------------------------+
   | .block fills the whole row    |   <- respects width + height
   +-------------------------------+
   text [inline] text   <- shrinks to content, IGNORES width/height
   [inline-block] [inline-block]      <- sized, but flows in a row
   ```

### Hard
7. `hard/p01-solve.css` — A complete card layout: border-box reset, cards with padding/border/margin, max-width container, responsive images (`max-width: 100%`).

   ```
   WHAT IT SHOULD LOOK LIKE:
          +--------------------+
          | [ img (fits) ]     |   <- max-width:100%, never overflows
          | Card text          |
          +--------------------+
          | [ img ]            |   <- 960px-max container,
          | Card text          |       auto-centered on the page
          +--------------------+
   ```
8. `hard/p02-solve.css` — A button group using `inline-block` with consistent spacing, borders, border-radius, and hover states (no flexbox — use box model only).

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------+-------+-------+
   | Left  | Mid   | Right |   <- buttons fused into one bar:
   +-------+-------+-------+      shared borders, rounded ends,
   (hover highlights one segment)   no gaps between them
   ```
9. `hard/p03-solve.css` — A page layout with header, sidebar, and content sections using margins, padding, borders, min-height, and max-width. Comment the box model of each section.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +------------------------------------------+
   |                 HEADER                   |
   +--------+-----------------+---------------+
   |        |                 |
   | SIDEBAR|    CONTENT      |   <- fixed-width sidebar,
   | (fixed)|   (flows)       |       content fills the rest
   +--------+-----------------+
   |                 FOOTER                   |
   +------------------------------------------+
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete CSS from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Link the CSS to an HTML file and open in a browser to check the box model.
- Use DevTools to inspect each element's box model (the visual diagram at the bottom of the Styles tab).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
