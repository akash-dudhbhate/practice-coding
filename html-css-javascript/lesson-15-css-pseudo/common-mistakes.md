# Lesson 15 — Common Mistakes

## Mistake 01: No :focus styles
```css
/* WRONG — keyboard users lost */
.btn:hover { background: blue; }
/* CORRECT */
.btn:hover, .btn:focus { background: blue; }
```

## Mistake 02: ::before without content
```css
/* WRONG — doesn't render */
.box::before { width: 100px; }
/* CORRECT */
.box::before { content: ""; width: 100px; }
```

## Mistake 03: Removing outline
```css
/* WRONG */
*:focus { outline: none; }
/* CORRECT — provide alternative */
*:focus-visible { outline: 2px solid blue; }
```

## Mistake 04: :nth-child confusion
```css
/* nth-child counts ALL siblings, not just <li> */
/* If there's an <h1> before <li>s, nth-child(1) is the <h1> */
```

## Mistake 05: Overusing ::before/::after
```css
/* Don't use pseudo-elements for important content */
/* Screen readers may not announce them */
```
