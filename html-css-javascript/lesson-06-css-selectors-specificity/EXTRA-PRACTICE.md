# lesson-06-css-selectors-specificity — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Specificity
Rank these by specificity (lowest to highest):
- `div`
- `.class`
- `#id`
- `div.class`
<details><summary>Answer</summary>
`div` (0,0,1) < `.class` (0,1,0) < `div.class` (0,1,1) < `#id` (1,0,0).
</details>

## Check 02: Combinators
What do ` `, `>`, `+`, `~` mean?
<details><summary>Answer</summary>
- ` ` (space) — descendant (any depth)
- `>` — direct child only
- `+` — adjacent sibling (immediately after)
- `~` — general sibling (any sibling after)
</details>

## Check 03: Pseudo-class vs pseudo-element
What's the difference between `:hover` and `::before`?
<details><summary>Answer</summary>
`:hover` is a pseudo-class (selects an element in a specific state). `::before` is a pseudo-element (creates a new virtual element). Single colon vs double colon (though `:` works for both in older CSS).
</details>

## Check 04: Universal selector
```css
* { margin: 0; }
```
What does `*` do?
<details><summary>Answer</summary>
Selects ALL elements. Common in CSS resets. Can be slow — use sparingly.
</details>

## Check 05: :not()
```css
.button:not(.disabled) { cursor: pointer; }
```
<details><summary>Answer</summary>
Selects `.button` elements that do NOT have `.disabled` class. Useful for excluding specific cases.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Wrong Selector
```css
p .text { color: red; }
```
**Hint:** Space means descendant. No space means something else.
<details><summary>Answer</summary>
**Bug:** `p .text` selects elements with class "text" INSIDE `<p>`. If you want `<p class="text">`, use `p.text` (no space).
</details>

## Debug 02 (Medium): Specificity War
```css
#header .title { color: blue; }
.title { color: red; }
```
Which wins for `<div id="header"><h1 class="title">Hi</h1></div>`?
<details><summary>Answer</summary>
Blue wins — `#header .title` has specificity (1,1,0) vs `.title` (0,1,0). ID beats class.
</details>

## Debug 03 (Hard): !important Overuse
```css
.text { color: red !important; }
#header .text { color: blue; }
```
<details><summary>Answer</summary>
Red wins — `!important` overrides specificity. This is why `!important` is a code smell. Avoid it.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Overusing IDs for styling
```css
/* WRONG — IDs are too specific, hard to override */
#header { color: blue; }
/* CORRECT — use classes */
.header { color: blue; }
```

## Mistake 02: !important everywhere
```css
/* WRONG — specificity war */
.text { color: red !important; }
/* CORRECT — fix specificity */
.header .text { color: red; }
```

## Mistake 03: Deep selectors
```css
/* WRONG — brittle */
.header nav ul li a { color: blue; }
/* CORRECT — use a class */
.nav-link { color: blue; }
```

## Mistake 04: Confusing descendant and child
```css
div p { }  /* any <p> inside <div> at any depth */
div > p { } /* only <p> that are direct children of <div> */
```

## Mistake 05: Tag-qualified classes
```css
/* WRONG — less reusable */
div.container { }
/* CORRECT */
.container { }
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): var Instead of const/let
### Before
```javascript
var x = 5;
var name = "John";
```
### After
```javascript
const x = 5;
const name = "John";
// let only if reassigned
```

## Refactor 02 (Medium): Function Instead of Arrow
### Before
```javascript
const nums = [1, 2, 3];
const doubled = nums.map(function(n) { return n * 2; });
```
### After
```javascript
const doubled = nums.map(n => n * 2);
```

## Refactor 03 (Hard): Manual Loop vs Array Methods
### Before
```javascript
const result = [];
for (let i = 0; i < arr.length; i++) {
  if (arr[i] > 0) result.push(arr[i] * 2);
}
```
### After
```javascript
const result = arr.filter(n => n > 0).map(n => n * 2);

---

## Approach Comparison — different ways to solve it

## Problem: Style Navigation Links

### Approach 1: Deep selector
```css
header nav ul li a { color: blue; }
```
**Cons:** Brittle — any HTML change breaks it.

### Approach 2: Class
```css
.nav-link { color: blue; }
```
**Pros:** Decoupled from HTML structure.

**Winner:** Approach 2 — classes are more maintainable.

---

## Problem: Override a Style

### Approach 1: !important
```css
.text { color: red !important; }
```
**Cons:** Creates arms race.

### Approach 2: Increase specificity
```css
.parent .text { color: red; }
```

**Winner:** Approach 2 — manage specificity, don't use !important.
