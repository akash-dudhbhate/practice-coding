# Lesson 06 — Common Mistakes

## Mistake 01: Overusing IDs for styling
```css
/* WRONG — IDs are too specific, hard to override */
#header { color: blue; }
/* CORRECT — use classes */
.header { color: blue; }
```

## Mistake 02: !important everywhere
```css
/* WRONG — specificity war */
.text { color: red !important; }
/* CORRECT — fix specificity */
.header .text { color: red; }
```

## Mistake 03: Deep selectors
```css
/* WRONG — brittle */
.header nav ul li a { color: blue; }
/* CORRECT — use a class */
.nav-link { color: blue; }
```

## Mistake 04: Confusing descendant and child
```css
div p { }  /* any <p> inside <div> at any depth */
div > p { } /* only <p> that are direct children of <div> */
```

## Mistake 05: Tag-qualified classes
```css
/* WRONG — less reusable */
div.container { }
/* CORRECT */
.container { }
```
