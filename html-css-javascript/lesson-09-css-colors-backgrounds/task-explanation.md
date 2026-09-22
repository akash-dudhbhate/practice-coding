# Lesson 09 — CSS Colors & Backgrounds

## What you'll learn
- Color formats (hex, rgb, hsl)
- opacity vs rgba transparency
- background-color
- background-image with positioning
- Linear and radial gradients
- background-size (cover, contain)
- box-shadow for depth
- text-shadow
- Color contrast & accessibility

## Lesson

### Colors
```css
color: #ff0000;          /* hex */
color: rgb(255, 0, 0);   /* rgb */
color: hsl(0, 100%, 50%); /* hsl */
```

### Gradients
```css
background: linear-gradient(to right, #ff0000, #0000ff);
background: radial-gradient(circle, #ff0000, #0000ff);
```

### Shadows
```css
box-shadow: 0 4px 8px rgba(0,0,0,0.2);
text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a page with 3 boxes side by side, each with a different background color (use hex, rgb, and hsl formats).

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------+  +-------+  +-------+
   | orange|  | green |  | purple|   <- three 100x100 squares in a row
   +-------+  +-------+  +-------+
     hex       rgb        hsl        <- same idea, 3 notations
   ```
2. `easy/p02-solve.html` — Create a card with a background image (use a placeholder URL), `background-size: cover`, and a semi-transparent overlay using rgba.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +--------------------+
   |  ~ photo ~         |
   |  ............      |   <- 300x200 card; image dimmed by a
   |  ............      |      40% black overlay (rgba)
   +--------------------+
   ```
3. `easy/p03-solve.html` — Create 3 buttons with different box-shadow depths (subtle, medium, strong). Add hover effect that increases the shadow.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ Button ]   [ Button ]   [ Button ]
      _soft_      __deeper__    ___deep___   <- 3 shadow depths
   (hover any button -> its shadow deepens, it "lifts")
   ```

### Medium
4. `medium/p01-solve.html` — Create a hero section with a linear gradient background (3 colors), centered white text with text-shadow for readability, and a CTA button.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +==========================================+
   | ~~gradient: color1 -> color2 -> color3~~ |
   |                                          |
   |         BIG WHITE HEADLINE               |   <- text-shadow keeps
   |         readable white subtext           |      it legible
   |               [ CTA ]                    |   <- white button
   +==========================================+
   ```
5. `medium/p02-solve.html` — Create a card grid (3 cards) with: background-image, gradient overlay on hover, box-shadow, and rounded corners. Each card has a title and description.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +--------+    +--------+    +--------+
   | ~img~  |    | ~img~  |    | ~img~  |    <- 3 cards, photo tops
   | (img)  |    |~DARK~~~|    | (img)  |       hover -> dark gradient
   | Title  |    | Title  |    | Title  |       fades over the photo
   | desc   |    | desc   |    | desc   |
   +--------+    +--------+    +--------+
   ```
6. `medium/p03-solve.html` — Create a color palette display: 5 color swatches showing hex, rgb, and hsl values. Use CSS variables for the colors. Verify contrast ratios are accessible.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ c1 ]   [ c2 ]   [ c3 ]   [ c4 ]   [ c5 ]   <- 5 swatch colors
   #hex     #hex     #hex     #hex     #hex        each labeled
   rgb(...) rgb(...) rgb(...) rgb(...) rgb(...)    with hex / rgb / hsl
   hsl(...) hsl(...) hsl(...) hsl(...) hsl(...)
   (colors come from :root CSS variables)
   ```

### Hard
7. `hard/p01-solve.html` — Create a glassmorphism card: semi-transparent background, backdrop-blur, subtle border, and box-shadow. Place it over a gradient background.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +==========================================+
   | ~~~ colorful gradient background ~~~~~~~ |
   |      +----------------------+            |
   |      | frosted glass card   |            |   <- translucent +
   |      | you can *almost* see |            |      backdrop-blur:
   |      | the gradient through |            |      bg shows through
   |      +----------------------+            |
   +==========================================+
   ```
8. `hard/p02-solve.html` — Create a profile card with: avatar (radial gradient placeholder), name, bio, stats row, and a follow button. Use box-shadow for elevation, gradients for visual interest, and hover transitions.

   ```
   WHAT IT SHOULD LOOK LIKE:
           +--------------------+
           |      ~~~~~~~       |
           |      ~avatar~      |   <- radial-gradient circle avatar
           |      ~~~~~~~       |
           |     Jane Doe       |
           |     short bio...   |
           |  100 | 200 | 50    |   <- stats row (3 columns)
           |   [  Follow  ]     |   <- gradient button
           +--------------------+
           (card lifts on hover via box-shadow)
   ```
9. `hard/p03-solve.html` — Create a landing page hero with: animated gradient background (CSS animation shifting colors), floating cards with box-shadow, glassmorphism navbar, and text with gradient clip (gradient text effect).

   ```
   WHAT IT SHOULD LOOK LIKE:
   +==========================================+
   | ~~animated shifting gradient bg~~~~~~~~~ |
   | [frosted navbar: logo | links | links ]  |
   |                                          |
   |   GRADIENT-FILLED HEADLINE TEXT          |   <- gradient clipped
   |                                          |      into the text itself
   |  [floating card]   [floating card]       |   <- shadowed cards
   +==========================================+
   ```

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Open in browser to test visually.
