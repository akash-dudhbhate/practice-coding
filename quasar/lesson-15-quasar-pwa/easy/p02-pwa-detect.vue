<!--
LESSON 15 — Quasar PWA
EASY P02 — Detect Standalone PWA Mode
============================================
CONCEPT: window.matchMedia('(display-mode: standalone)').matches is true
when running as an installed PWA. Listen to its 'change' event to react if
the display mode flips, and clean the listener up on unmount.

PROBLEM: A component showing a banner — "Running as PWA" when standalone,
"Running in browser" otherwise — with matching icon/color. Check on mount
and keep it updated via the media query change listener.

TRY THIS: const isPWA = ref(window.matchMedia('(display-mode: standalone)').matches);
mq.addEventListener('change', check) in onMounted, removeEventListener in onUnmounted

EXPECTED OUTPUT: An info banner in the browser, a positive "installed"
banner when launched from the home screen.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
