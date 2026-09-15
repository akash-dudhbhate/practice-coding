# Lesson 13 — Common Mistakes

## Mistake 01: Animating layout properties
```css
/* WRONG — janky */
.box { transition: width 1s, height 1s; }
/* CORRECT — use transform */
.box { transition: transform 1s; }
```

## Mistake 02: No initial value for transition
```css
/* WRONG — no starting point */
.box { transition: width 1s; }
/* CORRECT */
.box { width: 100px; transition: width 1s; }
```

## Mistake 03: Too many animations
```css
/* WRONG — distracting */
* { animation: pulse 2s infinite; }
/* CORRECT — purposeful animations only */
```

## Mistake 04: Not respecting prefers-reduced-motion
```css
/* WRONG — ignores accessibility */
/* CORRECT */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

## Mistake 05: Long animations
```css
/* WRONG — users get impatient */
transition: all 3s;
/* CORRECT — 200-400ms for UI */
transition: transform 200ms ease;
```
