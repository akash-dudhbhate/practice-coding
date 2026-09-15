# Lesson 12 — Concepts Explained (Quasar Icons & Theming)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Quasar Icons (Material, FontAwesome, etc.)

**What:** Quasar supports multiple icon libraries — Material Icons (default), FontAwesome, Ionicons, etc.

```vue
<!-- Material Icons (default) -->
<q-icon name="home" />
<q-icon name="settings" size="24px" color="primary" />

<!-- FontAwesome -->
<q-icon name="fab fa-facebook" />
<q-icon name="fas fa-coffee" size="32px" />

<!-- In buttons -->
<q-btn icon="add" label="Add Item" />
<q-btn flat icon="delete" color="negative" />

<!-- Size variants -->
<q-icon name="star" size="xs" />
<q-icon name="star" size="md" />
<q-icon name="star" size="xl" />
<q-icon name="star" size="2rem" />
```

**Why it exists:** Icons improve UX — visual cues are faster to recognize than text. Quasar integrates multiple libraries → consistent API → no need to set up each library separately.

**Where it's used:** Buttons, navigation, lists, alerts, anywhere visual cues help.

**What goes wrong without it:**
- Using FontAwesome icons without installing the library → blank icon. Install: `npm install @fortawesome/fontawesome-free`.
- Icon name typo → blank icon. Check the icon name on the library's website.
- Not setting `size` → default size might be too small/large. Use explicit sizes.

---

## Configuring Icon Sets

**What:** Set the default icon library in `quasar.config.js`.

```js
// quasar.config.js
export default configure(function(ctx) {
    return {
        framework: {
            iconSet: 'material-icons',  // default
            // or: 'fontawesome-v6', 'ionicons-v4', etc.
            // Auto-import: Quasar installs the icon set automatically
        },
        // For FontAwesome, add to extras:
        extras: [
            ctx.themeConfig.brand === 'fontawesome-v6'
                ? '@fortawesome/fontawesome-free'
                : 'material-icons',
        ]
    }
})
```

**Why it exists:** Different projects use different icon libraries. Quasar lets you choose → consistent icons across the app → no mixing.

**Where it's used:** Project setup — configured once in `quasar.config.js`.

**What goes wrong without it:**
- Mixing icon libraries → inconsistent look → unprofessional. Pick one and stick with it.
- Not importing the CSS for the icon library → icons don't render. Check `extras` in config.
- Changing icon set after development → all icon names might change → lots of refactoring.

---

## Theming with CSS Variables (Brand Colors)

**What:** Quasar uses CSS variables for brand colors → customize the entire app's look.

```css
/* src/css/quasar.variables.scss */
$primary   : #1976d2;
$secondary : #26a69a;
$accent    : #9c27b0;
$dark      : #1d1d1d;
$positive  : #21ba45;
$negative  : #c10015;
$info      : #31ccec;
$warning   : #f2c037;
```

```vue
<!-- Use brand colors -->
<q-btn color="primary" label="Primary" />
<q-btn color="negative" label="Delete" />
<q-card class="bg-primary text-white">...</q-card>

<!-- Custom CSS using variables -->
<style scoped>
.my-card {
    background: var(--q-primary);
    color: white;
}
</style>
```

**Why it exists:** Without CSS variables, changing the app's color scheme → find and replace in every component. With variables → change one file → entire app updates → consistent theming.

**Where it's used:** Every Quasar app — brand colors define the visual identity.

**What goes wrong without it:**
- Hardcoding colors (`#1976d2`) instead of using `var(--q-primary)` → can't theme globally.
- Too many custom colors → inconsistent palette. Stick to the 8 brand colors.
- Not testing dark mode → custom colors might clash with dark theme. Test both.

---

## Custom CSS and Scoped Styles

**What:** Add custom styles to components.

```vue
<template>
    <div class="my-component">
        <p class="highlight">Important text</p>
    </div>
</template>

<style scoped>
.my-component {
    padding: 20px;
    border-radius: 8px;
}

.highlight {
    color: var(--q-primary);
    font-weight: bold;
}
</style>

<!-- Global styles (not scoped) -->
<style>
.global-class {
    margin: 0;
}
</style>
```

**Why it exists:** Quasar components cover most needs, but custom styling is sometimes required. Scoped styles prevent leaks → component styles don't affect other components → clean.

**Where it's used:** Every component that needs custom styling.

**What goes wrong without it:**
- `scoped` missing → styles leak globally → affect other components → hard to debug.
- Overriding Quasar's internal classes (`.q-btn`) → breaks with updates. Use your own classes.
- Using `!important` → specificity war → unmaintainable. Fix the selector instead.

---

## Dark Mode Theming

**What:** Quasar handles dark mode automatically — components adapt.

```css
/* Custom dark mode styles */
.my-card {
    background: white;
    color: black;
}

.body--dark .my-card {
    background: var(--q-dark);
    color: white;
}
```

```js
// Toggle dark mode
$q.dark.toggle()

// Check dark mode in CSS
// .body--light → light mode
// .body--dark → dark mode
```

**Why it exists:** Dark mode is a common preference. Quasar adds `.body--dark` class → you can target it in CSS → custom components adapt → consistent dark mode.

**Where it's used:** Custom components that need different styling in dark mode.

**What goes wrong without it:**
- Hardcoding colors → don't adapt to dark mode → white background in dark mode → bad UX.
- Not testing dark mode → text invisible (white on white). Toggle and check every page.
- Forgetting `.body--dark` prefix → style applies in both modes → wrong.

---

## Responsive Design with Quasar

**What:** Quasar provides responsive grid and utility classes.

```vue
<template>
    <!-- Responsive grid -->
    <div class="row q-col-gutter-md">
        <div class="col-12 col-md-6 col-lg-4">
            <q-card>Card 1</q-card>
        </div>
        <div class="col-12 col-md-6 col-lg-4">
            <q-card>Card 2</q-card>
        </div>
    </div>

    <!-- Responsive visibility -->
    <div class="lt-md">Mobile only</div>      <!-- less than md -->
    <div class="gt-sm">Desktop only</div>     <!-- greater than sm -->
    <div class="md-hide">Hidden on md</div>
</template>
```

**Why it exists:** Different screen sizes need different layouts. Quasar's grid (based on CSS Grid) and visibility classes → responsive without media queries → fast.

**Where it's used:** Every layout that adapts to screen size.

**What goes wrong without it:**
- `col-12` → full width on all screens. `col-12 col-md-6` → full on mobile, half on desktop. Forgetting `col-12` → mobile might break.
- `q-col-gutter` missing → cards touch each other → cramped. Always add gutter.
- Visibility classes (`lt-md`, `gt-sm`) → CSS-based → content still in DOM (hidden). For conditional rendering, use `v-if` with `$q.screen`.

---

## Typography and Spacing

**What:** Quasar provides typography and spacing utility classes.

```vue
<!-- Typography -->
<div class="text-h4">Heading 4</div>
<div class="text-subtitle1">Subtitle</div>
<div class="text-body1">Body text</div>
<div class="text-caption">Caption text</div>
<div class="text-weight-bold">Bold text</div>
<div class="text-center">Centered text</div>

<!-- Spacing -->
<div class="q-pa-md">Padding all sides</div>
<div class="q-mt-lg">Margin top large</div>
<div class="q-px-sm">Padding horizontal small</div>
<div class="q-mb-xl">Margin bottom extra large</div>
```

**Why it exists:** Consistent spacing and typography → professional look. Without utilities, every component has different spacing → inconsistent. Quasar's utilities → standard scale → consistent.

**Where it's used:** Every component — use utilities instead of custom CSS for spacing.

**What goes wrong without it:**
- Mixing custom padding (`padding: 15px`) with Quasar classes (`q-pa-md`) → inconsistent scale. Use Quasar classes.
- `q-pa-md` = padding all sides medium. `q-px-md` = padding x-axis (left/right) only. Know the difference.
- Spacing scale: `xs` (4px), `sm` (8px), `md` (16px), `lg` (24px), `xl` (48px). Don't use custom values.

---

## Custom Themes (Multiple Themes)

**What:** Support multiple themes (e.g., brand themes for different clients).

```js
// Dynamically change brand colors
function setTheme(theme) {
    const colors = {
        blue: { primary: '#1976d2', secondary: '#26a69a' },
        green: { primary: '#21ba45', secondary: '#00bcd4' },
        purple: { primary: '#9c27b0', secondary: '#e91e63' },
    }

    const selected = colors[theme]
    document.documentElement.style.setProperty('--q-primary', selected.primary)
    document.documentElement.style.setProperty('--q-secondary', selected.secondary)
}

// In a component:
setTheme('green')  // changes the entire app's primary color
```

**Why it exists:** White-label apps (same app, different branding for different clients) → change colors dynamically → one codebase, multiple brands.

**Where it's used:** SaaS apps with branding, white-label products, theme switchers.

**What goes wrong without it:**
- Setting CSS variables before app loads → flash of wrong theme. Set in `created()` or `beforeMount()`.
- Not persisting the theme → resets on refresh. Save to localStorage.
- Only changing `--q-primary` → other colors (secondary, accent) still old → inconsistent. Change all relevant variables.
