<!--
LESSON 13 — Quasar Animations & Transitions
HARD P02 — Staggered Card Entrance
============================================
CONCEPT: Stagger animations by giving each card animation-delay =
index * 100ms via :style. Start cards at opacity:0 with a @keyframes
animation set to `forwards` so they end visible. GPU-friendly: only
transform and opacity.

PROBLEM: A responsive grid (col-12 col-sm-6 col-md-4) of 6 icon cards that
fade-and-rise in sequence on load (index * 100ms delay), plus a hover
effect scaling the card up with a shadow.

TRY THIS: :style="{ animationDelay: `${index * 100}ms` }"
@keyframes fadeInUp { to { opacity: 1; transform: translateY(0) } }
.stagger-card:hover { transform: scale(1.03) }

EXPECTED OUTPUT: On load the six cards cascade in left-to-right; hovering
one lifts it slightly.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
