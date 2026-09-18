# Lesson 05 — HTML Accessibility Deep Dive

## What you'll learn
- Why accessibility matters and who it's for.
- How to write good `alt` text and use ARIA attributes correctly.
- How to build keyboard-navigable pages with landmarks and skip links.
- How to make forms and tables accessible.
- Color contrast and colorblindness considerations.

## Lesson

Accessibility (a11y) means making your website usable by everyone — including people using screen readers, keyboards only, or with low vision.

### The core principles
1. **Perceivable** — users can see/hear content (alt text, contrast).
2. **Operable** — users can navigate (keyboard, skip links).
3. **Understandable** — content is clear (labels, instructions).
4. **Robust** — works with assistive tech (ARIA, semantic HTML).

### Alt text
```html
<img src="chart.png" alt="Revenue up 40% in Q2" />  <!-- meaningful -->
<img src="spacer.png" alt="" />                      <!-- decorative -->
```

### ARIA
```html
<button aria-label="Close">✕</button>
<div aria-live="polite">Saved!</div>
```
Rule: use native HTML first, ARIA only when HTML isn't enough.

### Landmarks
```html
<header>, <nav aria-label="Main">, <main id="main">, <footer>
```

### Skip link
```html
<a href="#main" class="skip-link">Skip to content</a>
```

### Keyboard focus
- Every interactive element must be reachable by Tab.
- Never use `outline: none` without a `:focus-visible` replacement.
- Use `<button>`/`<a>`, not `<div onclick>`.

### Forms
- Every input has a `<label for="id">`.
- Use `aria-describedby` for hints/errors.
- Use `<fieldset>`/`<legend>` to group related inputs.

### Key rules
- One `<h1>` per page, logical heading order.
- `<html lang="en">` on every page.
- Color contrast ≥ 4.5:1 for text.
- Don't rely on color alone to convey meaning.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete HTML from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.html` — A page with 3 images: one meaningful (with alt), one decorative (empty alt), one that's a link.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ photo ]     <- meaningful img, descriptive alt
   [ border ]    <- decorative img, alt="" (screen readers skip it)
   [ logo -> ]   <- img inside a link; alt = the LINK destination
   Visually they look the same -- the difference is in the alt text.
   ```
2. `easy/p02-solve.html` — A form with 3 labeled inputs, each with `aria-describedby` hints.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Name:    [____________]
            e.g. Jane Doe           <- hint text (aria-describedby)
   Email:   [____________]
            We'll never share it.
   Phone:   [____________]
            Include country code.
   [ Submit ]
   ```
3. `easy/p03-solve.html` — A page with landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`) and `<html lang="en">`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +------------------------------------------+
   | HEADER:  Site title                      |
   | NAV:     Home | About | Contact          |   <- labeled <nav>
   +------------------------------------------+
   | MAIN:    Section heading (h2) + content  |
   +------------------------------------------+
   | FOOTER:  (c) 2026                        |
   +------------------------------------------+
   ```

### Medium
4. `medium/p01-solve.html` — A page with a skip link, proper landmarks, labeled nav, and a heading hierarchy (h1 → h2 → h3).

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE Tab:               AFTER first Tab:
   +---------------------+   +---------------------+
   | Header + nav        |   |[Skip to content]    | <- revealed on focus
   | H1 Heading          |   | Header + nav        |
   |   H2 Section        |   | H1 -> H2 -> H3      |
   |     H3 Subsection   |   |   (clean outline,   |
   +---------------------+   |    no skipped levels)|
                             +---------------------+
   ```
5. `medium/p02-solve.html` — An accessible form with fieldset/legend, required fields, `aria-describedby`, and error messages with `role="alert"`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +- User Form -------------------------------+
   | Name:  [__________]                       |
   | Email: [__________]   * Email is required |  <- error, role="alert"
   |                                         |
   | [ Submit ]                                |
   +-------------------------------------------+
   (empty submit surfaces announced error messages)
   ```
6. `medium/p03-solve.html` — An accessible data table with caption, scope, thead/tbody, and proper structure.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Employee Directory                       <- <caption>
   +-------+-----------+------+
   | Name  | Role      | Dept |   <- <th scope="col"> (bold)
   +-------+-----------+------+
   | Akash | Developer | Eng  |   <- row label: <th scope="row">
   | Sara  | Designer  | UX   |
   +-------+-----------+------+
   ```

### Hard
7. `hard/p01-solve.html` — A full accessible page: skip link, landmarks, labeled nav, accessible form, alt text, heading hierarchy, `lang` attribute, focus-visible styles.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [Skip to content] <- appears on first Tab
   +------------------------------------------+
   | HEADER: title   NAV: Home About(*=curr.) |   <- aria-current style
   +------------------------------------------+
   | MAIN (h1):                               |
   |   [ img with real alt ]                  |
   |   Label: [________]  hint text           |   <- labeled field + hint
   |   [ Button ] <- visible :focus outline   |
   +------------------------------------------+
   | FOOTER                                   |
   +------------------------------------------+
   ```
8. `hard/p02-solve.html` — An accessible custom widget: a toggle button with `aria-expanded`, `aria-controls`, keyboard operability, and a live region for status.

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE click:               AFTER click:
   [v Show details ]           [^ Hide details ]    <- aria-expanded flips
                               +------------------+
                               | Panel content    |   <- hidden -> shown
                               +------------------+
                               Status: "Panel opened" <- live region
   ```
9. `hard/p03-solve.html` — An accessible navigation menu with `aria-label`, `aria-current="page"` for the active link, keyboard focus styles, and a skip link.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [Skip link appears on Tab]
   +--------------------------------------------+
   | *Home*   About   Contact                   |   <- Home bold/underlined
   |  ^-- aria-current="page" visual style      |      (current page)
   +--------------------------------------------+
   Tabbing shows a clear outline on each link.
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- Test with keyboard only (Tab through the whole page).
- When done, tell me and I'll review. Say **"give me next task"** to advance.
