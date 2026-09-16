<!--
LESSON 04 — Vue Composition API
EASY P02 — Reactive User Object
============================================
CONCEPT: reactive() makes a whole object deeply reactive — you change its
properties directly with no .value. Use reactive() for objects with several
fields, ref() for single primitives.

PROBLEM: A user card. A reactive object `user` with name, email, role.
Display all three inside a q-card. A q-btn that changes user.name.

TRY THIS: const user = reactive({ name: 'John Doe', email: '...', role: '...' });
button @click sets user.name = 'Jane Doe'

EXPECTED OUTPUT: A card showing name, email and a role badge; clicking the
button updates the displayed name.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
