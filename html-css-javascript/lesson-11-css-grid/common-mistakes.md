# Lesson 11 — Common Mistakes

## Mistake 01: Forgetting display: grid
```css
/* WRONG */
.container { grid-template-columns: 1fr 1fr; }
/* CORRECT */
.container { display: grid; grid-template-columns: 1fr 1fr; }
```

## Mistake 02: Using grid-gap
```css
/* DEPRECATED */
grid-gap: 20px;
/* CORRECT */
gap: 20px;
```

## Mistake 03: Overcomplicating with Grid when Flex works
```css
/* For a simple row of items, use Flexbox */
display: flex; gap: 10px;
/* Not Grid */
```

## Mistake 04: Not using minmax for responsive
```css
/* WRONG — fixed columns break on mobile */
grid-template-columns: 300px 300px 300px;
/* CORRECT — responsive */
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
```

## Mistake 05: Hardcoded row heights
```css
/* WRONG */
grid-template-rows: 100px 200px 100px;
/* BETTER — let content determine height */
/* Only set row heights when necessary */
```
