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

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-------+-----+--------+
   | Name  | Age | City   |   <- bold header row (th)
   +-------+-----+--------+
   | Akash | 25  | Pune   |
   | Sara  | 30  | Delhi  |
   | John  | 22  | Goa    |   <- 3 data rows (td)
   +-------+-----+--------+
   ```
2. `easy/p02-build-a-form.html` — labeled text input, email input, submit button.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Name:   [____________________]
   Email:  [____________________]
           [ Submit ]
   (bad email + submit -> browser shows a validation bubble)
   ```
3. `easy/p03-navigation-list.html` — nav with unordered list of 4 links.

   ```
   WHAT IT SHOULD LOOK LIKE:
   * Home
   * About
   * Services
   * Contact            <- bulleted <ul> of 4 links inside <nav>
   ```

### Medium
4. `medium/p01-semantic-blog-post.html` — article with header, time, section, footer.

   ```
   WHAT IT SHOULD LOOK LIKE:
   My Blog Post                  <- h1, large bold
   Posted on Jan 1, 2026         <- <time>, small text
   Introduction                  <- <section> with h2
     Text text text...
   Details                       <- second <section>
     Text text text...
   Written by Akash              <- <footer>, small line
   ```
5. `medium/p02-image-gallery-figures.html` — 3 figures with img + figcaption.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ image 1 ]
   caption under it              <- <figcaption> right below img
   [ image 2 ]
   caption under it
   [ image 3 ]
   caption under it              <- 3 <figure> blocks, stacked
   ```
6. `medium/p03-definition-list.html` — glossary using dl/dt/dd.

   ```
   WHAT IT SHOULD LOOK LIKE:
   HTML
         The markup language of the web.      <- <dd> indented
   CSS
         The styling language of the web.
   JavaScript
         The scripting language of the web.   <- <dl> glossary
   ```

### Hard
7. `hard/p01-accessible-full-page.html` — full page with skip link, ARIA, landmarks.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [Skip to content]               <- hidden until first Tab
   +------------------------------------------+
   | Site Title          Home About Contact   |   <- <header> + <nav>
   +------------------------------------------+
   | Page Heading (one h1)                    |   <- <main id="main">
   | [ image with alt text ]                  |
   +------------------------------------------+
   | (c) 2026 footer                          |   <- <footer>
   +------------------------------------------+
   ```
8. `hard/p02-nested-article-comments.html` — blog post with nested comment articles.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Post Title (h1)
   Jan 1, 2026                            <- <time> in header
   Body text of the post...
   Comments                               <- <section>
     * Comment one by Sara                <- nested <article>
       * Reply by Akash (indented,        <- <article> inside
         nested inside comment 1)            comment article
     * Comment two by John
   ```
9. `hard/p03-data-table-semantics.html` — table with caption, colgroup, scope, tfoot.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Quarterly Sales                          <- <caption> on top
   +---------+-----+-----+-----+--------+
   | Product |  Q1 |  Q2 |  Q3 | Total  |   <- <thead> (bold, scope="col")
   +---------+-----+-----+-----+--------+
   | Widget  |  10 |  20 |  15 |   45   |
   | Gadget  |  30 |  25 |  35 |   90   |
   +---------+-----+-----+-----+--------+
   | Total   |  40 |  45 |  50 |  135   |   <- <tfoot> (bold)
   +---------+-----+-----+-----+--------+
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete HTML from scratch** below the TODO marker.
- Remove the TODO comment when done.
- Open the file in a browser to check it renders correctly.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
