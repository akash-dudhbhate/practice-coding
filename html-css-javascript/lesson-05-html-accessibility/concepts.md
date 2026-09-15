# Lesson 05 — Concepts Explained (HTML Accessibility Deep Dive)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Accessibility (a11y)?

**What:** Accessibility (a11y) means making your website usable by everyone, including people using screen readers, keyboard navigation, voice control, or other assistive technologies.

```html
<!-- Accessible -->
<button>Submit</button>
<label for="email">Email</label>
<input type="email" id="email" />

<!-- Inaccessible -->
<div onclick="submit()">Submit</div>
<input type="email" placeholder="Email" />
```

**Why it exists:** ~15% of people have some disability. Without accessibility, they can't use your website. In many countries, accessibility is legally required (ADA, WCAG, EAA). It also improves SEO and UX for everyone (keyboard shortcuts, clear labels help all users).

**Where it's used:** Every web page. Accessibility is not a "feature" — it's a baseline requirement.

**What goes wrong without it:**
- Blind users can't navigate your site → lost customers, legal liability (ADA lawsuits are common).
- Keyboard-only users can't tab through your page → trapped, can't complete actions.
- Low-vision users can't read low-contrast text → excluded.
- Motor-impaired users can't click tiny targets → frustrated.

---

## Alt Text

**What:** The `alt` attribute on `<img>` describes the image for screen readers and when the image fails to load.

```html
<!-- Good: describes the image's meaning -->
<img src="chart.png" alt="Revenue increased 40% from Q1 to Q2 2026" />

<!-- Decorative image: empty alt means "ignore me" -->
<img src="border-decoration.png" alt="" />

<!-- Bad: no alt at all -->
<img src="chart.png" />  <!-- screen reader says "image" with no context -->
```

- Meaningful images → describe what they convey.
- Decorative images → use `alt=""` (empty) so screen readers skip them.
- Never omit the `alt` attribute entirely.

**Why it exists:** Screen readers can't "see" images. Alt text is the only way blind users know what an image shows. It also displays when an image fails to load.

**Where it's used:** Every `<img>` element, `<area>` elements, and `<input type="image">`.

**What goes wrong without it:**
- Missing `alt` → screen readers announce the filename ("chart.png") — useless.
- `alt="image"` or `alt="photo"` → redundant, screen readers already say "image."
- Alt text that's too long → interrupts the reading flow; keep it concise (under ~125 chars).
- Forgetting `alt=""` on decorative images → screen readers read useless filenames for borders/spacers.

---

## ARIA Attributes

**What:** ARIA (Accessible Rich Internet Applications) attributes add accessibility information that HTML alone can't express.

```html
<!-- Label an element with no visible text -->
<button aria-label="Close dialog">✕</button>

<!-- Describe an element's role -->
<div role="navigation" aria-label="Main navigation">...</div>

<!-- Live regions (announce updates) -->
<div aria-live="polite">Form submitted successfully!</div>

<!-- Expanded/collapsed state -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
```

Key ARIA attributes:
- `aria-label` = invisible text label for screen readers.
- `aria-labelledby` = reference to another element that labels this one.
- `aria-describedby` = reference to a description element.
- `aria-live` = announce changes (polite/assertive).
- `aria-expanded`, `aria-hidden`, `aria-disabled` = state.
- `role` = what the element IS (navigation, dialog, tab, alert).

**Why it exists:** HTML alone can't describe dynamic widgets (tabs, modals, dropdowns, live updates). ARIA fills the gap by telling screen readers what an element does and its current state.

**Where it's used:** Custom interactive widgets, icon-only buttons, dynamic content updates, AJAX-loaded content.

**What goes wrong without it:**
- Icon-only buttons (✕, ☰) → screen readers say "button" with no context. Use `aria-label`.
- Custom dropdowns built with `<div>`s → screen readers don't know it's a dropdown. Use `role="listbox"`.
- **Overusing ARIA** → adding `role="button"` to a `<button>` is redundant and can confuse screen readers. First rule of ARIA: "No ARIA is better than bad ARIA." Use native HTML when possible.
- `aria-hidden="true"` on a focusable element → screen reader ignores it but keyboard still tabs to it → confusing.

---

## Landmark Roles and Semantic HTML

**What:** Landmarks are page sections that screen readers can jump to. HTML5 semantic tags ARE landmarks.

```html
<header>   <!-- role="banner" -->
<nav>      <!-- role="navigation" -->
<main>     <!-- role="main" -->
<aside>    <!-- role="complementary" -->
<footer>   <!-- role="contentinfo" -->
<form>     <!-- role="form" -->
<section>  <!-- role="region" (with accessible name) -->
```

You can also use ARIA roles explicitly:
```html
<div role="banner">...</div>
<div role="main">...</div>
```

**Why it exists:** Screen reader users can't scan a page visually. Landmarks let them jump directly to navigation, main content, or footer — like a table of contents for the page.

**Where it's used:** Every web page should have at least `<header>`, `<main>`, and `<footer>` landmarks.

**What goes wrong without it:**
- All `<div>`s, no landmarks → screen reader users must tab through the entire page to find content.
- Multiple `<nav>` elements without `aria-label` → screen readers can't tell them apart ("navigation", "navigation"). Label them: `aria-label="Main navigation"`, `aria-label="Footer navigation"`.
- Using `role="main"` on a `<div>` when you could use `<main>` → redundant, more code.

---

## Keyboard Navigation and Focus

**What:** Many users (motor-impaired, power users) navigate with the keyboard (Tab, Shift+Tab, Enter, Space, arrows). Every interactive element must be focusable and operable by keyboard.

```html
<!-- Focusable by default: links, buttons, inputs -->
<a href="/about">About</a>
<button>Submit</button>
<input type="text" />

<!-- NOT focusable: divs, spans -->
<div onclick="doSomething()">Click me</div>  <!-- can't tab to this! -->
```

- `Tab` moves focus forward, `Shift+Tab` moves backward.
- Focus order follows DOM order (not visual order).
- Visible focus indicator (the outline) must be present — never remove it with `outline: none` without a replacement.

```css
/* Don't do this */
button { outline: none; }  /* removes keyboard focus indicator */

/* Do this instead */
button:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

**Why it exists:** If an element can't be reached by keyboard, keyboard users can't use it. This is WCAG criterion 2.1.1 (Keyboard) — a fundamental accessibility requirement.

**Where it's used:** Every interactive element — links, buttons, inputs, custom widgets.

**What goes wrong without it:**
- `<div onclick>` instead of `<button>` → not keyboard accessible. Users can't tab to it or press Enter to activate.
- `outline: none` with no replacement → keyboard users can't see where they are on the page.
- `tabindex="-1"` on an element users need → removes it from tab order.
- `tabindex="999"` → messes up tab order; tabbing jumps around unpredictably. Avoid positive tabindex values.

---

## Skip Links

**What:** A skip link is the first focusable element on a page. It lets keyboard users jump directly to the main content, skipping repetitive navigation.

```html
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  <nav>...50 nav links...</nav>
  <main id="main">
    <!-- actual content -->
  </main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;          /* hidden off-screen */
}
.skip-link:focus {
  left: 0;                /* visible when focused */
  background: #000;
  color: #fff;
  padding: 8px;
}
```

**Why it exists:** Without a skip link, a keyboard user must press Tab 50+ times to get past the navigation on every page. A skip link lets them jump straight to content with one keypress.

**Where it's used:** Every page with navigation before the main content (which is most pages).

**What goes wrong without it:**
- Keyboard users tab through every nav link on every page → exhausting, they leave.
- Skip link that's always visible → clutters the design for sighted users (hide it off-screen, show on focus).
- `href="#main"` but no element with `id="main"` → link does nothing.
- Skip link not first in the DOM → user tabs past it before finding it.

---

## Form Accessibility

**What:** Forms need labels, instructions, and error messages that screen readers can understand.

```html
<!-- Every input has a label -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" required aria-describedby="email-hint" />
<p id="email-hint">We'll never share your email.</p>

<!-- Group related inputs -->
<fieldset>
  <legend>Shipping address</legend>
  <label for="street">Street</label>
  <input type="text" id="street" name="street" />
</fieldset>

<!-- Error messages -->
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error" />
<p id="email-error" role="alert">Please enter a valid email address.</p>
```

- `aria-describedby` links an input to its hint/error text.
- `aria-invalid="true"` marks a field as having an error.
- `role="alert"` makes screen readers announce the error immediately.
- `<fieldset>`/`<legend>` groups related inputs with a shared label.

**Why it exists:** Without labels and instructions, screen reader users hear "text input, text input, text input" with no idea what to type. Form errors that are only shown visually are invisible to blind users.

**Where it's used:** Every form — login, registration, checkout, contact.

**What goes wrong without it:**
- No `<label>` → screen reader says "edit text" with no context.
- Placeholder as label → disappears when typing, screen readers may not announce it.
- Visual-only error messages (red border, icon) → blind users don't know there's an error.
- No `aria-describedby` → hints and errors aren't associated with the input.

---

## Accessible Tables

**What:** Data tables need `scope`, `<caption>`, and proper structure so screen readers can navigate them.

```html
<table>
  <caption>Sales by Quarter</caption>
  <thead>
    <tr>
      <th scope="col">Quarter</th>
      <th scope="col">Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Q1</th>
      <td>$10,000</td>
    </tr>
  </tbody>
</table>
```

**Why it exists:** Screen readers read tables cell by cell. Without `scope` and `<caption>`, they read "Q1, $10,000" with no context. With scope, they read "Quarter: Q1, Revenue: $10,000."

**Where it's used:** Every data table.

**What goes wrong without it:**
- Missing `scope` → no association between headers and cells.
- Missing `<caption>` → no context for what the table shows.
- Using tables for layout → screen readers announce it as a table, confusing users. Use CSS for layout.

---

## Color and Contrast

**What:** Text must have sufficient contrast against its background. WCAG AA requires a contrast ratio of at least 4.5:1 for normal text, 3:1 for large text.

```css
/* Good contrast (dark text on light background) */
p { color: #333; background: #fff; }   /* ratio ~12.6:1 */

/* Bad contrast (light grey on white) */
p { color: #ccc; background: #fff; }   /* ratio ~1.6:1 — fails */
```

- Don't rely on color alone to convey information (colorblind users).
- Use text labels, icons, or patterns in addition to color.

```html
<!-- Bad: only color indicates error -->
<span style="color: red;">*</span>

<!-- Good: color + text -->
<span style="color: red;" aria-label="required">*</span>
<label>Email <span aria-hidden="true">*</span></label>
```

**Why it exists:** ~8% of men have some color blindness. Low-vision users need contrast. Without sufficient contrast, text is unreadable for many users.

**Where it's used:** All text, icons, form borders, focus indicators.

**What goes wrong without it:**
- Light grey text on white → fails WCAG, unreadable for low-vision users.
- Red/green-only status indicators → colorblind users can't tell success from failure.
- Autofill backgrounds that hide text → check contrast in all states.
