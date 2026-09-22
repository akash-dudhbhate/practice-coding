<!--
LESSON 13 — Quasar Animations & Transitions
HARD P01 — Animated FAQ Accordion
============================================
CONCEPT: q-expansion-item already animates open/close (and rotates its
expand icon). Accordion behavior = track each item's expanded flag and
close every other item when one opens.

PROBLEM: A bordered q-list of 5 FAQs rendered with q-expansion-item
(v-model on each faq.expanded, question as label, answer inside). An
update handler closes all other items so only one is open at a time; add a
highlight class on the expanded header.

TRY THIS: <q-expansion-item v-for="(faq, i) in faqs" v-model="faq.expanded"
  :label="faq.question" @update:model-value="closeOthers(i)">
closeOthers: faqs.value.forEach((f, idx) => { if (idx !== i) f.expanded = false })

EXPECTED OUTPUT: Clicking a question slides its answer open and slides any
other open answer shut; the open header is highlighted.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
