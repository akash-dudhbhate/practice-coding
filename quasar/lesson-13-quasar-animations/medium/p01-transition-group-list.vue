<!--
LESSON 13 — Quasar Animations & Transitions
MEDIUM P01 — Animated List with TransitionGroup
============================================
CONCEPT: <TransitionGroup tag="div" name="list"> animates each keyed child
on enter/leave/move. Give leaving items position:absolute so the rest slide
into place, and add a .list-move rule for the shuffle.

PROBLEM: An "Add Item" q-btn pushing random items into `items`, a per-item
remove button, all rendered inside TransitionGroup — items slide in from
the left and out to the right.

TRY THIS: .list-enter-from { opacity: 0; transform: translateX(-30px) }
.list-leave-to { opacity: 0; transform: translateX(30px) }
.list-leave-active { position: absolute }

EXPECTED OUTPUT: Adding slides a row in from the left; removing slides it
right while siblings glide into the gap.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
