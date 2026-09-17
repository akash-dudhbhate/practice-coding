# lesson-09-css-colors-backgrounds — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Invalid Color
```css
.box { color: bluet; }
```
<details><summary>Answer</summary>
**Bug:** Typo "bluet" — invalid color. Property is ignored.
**Fix:** `color: blue` or use hex/rgb.
</details>

## Debug 02 (Medium): Opacity Affects Children
```css
.panel { opacity: 0.5; }
```
<details><summary>Answer</summary>
**Bug:** `opacity` affects the element AND all children. Text becomes hard to read.
**Fix:** Use `rgba()` for background only: `background: rgba(0,0,0,0.5)`.
</details>

## Debug 03 (Hard): Background Not Covering
```css
.hero { background: url("bg.jpg"); height: 500px; }
```
<details><summary>Answer</summary>
**Bug:** Image may not cover the area, leaving gaps or repeating.
**Fix:** `background-size: cover; background-position: center;`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: opacity for backgrounds
```css
/* WRONG — affects children too */
.panel { opacity: 0.5; }
/* CORRECT */
.panel { background: rgba(255,255,255,0.5); }
```

## Mistake 02: No background-size
```css
/* WRONG — image repeats or doesn't cover */
.hero { background: url("bg.jpg"); }
/* CORRECT */
.hero { background: url("bg.jpg") center/cover no-repeat; }
```

## Mistake 03: Hardcoded colors
```css
/* WRONG — repeated everywhere */
.btn { background: #007bff; }
.link { color: #007bff; }
/* CORRECT — use variables */
:root { --primary: #007bff; }
.btn { background: var(--primary); }
```

## Mistake 04: Bad contrast
```css
/* WRONG — unreadable */
.text { color: #ccc; background: #ddd; }
```

## Mistake 05: Too many colors
```css
/* WRONG — rainbow */
/* CORRECT — 3-5 colors max in a palette */
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): for Loop to forEach
### Before
```javascript
for (let i = 0; i < arr.length; i++) { console.log(arr[i]); }
```
### After
```javascript
arr.forEach(item => console.log(item));
```

## Refactor 02 (Medium): Manual Object Creation
### Before
```javascript
const user = {};
user.name = "John";
user.age = 30;
user.email = "john@example.com";
```
### After
```javascript
const user = { name: "John", age: 30, email: "john@example.com" };
```

## Refactor 03 (Hard): Nested Loops to Map/Filter
### Before
```javascript
const result = [];
for (const user of users) {
  for (const post of user.posts) {
    if (post.published) result.push(post);
  }
}
```
### After
```javascript
const result = users.flatMap(u => u.posts).filter(p => p.published);
```

---

## Approach Comparison — different ways to solve it

## Problem: Semi-transparent Background

### Approach 1: opacity
```css
.panel { opacity: 0.5; }
```
**Cons:** Makes text transparent too.

### Approach 2: rgba
```css
.panel { background: rgba(0,0,0,0.5); }
```
**Pros:** Only background is transparent.

**Winner:** Approach 2 — use rgba for transparent backgrounds.

---

## Problem: Color Theming

### Approach 1: Hardcoded
```css
.btn { background: #007bff; }
```
**Cons:** Hard to change, no consistency.

### Approach 2: CSS variables
```css
:root { --primary: #007bff; }
.btn { background: var(--primary); }
```

**Winner:** Approach 2 — variables enable theming and consistency.
