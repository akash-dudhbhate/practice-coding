# lesson-01-quasar-basics — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: What is Quasar?
<details><summary>Answer</summary>
Vue.js framework for building cross-platform apps (SPA, PWA, SSR, mobile, desktop). Material Design components. One codebase, multiple platforms.
</details>

## Check 02: Quasar vs plain Vue
<details><summary>Answer</summary>
Quasar adds: 100+ Material Design components, responsive layout system, platform-specific builds (Cordova, Electron), plugins (notify, dialog), icon sets. Saves time vs building from scratch.
</details>

## Check 03: q-btn props
```vue
<q-btn label="Save" color="primary" icon="save" @click="save" />
```
<details><summary>Answer</summary>
`label` — button text. `color` — Quasar color token. `icon` — Material icon. `@click` — click handler. Many more: `outline`, `flat`, `round`, `size`, `disable`.
</details>

## Check 04: quasar.config.js
What does this file do?
<details><summary>Answer</summary>
Central configuration: framework plugins, icon set, CSS, build settings, PWA/SSR/mobile config. The heart of a Quasar project.
</details>

## Check 05: Auto-import
How does Quasar auto-import components?
<details><summary>Answer</summary>
Quasar's build system auto-imports components and directives when used in templates. No manual imports needed. Configured in quasar.config.js.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Missing Quasar Import
```vue
<template>
  <q-btn label="Click" />
</template>
```
<details><summary>Answer</summary>
**Bug:** Quasar components need the framework imported. If not auto-imported, component won't render.
**Fix:** Ensure `app.use(Quasar)` in main.js, or configure auto-import in quasar.config.js.
</details>

## Debug 02 (Medium: Wrong Component Name
```vue
<q-button label="Click" />
```
<details><summary>Answer</summary>
**Bug:** Component is `q-btn`, not `q-button`. Quasar uses abbreviated names.
**Fix:** `<q-btn label="Click" />`.
</details>

## Debug 03 (Hard: CSS Not Loading
```javascript
// quasar.config.js
framework: { css: false }  // Quasar CSS disabled
```
<details><summary>Answer</summary>
**Bug:** CSS disabled — components render unstyled.
**Fix:** Remove `css: false` or set to true (default).
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Wrong component names
```vue
<!-- WRONG -->
<q-button>
<!-- CORRECT -->
<q-btn>
```

## Mistake 02: Not using Quasar CLI
```bash
# WRONG — manual setup
npm install quasar
# CORRECT — use CLI
npm i -g @quasar/cli
quasar create my-app
```

## Mistake 03: Modifying quasar.config.js incorrectly
```javascript
// Always restart dev server after changing config
# quasar dev
```

## Mistake 04: Not using Quasar components
```vue
<!-- WRONG — reinventing the wheel -->
<button class="my-btn">
<!-- CORRECT — use Quasar -->
<q-btn>
```

## Mistake 05: Ignoring Material Design guidelines
```css
/* Quasar follows Material Design */
/* Don't fight it with custom CSS */
/* Use Quasar's theming system */
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): HTML Button
### Before
```vue
<button class="btn-primary" @click="save">Save</button>
```
### After
```vue
<q-btn label="Save" color="primary" icon="save" @click="save" />
```

## Refactor 02 (Medium): Manual Setup
### Before
```bash
npm install vue quasar
# configure manually
```
### After
```bash
quasar create my-app
```

## Refactor 03 (Hard): No Layout System
### Before
```vue
<div class="header">...</div>
<div class="sidebar">...</div>
<div class="content">...</div>
```
### After
```vue
<q-layout view="hHh lpR fFf">
  <q-header>...</q-header>
  <q-drawer>...</q-drawer>
  <q-page-container><q-page>...</q-page></q-page-container>
</q-layout>
```

---

## Approach Comparison — different ways to solve it

## Problem: Create Button

### Approach 1: HTML button
```vue
<button class="btn-primary" @click="handle">Save</button>
```
**Cons:** Need to style, no Material Design, inconsistent.

### Approach 2: q-btn
```vue
<q-btn label="Save" color="primary" icon="save" @click="handle" />
```

**Winner:** Approach 2 — styled, consistent, accessible.

---

## Problem: Project Setup

### Approach 1: Manual Vue + Quasar
```bash
npm install vue quasar
# configure manually
```

### Approach 2: Quasar CLI
```bash
quasar create my-app
```

**Winner:** Approach 2 — handles everything, best practices.
