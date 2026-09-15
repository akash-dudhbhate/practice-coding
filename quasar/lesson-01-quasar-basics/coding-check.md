# Lesson 01 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-qpage-with-heading.vue
- [ ] Content wrapped in `<q-page>`.
- [ ] `<h1>` with text "Welcome to Quasar".
- [ ] Uses `<script setup>`.

### p02-two-buttons-colors.vue
- [ ] Two `<q-btn>` components.
- [ ] Save button has `color="primary"`.
- [ ] Delete button has `color="negative"`.
- [ ] Wrapped in `<q-page class="flex flex-center">`.

### p03-toggle-visibility.vue
- [ ] `visible` declared with `ref(false)`.
- [ ] Toggle button uses `@click`.
- [ ] `<p>` uses `v-if="visible"`.
- [ ] `ref` imported from 'vue'.

## Medium

### p01-text-input-display.vue
- [ ] `<q-input>` uses `v-model="text"`.
- [ ] `text` declared with `ref("")`.
- [ ] `<p>` shows "You typed: {text}".
- [ ] `<p>` only shows when text is not empty (v-if).

### p02-counter-inc-dec.vue
- [ ] `count` starts at 0.
- [ ] `<h2>` displays count.
- [ ] "+" increments, "-" decrements, "Reset" sets to 0.
- [ ] "-" button uses `:disable="count === 0"`.

### p03-todo-list-add-only.vue
- [ ] `newTodo` and `todos` (array) declared with ref.
- [ ] Add button pushes to `todos` and clears input.
- [ ] `<q-list>` uses `v-for` with `:key`.
- [ ] Each item rendered in `<q-item>`.

## Hard

### p01-todo-complete-delete.vue
- [ ] Todos are objects: `{ text, done }`.
- [ ] Done button toggles `todo.done`.
- [ ] Delete button removes from array.
- [ ] Empty state shows "No todos yet" (v-if).
- [ ] Done todos have line-through style (`:style` binding).

### p02-color-picker-card.vue
- [ ] Uses `<q-card>` and `<q-card-section>`.
- [ ] `<q-color>` bound with `v-model="color"`.
- [ ] `color` starts at "#1976d2".
- [ ] Preview `<div>` uses `:style` with backgroundColor.
- [ ] Reset button sets color back to "#1976d2".

### p03-multi-step-form.vue
- [ ] `step` ref starts at 1.
- [ ] Step 1: name input, Next disabled if empty.
- [ ] Step 2: email input, Next disabled if empty, Back button.
- [ ] Step 3: age input, Submit button.
- [ ] On submit: `submitted` = true, shows summary `<q-card>`.
- [ ] Uses `v-if` to show only current step.

## How to verify

Use the Docker container (see quasar/README.md):
```bash
docker build -t quasar-dev .
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
# Inside container:
quasar create test-app
cp easy/p01-qpage-with-heading.vue test-app/src/pages/Index.vue
cd test-app && quasar dev
```
Open http://localhost:8080 to see your component.
