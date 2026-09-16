<!--
LESSON 18 — Quasar SSR
EASY P02 — SSR-Aware Component
============================================
CONCEPT: process.env.SERVER is true while rendering in Node,
process.env.CLIENT in the browser. window/document don't exist on the
server — touch them only inside onMounted(), which never runs during SSR.

PROBLEM: A component that: reads process.env.SERVER/CLIENT into refs,
shows a banner saying whether it rendered on the SERVER or CLIENT, and
fills a client-only info card (viewport size, user agent, platform) inside
onMounted — with a spinner while that's null. Log on both sides.

TRY THIS: const isServer = ref(process.env.SERVER)
onMounted(() => { clientInfo.value = { viewport: `${window.innerWidth}×${window.innerHeight}` } })

EXPECTED OUTPUT: Page source shows the SERVER banner; after hydration the
client card appears — no "window is not defined" crash.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
