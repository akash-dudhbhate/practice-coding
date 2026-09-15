# Lesson 01 — HTML Structure & Semantic Tags

## What you'll learn
- How an HTML document is structured.
- The difference between structural tags and **semantic** tags.
- Why semantics matter for accessibility and SEO.

## Lesson

Every web page is an HTML document. The browser reads tags (elements) to understand what each piece of content is.

### The skeleton
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Page Title</title>
  </head>
  <body>
    <!-- visible content goes here -->
  </body>
</html>
```
- `<!DOCTYPE html>` tells the browser this is HTML5.
- `<head>` holds metadata (not visible).
- `<body>` holds everything the user sees.

### Semantic vs non-semantic tags
- **Non-semantic:** `<div>`, `<span>` — they say *nothing* about their content.
- **Semantic:** `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<h1>`–`<h6>`, `<p>`, `<ul>`, `<li>`, `<img>`, `<a>` — they describe the content's *meaning*.

Why care? Screen readers, search engines, and other developers all rely on semantics to understand your page.

### Key rules
- Use exactly **one** `<h1>` per page.
- Use `<nav>` only for the main navigation links.
- Use `<main>` once, to wrap the page's unique content.
- Images need an `alt` attribute describing them.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete HTML from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-build-a-table.html` — 3-column table with header + 3 data rows.
2. `easy/p02-build-a-form.html` — labeled text input, email input, submit button.
3. `easy/p03-navigation-list.html` — nav with unordered list of 4 links.

### Medium
4. `medium/p01-semantic-blog-post.html` — article with header, time, section, footer.
5. `medium/p02-image-gallery-figures.html` — 3 figures with img + figcaption.
6. `medium/p03-definition-list.html` — glossary using dl/dt/dd.

### Hard
7. `hard/p01-accessible-full-page.html` — full page with skip link, ARIA, landmarks.
8. `hard/p02-nested-article-comments.html` — blog post with nested comment articles.
9. `hard/p03-data-table-semantics.html` — table with caption, colgroup, scope, tfoot.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
