<!--
LESSON 05 — Vue Reactivity System
EASY P01 — ref vs reactive Side by Side
============================================
CONCEPT: ref() wraps a single primitive — you touch it with .value in the
script. reactive() wraps an object — you touch its properties directly. Both
update the UI automatically.

PROBLEM: A `title` ref (string) and a `book` reactive object ({ author,
year }). Display all three values, plus one q-btn that updates them all.

TRY THIS: const title = ref('Vue 3 Guide'); const book = reactive({ author: '...', year: 2020 });
updateAll() sets title.value and book.author / book.year

EXPECTED OUTPUT: Title, author and year displayed; clicking "Update All"
changes all three at once.

CHECK: python3 check.py easy/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
