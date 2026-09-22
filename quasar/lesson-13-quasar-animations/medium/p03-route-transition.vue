<!--
LESSON 13 — Quasar Animations & Transitions
MEDIUM P03 — Route Transition Wrapper
============================================
CONCEPT: Wrapping <router-view /> in <Transition name="..." mode="out-in">
animates page changes — out-in makes the old page finish leaving before the
new one enters, so they never overlap.

PROBLEM: 3 nav buttons (Home/About/Contact via `to`), a named slide-fade
Transition with mode="out-in" around <router-view />, and the matching
enter/leave CSS (translateX + opacity).

TRY THIS: <Transition name="slide-fade" mode="out-in"><router-view /></Transition>
.slide-fade-enter-from { transform: translateX(20px); opacity: 0 }

EXPECTED OUTPUT: Clicking nav buttons slides the current page out left while
the next fades in from the right.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
