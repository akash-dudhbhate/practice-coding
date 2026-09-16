<!--
LESSON 09 — Quasar Forms
HARD P02 — Dynamic Add/Remove Fields
============================================
CONCEPT: Model repeatable fields as an array in your form object (e.g.
phones: [{ value: '' }]) and v-for over it. push() adds a field, splice()
removes one — rules still apply per input.

PROBLEM: A form for a dynamic list of phone numbers: each row is a q-input
with required + min-length rules and a remove button (hidden when only one
remains). An "Add Another" button appends a field; submit collects all
values and shows them as JSON.

TRY THIS: form.value.phones.push({ value: '' });
form.value.phones.splice(index, 1);
const phones = form.value.phones.map(p => p.value).filter(Boolean)

EXPECTED OUTPUT: "+ Add" grows the list, "−" shrinks it, validation works
per field, and submit shows the collected array.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
