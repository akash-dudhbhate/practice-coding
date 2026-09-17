# lesson-05-html-accessibility — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Tab order
What determines tab order?
<details><summary>Answer</summary>
DOM order by default. Use `tabindex` to modify: `tabindex="0"` makes focusable, `tabindex="-1"` removes from tab flow, positive values are discouraged.
</details>

## Check 02: ARIA roles
When should you use ARIA?
<details><summary>Answer</summary>
Only when HTML doesn't provide the semantics you need. "No ARIA is better than bad ARIA." Use `<button>` not `<div role="button">`.
</details>

## Check 03: Color contrast
What's the minimum contrast ratio for normal text (WCAG AA)?
<details><summary>Answer</summary>
4.5:1 for normal text, 3:1 for large text. Use a contrast checker.
</details>

## Check 04: Focus indicator
Why must you never remove `outline` without replacing it?
<details><summary>Answer</summary>
Keyboard users need a visible focus indicator to know where they are. If you remove `outline: none`, provide an alternative focus style.
</details>

## Check 05: Screen reader testing
How do you test with a screen reader?
<details><summary>Answer</summary>
- NVDA (Windows, free)
- VoiceOver (macOS/iOS, built-in)
- JAWS (Windows, paid)
Test at least with one. Don't rely on visual testing alone.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Non-descriptive Link
```html
<a href="/page">Click here</a>
```
<details><summary>Answer</summary>
**Bug:** "Click here" doesn't describe the destination. Screen reader users scanning links hear "click here, click here, click here".
**Fix:** `<a href="/page">Read our privacy policy</a>`.
</details>

## Debug 02 (Medium): Missing ARIA
```html
<div onclick="toggle()">Menu</div>
```
<details><summary>Answer</summary>
**Bug:** Div with onclick isn't keyboard accessible or announced as interactive.
**Fix:** `<button onclick="toggle()" aria-expanded="false">Menu</button>`.
</details>

## Debug 03 (Hard): Missing skip link
```html
<body>
  <nav>...long navigation...</nav>
  <main>Content</main>
</body>
```
<details><summary>Answer</summary>
**Bug:** No skip link — keyboard users must tab through entire nav to reach content.
**Fix:** `<a href="#main" class="skip-link">Skip to content</a>` at the top.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: "Click here" links
```html
<!-- WRONG -->
<a href="/page">Click here</a>
<!-- CORRECT -->
<a href="/page">Read the documentation</a>
```

## Mistake 02: Div as button
```html
<!-- WRONG -->
<div onclick="submit()">Submit</div>
<!-- CORRECT -->
<button onclick="submit()">Submit</button>
```

## Mistake 03: Removing focus outline
```html
/* WRONG */
* { outline: none; }
/* CORRECT — provide alternative */
*:focus { outline: 2px solid blue; }
```

## Mistake 04: No skip link
```html
<!-- Add at top of body -->
<a href="#main" class="skip-link">Skip to main content</a>
```

## Mistake 05: Low contrast
```html
<!-- WRONG — light gray on white -->
<p style="color: #ccc;">Text</p>
<!-- CORRECT — sufficient contrast -->
<p style="color: #333;">Text</p>
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Fixed Pixel Widths
### Before
```css
.container { width: 1200px; }
```
### After
```css
.container { max-width: 1200px; width: 100%; }
```

## Refactor 02 (Medium): Many Media Queries
### Before
```css
@media (max-width: 1200px) { .grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 900px) { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px) { .grid { grid-template-columns: 1fr; } }
```
### After
```css
.grid { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
```

## Refactor 03 (Hard): Device-Specific Breakpoints
### Before
```css
@media (max-width: 768px) { /* iPad */ }
@media (max-width: 414px) { /* iPhone */ }
```
### After
```css
/* Content-based breakpoints, not device-based */
@media (max-width: 600px) { /* content needs 1 col */ }

---

## Approach Comparison — different ways to solve it

## Problem: Interactive Menu

### Approach 1: Div with onclick
```html
<div onclick="toggleMenu()" class="menu">Menu</div>
```
**Cons:** Not keyboard accessible, not announced as interactive.

### Approach 2: Button with ARIA
```html
<button onclick="toggleMenu()" aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" role="menu">...</ul>
```
**Pros:** Keyboard accessible, screen reader friendly.

**Winner:** Approach 2 — always use semantic HTML + ARIA when needed.

---

## Problem: Form Error Messages

### Approach 1: Visual only
```html
<input type="text" class="error">
<span class="error-text">Required</span>
```

### Approach 2: ARIA live
```html
<input type="text" aria-invalid="true" aria-describedby="error">
<span id="error" role="alert">Required</span>
```

**Winner:** Approach 2 — screen readers announce the error.
