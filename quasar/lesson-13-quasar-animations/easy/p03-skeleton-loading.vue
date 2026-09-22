<!--
LESSON 13 — Quasar Animations & Transitions
EASY P03 — Skeleton Loading Card
============================================
CONCEPT: q-skeleton renders animated placeholder shapes (type, height,
width, animation="wave") that should mirror the real content's geometry —
a 200px image block plus a few text lines.

PROBLEM: A card showing skeletons while `loading` is true (image-sized
skeleton + text skeletons), real content (q-img, title, paragraph) when
false. loading starts true; onMounted flips it after a 2s setTimeout.

TRY THIS: <template v-if="loading"><q-skeleton height="200px" square animation="wave" />...
onMounted(() => { setTimeout(() => loading.value = false, 2000) })

EXPECTED OUTPUT: A waving skeleton card for 2 seconds, then the real image,
title and text pop in.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
