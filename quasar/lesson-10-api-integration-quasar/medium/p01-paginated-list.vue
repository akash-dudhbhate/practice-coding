<!--
LESSON 10 — API Integration in Quasar
MEDIUM P01 — Paginated Fetch with Prev/Next
============================================
CONCEPT: Server pagination passes _page and _limit query params; the total
often comes back in a header (x-total-count). watch(page) refetches whenever
the page ref changes — Prev/Next just mutate it.

PROBLEM: A paginated user list: `page`, `totalPages`, PER_PAGE constants,
fetch with ?_page=&_limit=, Prev/Next buttons disabled at the bounds,
"Page X of Y" display, plus loading/error states.

TRY THIS: fetch(`${API}?_page=${page.value}&_limit=${PER_PAGE}`);
totalPages.value = Math.ceil(total / PER_PAGE);
watch(page, fetchPage); onMounted(fetchPage)

EXPECTED OUTPUT: 3 users per page; Next/Prev flip pages with a live
"Page N of M" label, disabled at the ends.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
