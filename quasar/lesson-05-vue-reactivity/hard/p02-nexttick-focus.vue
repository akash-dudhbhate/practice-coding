<!--
LESSON 05 — Vue Reactivity System
HARD P02 — nextTick Focus
============================================
CONCEPT: When you flip a v-if on, the DOM element doesn't exist until Vue
re-renders. await nextTick() pauses until the DOM is updated — only then can
you safely call .focus() on a template ref.

PROBLEM: A `showInput` ref toggled by a q-btn, a q-input wrapped in v-if
with template ref `inputRef`, and an async toggleInput() that awaits
nextTick() before calling inputRef.value.focus().

TRY THIS: showInput.value = true; await nextTick(); inputRef.value?.focus()

EXPECTED OUTPUT: A "Toggle Input" button; clicking reveals the input already
focused, with no "cannot read property of null" errors.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
