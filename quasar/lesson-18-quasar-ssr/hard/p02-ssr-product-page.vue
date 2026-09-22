<!--
LESSON 18 — Quasar SSR
HARD P02 — SSR E-commerce Product Page
============================================
CONCEPT: Rich product pages prefetch everything in parallel (product,
reviews, related) and ship structured data — a JSON-LD
application/ld+json Product schema — alongside OG/Twitter meta so Google
renders rich snippets.

PROBLEM: A product page: preFetch Promise.all's fetchProduct /
fetchReviews / fetchRelated by route id, stores all three, redirects to
/404 on missing; template shows name/price/description, a reviews list,
related-product cards, loading + error states; export seoMeta with
title, description, og:*, twitter:* and a ld+json Product schema with
offers + aggregateRating.

TRY THIS: script: { type: 'application/ld+json', innerHTML: JSON.stringify({
  '@context': 'https://schema.org/', '@type': 'Product', offers: {...} }) }

EXPECTED OUTPUT: View-source shows the product, reviews, and a parseable
JSON-LD block.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
