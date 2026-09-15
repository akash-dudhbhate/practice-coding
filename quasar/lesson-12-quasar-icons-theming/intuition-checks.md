# Lesson 12 — Intuition Checks

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
