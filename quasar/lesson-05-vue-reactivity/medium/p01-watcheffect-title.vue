<!--
LESSON 05 — Vue Reactivity System
MEDIUM P01 — watchEffect document.title
============================================
CONCEPT: watchEffect() runs immediately and auto-tracks every reactive
value read inside its callback. Unlike watch(), you don't list sources and
you don't get old values.

PROBLEM: firstName and lastName refs with q-input fields, plus a
watchEffect that sets document.title to the combined name. Editing either
input should update the browser tab title.

TRY THIS: watchEffect(() => { document.title = `${firstName.value} ${lastName.value}` })

EXPECTED OUTPUT: Two inputs; typing in either one changes the tab title to
"First Last" — proving both deps are auto-tracked.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
