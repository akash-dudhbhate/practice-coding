<!--
LESSON 13 — Quasar Animations & Transitions
EASY P02 — q-slide-transition Expandable Section
============================================
CONCEPT: q-slide-transition animates height for expand/collapse — no CSS
needed. Pair it with v-show (not v-if) so the element stays in the DOM and
can be measured.

PROBLEM: An Expand/Collapse q-btn (label + icon flip with `expanded`) and a
content block wrapped in <q-slide-transition> using v-show="expanded".

TRY THIS: <q-slide-transition><div v-show="expanded" class="expand-content">...</div></q-slide-transition>;
:icon="expanded ? 'expand_less' : 'expand_more'"

EXPECTED OUTPUT: Clicking Expand slides the content open; Collapse slides it
shut, both smoothly.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
