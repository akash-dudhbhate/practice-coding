# Lesson 01 — Coding Check

Use this to verify your solutions before asking me to review. Open each HTML file in a browser to check it renders correctly.

## Easy

### p01-build-a-table.html
- [ ] Has `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`.
- [ ] 3 columns: Name, Age, City.
- [ ] Header row with `<th>` for each column.
- [ ] 3 data rows.

### p02-build-a-form.html
- [ ] Has `<form>`, `<label>`, `<input>`, `<button>`.
- [ ] Each `<label>` has `for` matching its `<input>`'s `id`.
- [ ] Text input for name, email input for email.
- [ ] Submit button.

### p03-navigation-list.html
- [ ] Has `<nav>`, `<ul>`, `<li>`, `<a>`.
- [ ] 4 links: Home, About, Services, Contact.
- [ ] Each `<a>` has correct `href`.

## Medium

### p01-semantic-blog-post.html
- [ ] Uses `<article>`, `<header>`, `<time>`, `<section>`, `<footer>`.
- [ ] `<time>` has a `datetime` attribute.
- [ ] `<h2>` for post title, `<h3>` for section subheading.

### p02-image-gallery-figures.html
- [ ] 3 `<figure>` elements.
- [ ] Each has `<img>` with `src` and non-empty `alt`.
- [ ] Each has `<figcaption>` with a caption.

### p03-definition-list.html
- [ ] Uses `<dl>`, `<dt>`, `<dd>`.
- [ ] 3 term/definition pairs (HTML, CSS, JS).

## Hard

### p01-accessible-full-page.html
- [ ] Skip link is the first element in `<body>` (href="#main").
- [ ] `<main>` has `id="main"`.
- [ ] `<nav>` has `aria-label="Main navigation"`.
- [ ] `<img>` has meaningful `alt`.
- [ ] Form input has a `<label>`.
- [ ] `<footer>` has `role="contentinfo"`.
- [ ] `<html>` has `lang` attribute.

### p02-nested-article-comments.html
- [ ] Outer `<article>` with `<header>` containing `<h1>`.
- [ ] Comments `<section>` with `<h2>`.
- [ ] 2 nested `<article>` elements for comments.
- [ ] Heading hierarchy: h1 → h2 → h3.

### p03-data-table-semantics.html
- [ ] Has `<caption>`, `<colgroup>`, `<col>`.
- [ ] `<th scope="col">` for column headers.
- [ ] `<tfoot>` with `<th scope="row">` for total row.
- [ ] 4 data rows (Q1-Q4).

## How to verify

Open each file in a browser:
```bash
xdg-open easy/p01-build-a-table.html
```
