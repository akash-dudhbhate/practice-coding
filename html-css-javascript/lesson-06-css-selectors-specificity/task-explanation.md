# Lesson 06 — CSS Selectors & Specificity

## What you'll learn
- How to target elements with element, class, and ID selectors.
- How to combine selectors with combinators (descendant, child, sibling).
- How the cascade and specificity decide which rule wins.
- How to use pseudo-classes and attribute selectors.

## Lesson

CSS selectors tell the browser WHICH elements to style. Specificity decides which rule wins when rules conflict.

### Basic selectors
```css
p { }           /* element — all <p> tags */
.highlight { }  /* class — elements with class="highlight" */
#header { }     /* ID — the one element with id="header" */
```

### Combinators
```css
div p { }    /* descendant — <p> anywhere inside <div> */
div > p { }  /* child — <p> directly inside <div> */
h2 + p { }   /* adjacent sibling — <p> right after <h2> */
h2 ~ p { }   /* general sibling — all <p> after <h2> */
```

### Specificity (the scoring system)
```
(inline, ID, class, element)
*              -> 0,0,0,0
p              -> 0,0,0,1
.highlight     -> 0,0,1,0
#header        -> 0,1,0,0
style="..."    -> 1,0,0,0
```
Higher wins. ID beats any number of classes. Class beats any number of elements.

### The cascade
When specificity is equal, the LATER rule wins.
```css
p { color: blue; }
p { color: red; }  /* wins — comes later */
```

### Pseudo-classes
```css
a:hover { }
input:focus { }
li:first-child { }
li:nth-child(odd) { }
li:not(.active) { }
```

### Attribute selectors
```css
[type="text"] { }
[href^="https"] { }   /* starts with */
[href$=".pdf"] { }   /* ends with */
```

### Key rules
- Use classes for styling, IDs for JS/anchors.
- Avoid `!important` — fix specificity instead.
- Use DevTools to see which rule wins (overridden rules are struck through).
- Group selectors with commas: `h1, h2, h3 { }`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete CSS from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.css` — Style all `<p>` tags gray, all `<h1>` tags blue, and a `.highlight` class with yellow background.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Blue Heading                  <- all <h1> render blue
   Gray paragraph text here.     <- all <p> render gray
   [ YELLOW ] highlighted text   <- .highlight: yellow background
   ```
2. `easy/p02-solve.css` — Style links: default blue, `:hover` red, `:focus` underline. Use a `.btn` class for buttons with padding.

   ```
   WHAT IT SHOULD LOOK LIKE:
   A normal link        <- blue
   A hovered link       <- turns red on :hover
   A focused link       <- underlined on :focus (keyboard)
   [ .btn ]             <- padded inline-block, looks like a button
   ```
3. `easy/p03-solve.css` — Group selectors: `h1, h2, h3` share font-family and color. Style `#main-title` differently (higher specificity).

   ```
   WHAT IT SHOULD LOOK LIKE:
   Heading One          <- h1/h2/h3 all share: Arial + #333
   Heading Two          <- same grouped style
   MAIN TITLE           <- DIFFERENT color+font (id #main-title wins)
   ```

### Medium
4. `medium/p01-solve.css` — Use combinators: style `<p>` inside `<article>`, direct child `<li>` of `<ul>`, and `<p>` right after `<h2>`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   ARTICLE
     paragraph in #444           <- article p styled
     * square bullets            <- ul > li only
       * nested keeps discs      <- deeper <li> unaffected
   H2 Title
     first para = BOLD           <- only the <p> right after h2
     second para = normal
   ```
5. `medium/p02-solve.css` — Demonstrate specificity: write rules at element, class, and ID level that override each other. Comment which wins.

   ```
   WHAT IT SHOULD LOOK LIKE:
   plain <p>            -> black    (element rule)
   p.text               -> blue     (class beats element)
   p#important          -> red      (ID beats both -- all 3 match,
                                      specificity 1,0,0 wins)
   ```
6. `medium/p03-solve.css` — Use pseudo-classes: `:first-child`, `:last-child`, `:nth-child(odd)`, `:not(.active)` on a list.

   ```
   WHAT IT SHOULD LOOK LIKE:
   * ITEM ONE    <- bold (first-child)
     item two    ~~ shaded (odd rows striped #f0f0f0)
   * ITEM THREE  ~~ shaded
     item four
   * ITEM FIVE   <- bottom border (last-child)
   (all items dimmed except .active, which stays opaque)
   ```

### Hard
7. `hard/p01-solve.css` — A complete stylesheet using element/class/ID selectors, combinators, pseudo-classes, and grouping. Comment the specificity of each rule.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-- #header (colored bg) -------+
   | Site Name      nav | nav | nav|
   +-------------------------------+
   | ARTICLE                       |
   |  styled paragraphs            |
   |  [CARD: padded + bordered]    |
   |  links change on :hover       |
   +-------------------------------+
   (each CSS rule's specificity noted in a comment)
   ```
8. `hard/p02-solve.css` — Attribute selectors: style `[type="text"]`, `[href^="https"]` (external links), `[href$=".pdf"]` (PDF links), `[disabled]` inputs.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Name: [___________]            <- bordered, padded text input
   https://example.com            <- green  (external link)
   report.pdf                     <- red    (PDF link)
   [___________] disabled input   <- grayed out, not-allowed cursor
   ```
9. `hard/p03-solve.css` — A specificity challenge: write rules that demonstrate class-beats-element, ID-beats-class, and how to override an ID without `!important` (by using a more specific selector).

   ```
   WHAT IT SHOULD LOOK LIKE:
   p          -> element color        (0,0,1)
   p.text     -> class wins           (0,1,0)
   #main      -> ID wins              (1,0,0)
   body #main -> beats the bare ID    (1,0,1) -- no !important needed
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete CSS from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Link the CSS to an HTML file and open in a browser to check styles apply.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
