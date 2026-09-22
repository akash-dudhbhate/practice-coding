<!--
LESSON 05 — Vue Reactivity System
HARD P01 — Computed vs Function Filtering
============================================
CONCEPT: A computed() only re-runs when its dependencies change; a plain
function called in the template re-runs on every render. Counting calls in
each proves the caching difference.

PROBLEM: A `filter` ref + q-input, a `computedCalls` and `functionCalls`
counter ref, a computed `computedFiltered` list and a function-based
`functionFiltered` list over the same items array. Display both lists and
both counters.

TRY THIS: const computedFiltered = computed(() => { computedCalls.value++; return items.filter(...) });
increment functionCalls.value inside the function version

EXPECTED OUTPUT: A filter input, both filtered lists, and two counters —
the computed counter stays lower than the function counter as you type.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
