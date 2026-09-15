# Lesson 14 — Common Mistakes

## Mistake 01: No fallback
```css
/* WRONG — breaks if undefined */
color: var(--text);
/* CORRECT */
color: var(--text, #333);
```

## Mistake 02: Wrong scope
```css
/* WRONG — variable scoped too narrowly */
.card { --primary: blue; }
.btn { background: var(--primary); } /* can't access */
/* CORRECT */
:root { --primary: blue; }
```

## Mistake 03: Not using :root
```css
/* WRONG — hard to override */
body { --primary: blue; }
/* CORRECT */
:root { --primary: blue; }
```

## Mistake 04: Overusing variables
```css
/* WRONG — variable for everything */
:root { --color-red: red; --color-blue: blue; }
/* Use variables for theme values, not every value */
```

## Mistake 05: Not organizing variables
```css
/* WRONG — scattered */
:root { --primary: blue; --spacing: 10px; --radius: 4px; }
/* BETTER — grouped */
:root {
  --color-primary: blue;
  --space-md: 10px;
  --radius-sm: 4px;
}
```
