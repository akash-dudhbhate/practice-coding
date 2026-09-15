# Lesson 05 — Coding Check

Use this to verify your solutions before asking me to review. Open each HTML file in a browser and test with keyboard only (unplug your mouse).

## Easy

### p01-solve.html (Images with alt text)
- [ ] Image 1 has meaningful `alt` text (describes what the image conveys).
- [ ] Image 2 has `alt=""` (empty, decorative).
- [ ] Image 3 is wrapped in an `<a>` tag (image link) with descriptive `alt`.
- [ ] No image is missing the `alt` attribute entirely.
- [ ] Temporarily break an image `src` → alt text displays as fallback.

### p02-solve.html (Form with labels and hints)
- [ ] 3 inputs, each with a `<label>` whose `for` matches the input's `id`.
- [ ] Each input has `aria-describedby` pointing to a hint `<p>` with matching `id`.
- [ ] Hints are visible text below or beside each input.
- [ ] Clicking a label focuses the correct input.
- [ ] All inputs have `name` attributes.

### p03-solve.html (Page with landmarks)
- [ ] `<html lang="en">` on the root element.
- [ ] Has `<header>`, `<nav>`, `<main>`, `<footer>`.
- [ ] `<nav>` contains at least 2 links.
- [ ] `<main>` wraps the primary content.
- [ ] Page has one `<h1>`.

## Medium

### p01-solve.html (Skip link and heading hierarchy)
- [ ] Skip link (`<a href="#main">`) is the first element in `<body>`.
- [ ] `<main>` has `id="main"`.
- [ ] Skip link is hidden off-screen by default, visible on focus (CSS).
- [ ] Heading order: h1 → h2 → h3 (no skipped levels).
- [ ] `<nav>` has `aria-label` if there are multiple navs.
- [ ] Tab to the page → skip link appears first.

### p02-solve.html (Accessible form with errors)
- [ ] Uses `<fieldset>` and `<legend>` to group related inputs.
- [ ] Every input has a `<label>`.
- [ ] Required inputs have `required` attribute.
- [ ] At least one error message with `role="alert"`.
- [ ] Error input has `aria-invalid="true"` and `aria-describedby` pointing to the error.
- [ ] Submitting empty form triggers browser validation + shows error region.

### p03-solve.html (Accessible data table)
- [ ] Has `<caption>` as first child of `<table>`.
- [ ] Column headers have `scope="col"`.
- [ ] Row headers have `scope="row"`.
- [ ] Has `<thead>` and `<tbody>`.
- [ ] At least 3 data rows.
- [ ] No layout tables — table contains actual tabular data.

## Hard

### p01-solve.html (Full accessible page)
- [ ] `<html lang="en">` present.
- [ ] Skip link is first in `<body>`, `href="#main"`, `<main id="main">`.
- [ ] Landmarks: `<header>`, `<nav aria-label="...">`, `<main>`, `<footer>`.
- [ ] One `<h1>`, logical heading hierarchy (h1 → h2 → h3).
- [ ] All images have appropriate `alt` (meaningful or empty for decorative).
- [ ] Form: every input has a `<label>`, `aria-describedby` for hints.
- [ ] CSS has `:focus-visible` styles (visible focus indicator).
- [ ] Tab through the entire page → every interactive element is reachable, focus is visible.

### p02-solve.html (Accessible toggle widget)
- [ ] Toggle button has `aria-expanded` (false when collapsed, true when expanded).
- [ ] Button has `aria-controls` pointing to the toggleable content's `id`.
- [ ] Content section has matching `id`.
- [ ] A live region (`aria-live="polite"`) announces status changes.
- [ ] Button is a `<button>` element (keyboard accessible by default).
- [ ] Pressing Enter/Space toggles the content (test with keyboard).
- [ ] Focus indicator is visible on the button.

### p03-solve.html (Accessible navigation menu)
- [ ] `<nav>` has `aria-label="Main navigation"` (or similar).
- [ ] Active/current link has `aria-current="page"`.
- [ ] Menu is a `<ul>` of `<li>` containing `<a>` tags.
- [ ] Skip link present before the nav.
- [ ] CSS has `:focus-visible` styles on links.
- [ ] Tab through the menu → each link is reachable and focus is visible.
- [ ] Active link is visually distinct (not by color alone — use bold, underline, or icon too).

## How to verify

Open each file in a browser:
```bash
xdg-open easy/p01-solve.html
```
- **Keyboard test:** Press Tab repeatedly. Every link, button, and input must be reachable. Focus indicator must be visible at all times.
- **Skip link test:** Tab once on page load → skip link should appear. Press Enter → focus jumps to main content.
- **Form test:** Click each label → correct input focuses. Submit empty form → validation errors appear and are announced (role="alert").
- **Contrast check:** Use a browser extension or WebAIM contrast checker to verify text contrast ≥ 4.5:1.
- **Screen reader test (optional):** Try NVDA (Windows) or VoiceOver (Mac) to hear how the page is announced.
