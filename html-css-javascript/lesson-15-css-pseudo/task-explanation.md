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
2. `easy/p02-solve.html` — Create a zebra-striped list using `:nth-child(even)` and `:nth-child(odd)`. Add a different style for `:first-child` and `:last-child`.
3. `easy/p03-solve.html` — Create a custom list with decorative bullets using `::before` with `content: "→ "` on each `<li>`.

### Medium
4. `medium/p01-solve.html` — Create a pure CSS tooltip: element with `data-tooltip` attribute, `::after` shows the tooltip text on hover using `content: attr(data-tooltip)`. Style and position the tooltip.
5. `medium/p02-solve.html` — Create a styled form: inputs with `:focus` highlight, `:invalid` red border (use `required` and `type="email"`), `:disabled` greyed out, and `:checked` label styling for a checkbox.
6. `medium/p03-solve.html` — Create an article with a drop cap (first letter large using `::first-letter`) and uppercase first line (`::first-line`). Style it like a magazine article.

### Hard
7. `hard/p01-solve.html` — Build a pure CSS accordion/FAQ using `:target`. Clicking a question link (`#faq1`) shows/hides the answer. No JavaScript needed. Use `:target` to show the answer.
8. `hard/p02-solve.html` — Build a custom-styled checkbox and radio button: hide the default input, use `::before`/`::after` on the label to create a custom visual. Use `:checked` to show selected state. Include hover and focus states.
9. `hard/p03-solve.html` — Build a navigation menu with pure CSS effects: hover underline animation (using `::after` with `transform: scaleX(0)` → `scaleX(1)`), active item indicator using `:target` or a class, and a badge on one item using `::after` with `content`.

### How to work
- Write your complete HTML + CSS solution (inline or in `<style>` tags).
- Remove the TODO comment when done.
- Open in browser to test visually.
