# lesson-12-css-responsive — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Mobile-first vs desktop-first
Which approach is preferred?
<details><summary>Answer</summary>
Mobile-first — start with mobile styles, add `min-width` media queries for larger screens. Forces simplicity and improves mobile performance.
</details>

## Check 02: viewport meta
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
<details><summary>Answer</summary>
`width=device-width` — sets viewport width to device width. `initial-scale=1.0` — no zoom on load. Essential for responsive design.
</details>

## Check 03: rem vs px in media queries
```css
@media (min-width: 48rem) { }  /* A */
@media (min-width: 768px) { }  /* B */
```
<details><summary>Answer</summary>
Both work. px is more common. rem respects user font size settings but browser support varies in media queries.
</details>

## Check 04: max-width
```css
.container { max-width: 1200px; margin: 0 auto; width: 100%; }
```
<details><summary>Answer</summary>
Container is 100% width up to 1200px, then fixed at 1200px and centered. Standard responsive container pattern.
</details>

## Check 05: responsive images
```css
img { max-width: 100%; height: auto; }
```
<details><summary>Answer</summary>
Images scale down to fit container but never scale up beyond natural size. Essential responsive rule.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Missing viewport meta
```html
<head>
  <title>My Site</title>
</head>
```
<details><summary>Answer</summary>
**Bug:** No viewport meta tag — site doesn't scale on mobile.
**Fix:** `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
</details>

## Debug 02 (Medium): Fixed Width
```css
.container { width: 1200px; }
```
<details><summary>Answer</summary>
**Bug:** Fixed width overflows on screens < 1200px.
**Fix:** `max-width: 1200px; width: 100%;`.
</details>

## Debug 03 (Hard): Media Query Order
```css
@media (max-width: 768px) { .box { font-size: 14px; } }
@media (min-width: 1024px) { .box { font-size: 18px; } }
/* What size on a 500px screen? */
```
<details><summary>Answer</summary>
14px — only the max-width: 768px query applies. But on 1024px+, both could apply if not careful. Order matters: mobile-first should use min-width in ascending order.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: No viewport meta
```html
<!-- WRONG — site looks tiny on mobile -->
<!-- CORRECT -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Mistake 02: Fixed widths
```css
/* WRONG */
.container { width: 1200px; }
/* CORRECT */
.container { max-width: 1200px; width: 100%; }
```

## Mistake 03: Desktop-first media queries
```css
/* WRONG — desktop then override for mobile */
.box { font-size: 18px; }
@media (max-width: 768px) { .box { font-size: 14px; } }
/* CORRECT — mobile first */
.box { font-size: 14px; }
@media (min-width: 768px) { .box { font-size: 18px; } }
```

## Mistake 04: Not testing on real devices
```css
/* Always test on actual phones, not just browser dev tools */
```

## Mistake 05: Forgetting responsive images
```css
/* WRONG — images overflow */
img { width: 800px; }
/* CORRECT */
img { max-width: 100%; height: auto; }
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No JSON Parse on Get
### Before
```javascript
const user = localStorage.getItem("user");
const name = JSON.parse(user).name;
```
### After
```javascript
const user = JSON.parse(localStorage.getItem("user") || "{}");
const name = user.name;
```

## Refactor 02 (Medium): Repeated localStorage Code
### Before
```javascript
localStorage.setItem("theme", JSON.stringify(theme));
const t = JSON.parse(localStorage.getItem("theme"));
```
### After
```javascript
const store = {
  get: (k) => JSON.parse(localStorage.getItem(k) || "null"),
  set: (k, v) => localStorage.setItem(k, JSON.stringify(v)),
};
store.set("theme", theme);
const t = store.get("theme");
```

## Refactor 03 (Hard): No Error Handling on Parse
### Before
```javascript
const data = JSON.parse(localStorage.getItem("data"));
```
### After
```javascript
function safeParse(key, fallback = null) {
  try { return JSON.parse(localStorage.getItem(key)); }
  catch { return fallback; }
}
const data = safeParse("data", {});
```

---

## Approach Comparison — different ways to solve it

## Problem: Responsive Navigation

### Approach 1: Media queries
```css
.nav { display: flex; }
@media (max-width: 768px) {
  .nav { flex-direction: column; }
}
```

### Approach 2: Container queries
```css
@container (min-width: 768px) {
  .nav { flex-direction: row; }
}
```

**Winner:** Approach 2 (container queries) for components. Approach 1 for page layout.

---

## Problem: Responsive Font Size

### Approach 1: Media queries
```css
h1 { font-size: 1.5rem; }
@media (min-width: 768px) { h1 { font-size: 2rem; } }
@media (min-width: 1024px) { h1 { font-size: 3rem; } }
```

### Approach 2: clamp()
```css
h1 { font-size: clamp(1.5rem, 5vw, 3rem); }
```

**Winner:** Approach 2 — fluid, no breakpoints.
