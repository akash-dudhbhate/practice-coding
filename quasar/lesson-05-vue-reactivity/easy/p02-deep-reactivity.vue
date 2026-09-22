<!--
LESSON 05 — Vue Reactivity System
EASY P02 — Deep Reactivity
============================================
CONCEPT: reactive() is deep by default — nested objects are wrapped in
proxies too, so changing user.profile.settings.theme still triggers a UI
update. No extra work needed for nesting.

PROBLEM: A reactive `user` object nested three levels deep
(user.profile.settings.theme). Display the theme and add a q-btn that
toggles it between 'light' and 'dark'.

TRY THIS: user.profile.settings.theme = user.profile.settings.theme === 'light' ? 'dark' : 'light'

EXPECTED OUTPUT: "Theme: light" displayed; clicking the button flips it to
"dark" (and back), proving deep changes are tracked.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
