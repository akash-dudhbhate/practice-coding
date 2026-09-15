# Lesson 12 — Quasar Icons & Theming

## What you'll learn
- Quasar icons (Material, FontAwesome)
- Configuring icon sets
- Theming with CSS variables (brand colors)
- Custom CSS and scoped styles
- Dark mode theming
- Responsive design with Quasar
- Typography and spacing utilities
- Custom themes (multiple themes)

## Lesson

### Icons
```vue
<q-icon name="home" size="24px" color="primary" />
<q-btn icon="add" label="Add" />
```

### Brand colors
```css
$primary: #1976d2;
$negative: #c10015;
```

### Responsive
```vue
<div class="col-12 col-md-6 col-lg-4">...</div>
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a component with 5 different icons (home, settings, user, bell, search). Each icon has a different size and color. Display them in a row with labels.
2. `easy/p02-solve.vue` — Create a component using Quasar typography classes: text-h4 title, text-subtitle1 subtitle, text-body1 paragraph, text-caption note. Use spacing utilities (q-pa-md, q-mt-lg) for layout.
3. `easy/p03-solve.vue` — Create a responsive grid: 3 cards using `col-12 col-md-6 col-lg-4`. Each card has an icon, title, and description. Verify it stacks on mobile and shows 3 columns on desktop.

### Medium
4. `medium/p01-solve.vue` — Customize brand colors in `quasar.variables.scss` (change primary to a custom color). Create a component that uses `color="primary"` in buttons, cards, and icons. Verify the custom color applies.
5. `medium/p02-solve.vue` — Create a component with custom dark mode styles. Use `.body--dark` to change a card's background and text color. Toggle dark mode and verify the styles adapt.
6. `medium/p03-solve.vue` — Create a theme switcher: 3 theme buttons (blue, green, purple). Clicking a button changes `--q-primary` and `--q-secondary` CSS variables dynamically. Persist the selected theme to localStorage.

### Hard
7. `hard/p01-solve.vue` — Build a complete themed dashboard: custom brand colors, responsive grid layout, typography hierarchy, icons in navigation and cards, dark mode support, and spacing utilities throughout. Include at least 6 components.
8. `hard/p02-solve.vue` — Build a white-label theme system: a settings page where users can customize primary, secondary, and accent colors with color pickers. Changes apply live and persist to localStorage. Include a "reset to default" button.
9. `hard/p03-solve.vue` — Build a responsive navigation: top bar on desktop, bottom tabs on mobile (use `lt-md` and `gt-sm` classes). Include icons and labels. Verify it switches automatically on resize. Use Quasar's QLayout and QTabs.

### How to work
- Write your complete Vue/Quasar solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
