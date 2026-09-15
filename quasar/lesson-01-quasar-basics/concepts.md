# Lesson 01 — Concepts Explained (Quasar Basics)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Quasar q-page

**What:** In Quasar, every page component must wrap its content in `<q-page>`.

```html
<template>
  <q-page>
    <h1>Welcome</h1>
  </q-page>
</template>
```

**Why it exists:** Quasar has a layout system (header, drawer, footer). `<q-page>` integrates with this system — it provides proper spacing, scrolling, and positioning within the layout. Without it, your content may overlap with the header or not scroll correctly.

**Where it's used:** Every page component in a Quasar app. No exceptions.

**What goes wrong without it:**
- Content displays but with broken spacing — overlaps with header/footer.
- Scrolling may not work correctly within the layout.
- Quasar's layout system doesn't recognize the page → drawer/header interactions break.

---

## Vue Single-File Component (.vue)

**What:** A Vue component file has three sections:

```vue
<template>       <!-- HTML structure (what renders on screen) -->
  <h1>Hello</h1>
</template>

<script setup>   <!-- JavaScript logic (state, functions) -->
  import { ref } from 'vue'
</script>

<style scoped>   <!-- CSS (optional, scoped = only this component) -->
</style>
```

`<script setup>` is the modern Vue 3 way (Composition API).

**Why it exists:** Before SFCs, Vue components were split across 3 files (HTML, JS, CSS) or defined as string templates. SFCs keep everything for one component in one file — easier to find, edit, and understand. The `scoped` attribute prevents CSS from leaking to other components.

**Where it's used:** Every Vue/Quasar component. This is the standard way to write Vue 3.

**What goes wrong without it:**
- Splitting template/script/style into separate files → harder to maintain, more imports.
- Using Options API (old style) instead of `<script setup>` → more boilerplate, harder to read, less tree-shakeable.
- Forgetting `<template>` → nothing renders. Forgetting `<script setup>` → no logic works.

---

## Quasar q-btn Component

**What:** Quasar's button component — styled and feature-rich.

```html
<q-btn label="Click me" color="primary" @click="handleClick" />
```

Key props: `label` (text), `color` (background), `icon`, `disable`.
Events: `@click` fires when clicked.

**Why it exists:** Quasar provides pre-styled, cross-platform buttons so you don't write CSS for every button. They handle ripple effects, loading states, icons, and accessibility automatically.

**Where it's used:** Every button in a Quasar app — forms, toolbars, dialogs, navigation.

**What goes wrong without it:**
- Using raw `<button>` → no Quasar styling, no ripple effect, inconsistent across platforms.
- Missing `@click` → button does nothing when clicked.
- Using `disabled` instead of `:disable` → Quasar's prop is `disable`, not the HTML attribute `disabled`.

---

## Quasar Component Props

**What:** Quasar components accept props to customize appearance/behavior.

```html
<q-btn label="Save" color="primary" />
```

Props are passed as attributes, like HTML attributes but with camelCase or kebab-case.

**Why it exists:** Without props, every button looks identical. Props let you customize without writing custom CSS — one component, many configurations.

**Where it's used:** Every Quasar component accepts props for colors, sizes, icons, behavior.

**What goes wrong without it:**
- Using wrong prop names → silently ignored, no error, just default styling.
- Using string for boolean props: `disable="false"` → it's the string "false" which is truthy → button is disabled! Use `:disable="false"`.
- Not using `:` prefix for dynamic values → `color="myColor"` sets color to literal string "myColor", not the variable's value.

---

## ref() — Reactive State

**What:** `ref()` creates a reactive variable — when it changes, Vue automatically updates the UI.

```javascript
import { ref } from 'vue'
const count = ref(0)       // initial value 0
count.value++              // change it in script (use .value)
```

```html
{{ count }}                <!-- use it in template (no .value needed) -->
```

**Why it exists:** Without reactivity, you'd have to manually update the DOM every time data changes. `ref()` makes Vue watch the variable — change it, and the UI updates automatically. This is the core of Vue's magic.

**Where it's used:** Every component that has state — counters, form inputs, toggles, fetched data.

**What goes wrong without it:**
- Using a plain variable (`let count = 0`) → changing it does NOT update the UI. No reactivity.
- Forgetting `.value` in script → `count++` throws error (count is a ref object, not a number). Must use `count.value++`.
- Using `.value` in template → `{{ count.value }}` shows the raw object. Vue auto-unwraps in template, so just use `{{ count }}`.

---

## v-if — Conditional Rendering

**What:** `v-if` shows/hides an element based on a condition. If false, the element is NOT in the DOM.

```html
<p v-if="isVisible">You can see me!</p>
<p v-else>Hidden message</p>
```

**Why it exists:** UIs need to show different things based on state — loading vs. loaded, logged in vs. logged out, error vs. success. `v-if` lets you conditionally render without JavaScript DOM manipulation.

**Where it's used:** Loading states, error messages, auth-gated content, toggles, tabs.

**What goes wrong without it:**
- Using CSS `display: none` instead → element is still in DOM → screen readers still read it → accessibility issue.
- `v-if` vs `v-show`: `v-if` removes from DOM (better for rarely-changed content), `v-show` just hides with CSS (better for frequently-toggled content). Using the wrong one → performance issues.
- `v-if` and `v-for` on the same element → Vue warns against this (v-if has higher precedence). Use a computed property to filter first.

---

## Quasar q-input Component

**What:** Quasar's text input component — styled with built-in features.

```html
<q-input v-model="name" label="Your name" />
```

Key props: `v-model` (two-way binding), `label` (floating label), `type` (text, password, number), `disable`.

**Why it exists:** Quasar inputs come with floating labels, validation styling, error messages, and consistent cross-platform appearance. You'd spend hours building this with raw HTML + CSS.

**Where it's used:** Every form in a Quasar app — login, registration, search, settings.

**What goes wrong without it:**
- Using raw `<input>` → no Quasar styling, no floating labels, no built-in validation display.
- Forgetting `v-model` → input doesn't connect to any data → typing does nothing useful.
- Using `value` instead of `v-model` → one-way binding, user input doesn't update your data.

---

## v-model — Two-Way Binding

**What:** `v-model` creates a two-way connection between an input and a ref: user types → ref updates; ref changes → input updates.

```javascript
const text = ref("")
```
```html
<q-input v-model="text" />
<!-- user types "hello" → text.value becomes "hello" -->
<!-- you set text.value = "world" → input shows "world" -->
```

**Why it exists:** Without two-way binding, you'd need to: add an `@input` event listener, read the input value, update the ref, then manually update the input when the ref changes. `v-model` does all of this in one directive.

**Where it's used:** Every form input — text fields, checkboxes, radio buttons, selects, sliders.

**What goes wrong without it:**
- One-way binding only → user types but your data doesn't update → form submission fails.
- Forgetting `v-model` → input is disconnected, you can't read what the user typed.
- Using `v-model` on wrong element type → each input type has specific v-model behavior. Check Quasar docs.

---

## Reactive Display

**What:** When you display a ref in the template, Vue automatically updates the display whenever the ref changes.

```javascript
const name = ref("Akash")
```
```html
<p>Hello, {{ name }}!</p>   <!-- shows "Hello, Akash!" -->
<!-- name.value = "Bob" → template automatically updates to "Hello, Bob!" -->
```

**Why it exists:** Without reactive display, you'd manually update the DOM every time data changes (`document.getElementById('name').textContent = newName`). Vue does this automatically — you change data, UI follows.

**Where it's used:** Every template that displays reactive data — counters, names, lists, computed values.

**What goes wrong without it:**
- Using a plain variable → UI shows initial value forever, never updates.
- Forgetting `{{ }}` → `Hello, name!` renders literal text "name!" not the variable.
- Complex expressions in template → hard to debug. Move to computed properties instead.

---

## Multiple Event Handlers

**What:** A component can have multiple `@click` handlers on different elements, each calling a different function.

```html
<q-btn @click="increment" label="+" />
<q-btn @click="decrement" label="-" />
<q-btn @click="reset" label="Reset" />
```

**Why it exists:** Real UIs have many interactive elements, each with different behavior. Multiple handlers let each element trigger its own logic.

**Where it's used:** Forms (submit/reset), counters (inc/dec), lists (add/remove/edit), toolbars.

**What goes wrong without it:**
- One handler trying to do everything → massive if/else checking which button was clicked → messy.
- Forgetting `@click` → button looks clickable but does nothing.
- Calling function with wrong arguments → `@click="increment(5)"` when function expects no args → error or unexpected behavior.

---

## Computed Display / Dynamic Binding

**What:** You can compute values in the template and bind props dynamically using `:` prefix.

```html
<h2>{{ count }}</h2>
<p>{{ count * 2 }}</p>
<q-btn :disable="count === 0" label="-" />
```

The `:` tells Vue: "this is JavaScript, evaluate it." Without `:`, it's a literal string.

**Why it exists:** Props often depend on state — disable a button when count is 0, change color based on status. Dynamic binding lets you compute prop values from your reactive data.

**Where it's used:** Conditional disabling, dynamic colors/sizes, computed display values.

**What goes wrong without it:**
- `disable="count === 0"` → sets disable to literal string "count === 0" (truthy) → button always disabled.
- Must use `:disable="count === 0"` → Vue evaluates the expression → button disabled only when count is 0.
- Complex expressions in `:prop` → hard to debug. Move to computed properties.

---

## Quasar q-list and q-item

**What:** Quasar's list components for displaying collections.

```html
<q-list>
  <q-item v-for="todo in todos" :key="todo.id">
    {{ todo.text }}
  </q-item>
</q-list>
```

`q-list` = container, `q-item` = each individual item.

**Why it exists:** Lists are everywhere — todo lists, settings menus, search results. Quasar's list components provide consistent styling, spacing, and interaction patterns (swipe, slide, expand).

**Where it's used:** Todo lists, navigation menus, settings pages, search results, chat messages.

**What goes wrong without it:**
- Using raw `<ul>/<li>` → no Quasar styling, inconsistent with the rest of the app.
- Forgetting `v-for` → only one item renders, or you hardcode multiple `q-item`s → not dynamic.
- Missing `:key` in `v-for` → Vue warnings, rendering bugs when list changes.

---

## Reactive Arrays

**What:** A ref can hold an array. When you modify it, Vue updates the UI.

```javascript
const todos = ref([])
todos.value.push({ text: "Buy milk" })  // add item → UI updates
todos.value.splice(index, 1)            // remove item → UI updates
```

**Why it exists:** Most real apps deal with lists of data — todos, users, messages. Reactive arrays let you add/remove items and have the UI update automatically.

**Where it's used:** Todo lists, shopping carts, message threads, search results.

**What goes wrong without it:**
- Using a plain array → UI doesn't update when you add/remove items.
- Mutating array incorrectly → `todos.value[todos.value.length] = newItem` → Vue may not detect the change. Use `.push()` instead.
- Reassigning instead of mutating → `todos = newArray` → error (todos is a ref, use `todos.value = newArray`).

---

## v-for — List Rendering

**What:** `v-for` loops through an array and renders an element for each item.

```html
<div v-for="item in items" :key="item.id">
  {{ item.name }}
</div>
```

ALWAYS include `:key` with a unique value. You can also get the index: `v-for="(item, index) in items"`.

**Why it exists:** You often don't know how many items there are at compile time. `v-for` handles any number of items dynamically — 0, 1, or 1000.

**Where it's used:** Rendering any list — todos, users, products, messages, menu items.

**What goes wrong without it:**
- Missing `:key` → Vue warnings, items get confused when list reorders/inserts/deletes.
- Using index as key when list reorders → Vue attaches state to wrong item → bugs.
- `v-for` and `v-if` on same element → Vue processes v-if first → may skip items unexpectedly. Use a computed property to filter.

---

## Filtering Arrays

**What:** `.filter()` returns a new array with only items matching a condition.

```javascript
const allTodos = ref([{ text: "A", done: false }, { text: "B", done: true }])
// In template:
v-for="todo in allTodos.filter(t => !t.done)"  // only incomplete todos
```

**Why it exists:** You often need to show a subset of data — incomplete todos, active users, products in stock. `.filter()` lets you show only matching items without modifying the original array.

**Where it's used:** Todo filters (all/active/completed), search results, category filters.

**What goes wrong without it:**
- Modifying the original array to filter → you lose data permanently.
- Filtering in template on every render → performance issue for large lists. Use a computed property instead.
- Wrong filter condition → `filter(t => t.done)` shows COMPLETED when you wanted INCOMPLETE.

---

## Quasar q-card

**What:** A card is a container with visual border/shadow for grouping content.

```html
<q-card>
  <q-card-section>
    <h3>Title</h3>
  </q-card-section>
  <q-card-section>
    <p>Content goes here</p>
  </q-card-section>
</q-card>
```

**Why it exists:** Cards group related information visually — a profile card, a product card, a summary card. They provide consistent spacing, shadows, and borders without custom CSS.

**Where it's used:** Profile displays, product listings, dashboards, summary panels, result cards.

**What goes wrong without it:**
- Using raw `<div>` → no visual grouping, no shadow, inconsistent spacing.
- Forgetting `q-card-section` → content touches card edges → looks cramped.
- Too many cards → visual clutter. Use cards for distinct groupings, not every piece of content.

---

## Quasar q-color

**What:** A color picker that lets users choose a color visually.

```html
<q-color v-model="color" />
```
```javascript
const color = ref("#1976d2")   // hex color string
```

**Why it exists:** Letting users pick colors with a text input (typing hex codes) is terrible UX. A visual color picker is intuitive and prevents invalid color values.

**Where it's used:** Theme customization, design tools, settings pages, any app where users choose colors.

**What goes wrong without it:**
- Text input for colors → users type "blue" or "1976d2" (missing #) → invalid → broken styling.
- Not binding with `v-model` → user picks a color but you can't read the value.
- Forgetting to use the color value → picker works but nothing changes in the UI.

---

## Reactive Style Binding (:style)

**What:** Bind styles dynamically — when the bound value changes, the style updates automatically.

```html
<div :style="{ backgroundColor: color }">Preview</div>
```

The style object uses camelCase CSS properties: `{ backgroundColor: "red", fontSize: "14px" }`.

**Why it exists:** Styles often depend on data — preview a chosen color, highlight a selected item, show progress. Dynamic binding lets styles react to state changes.

**Where it's used:** Color pickers, progress bars, theme switching, highlighting, dynamic sizing.

**What goes wrong without it:**
- Using CSS string syntax: `style="background-color: red"` → static, can't react to data changes.
- Using CSS property names: `:style="{ background-color: color }"` → syntax error (hyphen). Must use camelCase `backgroundColor`.
- Not wrapping in object: `:style="color"` → Vue tries to parse "color" as a style string → broken.

---

## Validation Logic

**What:** Before moving to the next step or submitting, check if input is valid.

```javascript
function nextStep() {
  if (name.value === "") return;   // don't proceed if empty
  step.value++;
}
```
```html
<q-btn @click="nextStep" :disable="name === ''" label="Next" />
```

**Why it exists:** Without validation, users submit empty forms, invalid emails, negative ages → garbage data in your database → broken downstream systems. Validation catches errors before they cause damage.

**Where it's used:** Every form — registration, checkout, settings, search filters.

**What goes wrong without it:**
- Empty required fields → server errors, database constraints violated.
- Invalid email format → emails bounce, users can't reset passwords.
- Wrong data type (string in number field) → calculations crash.
- No feedback to user → they don't know what's wrong → frustration → abandonment.
