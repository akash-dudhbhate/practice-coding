<!--
LESSON 04 — Vue Composition API
MEDIUM P03 — Timer with Lifecycle Hooks
============================================
CONCEPT: onMounted runs after the component hits the DOM — start timers and
listeners there. onUnmounted runs on teardown — always clear intervals and
remove listeners to avoid leaks.

PROBLEM: A timer. `elapsed` ref in seconds, `running` ref flag, setInterval
to tick every second, clearInterval to stop. Start/Stop buttons, and the
timer auto-starts on mount.

TRY THIS: intervalId = setInterval(() => { elapsed.value++ }, 1000);
onMounted(() => start()); onUnmounted(() => stop())

EXPECTED OUTPUT: "0s" counting up once per second; Stop halts it, Start
resumes it; no ticking after the component unmounts.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
