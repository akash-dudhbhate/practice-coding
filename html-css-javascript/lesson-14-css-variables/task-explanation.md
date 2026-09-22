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

   ```
   WHAT IT SHOULD LOOK LIKE:
   [  Button  ]      <- --primary background, --radius corners
   +-----------+
   | Card      |     <- --spacing padding, --radius corners
   +-----------+
   [ input   ]       <- same --radius corners
   (edit ONE variable -> all three restyle together)
   ```
2. `easy/p02-solve.html` — Create a button using `var(--btn-bg, #ccc)` with a fallback. Then define the variable so it uses the custom color. Show that removing the variable falls back.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ Button ]   <- renders #0066cc (the custom --btn-bg)
   (comment out --btn-bg -> it falls back to gray #ccc)
   ```
3. `easy/p03-solve.html` — Create a card component that uses scoped variables. Define `--card-color` on the card element (not :root) and use it for background and border.

   ```
   WHAT IT SHOULD LOOK LIKE:
   +-----------+    +-----------+
   | blue card |    | pink card |    <- SAME variable name
   +-----------+    +-----------+       (--card-color), a different
                                           value scoped per element
   ```

### Medium
4. `medium/p01-solve.html` — Build a dark/light theme toggle: define light theme variables in `:root`, dark theme in `[data-theme="dark"]`. Add a button that toggles `data-theme` on `<body>` using minimal JS.

   ```
   WHAT IT SHOULD LOOK LIKE:
   LIGHT (before click):        DARK (after click):
   +---------------------+      +#####################+
   | white bg, dark text |      |# dark bg, light txt#|
   | [ Toggle theme ]    |      |# [ Toggle theme ]  #|
   +---------------------+      +#####################+
   ```
5. `medium/p02-solve.html` — Build a page that respects `prefers-color-scheme: dark` automatically. Define both themes. Test by changing OS theme or DevTools emulation.

   ```
   WHAT IT SHOULD LOOK LIKE:
   OS in light mode:            OS in dark mode:
   +---------------------+      +#####################+
   | light page          |      |# page goes dark    #|
   | automatically       |      |# automatically     #|
   +---------------------+      +#####################+
   (no JS -- prefers-color-scheme does the switching)
   ```
6. `medium/p03-solve.html` — Create a design system with CSS variables: color palette (5 colors), spacing scale (5 sizes), font sizes (4 sizes), border radius (3 sizes). Use them in a sample card and button.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Tokens -> 5 colors / 5 spacings / 4 font sizes / 3 radii
   +-------------------------+
   | Card styled ONLY with   |
   | var(--...) tokens       |
   | [primary btn] [ghost]   |
   +-------------------------+
   ```

### Hard
7. `hard/p01-solve.html` — Build a theme customizer: 3 color pickers (primary, secondary, accent) that update CSS variables via JavaScript. All elements on the page update in real-time. Include a reset button.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Primary:   [#0066cc]   <- color picker
   Secondary: [#6c757d]   <- color picker
   Accent:    [#ff6600]   <- color picker
   +----------------------------------+
   | Sample card recolors INSTANTLY   |
   | as you drag each picker          |
   +----------------------------------+
   [ Reset ]   <- restores the default palette
   ```
8. `hard/p02-solve.html` — Build a responsive design system: variables for spacing, font-size, and container width that change at 3 breakpoints. Create a sample page (header, cards, footer) that uses only variables. Resize to see values adapt.

   ```
   WHAT IT SHOULD LOOK LIKE:
   MOBILE:                  DESKTOP:
   +--------------+         | +----------------+ |
   | tight space, |         | | roomy spacing, | |  <- the same variables
   | small fonts  |         | | bigger fonts,  | |      redefined at each
   +--------------+         | | wider container| |      breakpoint
                            | +----------------+ |
   ```
9. `hard/p03-solve.html` — Build a multi-theme system: 3 themes (light, dark, high-contrast). Each theme redefines all variables. Theme switcher persists choice in localStorage. Include smooth transitions between themes.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ Light ] [ Dark ] [ High-Contrast ]   <- 3 theme buttons
   +--------------------------+
   | page restyles smoothly   |   <- transitions between themes
   | choice survives refresh  |      (saved in localStorage)
   +--------------------------+
   ```

### How to work
- Write your complete HTML + CSS + JS solution.
- Remove the TODO comment when done.
- Open in browser to test visually.
