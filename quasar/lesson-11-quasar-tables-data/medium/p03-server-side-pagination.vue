<!--
PROBLEM: Server-Side Pagination (Medium)
=========================================

CONCEPT: QTable @request event — server-side pagination, sorting, and
loading state for large datasets.

TASK: Create a table with server-side pagination. Simulate an API call
(setTimeout) that returns 10 items per page from a large dataset
(100 items). Show loading state during fetch. Handle sorting server-side.

TRY THIS:
- Keep the full 100-item dataset separate from the displayed rows
- Bind a pagination object (page, rowsPerPage, sortBy, descending, rowsNumber)
- Handle the request event: slice + sort the dataset, update rows
- Toggle a loading flag while the simulated fetch runs
- Load the first page when the component mounts

EXPECTED OUTPUT: Table loads page 1 after a short delay (spinner shown).
Changing page or sorting re-fetches the correct slice.

CHECK: python3 check.py medium/p03

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: table wired to @request with loading state -->
  </q-page>
</template>

<script setup>
// TODO: import ref + onMounted; simulate a paginated API
</script>
