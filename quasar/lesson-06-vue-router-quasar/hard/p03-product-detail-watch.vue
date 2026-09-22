<!--
LESSON 06 — Vue Router in Quasar
HARD P03 — Product Detail with Param Watch
============================================
CONCEPT: Navigating /products/1 → /products/2 reuses the same component —
no remount. Watch () => route.params.id and refetch so the page updates in
place. { immediate: true } handles the first load too.

PROBLEM: A product detail page. Mock array of 3 products, fetchProduct(id)
that simulates an async lookup (setTimeout) with loading/error/product
refs, a watch on route.params.id with immediate: true, and buttons calling
router.push to jump between products.

TRY THIS: watch(() => route.params.id, (newId) => { if (newId) fetchProduct(newId) }, { immediate: true })

EXPECTED OUTPUT: Product name/price/description shown after a short
"loading" state; clicking "View Product N" swaps the data without a
remount.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
