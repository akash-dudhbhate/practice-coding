# Lesson 06 — Coding Check

Use this to verify your solutions before asking me to review. Link your CSS to an HTML file and open in a browser to check styles apply.

## Easy

### p01-solve.css (Basic selectors)
- [ ] `p` selector sets `color: gray` (or similar).
- [ ] `h1` selector sets `color: blue` (or similar).
- [ ] `.highlight` class sets `background: yellow` (or similar).
- [ ] All three rules use correct syntax (selector, braces, property: value).
- [ ] Test: a `<p class="highlight">` shows yellow background (class wins over element).

### p02-solve.css (Link states and button class)
- [ ] `a` default state styled (e.g. `color: blue`).
- [ ] `a:hover` styled (e.g. `color: red`).
- [ ] `a:focus` has underline (or visible focus style).
- [ ] `.btn` class has `padding` and `cursor: pointer`.
- [ ] Test: hovering a link changes its color; tabbing to it shows focus style.

### p03-solve.css (Grouping and ID selector)
- [ ] `h1, h2, h3` grouped with shared `font-family` and `color`.
- [ ] `#main-title` has a different style (e.g. larger font-size, different color).
- [ ] `#main-title` overrides the grouped `h1` rule (ID specificity 0,1,0,0 beats element 0,0,0,1).
- [ ] Test: the element with `id="main-title"` looks different from other `h1`s.

## Medium

### p01-solve.css (Combinators)
- [ ] `article p` styles paragraphs inside articles (descendant).
- [ ] `ul > li` styles direct-child list items (child combinator).
- [ ] `h2 + p` styles the paragraph immediately after an h2 (adjacent sibling).
- [ ] Each combinator uses the correct symbol (space, `>`, `+`).
- [ ] Test: nested paragraphs are styled; the paragraph right after h2 has the adjacent style.

### p02-solve.css (Specificity demonstration)
- [ ] Has an element-level rule (e.g. `p { color: blue; }`).
- [ ] Has a class-level rule (e.g. `.text { color: green; }`).
- [ ] Has an ID-level rule (e.g. `#special { color: red; }`).
- [ ] Comments explain which rule wins and why (ID > class > element).
- [ ] Test: an element with all three (id, class, element) shows the ID color.

### p03-solve.css (Pseudo-classes on a list)
- [ ] `li:first-child` styled (e.g. bold).
- [ ] `li:last-child` styled (e.g. no bottom border).
- [ ] `li:nth-child(odd)` styled (e.g. background color for zebra striping).
- [ ] `li:not(.active)` styled (e.g. reduced opacity).
- [ ] Test: first item is bold, last item has no bottom border, odd items have background, `.active` item is full opacity.

## Hard

### p01-solve.css (Complete stylesheet)
- [ ] Uses element selectors (e.g. `body`, `p`, `a`).
- [ ] Uses class selectors (e.g. `.card`, `.btn`).
- [ ] Uses at least one ID selector.
- [ ] Uses at least one combinator (descendant or child).
- [ ] Uses at least one pseudo-class (`:hover` or `:first-child`).
- [ ] Uses grouping (`h1, h2, h3 { }`).
- [ ] Comments show the specificity score of at least 3 rules.
- [ ] Test: all styles apply correctly in the browser.

### p02-solve.css (Attribute selectors)
- [ ] `[type="text"]` styles text inputs (e.g. border, padding).
- [ ] `[href^="https"]` styles external links (e.g. green color).
- [ ] `[href$=".pdf"]` styles PDF links (e.g. red color or icon).
- [ ] `[disabled]` styles disabled inputs (e.g. opacity 0.5).
- [ ] Test: external links are green, PDF links are red, disabled inputs are faded.

### p03-solve.css (Specificity challenge)
- [ ] Has a rule with element-only specificity (0,0,0,n).
- [ ] Has a rule with class specificity (0,0,n,0) that overrides the element rule.
- [ ] Has a rule with ID specificity (0,n,0,0) that overrides the class rule.
- [ ] Has a rule that overrides the ID WITHOUT `!important` (e.g. `#parent #child` or a more specific ID selector).
- [ ] No use of `!important` anywhere.
- [ ] Comments explain each override and its specificity score.
- [ ] Test: the final winning style is the one predicted by specificity, not `!important`.

## How to verify

Create a test HTML file that links your CSS:
```html
<link rel="stylesheet" href="easy/p01-solve.css" />
```
- Open in a browser and check styles apply.
- Use DevTools (F12) → Elements tab → click an element → see which rules apply and which are struck through (overridden).
- For specificity: confirm the winning rule matches your prediction in the comments.
- For pseudo-classes: hover/focus elements to test `:hover`/`:focus`; check list items for `:first-child`/`:nth-child`.
