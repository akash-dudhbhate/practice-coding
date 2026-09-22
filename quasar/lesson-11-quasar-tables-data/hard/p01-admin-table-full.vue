<!--
PROBLEM: Complete Admin Table (Hard)
=====================================

CONCEPT: Everything combined — search, sorting, pagination, selection,
custom cells, CSV export, loading and empty states.

TASK: Build a complete admin table: 100 users, search filter, sortable
columns, pagination (10/page), row selection with bulk delete, custom
cells (status badge, actions), and CSV export button. Include loading
and empty states.

TRY THIS:
- Toolbar row: search input, export button, bulk-delete button
- Simulate loading 100 users on mount (loading flag + delay)
- Status column -> colored badge; actions column -> edit/delete buttons
- Export: build CSV text from filtered rows, download via Blob + anchor
- Empty state: no-data slot with an icon and message

EXPECTED OUTPUT: A full-featured admin grid. Search filters instantly,
columns sort, selection enables bulk delete, Export CSV downloads a file,
and a friendly message shows when nothing matches.

CHECK: python3 check.py hard/p01

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: toolbar + full-featured table -->
  </q-page>
</template>

<script setup>
// TODO: ref/computed/onMounted + useQuasar; search, selection, CSV export
</script>
