# Lesson 15 — Concepts Explained (CSS Pseudo-classes & Pseudo-elements)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Pseudo-classes vs Pseudo-elements

**What:**
- **Pseudo-class** (`:`) — selects elements in a specific STATE (hover, focus, first-child).
- **Pseudo-element** (`::`) — selects a specific PART of an element (first letter, before, after).

```css
/* Pseudo-class: selects .button WHEN hovered */
.button:hover { background: darkblue; }

/* Pseudo-element: selects the FIRST LETTER of .article */
.article::first-letter { font-size: 3em; }
```

**Why it exists:** Without pseudo-classes, you'd need JS to detect hover/focus and add classes. Without pseudo-elements, you'd add extra `<span>` elements for things like the first letter or decorative content.

**Where it's used:** Every interactive element (hover, focus), form states (checked, disabled), structural selection (first-child, nth-child), decorative content (::before, ::after).

**What goes wrong without it:**
- `:` vs `::`: pseudo-elements use `::` (double colon) in modern CSS. `:before` works (old syntax) but `::before` is correct. Pseudo-classes always use `:` (single).
- Confusing the two: `:hover` is a state (pseudo-class), `::before` is a part (pseudo-element). Can't have `::hover`.

---

## :hover, :focus, :active

**What:** Interactive state pseudo-classes.

```css
.button:hover { background: darkblue; }     /* mouse is over it */
.button:focus { outline: 2px solid blue; }  /* has keyboard focus */
.button:active { transform: scale(0.95); }  /* being clicked (mouse down) */
```

**Why it exists:** Without these, you'd need JS to detect mouse position, focus state, and click state → add/remove classes → complex. CSS pseudo-classes handle it natively.

**Where it's used:** Every interactive element — buttons, links, inputs, cards.

**What goes wrong without it:**
- `:focus` without `:focus-visible` → focus outline shows on mouse click too → ugly. Use `:focus-visible` for keyboard-only focus styles.
- Order matters: `:link → :visited → :hover → :active` (LVHA). Wrong order → hover doesn't work on visited links.
- Touch devices: `:hover` triggers on tap → "sticky hover" → element stays in hover state. Use `@media (hover: hover)` to apply hover only on devices that support it.

---

## :nth-child()

**What:** Select elements by their position among siblings.

```css
/* Every 2nd child */
li:nth-child(2) { color: red; }          /* 2nd item */
li:nth-child(even) { background: #f0f0f0; }  /* even items (zebra stripe) */
li:nth-child(odd) { background: #fff; }      /* odd items */
li:nth-child(3n+1) { color: blue; }          /* 1st, 4th, 7th, 10th... */

/* First and last */
li:first-child { font-weight: bold; }
li:last-child { border-bottom: none; }
```

**Why it exists:** Without `:nth-child`, you'd add classes manually (`<li class="even">`) or use JS. `:nth-child` handles zebra striping, grid layouts, and positional styling in pure CSS.

**Where it's used:** Zebra-striped tables, alternating card backgrounds, grid item positioning, "first item is special" patterns.

**What goes wrong without it:**
- `:nth-child(2)` selects the 2nd child, NOT the 2nd matching element. If children are mixed types (divs and spans), it counts ALL children.
- `3n+1` formula: `n` starts at 0. So `3(0)+1=1`, `3(1)+1=4`, `3(2)+1=7` → 1st, 4th, 7th. Understand the formula.
- `:nth-child` vs `:nth-of-type`: `nth-of-type` counts only same-type siblings. `li:nth-of-type(2)` = 2nd `<li>`, ignoring other elements.

---

## :first-child, :last-child, :only-child

**What:** Select elements based on their position in the parent.

```css
li:first-child { border-top: none; }      /* first item — no top border */
li:last-child { border-bottom: none; }    /* last item — no bottom border */
div:only-child { width: 100%; }           /* only child — full width */
```

**Why it exists:** Without these, you'd add classes like `<li class="first">` manually. These pseudo-classes handle edge cases automatically — first item has no top separator, last item has no bottom separator.

**Where it's used:** Menu items (remove border from first/last), grid items (first item spans wider), conditional layouts.

**What goes wrong without it:**
- `:first-child` → element must be the FIRST child of its parent. If there's a hidden element before it, it's not the first child.
- `:only-child` → element has NO siblings. If you add a second element, it's no longer `:only-child` → styles change → surprising.
- `:first-of-type` vs `:first-child`: `p:first-child` → `<p>` that is also the first child. `p:first-of-type` → first `<p>` among siblings (might not be the first child).

---

## ::before and ::after

**What:** Insert content before or after an element via CSS (no HTML change needed).

```css
/* Add a decorative arrow before links */
a::before {
    content: "→ ";
}

/* Add a clear-fix after floated elements */
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}

/* Tooltip using ::after */
.tooltip::after {
    content: attr(data-tooltip);   /* use HTML attribute value */
    position: absolute;
    background: black;
    color: white;
    padding: 4px 8px;
    opacity: 0;
    transition: opacity 0.3s;
}
.tooltip:hover::after {
    opacity: 1;
}
```

**Why it exists:** Without `::before`/`::after`, you'd add `<span>` elements for decorative content → cluttered HTML. These pseudo-elements add visual content without modifying HTML.

**Where it's used:** Icons before links, tooltips, badges, decorative shapes, clearfix, quotes, custom list bullets.

**What goes wrong without it:**
- `content` is REQUIRED. Without `content: ""`, the pseudo-element doesn't appear. Even an empty string is needed.
- `::before`/`::after` are inline by default. Set `display: block` or `position: absolute` for positioning.
- `content: attr(data-tooltip)` → reads the `data-tooltip` attribute from the element. Powerful for tooltips, but the attribute must exist.
- Pseudo-elements can't have children or be selected by JS → they're CSS-only, not real DOM elements.

---

## ::first-letter, ::first-line

**What:** Style the first letter or first line of text.

```css
.article::first-letter {
    font-size: 3em;
    float: left;
    line-height: 1;
    margin-right: 8px;
    font-weight: bold;
}

.article::first-line {
    text-transform: uppercase;
    letter-spacing: 2px;
}
```

**Why it exists:** Without these, you'd wrap the first letter in a `<span>` manually → tedious, breaks if text changes. `::first-letter` does it automatically → magazine-style drop caps.

**Where it's used:** Articles, blog posts, book-style typography, decorative first lines.

**What goes wrong without it:**
- `::first-letter` only works on block-level elements. On inline elements → no effect.
- "First letter" includes punctuation before the letter: `"Hello"` → the `"` is part of the first letter.
- `::first-line` responds to viewport width — as you resize, what counts as "first line" changes → the styling adjusts automatically.

---

## :not()

**What:** Select elements that do NOT match a selector.

```css
/* All inputs except checkboxes and radios */
input:not([type="checkbox"]):not([type="radio"]) {
    padding: 8px;
    border: 1px solid #ccc;
}

/* All list items except the last */
li:not(:last-child) {
    border-bottom: 1px solid #ccc;
}

/* All buttons except disabled */
button:not(:disabled) {
    cursor: pointer;
}
```

**Why it exists:** Without `:not()`, you'd add a class to every element that should be excluded → tedious. `:not()` lets you exclude elements in CSS → cleaner, no HTML changes.

**Where it's used:** Form styling (exclude checkboxes), list separators (exclude last item), conditional styles (exclude disabled).

**What goes wrong without it:**
- `:not()` has low specificity (0,0,1) → easily overridden. Don't rely on it for important exclusions.
- Complex `:not()` chains → `:not(.a):not(.b):not(.c)` → hard to read. Consider a different approach.
- `:not(*)` → matches nothing (everything is excluded). Don't do this.

---

## :checked, :disabled, :valid, :invalid

**What:** Form state pseudo-classes.

```css
/* Checked checkbox/radio */
input:checked + label { font-weight: bold; }

/* Disabled inputs */
input:disabled { opacity: 0.5; cursor: not-allowed; }

/* Valid/invalid form fields */
input:valid { border-color: green; }
input:invalid { border-color: red; }

/* Focus within a form */
form:focus-within { background: #f8f8ff; }
```

**Why it exists:** Without these, you'd use JS to check form state and add classes. These pseudo-classes handle form state in pure CSS → validation feedback, disabled styling, checked state.

**Where it's used:** Form styling, validation feedback, custom checkboxes/radios, disabled states.

**What goes wrong without it:**
- `:checked` only works on `<input type="checkbox">` and `<input type="radio">`. Not on `<select>`.
- `:valid`/`:invalid` depends on HTML validation attributes (`required`, `type="email"`, `pattern`). Without these attributes, all inputs are valid.
- `:focus-within` → matches an element that CONTAINS a focused element. Great for highlighting a form when any field is focused.

---

## :target

**What:** Select the element that matches the URL fragment (#id).

```css
/* URL: example.com/page#section2 */
#section2:target {
    background: yellow;
    animation: highlight 2s;
}

/* Smooth scroll to target */
html { scroll-behavior: smooth; }
```

**Why it exists:** Without `:target`, you'd need JS to detect URL hash changes and highlight sections. `:target` does it in CSS → great for FAQ pages, documentation, anchor links.

**Where it's used:** FAQ sections, documentation anchors, tab content (pure CSS tabs), highlight on navigation.

**What goes wrong without it:**
- `:target` only activates when the URL has `#id`. Without the hash → no match → no style.
- Multiple elements with the same ID → invalid HTML → `:target` may behave unexpectedly.
- `:target` persists until the URL hash changes → the highlight stays until user clicks another anchor.
