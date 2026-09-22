<!--
LESSON 05 — Vue Reactivity System
EASY P03 — Computed Caching Proof
============================================
CONCEPT: computed() caches its result and only re-runs when a dependency
changes. Put a console.log inside it — even rendered twice in the template,
it logs once per change, not once per render.

PROBLEM: firstName and lastName refs, a computed `fullName` with a
console.log inside, displayed in TWO places, plus inputs for both names and
a button that changes firstName.

TRY THIS: const fullName = computed(() => { console.log('computed called'); return `${firstName.value} ${lastName.value}` })

EXPECTED OUTPUT: The full name shown twice; typing or clicking the button
updates both spots while the console logs only once per actual change.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
