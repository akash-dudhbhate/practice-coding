# Lesson 14 — CSS Variables (Custom Properties)

## What you'll learn
- Defining and using CSS custom properties
- :root and variable scope
- var() with fallback values
- Theming (dark/light mode) with variables
- prefers-color-scheme for system theme
- Responsive variables (per breakpoint)
- JavaScript interaction with CSS variables
- Building a design system

## Lesson

### Define and use
```css
:root { --primary: #007bff; --spacing: 16px; }
.btn { background: var(--primary); padding: var(--spacing); }
```

### Dark mode
```css
[data-theme="dark"] { --bg: #1a1a1a; --text: white; }
body { background: var(--bg); color: var(--text); }
```

### JS interaction
```javascript
document.documentElement.style.setProperty('--primary', '#ff0000');
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a page with 3 CSS variables (--primary, --spacing, --radius). Use them in at least 3 elements (button, card, input).
2. `easy/p02-solve.html` — Create a button using `var(--btn-bg, #ccc)` with a fallback. Then define the variable so it uses the custom color. Show that removing the variable falls back.
3. `easy/p03-solve.html` — Create a card component that uses scoped variables. Define `--card-color` on the card element (not :root) and use it for background and border.

### Medium
4. `medium/p01-solve.html` — Build a dark/light theme toggle: define light theme variables in `:root`, dark theme in `[data-theme="dark"]`. Add a button that toggles `data-theme` on `<body>` using minimal JS.
5. `medium/p02-solve.html` — Build a page that respects `prefers-color-scheme: dark` automatically. Define both themes. Test by changing OS theme or DevTools emulation.
6. `medium/p03-solve.html` — Create a design system with CSS variables: color palette (5 colors), spacing scale (5 sizes), font sizes (4 sizes), border radius (3 sizes). Use them in a sample card and button.

### Hard
7. `hard/p01-solve.html` — Build a theme customizer: 3 color pickers (primary, secondary, accent) that update CSS variables via JavaScript. All elements on the page update in real-time. Include a reset button.
8. `hard/p02-solve.html` — Build a responsive design system: variables for spacing, font-size, and container width that change at 3 breakpoints. Create a sample page (header, cards, footer) that uses only variables. Resize to see values adapt.
9. `hard/p03-solve.html` — Build a multi-theme system: 3 themes (light, dark, high-contrast). Each theme redefines all variables. Theme switcher persists choice in localStorage. Include smooth transitions between themes.

### How to work
- Write your complete HTML + CSS + JS solution.
- Remove the TODO comment when done.
- Open in browser to test visually.
