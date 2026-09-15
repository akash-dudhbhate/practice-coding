# Lesson 08 — Common Mistakes

## Mistake 01: px for font size
```css
/* WRONG — doesn't scale */
body { font-size: 16px; }
/* CORRECT */
body { font-size: 1rem; }
```

## Mistake 02: Too many fonts
```css
/* WRONG — 5 font families */
/* CORRECT — 1-2 max */
```

## Mistake 03: Tight line-height
```css
/* WRONG */
p { line-height: 1.1; }
/* CORRECT */
p { line-height: 1.6; }
```

## Mistake 04: Small font size
```css
/* WRONG — hard to read */
.text { font-size: 10px; }
/* CORRECT */
.text { font-size: 0.875rem; } /* 14px */
```

## Mistake 05: Justify text
```css
/* WRONG — creates rivers of whitespace */
p { text-align: justify; }
/* CORRECT — left align for web */
p { text-align: left; }
```
