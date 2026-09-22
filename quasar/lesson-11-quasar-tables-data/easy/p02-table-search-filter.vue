<!--
PROBLEM: Table Search Filter (Easy)
====================================

CONCEPT: Filtering table rows with a QInput + debounce, computed filtered rows.

TASK: Add a search filter to the table. Use a QInput with debounce.
Filter the rows by the search term. Display the filter input above the table.

TRY THIS:
- Add a search ref bound to a QInput placed above the table
- Give the input a debounce so filtering doesn't run on every keystroke
- Use a computed value that filters rows when the term is non-empty
- Match the term against name, email, or age (case-insensitive)

EXPECTED OUTPUT: Typing in the search box narrows the table to matching
rows after a short delay; clearing it shows all rows again.

CHECK: python3 check.py easy/p02

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: search input above the table -->
  </q-page>
</template>

<script setup>
// TODO: import ref + computed from 'vue', define search/columns/rows
</script>
