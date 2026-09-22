# lesson-01-html-structure — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Block vs Inline
Is `<span>` block or inline? Is `<div>` block or inline?
<details><summary>Answer</summary>
`<span>` is inline (doesn't break line). `<div>` is block (takes full width, breaks line).
</details>

## Check 02: Semantic Tags
Why use `<nav>` instead of `<div class="nav">`?
<details><summary>Answer</summary>
Semantic tags convey meaning to screen readers, search engines, and developers. `<nav>` = navigation, `<header>` = header, `<main>` = main content. Improves accessibility and SEO.
</details>

## Check 03: Self-closing Tags
Which of these need a closing tag: `<img>`, `<br>`, `<p>`, `<input>`?
<details><summary>Answer</summary>
- `<img>`, `<br>`, `<input>` — void elements, self-closing (no closing tag needed)
- `<p>` — needs `</p>`
</details>

## Check 04: Attributes
```html
<a href="https://example.com" target="_blank">Link</a>
```
What does `target="_blank"` do?
<details><summary>Answer</summary>
Opens the link in a new tab/window. Add `rel="noopener noreferrer"` for security (prevents the new page from accessing `window.opener`).
</details>

## Check 05: HTML vs XHTML
Why is `<br>` valid in HTML5 but `<br />` was required in XHTML?
<details><summary>Answer</summary>
HTML5 allows void elements without `/`. XHTML required self-closing syntax. HTML5 is more lenient.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Unclosed Tag
```html
<div>
  <p>Hello world
</div>
```
<details><summary>Answer</summary>
**Bug:** `<p>` is never closed. Browsers auto-close it, but it's invalid HTML.
**Fix:** `<p>Hello world</p>`.
</details>

## Debug 02 (Medium): Wrong Heading Hierarchy
```html
<h1>Title</h1>
<h3>Subtitle</h3>
<h2>Section</h2>
```
<details><summary>Answer</summary>
**Bug:** Skips h2 before h3. Bad for accessibility and SEO.
**Fix:** Use h1 → h2 → h3 in order. Don't skip levels.
</details>

## Debug 03 (Hard): Missing DOCTYPE
```html
<html>
<head><title>Test</title></head>
<body>Hello</body>
</html>
```
<details><summary>Answer</summary>
**Bug:** No `<!DOCTYPE html>`. Browser may render in quirks mode (inconsistent behavior).
**Fix:** Add `<!DOCTYPE html>` as the first line.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using `<div>` for everything
```html
<!-- WRONG — no semantics -->
<div class="header">...</div>
<div class="nav">...</div>

<!-- CORRECT — semantic HTML -->
<header>...</header>
<nav>...</nav>
```

## Mistake 02: Skipping heading levels
```html
<!-- WRONG -->
<h1>Title</h1>
<h4>Subtitle</h4>

<!-- CORRECT -->
<h1>Title</h1>
<h2>Subtitle</h2>
```

## Mistake 03: Missing alt text
```html
<!-- WRONG — accessibility failure -->
<img src="logo.png">

<!-- CORRECT -->
<img src="logo.png" alt="Company Logo">
```

## Mistake 04: Using `<br>` for spacing
```html
<!-- WRONG -->
<p>Line 1<br><br><br>Line 2</p>

<!-- CORRECT — use CSS margin -->
<p>Line 1</p>
<p>Line 2</p>
```

## Mistake 05: Inline styles
```html
<!-- WRONG -->
<div style="color: red; font-size: 20px;">

<!-- CORRECT — use CSS classes -->
<div class="error">
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Div Soup
### Before
```html
<div class="header"><div class="nav">...</div></div>
<div class="main"><div class="article">...</div></div>
<div class="footer">...</div>
```
### After
```html
<header><nav>...</nav></header>
<main><article>...</article></main>
<footer>...</footer>
```

## Refactor 02 (Medium): Inline Styles
### Before
```html
<p style="color: red; font-size: 18px; margin: 10px;">Text</p>
```
### After
```html
<p class="warning">Text</p>
<style>.warning { color: red; font-size: 18px; margin: 10px; }</style>
```

## Refactor 03 (Hard): No Semantic Structure
### Before
```html
<div id="page">
  <div id="top"><div class="links">...</div></div>
  <div id="content"><div class="post">...</div></div>
</div>
```
### After
```html
<body>
  <header><nav>...</nav></header>
  <main><article>...</article></main>
</body>

---

## Approach Comparison — different ways to solve it

## Problem: Page Layout Structure

### Approach 1: Div soup
```html
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">...</div>
<div class="footer">...</div>
```
**Cons:** No semantic meaning. Bad for accessibility/SEO.

### Approach 2: Semantic HTML5
```html
<header>
  <nav>...</nav>
</header>
<main>...</main>
<footer>...</footer>
```
**Pros:** Meaningful, accessible, better SEO.

**Winner:** Approach 2 — always use semantic HTML5 tags.

---

## Problem: Image with Caption

### Approach 1: Div wrapper
```html
<div class="figure">
  <img src="photo.jpg" alt="Sunset">
  <p class="caption">A beautiful sunset</p>
</div>
```

### Approach 2: figure/figcaption
```html
<figure>
  <img src="photo.jpg" alt="Sunset">
  <figcaption>A beautiful sunset</figcaption>
</figure>
```

**Winner:** Approach 2 — semantic, built for this exact use case.
