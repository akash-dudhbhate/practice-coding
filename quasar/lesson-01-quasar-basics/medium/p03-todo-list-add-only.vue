<!--
LESSON 01 — Quasar Basics
MEDIUM P03 — List: Add Items
============================================
CONCEPT: A ref holding an array stays reactive — pushing into it
re-renders the template. Looping over the array with a list
directive builds the rows, and q-list / q-item are Quasar's list
components.

PROBLEM: Create an items ref (array of strings) and a newItem ref.
Add a <q-input> bound with v-model="newItem" and an "Add" <q-btn>
that pushes the trimmed input into items and clears the field
(@keyup.enter should add too). Render one <q-item> per entry of the
items array inside a <q-list> (give each a :key).

TRY THIS: type an item and click Add (or press Enter) — it appears
in the list. Optionally show an empty-state message with v-if when
the list is empty.

EXPECTED OUTPUT: an input + Add button; each added entry shows as a
list item below.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
