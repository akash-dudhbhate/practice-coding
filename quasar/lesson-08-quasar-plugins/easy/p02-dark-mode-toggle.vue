<!--
LESSON 08 — Quasar Plugins
EASY P02 — Dark Mode Toggle
============================================
CONCEPT: $q.dark controls app-wide dark mode: .toggle() flips it, .set(bool)
forces it, .isActive reads the current state (reactive — wrap in computed).

PROBLEM: A dark mode card showing the current state ("Dark"/"Light") from
$q.dark.isActive, plus a q-btn calling $q.dark.toggle() with a label/icon
that flips with the state.

TRY THIS: const darkActive = computed(() => $q.dark.isActive);
function toggleDark() { $q.dark.toggle() }

EXPECTED OUTPUT: The state text and button label update as dark mode flips
on and off.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
