# Lesson 01 — Intuition Checks

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
