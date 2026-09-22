<!--
LESSON 08 — Quasar Plugins
MEDIUM P02 — Responsive Grid via $q.screen
============================================
CONCEPT: $q.screen knows the current breakpoint: .xs, .sm, .md, .name,
.width, .height — all reactive. Pair it with Quasar's col-* grid classes
(col-12 col-sm-6 col-md-4) for a responsive layout.

PROBLEM: A grid of ~9 q-cards that is 1 column on xs, 2 on sm, 3 on md+,
plus a badge showing the current breakpoint name read from $q.screen.

TRY THIS: class="col-12 col-sm-6 col-md-4" on each grid cell;
computed returning 'xs' / 'sm' / 'md+' from $q.screen

EXPECTED OUTPUT: Cards reflow as the window resizes; the badge always shows
the live breakpoint.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
