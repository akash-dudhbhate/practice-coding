# Lesson 08 — Intuition Checks

## Check 01: Units
What's the difference between `em`, `rem`, `px`, `%`?
<details><summary>Answer</summary>
- `px` — absolute pixels
- `em` — relative to parent's font size
- `rem` — relative to root (html) font size
- `%` — relative to parent
</details>

## Check 02: font-weight
```css
.normal { font-weight: 400; }
.bold { font-weight: 700; }
```
<details><summary>Answer</summary>
400 = normal, 700 = bold. Range is 100-900. Not all fonts have all weights.
</details>

## Check 03: line-height units
```css
p { line-height: 1.5; }     /* A */
p { line-height: 1.5em; }   /* B */
p { line-height: 24px; }    /* C */
```
<details><summary>Answer</summary>
A (unitless) is best — inherits as a multiplier. B and C are fixed values that don't scale with font size changes.
</details>

## Check 04: font shorthand
```css
font: bold 16px/1.5 Arial, sans-serif;
```
<details><summary>Answer</summary>
Shorthand: weight, size/line-height, family. Must include size and family. Order matters.
</details>

## Check 05: text-align
```css
.center { text-align: center; }
```
What does this center?
<details><summary>Answer</summary>
Centers inline text within the element. Does NOT center the element itself (use margin: auto or flexbox for that).
</details>
