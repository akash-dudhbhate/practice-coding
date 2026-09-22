<!--
LESSON 04 — Vue Composition API
MEDIUM P02 — Search Filter with watch
============================================
CONCEPT: computed() derives the filtered list; watch() runs a side effect
(like console.log) every time a ref changes. computed is for derived state,
watch is for side effects.

PROBLEM: A `searchQuery` ref bound to a q-input, an `items` ref (array of
strings), a computed `filteredItems` that filters case-insensitively, and a
watch on searchQuery that logs old → new.

TRY THIS: filteredItems = computed(() => items.value.filter(i => i.toLowerCase().includes(query)));
watch(searchQuery, (newVal, oldVal) => console.log(...))

EXPECTED OUTPUT: A search box and a list; typing narrows the list, and each
keystroke logs the change in the console.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
