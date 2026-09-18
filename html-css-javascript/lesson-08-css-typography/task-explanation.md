# Lesson 08 — CSS Text & Typography

> Content to be filled in.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete CSS from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-font-family-stacks.css` — Assign font stacks: sans-serif body text, serif headings, monospace code.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Serif Heading (Georgia)         <- h1 in a serif stack
   Body text in Helvetica/Arial    <- body in a sans-serif stack
   const x = 1;                    <- code in a monospace stack
   ```
2. `easy/p02-rem-font-sizes.css` — Build a rem size scale on a 16px root: 2rem h1, 1.5rem h2, 1rem body, 0.875rem small.

   ```
   WHAT IT SHOULD LOOK LIKE:
   HUGE Heading (2rem = 32px)
   Smaller heading (1.5rem = 24px)
   Body text (1rem = 16px)
   small print (0.875rem = 14px)   <- whole scale shifts if root
                                      font-size changes
   ```
3. `easy/p03-line-height-align.css` — Control line-height (1.5 paragraphs, 1.2 heading) and text-align (centered h1, right-aligned date).

   ```
   WHAT IT SHOULD LOOK LIKE:
            Centered Heading        <- h1 text-align: center
   Paragraph lines have relaxed
   spacing between them (1.5).
                        Jan 1, 2026 <- .date right-aligned
   ```

### Medium
4. `medium/p01-weight-style.css` — Use font-weight 700/400/300 and italics: bold headings + strong, italic em, light italic caption.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Bold Heading (weight 700)
   Normal-weight paragraph with an *italic* word and bold strong text.
   light italic caption text       <- .caption: weight 300 + italic
   ```
5. `medium/p02-text-decoration-links.css` — Style text-decoration: underlined links lose the underline on hover, clean nav links, line-through `.done` items.

   ```
   WHAT IT SHOULD LOOK LIKE:
   a normal underlined link        <- underline, removed on :hover
   Home   About   Contact          <- nav links: never underlined
   [x] ~~finished task~~           <- .done struck through
   [ ] pending task
   ```
6. `medium/p03-spacing-transform.css` — Use letter-spacing and text-transform: uppercase tracked headings/buttons, capitalize a label, force lowercase.

   ```
   WHAT IT SHOULD LOOK LIKE:
   W I D E   H E A D I N G         <- h1: uppercase + letter-spacing
   [ B U T T O N ]                 <- .btn: uppercase, wide tracking
   A Label Like This               <- .label: capitalize
   shout becomes quiet             <- .lower: forced lowercase
   ```

### Hard
7. `hard/p01-typography-stylesheet.css` — A complete type system: rem heading scale (2.5/1.75/1.25rem), 1.6 line-height, styled links, `.small`/`.caption` utilities.

   ```
   WHAT IT SHOULD LOOK LIKE:
   LARGE BOLD TITLE (2.5rem)
   Medium heading (1.75rem)
   Small heading (1.25rem)
   Comfortable 1.6 line-height paragraphs; blue, non-underlined
   links that underline on hover; plus .small / .caption utility
   text -- the whole type system lives in one stylesheet.
   ```
8. `hard/p02-text-shadow-hero.css` — Keep white hero text readable over a busy background with text-shadow, plus a `.glow` accent class.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +------------------------------------------+
   |  ~~ busy / colorful background ~~~~~~    |
   |   BIG WHITE TITLE w/ drop shadow         |   <- readable via
   |   white subtitle w/ subtle shadow        |      text-shadow
   |   glowing cyan accent text               |   <- .glow
   +------------------------------------------+
   ```
9. `hard/p03-typography-system-variables.css` — Tokenize the type system with CSS variables (--font-body, --font-heading, --color-text, --color-link) plus `.lead`/`.caption`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   BOLD UPPERCASE TITLE            <- var(--font-heading)
   Body text in var(--font-body), var(--color-text), 1.6 height.
   Lead paragraph renders larger + muted.   Links in var(--color-link).
   (small italic muted caption)
   (re-theme the whole page by editing ~4 :root variables)
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete CSS from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Link the CSS to an HTML file and open in a browser to check the styles.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
