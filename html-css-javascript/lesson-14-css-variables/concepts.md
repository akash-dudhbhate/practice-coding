# Lesson 14 — Concepts Explained (CSS Variables / Custom Properties)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## CSS Custom Properties (Variables)

**What:** CSS variables let you store values and reuse them throughout your stylesheet.

```css
:root {
    --primary-color: #007bff;
    --spacing: 16px;
    --font-size: 1rem;
}

.button {
    background: var(--primary-color);
    padding: var(--spacing);
    font-size: var(--font-size);
}

.card {
    padding: var(--spacing);
    border: 2px solid var(--primary-color);
}
```

**Why it exists:** Without CSS variables, you repeat `#007bff` in 50 places. To change the primary color, you search-and-replace → miss some → inconsistent. CSS variables define once, use everywhere. Change the variable → all references update.

**Where it's used:** Design systems, themes, spacing scales, color palettes, responsive breakpoints, any value used more than once.

**What goes wrong without it:**
- Hardcoding colors everywhere → changing the brand color requires editing 100 lines → error-prone.
- `var(--name)` with no fallback → if variable is undefined, the property is invalid → element unstyled. Use `var(--name, fallback)`.
- CSS variables are case-sensitive: `--Primary` ≠ `--primary`. Be consistent.

---

## :root and Scope

**What:** CSS variables have scope. `:root` makes them global. Declaring inside a selector scopes them to that element and its children.

```css
:root {
    --color: blue;        /* global — available everywhere */
}

.card {
    --color: red;         /* scoped to .card and its children */
    background: var(--color);  /* red */
}

.sidebar {
    background: var(--color);  /* blue (from :root, not .card) */
}
```

**Why it exists:** Without scoping, all variables are global → can't have different values in different contexts. Scoping lets `.dark-theme` override `--bg-color` for just that section → theme variations.

**Where it's used:** Theme switching (dark/light), component variants, section-specific styling.

**What goes wrong without it:**
- Variable in `:root` vs in a selector → the selector version overrides for that subtree. Forgetting this → confused why a variable has a different value in one section.
- `:root` is the same as `html` but with higher specificity. Use `:root` for global variables.
- Variables cascade like other CSS — a variable on `body` applies to all children unless overridden.

---

## var() with Fallbacks

**What:** `var()` can take a second argument as a fallback if the variable is not defined.

```css
.element {
    /* Use --primary if defined, otherwise use #007bff */
    color: var(--primary, #007bff);

    /* Nested fallbacks */
    color: var(--primary, var(--default, black));
}
```

**Why it exists:** Without fallbacks, an undefined variable → invalid CSS → element unstyled. Fallbacks ensure the element still looks reasonable even if the variable is missing.

**Where it's used:** Third-party components (you don't control their variables), progressive enhancement, defensive CSS.

**What goes wrong without it:**
- `var(--undefined)` with no fallback → `color: ` is invalid → element uses inherited/default color → unexpected.
- Fallback is only used if the variable is UNDEFINED, not if it's empty. `--color: ;` → `var(--color, red)` → uses the empty value (invalid), NOT the fallback.
- Nested fallbacks work but get complex. Keep it to one level if possible.

---

## Theming with CSS Variables

**What:** Switch between themes by changing variable values.

```css
:root {
    --bg: #ffffff;
    --text: #333333;
    --card-bg: #f5f5f5;
}

[data-theme="dark"] {
    --bg: #1a1a1a;
    --text: #ffffff;
    --card-bg: #2a2a2a;
}

body {
    background: var(--bg);
    color: var(--text);
}
.card {
    background: var(--card-bg);
}
```

```html
<body data-theme="dark">
    <!-- All variables use dark theme values -->
</body>
```

**Why it exists:** Without CSS variables, theming requires duplicating all CSS for each theme → huge stylesheets. With variables, you only redefine the variables → one set of styles, multiple themes.

**Where it's used:** Dark/light mode, user-customizable themes, white-label products, seasonal themes.

**What goes wrong without it:**
- Forgetting to override ALL necessary variables in the theme → some elements keep the old theme → inconsistent.
- Theme switch requires JS to change `data-theme` attribute → without JS, theme can't toggle. Use `prefers-color-scheme` media query for system-based theming.
- Transition between themes → add `transition: background 0.3s, color 0.3s` for smooth theme switching.

---

## prefers-color-scheme (System Theme)

**What:** Detect the user's OS theme preference (dark/light) and apply it automatically.

```css
:root {
    --bg: white;
    --text: black;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #1a1a1a;
        --text: white;
    }
}

body {
    background: var(--bg);
    color: var(--text);
}
```

**Why it exists:** Without this, users who set their OS to dark mode still get a light-themed site → jarring. `prefers-color-scheme` respects the user's system preference → automatic dark mode.

**Where it's used:** Every modern website. Users expect dark mode to follow their OS setting.

**What goes wrong without it:**
- Only using a manual toggle → users have to set it on every site → annoying. Combine: auto-detect + manual override.
- Forgetting to set `color-scheme: light dark` in CSS → form controls (scrollbars, inputs) don't adapt → looks wrong.
- Testing: DevTools → Rendering → Emulate CSS media feature `prefers-color-scheme`.

---

## Responsive Variables

**What:** Change variable values at different breakpoints.

```css
:root {
    --spacing: 16px;
    --font-size: 1rem;
}

@media (min-width: 768px) {
    :root {
        --spacing: 24px;
        --font-size: 1.125rem;
    }
}

@media (min-width: 1024px) {
    :root {
        --spacing: 32px;
        --font-size: 1.25rem;
    }
}

/* All elements using var(--spacing) automatically adapt */
```

**Why it exists:** Without responsive variables, you repeat media queries for every element → verbose. With variables, one media query changes the variable → all references adapt automatically.

**Where it's used:** Responsive spacing, fluid typography, responsive border-radius, any value that changes per breakpoint.

**What goes wrong without it:**
- Overriding too many variables per breakpoint → hard to track what changes where. Keep it to key values.
- Forgetting that variable changes cascade → all children get the new value → sometimes unexpected.

---

## JavaScript and CSS Variables

**What:** Read and set CSS variables from JavaScript.

```javascript
// Read a variable
const color = getComputedStyle(document.documentElement)
    .getPropertyValue('--primary-color');
// → "#007bff"

// Set a variable
document.documentElement.style.setProperty('--primary-color', '#ff0000');
// All elements using var(--primary-color) now use red

// Set on a specific element
element.style.setProperty('--local-var', 'value');
```

**Why it exists:** Without JS access, CSS variables are static (defined in CSS only). JS access enables dynamic theming — user picks a color → JS updates the variable → entire UI changes instantly.

**Where it's used:** Theme customizers, color pickers, dynamic font size, user preferences, real-time style updates.

**What goes wrong without it:**
- `getPropertyValue` returns a string with leading space → `trim()` it.
- Setting a variable on `document.documentElement` (the `:root`) → global change. Setting on an element → scoped change.
- Removing a variable: `element.style.removeProperty('--name')` → falls back to the value from a higher scope or the fallback in `var()`.

---

## Building a Design System with Variables

**What:** Organize variables into a structured system:

```css
:root {
    /* Colors */
    --color-primary: #007bff;
    --color-primary-dark: #0056b3;
    --color-primary-light: #e7f1ff;
    --color-danger: #dc3545;
    --color-success: #28a745;

    /* Spacing scale */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 48px;

    /* Typography */
    --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-mono: 'Fira Code', monospace;
    --text-sm: 0.875rem;
    --text-base: 1rem;
    --text-lg: 1.25rem;
    --text-xl: 1.5rem;

    /* Borders */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 16px;

    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 8px rgba(0,0,0,0.1);
    --shadow-lg: 0 8px 16px rgba(0,0,0,0.15);

    /* Transitions */
    --transition: 0.3s ease;
}
```

**Why it exists:** Without a design system, every component uses ad-hoc values → inconsistent spacing, colors, fonts. A variable-based system ensures consistency → change one variable → all components update.

**Where it's used:** Every professional codebase. Material Design, Tailwind, Bootstrap all use variable-based systems.

**What goes wrong without it:**
- Inconsistent values → `padding: 15px` in one place, `16px` in another → looks sloppy.
- Too many variables → hard to remember. Group them logically and keep the set manageable.
- Not using the variables → defining them but hardcoding values in components → defeats the purpose.
