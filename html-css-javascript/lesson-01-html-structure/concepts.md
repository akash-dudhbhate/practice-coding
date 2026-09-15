# Lesson 01 — Concepts Explained (HTML Structure & Semantic Tags)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## HTML Structure

**What:** HTML (HyperText Markup Language) is the skeleton of every web page. It uses 'tags' (words in angle brackets) to tell the browser what each piece of content is.

```html
<p>This is a paragraph</p>       <!-- opening tag, content, closing tag -->
<h1>This is a heading</h1>
<img src="photo.jpg" alt="A cat" />   <!-- self-closing tag -->
```

Most tags come in pairs: opening `<p>` and closing `</p>`. Content goes between them.

**Why it exists:** Without HTML, a browser just sees a wall of plain text — no headings, no paragraphs, no links, no images. HTML tells the browser the STRUCTURE and MEANING of each piece of content so it can render it correctly.

**Where it's used:** Every single web page on the internet. HTML is the foundation — CSS makes it pretty, JavaScript makes it interactive, but without HTML there's nothing.

**What goes wrong without it:**
- Browser displays raw text with no formatting — no headings, no paragraphs, no links.
- No accessibility — screen readers can't navigate without structure.
- SEO fails — search engines can't understand your page content.

---

## Table Elements

**What:** Tables display data in rows and columns, like a spreadsheet.

```html
<table>           <!-- the table wrapper -->
  <thead>         <!-- header section (column titles) -->
    <tr>          <!-- a row -->
      <th>Name</th>  <!-- header cell (bold, centered) -->
    </tr>
  </thead>
  <tbody>         <!-- body section (data rows) -->
    <tr>
      <td>Akash</td>  <!-- data cell -->
    </tr>
  </tbody>
</table>
```

- `thead` = column headers, `tbody` = the actual data, `tr` = a row, `th` = header cell, `td` = regular cell.

**Why it exists:** Some data is naturally tabular — financial reports, schedules, comparison charts. Tables give structure that makes this data readable and accessible.

**Where it's used:** Data dashboards, pricing tables, schedules, spreadsheets on web pages, email clients.

**What goes wrong without it:**
- Using `<div>` for tabular data → screen readers can't navigate rows/columns.
- Missing `<thead>`/`<tbody>` → no structural distinction between headers and data.
- Using tables for LAYOUT (not data) → terrible accessibility, hard to make responsive. This was common in the 1990s — don't do it today.

---

## HTML Forms

**What:** Forms collect user input — login forms, search bars, contact forms are all `<form>` elements.

```html
<form>
  <label for="name">Name:</label>
  <input type="text" id="name" />
  <button type="submit">Send</button>
</form>
```

The `<label>`'s `for` must match the `<input>`'s `id` — this links them.

**Why it exists:** Without forms, websites are read-only. You can't log in, search, comment, buy, or submit anything. Forms are how users send data to servers.

**Where it's used:** Login pages, search bars, registration, checkout, contact pages, surveys, admin panels.

**What goes wrong without it:**
- No way for users to send data to your server.
- Missing `<label>` → screen readers don't announce what the input is for → inaccessible.
- Missing `for`/`id` link → clicking the label doesn't focus the input → bad UX.
- Wrong `type` → mobile shows wrong keyboard, no built-in validation.

---

## Input Types

**What:** The `<input>` element has a `type` attribute that controls what kind of input it shows:

```html
type="text"      -> normal text box
type="email"     -> text box that validates email format
type="password"  -> hides characters as dots
type="number"    -> only accepts numbers
type="checkbox"  -> a check box
type="radio"     -> radio button (select one from group)
type="submit"    -> a submit button
```

**Why it exists:** Different data needs different inputs. An email field should validate email format. A number field should show a numeric keyboard on mobile. Choosing the right type gives users the right tool.

**Where it's used:** Every form input — choosing the right type improves UX and validation.

**What goes wrong without it:**
- Using `type="text"` for emails → no built-in validation, wrong mobile keyboard.
- Using `type="text"` for numbers → users can type letters, you have to validate manually.
- Accessibility suffers — screen readers use the type to announce what input is expected.

---

## Label Element

**What:** The `<label>` element gives a text description to a form input.

```html
<label for="email">Email:</label>
<input type="email" id="email" />
```

The `for` attribute MUST match the input's `id`.

**Why it exists:** Inputs without labels are meaningless — a text box with no description is confusing. Labels tell users (and screen readers) what to enter.

**Where it's used:** Every form input should have a label. No exceptions.

**What goes wrong without it:**
- Screen readers announce "text input" with no context → blind users can't fill the form.
- Clicking the label text doesn't focus the input → worse UX on mobile.
- Form validation errors don't have context → "This field is required" — which field?

---

## HTML Lists

**What:** Lists group related items. Two main types:

```html
<!-- Unordered (bullet points) -->
<ul>
  <li>Apple</li>
  <li>Banana</li>
</ul>

<!-- Ordered (numbered) -->
<ol>
  <li>First step</li>
  <li>Second step</li>
</ol>
```

`<ul>`/`<ol>` = container, `<li>` = each entry.

**Why it exists:** Lists are one of the most common ways to organize information — navigation menus, step-by-step instructions, feature lists, shopping items. HTML lists give them proper structure.

**Where it's used:** Navigation menus, instructions, feature lists, comments, search results.

**What goes wrong without it:**
- Using `<div>` for lists → screen readers can't announce "list with 3 items."
- SEO misses the list structure — search engines use lists to understand content relationships.
- Styling is harder — CSS has special list properties (`list-style`, `list-item`) that only work on proper list elements.

---

## Links (anchor tag)

**What:** The `<a>` (anchor) tag creates a clickable link.

```html
<a href="about.html">About Us</a>
<a href="#section1">Jump to Section 1</a>        <!-- same-page link -->
<a href="mailto:hello@email.com">Email me</a>    <!-- opens email app -->
```

`href` is the destination. The text between `<a>` and `</a>` is what the user clicks.

**Why it exists:** The "HyperText" in HTML is about linking — the web is a web because pages link to each other. Without links, every page is an isolated island.

**Where it's used:** Navigation menus, "read more" links, external links, same-page jumps, email/phone links.

**What goes wrong without it:**
- Users can't navigate between pages.
- Using `<div onclick="...">` instead of `<a>` → not keyboard accessible, not bookmarkable, not right-clickable ("open in new tab" doesn't work).

---

## Semantic Navigation (`<nav>`)

**What:** The `<nav>` tag tells browsers and screen readers: "this section contains the main navigation links."

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
  </ul>
</nav>
```

**Why it exists:** Screen readers can jump directly to navigation. Search engines understand your site structure. Other developers can find the nav without reading every `<div>`.

**Where it's used:** Main navigation menus, table of contents, breadcrumbs. Use `<nav>` only for the MAIN navigation, not every group of links.

**What goes wrong without it:**
- Screen reader users have to tab through every link to find navigation.
- Using `<div class="nav">` → no semantic meaning, accessibility tools ignore it.
- Too many `<nav>` tags → screen readers get confused about which is the main navigation.

---

## Semantic HTML5 Tags

**What:** Semantic tags describe what their content MEANS, not just how it looks.

```html
<header>   <!-- top section (logo, nav, title) -->
<nav>      <!-- navigation links -->
<main>     <!-- the main unique content of the page -->
<section>  <!-- a thematic grouping of content -->
<article>  <!-- a self-contained piece (blog post, news item) -->
<aside>    <!-- sidebar content (related links, ads) -->
<footer>   <!-- bottom section (copyright, links) -->
<time>     <!-- a date or time -->
```

**Why it exists:** Before HTML5, everything was `<div>` — a page was a sea of `<div>` tags with no meaning. Semantic tags tell browsers, screen readers, and search engines what each section IS, making pages accessible, SEO-friendly, and readable by developers.

**Where it's used:** Every modern web page should use semantic tags for structure instead of generic `<div>`s.

**What goes wrong without it:**
- "Div soup" — `<div class="header">`, `<div class="footer">` — no standard meaning, every site is different.
- Screen readers can't navigate by landmarks → terrible accessibility.
- Search engines can't identify the main content vs. navigation vs. ads.
- Harder for developers to understand the page structure.

---

## Semantic Media Tags (figure, figcaption)

**What:** The `<figure>` tag wraps an image that is referenced in the text. `<figcaption>` gives it a caption.

```html
<figure>
  <img src="chart.png" alt="Sales chart showing 2026 revenue" />
  <figcaption>Figure 1: Monthly revenue for 2026</figcaption>
</figure>
```

**Why it exists:** Images and their captions belong together as a unit. Without `<figure>`, the image and caption are separate elements that could get separated by layout. `<figure>` says "these belong together."

**Where it's used:** Blog posts with images, scientific articles, documentation, photo galleries.

**What goes wrong without it:**
- Image and caption get separated in responsive layouts.
- Screen readers don't know the caption is related to the image.
- Using `<div>` → no semantic relationship between image and caption.

---

## Description Lists (dl, dt, dd)

**What:** A description list pairs terms with their definitions — like a glossary.

```html
<dl>
  <dt>HTML</dt>           <!-- the term -->
  <dd>Markup language for web pages</dd>  <!-- the definition -->
  <dt>CSS</dt>
  <dd>Styling language for web pages</dd>
</dl>
```

**Why it exists:** Unlike `<ul>` (which is just a list), `<dl>` shows a term-definition relationship. This is a specific, common pattern (glossaries, FAQs, metadata) that deserves its own structure.

**Where it's used:** Glossaries, FAQs, product specifications (key-value pairs), definition lists.

**What goes wrong without it:**
- Using `<ul>` for term-definition pairs → no semantic relationship between term and definition.
- Screen readers can't announce "term: HTML, definition: Markup language..."
- Harder to style — `<dl>` has built-in styling for term/definition pairs.

---

## Accessibility (ARIA, alt, labels, landmarks)

**What:** Accessibility (a11y) means making your website usable by everyone, including people using screen readers, keyboard navigation, or other assistive technologies.

Key practices:
- `alt` on `<img>`: describes the image for screen readers.
- `<label for="id">`: links text to form inputs.
- ARIA attributes: `aria-label="Main navigation"`, `role="contentinfo"`.
- Landmark roles: `<header>`, `<nav>`, `<main>`, `<footer>` help screen readers navigate.
- Skip link: `<a href="#main">Skip to content</a>` as the first element.

**Why it exists:** ~15% of people have some disability. Without accessibility, they can't use your website. In many countries, accessibility is legally required (ADA, WCAG). It also improves SEO and UX for everyone.

**Where it's used:** Every web page. Accessibility is not a "feature" — it's a baseline requirement.

**What goes wrong without it:**
- Blind users can't navigate your site → lost customers, legal liability.
- Keyboard-only users can't tab through your page → trapped.
- Missing `alt` → screen readers say "image" with no context.
- No skip link → keyboard users must tab through 50 nav links to reach content.
- No landmarks → screen reader users can't jump to main content.

---

## Semantic Nesting

**What:** HTML elements can be nested (placed inside each other), like Russian dolls.

```html
<article>              <!-- a blog post -->
  <header>             <!-- post header -->
    <h1>My Post</h1>
  </header>
  <section>            <!-- a section of the post -->
    <p>Content...</p>
  </section>
  <article>            <!-- a comment ON the post (nested article!) -->
    <h3>Great post!</h3>
  </article>
</article>
```

**Why it exists:** Content has natural hierarchy — a blog post contains comments, a section contains paragraphs, a card contains an image and text. Nesting reflects this real-world structure.

**Where it's used:** Comment threads, nested menus, card layouts, article-with-sections.

**What goes wrong without it:**
- Flat structure → no relationship between parent and child content.
- Screen readers can't understand "this comment belongs to that post."
- CSS styling becomes harder — you can't target "the image inside the card" without nesting.

---

## Heading Hierarchy

**What:** HTML has 6 heading levels: `<h1>` (most important) to `<h6>` (least). They must go in order — don't skip levels.

```html
<h1>Page Title</h1>          <!-- only ONE h1 per page -->
  <h2>Section Title</h2>     <!-- major sections -->
    <h3>Subsection</h3>      <!-- subsections within a section -->
```

**Why it exists:** Headings create a document outline — like a table of contents. Screen readers use this to navigate. Search engines use it to understand page structure.

**Where it's used:** Every page with any structure. One `<h1>`, then `<h2>` for sections, `<h3>` for subsections.

**What goes wrong without it:**
- Skipping levels (`<h1>` then `<h3>`) → screen readers think content is missing.
- Multiple `<h1>` tags → confusing outline, bad SEO.
- Using headings for styling (`<h1>` because it's big) → destroys the document structure. Use CSS for size, headings for hierarchy.

---

## Complex Table Semantics

**What:** Advanced table elements for accessibility and structure:

```html
<caption>           <!-- a title for the whole table -->
<colgroup><col />   <!-- defines column widths/styling -->
<th scope="col">    <!-- header cell for a COLUMN -->
<th scope="row">    <!-- header cell for a ROW -->
<tfoot>             <!-- footer section (totals, summaries) -->
```

**Why it exists:** `scope` tells screen readers which cells a header applies to. Without it, a screen reader can't tell if a header labels the column below it or the row beside it. `<caption>` gives the table a title for context.

**Where it's used:** Data tables with headers, financial tables, complex comparison tables.

**What goes wrong without it:**
- Missing `scope` → screen readers read "Name, Akash, Age, 25" instead of "Name: Akash, Age: 25" — no relationship between headers and cells.
- Missing `<caption>` → screen reader users don't know what the table is about before hearing all the cells.
- Missing `<tfoot>` → totals row is mixed with data rows, no structural distinction.
