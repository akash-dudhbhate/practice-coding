# lesson-14-css-variables — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Variable Not Defined
```css
.btn { background: var(--primary); }
```
<details><summary>Answer</summary>
**Bug:** `--primary` not defined anywhere.
**Fix:** `:root { --primary: #007bff; }`.
</details>

## Debug 02 (Medium): Wrong Scope
```css
.card { --padding: 20px; }
.btn { padding: var(--padding); }
```
<details><summary>Answer</summary>
**Bug:** `--padding` is scoped to `.card`. `.btn` can't access it.
**Fix:** Define in `:root` or a shared parent.
</details>

## Debug 03 (Hard): No Fallback
```css
.box { color: var(--text-color); }
```
<details><summary>Answer</summary>
**Bug:** If `--text-color` isn't defined, color is invalid (defaults to inherited).
**Fix:** `color: var(--text-color, black)`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: No fallback
```css
/* WRONG — breaks if undefined */
color: var(--text);
/* CORRECT */
color: var(--text, #333);
```

## Mistake 02: Wrong scope
```css
/* WRONG — variable scoped too narrowly */
.card { --primary: blue; }
.btn { background: var(--primary); } /* can't access */
/* CORRECT */
:root { --primary: blue; }
```

## Mistake 03: Not using :root
```css
/* WRONG — hard to override */
body { --primary: blue; }
/* CORRECT */
:root { --primary: blue; }
```

## Mistake 04: Overusing variables
```css
/* WRONG — variable for everything */
:root { --color-red: red; --color-blue: blue; }
/* Use variables for theme values, not every value */
```

## Mistake 05: Not organizing variables
```css
/* WRONG — scattered */
:root { --primary: blue; --spacing: 10px; --radius: 4px; }
/* BETTER — grouped */
:root {
  --color-primary: blue;
  --space-md: 10px;
  --radius-sm: 4px;
}
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): var
### Before
```javascript
var x = 1; var y = 2;
```
### After
```javascript
const x = 1; const y = 2;
```

## Refactor 02 (Medium): String Concatenation
### Before
```javascript
const msg = "Hello " + name + ", you are " + age + " years old";
```
### After
```javascript
const msg = `Hello ${name}, you are ${age} years old`;
```

## Refactor 03 (Hard): Manual Object Property
### Before
```javascript
const obj = {};
obj.name = name;
obj.age = age;
obj[x] = value;
```
### After
```javascript
const obj = { name, age, [x]: value };
```

---

## Approach Comparison — different ways to solve it

## Problem: Theming

### Approach 1: Multiple stylesheets
```html
<link rel="stylesheet" href="light.css">
<link rel="stylesheet" href="dark.css" disabled>
```

### Approach 2: CSS variables
```css
:root { --bg: white; --text: black; }
[data-theme="dark"] { --bg: black; --text: white; }
body { background: var(--bg); color: var(--text); }
```

**Winner:** Approach 2 — switch themes by changing one attribute. No stylesheet swapping.

---

## Problem: Spacing System

### Approach 1: Hardcoded
```css
.margin-sm { margin: 8px; }
.margin-md { margin: 16px; }
```

### Approach 2: Variables
```css
:root { --space-sm: 8px; --space-md: 16px; }
.box { margin: var(--space-md); }
```

**Winner:** Approach 2 — change one variable to update all spacing.
