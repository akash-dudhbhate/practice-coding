<!--
LESSON 13 — Quasar Animations & Transitions
HARD P03 — Complete Loading Experience
============================================
CONCEPT: Combine the pieces: a top loading bar, a skeleton grid during
load, then real content fading in — all animated only with transform and
opacity (GPU-accelerated; will-change hints help).

PROBLEM: A `loading` ref driving: an indeterminate q-linear-progress pinned
to the top, a 4-card skeleton grid inside a fade <Transition>, a matching
content grid (q-img + text) in another fade Transition, a 2s setTimeout
that flips loading and fires a success $q.notify, and a Reload button.

TRY THIS: <Transition name="fade"><div v-if="loading">...skeletons...</div></Transition>
<Transition name="fade"><div v-if="!loading">...content...</div></Transition>
will-change: opacity, transform

EXPECTED OUTPUT: Loading bar + waving skeletons for 2s, a fade swap to real
cards, a "Content loaded" toast, and Reload replays it all.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
