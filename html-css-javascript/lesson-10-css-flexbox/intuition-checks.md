# Lesson 10 — Intuition Checks

## Check 01: Main vs Cross axis
In `flex-direction: row`, which is the main axis?
<details><summary>Answer</summary>
Horizontal (row) is main axis. Vertical is cross axis. `justify-content` aligns on main axis, `align-items` on cross axis.
</details>

## Check 02: justify-content
```css
justify-content: space-between;
```
What does this do?
<details><summary>Answer</summary>
First item at start, last at end, equal space between. Other values: `flex-start`, `center`, `space-around`, `space-evenly`.
</details>

## Check 03: flex: 1
```css
.item { flex: 1; }
```
What does `flex: 1` mean?
<details><summary>Answer</summary>
`flex: 1` = `flex: 1 1 0` = grow: 1, shrink: 1, basis: 0. Item grows to fill available space equally with other flex:1 items.
</details>

## Check 04: flex-wrap
```css
.container { display: flex; flex-wrap: wrap; }
```
<details><summary>Answer</summary>
Items wrap to new line when they don't fit. Default is `nowrap` (items shrink to fit).
</details>

## Check 05: gap
```css
.container { display: flex; gap: 20px; }
```
<details><summary>Answer</summary>
Adds 20px gap between flex items. Replaces the old margin hacks for spacing.
</details>
