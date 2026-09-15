# Lesson 15 — Intuition Checks

## Check 01: :hover vs :focus
Why do you need :focus styles?
<details><summary>Answer</summary>
Keyboard users navigate with Tab. `:focus` shows where they are. `:hover` only works with mouse. Always provide `:focus` (or `:focus-visible`).
</details>

## Check 02: ::before and ::after
```css
.quote::before { content: "\""; }
.quote::after { content: "\""; }
```
<details><summary>Answer</summary>
Adds quotation marks before and after. Pseudo-elements create virtual elements. Need `content` property to render.
</details>

## Check 03: :nth-child vs :nth-of-type
```css
li:nth-child(2) { }     /* A */
li:nth-of-type(2) { }   /* B */
```
<details><summary>Answer</summary>
A — 2nd child of its parent (regardless of type). B — 2nd `<li>` of its parent. Use nth-of-type when parent has mixed element types.
</details>

## Check 04: :not()
```css
a:not(.external) { color: blue; }
```
<details><summary>Answer</summary>
Styles all links EXCEPT those with class "external". Useful for exceptions.
</details>

## Check 05: :focus-visible
```css
:focus { outline: 2px solid blue; }        /* A */
:focus-visible { outline: 2px solid blue; } /* B */
```
<details><summary>Answer</summary>
`:focus` shows outline for ALL focus (mouse click too). `:focus-visible` only shows for keyboard focus. B is better — no outline for mouse users.
</details>
