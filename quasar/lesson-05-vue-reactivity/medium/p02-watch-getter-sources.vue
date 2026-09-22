<!--
LESSON 05 — Vue Reactivity System
MEDIUM P02 — watch with Getter + Multiple Sources
============================================
CONCEPT: To watch one property of a reactive() object, pass a getter:
watch(() => state.count, ...). To watch several things at once, pass an
array of getters and get arrays of old/new values back.

PROBLEM: A reactive `state` ({ count, name }). Watch state.count via a
getter and log old → new. Also watch [count, name] together. Buttons to
increment count and change name.

TRY THIS: watch(() => state.count, (n, o) => console.log(...));
watch([() => state.count, () => state.name], ([nc, nn], [oc, on]) => ...)

EXPECTED OUTPUT: Count and name displayed with two buttons; each click
logs old and new values from both watchers.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
