# Lesson 11 — Intuition Checks

## Check 01: fr unit
```css
grid-template-columns: 1fr 2fr 1fr;
```
What does `fr` mean?
<details><summary>Answer</summary>
`fr` = fraction of available space. 1fr 2fr 1fr = 25% 50% 25% of the container width.
</details>

## Check 02: Grid vs Flexbox
When should you use Grid vs Flexbox?
<details><summary>Answer</summary>
- Flexbox — 1D layouts (row OR column), content-based sizing
- Grid — 2D layouts (rows AND columns), container-based sizing
Use Grid for page layout, Flexbox for component layout.
</details>

## Check 03: repeat()
```css
grid-template-columns: repeat(3, 1fr);
```
<details><summary>Answer</summary>
Creates 3 equal columns. Equivalent to `1fr 1fr 1fr`. Can use `repeat(auto-fit, minmax(200px, 1fr))` for responsive grids.
</details>

## Check 04: Grid areas
```css
grid-template-areas:
  "header header"
  "sidebar main";
```
<details><summary>Answer</summary>
Names grid cells. Items can be placed with `grid-area: header`. Visual layout in CSS.
</details>

## Check 05: auto-fit vs auto-fill
```css
repeat(auto-fit, minmax(200px, 1fr));  /* A */
repeat(auto-fill, minmax(200px, 1fr)); /* B */
```
<details><summary>Answer</summary>
`auto-fit` stretches items to fill the row. `auto-fill` keeps empty columns. Use auto-fit for responsive cards.
</details>
