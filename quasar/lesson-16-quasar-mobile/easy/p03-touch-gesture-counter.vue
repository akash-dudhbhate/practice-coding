<!--
LESSON 16 — Quasar Mobile (Capacitor)
EASY P03 — Touch Gesture Counter
============================================
CONCEPT: Quasar touch directives attach gesture handlers declaratively:
v-touch-swipe.left / .right for swipes, v-touch-hold for long-press. Add
touch-action: none + user-select: none on the target so the browser
doesn't fight the gesture.

PROBLEM: A counter in a dashed touch area — swipe left decrements, swipe
right increments, long-press resets. An instruction card explains the
gestures; the count renders big.

TRY THIS: <div v-touch-swipe.left="decrement" v-touch-swipe.right="increment"
  v-touch-hold="reset" class="touch-area">...

EXPECTED OUTPUT: Swiping right bumps the number, left lowers it (not below
0), and a long press zeroes it.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
