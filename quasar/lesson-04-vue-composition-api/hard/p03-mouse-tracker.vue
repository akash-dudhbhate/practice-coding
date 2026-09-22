<!--
LESSON 04 — Vue Composition API
HARD P03 — Mouse Position Tracker
============================================
CONCEPT: window event listeners are added in onMounted and removed in
onUnmounted — the handler must be a named function so removeEventListener
can find it. A template ref (ref="..." + a ref(null) in script) gives you
the raw DOM element.

PROBLEM: A mouse tracker. `mouseX`/`mouseY` refs updated by a 'mousemove'
listener, a named handleMouseMove function, listener add/remove in the
lifecycle hooks, a div with a template ref `boxRef`, and its offsetWidth
logged on mount.

TRY THIS: window.addEventListener('mousemove', handleMouseMove) in onMounted;
window.removeEventListener('mousemove', handleMouseMove) in onUnmounted;
boxRef.value.offsetWidth

EXPECTED OUTPUT: A dashed box showing live "Mouse X" / "Mouse Y" values;
the console logs the box width once on mount.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
