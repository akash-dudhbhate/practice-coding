# Lesson 09 — Intuition Checks

## Check 01: Color formats
```css
color: #ff0000;      /* hex */
color: rgb(255,0,0); /* rgb */
color: red;          /* named */
color: hsl(0,100%,50%); /* hsl */
```
Which is most intuitive for adjusting?
<details><summary>Answer</summary>
HSL — hue, saturation, lightness. Easy to make variations: change lightness for shades, hue for different colors.
</details>

## Check 02: opacity vs rgba
```css
.a { opacity: 0.5; }
.b { background: rgba(0,0,0,0.5); }
```
<details><summary>Answer</summary>
`.a` makes the ENTIRE element (and children) 50% transparent. `.b` makes only the background 50% transparent — text stays fully opaque.
</details>

## Check 03: background-size
```css
background-size: cover;   /* A */
background-size: contain; /* B */
```
<details><summary>Answer</summary>
- `cover` — fills area, may crop image
- `contain` — fits entire image, may leave gaps
</details>

## Check 04: gradient
```css
background: linear-gradient(to right, red, blue);
```
<details><summary>Answer</summary>
Gradient from red (left) to blue (right). Can use angles: `linear-gradient(45deg, red, blue)`.
</details>

## Check 05: CSS variables
```css
:root { --primary: #007bff; }
.btn { background: var(--primary); }
```
<details><summary>Answer</summary>
CSS variables (custom properties) allow reuse and dynamic changes. Defined in `:root`, used with `var()`.
</details>
