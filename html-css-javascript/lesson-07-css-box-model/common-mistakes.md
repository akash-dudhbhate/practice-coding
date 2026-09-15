# Lesson 07 — Common Mistakes

## Mistake 01: Not using border-box
```css
/* WRONG — width doesn't include padding */
* { box-sizing: content-box; }
/* CORRECT */
* { box-sizing: border-box; }
```

## Mistake 02: Margin collapse surprise
```css
/* Vertical margins collapse — 30px not 50px */
.a { margin-bottom: 30px; }
.b { margin-top: 20px; }
```

## Mistake 03: Using margin for spacing inside
```css
/* WRONG — use padding for internal space */
.box { margin: 20px; }
/* CORRECT */
.box { padding: 20px; }
```

## Mistake 04: Forgetting display
```html
<!-- span can't have width -->
<span style="width: 200px;">Hi</span>
<!-- Fix: use display: inline-block or block -->
```

## Mistake 05: Negative margins
```css
/* AVOID — can cause overlap issues */
.box { margin-top: -20px; }
```
