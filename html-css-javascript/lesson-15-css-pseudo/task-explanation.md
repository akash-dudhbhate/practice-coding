# Lesson 15 — CSS Pseudo-classes & Pseudo-elements

## What you'll learn
- Pseudo-class vs pseudo-element (: vs ::)
- :hover, :focus, :active, :focus-visible
- :nth-child(), :first-child, :last-child, :only-child
- ::before and ::after (content insertion)
- ::first-letter, ::first-line
- :not() (negation)
- :checked, :disabled, :valid, :invalid (form states)
- :target (URL fragment matching)

## Lesson

### Interactive states
```css
.btn:hover { background: darkblue; }
.btn:focus-visible { outline: 2px solid blue; }
.btn:active { transform: scale(0.95); }
```

### Decorative content
```css
.link::before { content: "→ "; }
.tooltip::after { content: attr(data-tip); }
```

### Structural selection
```css
li:nth-child(even) { background: #f0f0f0; }
li:not(:last-child) { border-bottom: 1px solid #ccc; }
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create 3 links with different hover effects: one changes color, one underlines, one scales up. Use `:hover` and `transition`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Link one      <- changes color on hover
   Link two      <- an underline appears on hover
   Link three    <- grows slightly bigger on hover
   ```
2. `easy/p02-solve.html` — Create a zebra-striped list using `:nth-child(even)` and `:nth-child(odd)`. Add a different style for `:first-child` and `:last-child`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   * item 1    <- first-child stands out (e.g. bold)
     item 2    ~~ shaded (even rows striped)
   * item 3
     item 4    ~~ shaded
   * item 5    <- last-child stands out (e.g. border)
   ```
3. `easy/p03-solve.html` — Create a custom list with decorative bullets using `::before` with `content: "→ "` on each `<li>`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   -> First item
   -> Second item     <- every <li> prefixed by a colored arrow
   -> Third item         via ::before (no default bullet dots)
   ```

### Medium
4. `medium/p01-solve.html` — Create a pure CSS tooltip: element with `data-tooltip` attribute, `::after` shows the tooltip text on hover using `content: attr(data-tooltip)`. Style and position the tooltip.

   ```
   WHAT IT SHOULD LOOK LIKE:
                       +----------------+
   Hover the text -->  | tooltip text   |   <- ::after bubble fades in
                       +----------------+
   some marked text    <- its content comes from data-tooltip
   ```
5. `medium/p02-solve.html` — Create a styled form: inputs with `:focus` highlight, `:invalid` red border (use `required` and `type="email"`), `:disabled` greyed out, and `:checked` label styling for a checkbox.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Name:  [___________]   <- glows / highlights on :focus
   Email: [bad-email  ]   <- red border while :invalid
   Other: [___________]   <- grayed out when :disabled
   [x] I agree            <- label highlights when :checked
   ```
6. `medium/p03-solve.html` — Create an article with a drop cap (first letter large using `::first-letter`) and uppercase first line (`::first-line`). Style it like a magazine article.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-- W --+  HEN THE FIRST LETTER OF AN ARTICLE
   |       |  is oversized (drop cap via ::first-letter)
   +-------+  and the whole opening line renders in
   capitals (::first-line), magazine-style, before
   the paragraph settles into normal body text.
   ```

### Hard
7. `hard/p01-solve.html` — Build a pure CSS accordion/FAQ using `:target`. Clicking a question link (`#faq1`) shows/hides the answer. No JavaScript needed. Use `:target` to show the answer.

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE:                      AFTER clicking question 2:
   > Question one?              > Question one?
   > Question two?              > Question two?
   > Question three?              Answer revealed here.
                                  > Question three?
   (URL #fragment does the work -- zero JavaScript)
   ```
8. `hard/p02-solve.html` — Build a custom-styled checkbox and radio button: hide the default input, use `::before`/`::after` on the label to create a custom visual. Use `:checked` to show selected state. Include hover and focus states.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ ] Option A      <- empty custom box (::before square)
   [x] Option B      <- checked: filled / ticked box
   ( ) Choice 1      <- empty custom circle (radio)
   (*) Choice 2      <- checked: dot inside circle
   (real inputs hidden; the label shows the state)
   ```
9. `hard/p03-solve.html` — Build a navigation menu with pure CSS effects: hover underline animation (using `::after` with `transform: scaleX(0)` → `scaleX(1)`), active item indicator using `:target` or a class, and a badge on one item using `::after` with `content`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Home    About    Messages(3)    Contact
   -----                ^-- red '3' badge via ::after
    ^-- underline grows on hover (scaleX 0 -> 1);
        the active/target item keeps its underline
   ```

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Open in browser to test visually.
