<!--
LESSON 06 — Vue Router in Quasar
EASY P03 — Query Params + router.push
============================================
CONCEPT: Query strings (?q=vue&page=1) live in route.query — same reactivity
as params. useRouter() gives you router.push() to navigate with new query
values without reloading.

PROBLEM: A search results page reading route.query.q and route.query.page,
displayed as text, plus a "Next Page" q-btn that calls router.push with the
same path and page + 1 in the query.

TRY THIS: const searchTerm = computed(() => route.query.q || '');
router.push({ path: route.path, query: { q: route.query.q, page: currentPage + 1 } })

EXPECTED OUTPUT: "Search term: X / Page: N" shown; clicking Next Page bumps
the page number in the URL and on screen.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
