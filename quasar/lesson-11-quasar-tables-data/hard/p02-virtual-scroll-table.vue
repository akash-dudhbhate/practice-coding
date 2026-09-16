<!--
PROBLEM: Virtual Scroll Table — 10,000 Rows (Hard)
===================================================

CONCEPT: QTable virtual scrolling — rendering only visible rows for huge
datasets, plus a filter that still works with virtual scroll.

TASK: Build a table with virtual scrolling: 10,000 rows of generated data.
Enable virtual scroll. Show smooth scrolling. Add a search filter that
works with virtual scroll. Display row count.

TRY THIS:
- Generate 10,000 rows with Array.from
- Turn on virtual scroll and set an item size; disable pagination
  (zero rows-per-page) so scrolling handles everything
- Give the table a fixed height via style
- Filter the computed rows the same way as a normal table
- Show the filtered row count in a badge

EXPECTED OUTPUT: Buttery-smooth scrolling through 10k rows; searching
instantly narrows results and the count badge updates.

CHECK: python3 check.py hard/p02

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: search + count badge + virtual-scroll table -->
  </q-page>
</template>

<script setup>
// TODO: generate 10k rows; computed filtered rows
</script>
