# Lesson 06 — Concepts Explained (CSS Selectors & Specificity)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Element, Class, and ID Selectors

**What:** CSS selectors target HTML elements to style them. The three basic types:

```css
/* Element selector — targets all <p> tags */
p { color: gray; }

/* Class selector — targets elements with class="highlight" */
.highlight { background: yellow; }

/* ID selector — targets the ONE element with id="header" */
#header { font-size: 24px; }
```

```html
<p>Gray text</p>
<p class="highlight">Yellow background</p>
<h1 id="header">Big text</h1>
```

- Element = tag name (`p`, `h1`, `div`).
- Class = `.classname` — reusable, multiple elements can share it.
- ID = `#idname` — unique, only ONE element per page.

**Why it exists:** Without selectors, you can't tell CSS which elements to style. Selectors are how CSS knows what to target.

**Where it's used:** Every CSS rule ever written uses a selector.

**What goes wrong without it:**
- Using IDs for styling → can't reuse styles (IDs must be unique). Use classes for styling, IDs for JS anchors.
- Duplicate IDs on a page → `#id` only styles the first one, HTML is invalid.
- Overusing element selectors → styles every `<p>` on the page when you only wanted one section's paragraphs. Use classes for specificity.

---

## Combinators (descendant, child, sibling)

**What:** Combinators combine selectors to target elements based on their relationships.

```css
/* Descendant — any <p> inside a <div> (any depth) */
div p { color: blue; }

/* Child — <p> that is a DIRECT child of <div> */
div > p { color: red; }

/* Adjacent sibling — <p> right after an <h2> */
h2 + p { margin-top: 0; }

/* General sibling — all <p> that come after <h2> */
h2 ~ p { font-style: italic; }
```

```html
<div>
  <p>Direct child — red</p>
  <span><p>Not direct child — blue (descendant)</p></span>
</div>
<h2>Title</h2>
<p>Right after h2 — margin-top: 0</p>
<p>Also after h2 — italic</p>
```

**Why it exists:** You often need to style elements based on where they are — "paragraphs inside articles," "the paragraph right after a heading." Combinators express these relationships without needing extra classes.

**Where it's used:** Styling nested content, removing top margin from paragraphs after headings, styling list items inside specific sections.

**What goes wrong without it:**
- Adding classes to everything instead of using combinators → bloated HTML, harder to maintain.
- Confusing `div p` (descendant, any depth) with `div > p` (direct child only) → styles apply too broadly or too narrowly.
- Over-nesting combinators (`div div div p`) → brittle, breaks when HTML structure changes slightly.

---

## The Cascade

**What:** The "C" in CSS. When multiple rules target the same element, the cascade decides which one wins based on: importance, specificity, source order.

```css
p { color: blue; }     /* rule 1 */
p { color: red; }      /* rule 2 — same specificity, LATER wins */
```
Result: red (later rule wins when specificity is equal).

```css
p { color: blue; }          /* specificity: 0,0,1 */
.text { color: red; }       /* specificity: 0,1,0 — higher, wins */
```
Result: red (class beats element).

**Why it exists:** Multiple stylesheets and rules always overlap (your CSS, a framework's CSS, browser defaults). The cascade provides a predictable system for resolving conflicts.

**Where it's used:** Every time two rules could apply to the same element — which is almost always.

**What goes wrong without it:**
- `!important` to "win" every conflict → creates a war of `!important`s, unmaintainable. Fix specificity instead.
- Confused why a style isn't applying → usually a higher-specificity rule is overriding it. Use DevTools to find which rule wins.
- Loading order matters — a stylesheet loaded later overrides an earlier one at equal specificity.

---

## Specificity

**What:** Specificity is a score that determines which selector wins when rules conflict. Think of it as four numbers: (inline, ID, class, element).

```css
*              { }  /* 0,0,0,0 — universal */
p              { }  /* 0,0,0,1 — one element */
div p          { }  /* 0,0,0,2 — two elements */
.highlight     { }  /* 0,0,1,0 — one class */
div.highlight  { }  /* 0,0,1,1 — one class + one element */
#header        { }  /* 0,1,0,0 — one ID */
#header p      { }  /* 0,1,0,1 — one ID + one element */
style="..."    { }  /* 1,0,0,0 — inline style */
```

Higher numbers win. Compare left to right: ID beats any number of classes; class beats any number of elements.

**Why it exists:** Without a scoring system, there's no way to decide which rule wins when they conflict. Specificity gives a deterministic answer.

**Where it's used:** Every CSS conflict resolution. Understanding specificity is THE key to not fighting with CSS.

**What goes wrong without it:**
- "Why isn't my style applying?!" → a higher-specificity rule is winning. Check DevTools (struck-through rules are overridden).
- Adding more element selectors to "win" → doesn't help against a single class (0,0,0,5 still loses to 0,0,1,0).
- Using IDs for styling → very high specificity (0,1,0,0), hard to override without more IDs or `!important`. Prefer classes.
- `!important` → breaks the cascade, should be avoided except for genuine overrides of third-party code.

---

## Pseudo-class Selectors

**What:** Pseudo-classes target elements in a specific STATE (hover, focus, first-child, etc.), selected with `:`.

```css
a:hover { color: red; }           /* link being hovered */
input:focus { border-color: blue; } /* input being typed in */
li:first-child { font-weight: bold; }  /* first <li> in a list */
li:nth-child(odd) { background: #eee; } /* every odd item */
li:not(.active) { opacity: 0.5; }  /* all <li> except .active */
```

**Why it exists:** Some styles depend on state or position — a hovered button, the first item in a list, every other row in a table. Pseudo-classes let you target these without adding extra classes to the HTML.

**Where it's used:** Hover/focus effects, zebra-striped tables, first/last item styling, form field validation states.

**What goes wrong without it:**
- Adding JS to toggle a "hover" class → unnecessary; `:hover` does it for free.
- `:nth-child(n)` vs `:nth-of-type(n)` → `nth-child` counts ALL siblings; `nth-of-type` counts only same-type siblings. Mixing them up gives wrong targets.
- `:hover` on mobile → no hover on touch devices; always pair hover with `:focus` for keyboard/touch users.

---

## Attribute Selectors

**What:** Attribute selectors target elements based on their HTML attributes.

```css
/* Has the attribute at all */
[disabled] { opacity: 0.5; }

/* Attribute equals exact value */
[type="text"] { border: 1px solid gray; }

/* Attribute starts with */
[href^="https"] { color: green; }

/* Attribute ends with */
[href$=".pdf"] { color: red; }

/* Attribute contains */
[class*="button"] { cursor: pointer; }
```

**Why it exists:** Sometimes the best way to target elements is by their attributes, not by adding classes — e.g., styling all external links, all PDF links, all disabled inputs.

**Where it's used:** Styling links by type (external, PDF, mailto), form inputs by type, elements with specific data attributes.

**What goes wrong without it:**
- Adding classes to every external link instead of `[href^="http"]` → tedious, easy to miss new links.
- Case sensitivity → `[type="Text"]` won't match `type="text"`. Use `[type="text" i]` for case-insensitive (the `i` flag).
- Overusing attribute selectors when a class would be clearer → hurts readability.

---

## Grouping Selectors

**What:** You can apply the same styles to multiple selectors with a comma.

```css
h1, h2, h3 {
  font-family: Arial, sans-serif;
  color: #333;
}

.button, .btn, .cta {
  padding: 10px 20px;
  cursor: pointer;
}
```

**Why it exists:** Without grouping, you'd repeat the same rule block for each selector. Grouping keeps CSS DRY (Don't Repeat Yourself).

**Where it's used:** Shared styles across multiple element types or classes.

**What goes wrong without it:**
- Copy-pasting the same rule for each selector → if you change one, you must change all. Grouping keeps them in sync.
- Comma with a missing selector (`.btn, .button,`) → the trailing comma can cause the next rule to be ignored in some older browsers. Avoid trailing commas.

---

## Universal Selector and Inheritance

**What:** The `*` selector matches every element. Some CSS properties inherit (pass from parent to child) automatically.

```css
/* Reset all margins */
* { margin: 0; }

/* Box-sizing reset */
*, *::before, *::after { box-sizing: border-box; }

/* Inherited properties: color, font-family, font-size, line-height */
body { color: #333; font-family: Arial; }
/* All children inherit color and font-family from body */
```

- **Inherited:** `color`, `font-family`, `font-size`, `line-height`, `text-align`, `visibility`.
- **NOT inherited:** `margin`, `padding`, `border`, `width`, `height`, `background`.

**Why it exists:** The universal selector is useful for resets. Inheritance saves you from setting `font-family` on every single element — set it on `<body>` and children inherit it.

**Where it's used:** CSS resets (`* { margin: 0; box-sizing: border-box; }`), setting base font/color on `body`.

**What goes wrong without it:**
- `* { margin: 0; }` without understanding → removes all spacing, layout looks cramped. Pair with intentional spacing.
- Assuming `border` inherits → it doesn't; children don't get the parent's border.
- `*` selector has zero specificity (0,0,0,0) → easily overridden by anything, which is usually what you want in a reset.
