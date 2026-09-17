# lesson-12-quasar-icons-theming — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Icon sets
<details><summary>Answer</summary>
Material Icons (default), Font Awesome, Ionicons, EV Icons, Bootstrap Icons. Set in quasar.config.js. Can use any via `<q-icon name="img:/path.png" />`.
</details>

## Check 02: Theming
```scss
// quasar.variables.scss
$primary: #1976d2;
$secondary: #26a69a;
$negative: #c10015;
```
<details><summary>Answer</summary>
SCSS variables define theme colors. Used by all Quasar components. Change once, applies everywhere. Restart dev server after change.
</details>

## Check 03: Dark mode
```javascript
$q.dark.set(true);  // enable
$q.dark.set(false); // disable
$q.dark.toggle();   // toggle
$q.dark.isActive;   // check
```
<details><summary>Answer</summary>
Programmatic dark mode. Components auto-adapt. Persist preference in localStorage.
</details>

## Check 04: Brand colors
```vue
<q-btn color="primary" />
<q-btn color="red-5" />
```
<details><summary>Answer</summary>
Named colors (primary, secondary) from theme. Numbered colors (red-5) from Material palette. Custom colors via CSS classes.
</details>

## Check 05: CSS variables vs SCSS
<details><summary>Answer</summary>
SCSS — compile-time, set in quasar.variables.scss. CSS vars — runtime, can change dynamically. Use SCSS for theme, CSS vars for dynamic theming.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01: Wrong Icon Set
```javascript
// quasar.config.js
iconSet: 'fontawesome-v6'
// but not installed
```
<details><summary>Answer</summary>
**Bug:** Icon set not installed. Icons won't show.
**Fix:** `npm i @quasar/extras` and configure properly.
</details>

## Debug 02: CSS Variables Not Applied
```css
:root { --q-primary: #ff0000; }
```
<details><summary>Answer</summary>
**Bug:** Quasar uses `$primary` in SCSS, not CSS variables directly. Need to set in quasar.variables.scss.
**Fix:** Edit `src/css/quasar.variables.scss`: `$primary: #ff0000;`.
</details>

## Debug 03: Dark Mode Not Toggling
```javascript
$q.dark.toggle(); // nothing happens
```
<details><summary>Answer</summary>
**Bug:** Dark mode CSS not imported. Need `@import 'quasar/src/css/index.sass'` or dark mode extras.
**Fix:** Ensure dark mode is enabled in config.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not installing icon extras
```bash
npm i @quasar/extras
# Then configure in quasar.config.js
```

## Mistake 02: Editing wrong file for theme
```css
/* WRONG — custom CSS */
/* CORRECT — quasar.variables.scss */
```

## Mistake 03: Not restarting after theme change
```bash
# SCSS changes require restart
quasar dev
```

## Mistake 04: Hardcoding colors
```vue
<!-- WRONG -->
<q-btn style="background: #1976d2" />
<!-- CORRECT -->
<q-btn color="primary" />
```

## Mistake 05: Not persisting dark mode
```javascript
// Save preference
watch(() => $q.dark.isActive, (val) => {
  localStorage.setItem('dark', val);
});
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Hardcoded Colors
### Before
```vue
<q-btn style="background: #1976d2" />
```
### After
```vue
<q-btn color="primary" />
```

## Refactor 02 (Medium): CSS Overrides
### Before
```css
.q-btn { background: red !important; }
```
### After
```scss
$primary: #ff0000;
```

## Refactor 03 (Hard: Manual Dark Mode
### Before
```css
.dark { background: #000; color: #fff; }
```
### After
```javascript
$q.dark.set(true);
```

---

## Approach Comparison — different ways to solve it

## Problem: Theming

### Approach 1: CSS overrides
```css
.q-btn { background: red !important; }
```
**Cons:** Fragile, breaks on updates.

### Approach 2: SCSS variables
```scss
$primary: #ff0000;
```

**Winner:** Approach 2 — official, clean, applies everywhere.

---

## Problem: Dark Mode

### Approach 1: Manual CSS
```css
.dark-theme { background: #000; color: #fff; }
```

### Approach 2: $q.dark
```javascript
$q.dark.set(true);
```

**Winner:** Approach 2 — auto-adapts all components.
