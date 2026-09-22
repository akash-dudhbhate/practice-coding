<!--
LESSON 01 — Quasar Basics
MEDIUM P02 — Counter with Increment / Decrement / Reset
============================================
CONCEPT: Multiple @click handlers can mutate the same ref. The
:disable prop bound to a condition grays out a button when an
action isn't allowed.

PROBLEM: Create a count ref starting at 0 and display it big. Add
THREE <q-btn> components — Increment (@click="count++"), Decrement
(@click="count--") with :disable="count === 0" so it can't go
negative, and Reset (@click="count = 0").

TRY THIS: click Increment and Decrement — at 0 the Decrement button
should disable. Give each button a different color.

EXPECTED OUTPUT: a number with three buttons; decrement is disabled
at zero, reset returns the count to 0.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
