# Lesson 03 — Intuition Checks

## Check 01: Component categories
What types of components does Quasar offer?
<details><summary>Answer</summary>
Buttons, forms, navigation, layout, cards, tables, dialogs, notifications, loading, media, chips, badges, expansion items, tabs, timelines, etc. 100+ components.
</details>

## Check 02: v-model on inputs
```vue
<q-input v-model="text" />
<q-select v-model="selected" />
<q-toggle v-model="checked" />
```
<details><summary>Answer</summary>
All form components support v-model. Two-way binding — input updates state, state updates input.
</details>

## Check 03: Color system
```vue
<q-btn color="primary" />
<q-card class="bg-secondary text-white" />
```
<details><summary>Answer</summary>
Quasar has color tokens: primary, secondary, accent, positive, negative, info, warning. Also arbitrary: `bg-red-5`, `text-blue-3`. Configured in quasar.config.js.
</details>

## Check 04: Slots
```vue
<q-card>
  <template #header>My Header</template>
  <q-card-section>Content</q-card-section>
  <template #actions>
    <q-btn label="OK" />
  </template>
</q-card>
```
<details><summary>Answer</summary>
Slots customize component parts. `#header`, `#actions` are named slots. Default slot for main content.
</details>

## Check 05: Dark mode
```vue
<q-dark style="background: #000">
```
<details><summary>Answer</summary>
`$q.dark.set(true)` programmatically. Or use `class="q-dark"`. Quasar components automatically adapt to dark mode.
</details>
