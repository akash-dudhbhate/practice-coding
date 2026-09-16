<!--
LESSON 04 — Vue Composition API
HARD P01 — useCounter Composable
============================================
CONCEPT: A composable is just a function that packages reactive state plus
the functions that change it, and returns them. Name it use* and destructure
what it returns inside <script setup>.

PROBLEM: An inline composable `useCounter()` returning { count, double,
increment, decrement, reset } — double is a computed of count * 2. Use it in
the component and wire the buttons.

TRY THIS: function useCounter() { ...; return { count, double, increment, decrement, reset } }
const { count, double, increment, decrement, reset } = useCounter()

EXPECTED OUTPUT: The count, a "Doubled: X" line, and Decrement / Reset /
Increment buttons that all work.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
