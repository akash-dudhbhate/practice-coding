# Mini Project 01 — Accessible Contact Form Page

> **Type:** Mini Project
> **Subject:** HTML/CSS/JS
> **Estimated sell price:** $50–100
> **Difficulty:** Beginner
> **Prerequisites:** Lessons 01–05 (HTML Structure, Forms, Tables, Media, Accessibility)

## Project Brief

Build a complete, accessible contact form page that a small business could use on their website. The form must be fully accessible (screen-reader friendly, keyboard navigable) and validate user input before submission.

## What you'll build

A single HTML page with:
- A semantic page structure (header, main, footer)
- A contact form with: Name, Email, Subject (dropdown), Message, and a Submit button
- Proper labels linked to inputs via `for`/`id`
- ARIA attributes where needed
- Basic client-side validation (required fields, email format)
- A success message displayed after "submission" (no server needed)
- Responsive layout (works on mobile and desktop)

## Skills you'll demonstrate

- Semantic HTML5 structure
- Form elements and input types
- Accessibility (ARIA, labels, landmarks, keyboard navigation)
- Basic CSS styling (clean, professional look)
- Client-side validation

## Sellable pitch

> "I'll build you a professional, accessible contact form page that works on all devices. It includes form validation, screen-reader support, and a clean design that matches your brand. Fully WCAG-compliant."

## Requirements

- [ ] Page uses semantic HTML5 (`<header>`, `<main>`, `<footer>`, `<nav>`)
- [ ] Form has: Name (text), Email (email), Subject (select with 3+ options), Message (textarea), Submit button
- [ ] Every input has a `<label>` with matching `for`/`id`
- [ ] Required fields marked with `required` attribute and `aria-required="true"`
- [ ] Email field uses `type="email"` for built-in validation
- [ ] Error messages have `role="alert"` and `aria-live="assertive"`
- [ ] Form shows a success message after submit (use JS to prevent default and show message)
- [ ] Page is responsive (form works on mobile — max-width container, full-width inputs on mobile)
- [ ] Skip-to-content link as the first element
- [ ] All interactive elements are keyboard accessible (tab order is logical)

## Getting started

1. Create an `index.html` file with the semantic structure.
2. Add the form with all required fields and labels.
3. Add ARIA attributes for accessibility.
4. Add a `<style>` block (or separate CSS file) for clean, professional styling.
5. Add a `<script>` for form submission handling and validation.
6. Test with keyboard only (Tab through everything).
7. Test with a screen reader (or use accessibility inspector).

## Deliverables

- `index.html` (with embedded or linked CSS/JS, or separate files)
- Works in any modern browser
- Passes basic accessibility audit (Chrome Lighthouse accessibility score 90+)
