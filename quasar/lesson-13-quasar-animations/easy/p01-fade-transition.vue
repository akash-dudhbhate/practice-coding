<!--
LESSON 13 — Quasar Animations & Transitions
EASY P01 — Fade Transition Toggle
============================================
CONCEPT: Vue's <Transition> component wraps a v-if element and applies
*-enter-active / *-leave-active / *-enter-from / *-leave-to classes. With no
name prop the prefix is "v-" — you write the CSS yourself.

PROBLEM: A Show/Hide q-btn toggling a `visible` ref, a styled box wrapped in
<Transition>, and CSS: .v-enter-active/.v-leave-active transition opacity,
.v-enter-from/.v-leave-to opacity: 0.

TRY THIS: <Transition><div v-if="visible" class="fade-box">...</div></Transition>
.v-enter-active, .v-leave-active { transition: opacity 0.4s ease }

EXPECTED OUTPUT: Clicking the button fades the box in/out over ~0.4s.

CHECK: python3 check.py easy/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
