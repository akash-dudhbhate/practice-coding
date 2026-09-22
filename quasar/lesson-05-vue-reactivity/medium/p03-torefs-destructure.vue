<!--
LESSON 05 — Vue Reactivity System
MEDIUM P03 — toRefs Destructuring
============================================
CONCEPT: Destructuring a reactive() object directly breaks reactivity — you
get plain values. toRefs() converts each property to a ref that stays linked
to the source, so const { name } = toRefs(form) stays live.

PROBLEM: A reactive `form` ({ name, email }). Destructure it with toRefs,
bind both to q-input fields via v-model, display them, and watch the
destructured `name` ref to log changes.

TRY THIS: const { name, email } = toRefs(form);
watch(name, (newVal, oldVal) => console.log(...))

EXPECTED OUTPUT: Two inputs showing the values; typing updates the display
and fires the watcher — reactivity survived destructuring.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
