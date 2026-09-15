# Lesson 10 — Common Mistakes

## Mistake 01: Forgetting display: flex
```css
/* WRONG — flex properties do nothing */
.container { justify-content: center; }
/* CORRECT */
.container { display: flex; justify-content: center; }
```

## Mistake 02: Using flex for everything
```css
/* Flex is great but not for everything */
/* Use Grid for 2D layouts, Flex for 1D */
```

## Mistake 03: Confusing axes
```css
/* In row direction: */
justify-content: center; /* horizontal center */
align-items: center;     /* vertical center */
```

## Mistake 04: Not using gap
```css
/* WRONG — margin hacks */
.item { margin-right: 20px; }
.item:last-child { margin-right: 0; }
/* CORRECT */
.container { gap: 20px; }
```

## Mistake 05: flex-shrink surprise
```css
/* Items shrink by default */
.item { width: 200px; } /* may be less than 200px */
/* Fix */
.item { flex-shrink: 0; width: 200px; }
```
