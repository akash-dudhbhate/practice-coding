# Lesson 01 — Intuition Checks

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
