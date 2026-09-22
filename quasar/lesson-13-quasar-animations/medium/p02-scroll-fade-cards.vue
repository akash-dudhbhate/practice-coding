<!--
LESSON 13 — Quasar Animations & Transitions
MEDIUM P02 — Scroll-Fade Cards (v-intersection)
============================================
CONCEPT: The v-intersection directive fires a callback when an element
enters the viewport; :once makes it fire only the first time. Toggle an
is-visible class to run a CSS opacity/transform transition.

PROBLEM: 5 cards (icon + title + description) starting at opacity:0,
translateY(40px). Each uses v-intersection:once to flip its `visible` flag
(or add a class), animating in once when scrolled into view.

TRY THIS: <div v-for="card in cards" v-intersection:once="onIntersection"
  :class="{ 'is-visible': card.visible }">
.scroll-card { opacity: 0; transform: translateY(40px); transition: ... }

EXPECTED OUTPUT: Cards sit invisible below the fold and fade/slide up one
time as you scroll to each.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
