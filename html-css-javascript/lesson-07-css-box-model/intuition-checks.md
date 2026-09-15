# Lesson 07 — Intuition Checks

## Check 01: Box model components
What are the 4 parts of the box model (inside to outside)?
<details><summary>Answer</summary>
content → padding → border → margin. Padding is inside the border (background shows), margin is outside (transparent).
</details>

## Check 02: box-sizing
```css
/* content-box (default) */
width = content width
/* border-box */
width = content + padding + border
```
Which is more intuitive?
<details><summary>Answer</summary>
`border-box` — what you set is what you get. Always use `* { box-sizing: border-box; }` in resets.
</details>

## Check 03: margin: auto
```css
.box { width: 200px; margin: 0 auto; }
```
What does `margin: 0 auto` do?
<details><summary>Answer</summary>
Centers horizontally. `0` = top/bottom margin, `auto` = left/right share remaining space equally. Only works with a defined width.
</details>

## Check 04: display
What's the difference between `block`, `inline`, and `inline-block`?
<details><summary>Answer</summary>
- block — full width, breaks line, can set width/height
- inline — content width, no line break, can't set width/height
- inline-block — content width, no line break, CAN set width/height
</details>

## Check 05: padding shorthand
```css
padding: 10px 20px 30px 40px;
```
Which sides get which values?
<details><summary>Answer</summary>
top 10, right 20, bottom 30, left 40 (clockwise from top). Or `padding: 10px 20px` = top/bottom 10, left/right 20.
</details>
