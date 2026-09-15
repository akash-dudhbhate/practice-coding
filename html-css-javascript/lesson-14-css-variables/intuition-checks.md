# Lesson 14 — Intuition Checks

## Check 01: Variable scope
```css
:root { --global: blue; }
.card { --local: red; }
```
Where is each accessible?
<details><summary>Answer</summary>
`--global` is accessible everywhere (defined on :root). `--local` only inside `.card` and its children.
</details>

## Check 02: Fallback values
```css
color: var(--missing, #333);
```
<details><summary>Answer</summary>
If `--missing` is not defined, uses `#333`. Good for resilience.
</details>

## Check 03: JS access
```javascript
document.documentElement.style.setProperty('--primary', 'red');
```
<details><summary>Answer</summary>
Sets `--primary` on `:root` via JS. Enables dynamic theming (dark mode toggle, user customization).
</details>

## Check 04: Inheritance
```css
:root { --color: blue; }
.child { color: var(--color); }
```
<details><summary>Answer</summary>
CSS variables inherit like other properties. `--color` defined on :root is available to all descendants.
</details>

## Check 05: calc with variables
```css
:root { --spacing: 10px; }
.box { padding: calc(var(--spacing) * 2); }
```
<details><summary>Answer</summary>
`calc()` works with CSS variables. Result: 20px padding.
</details>
