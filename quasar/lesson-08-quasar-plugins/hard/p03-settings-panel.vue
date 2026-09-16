<!--
LESSON 08 — Quasar Plugins
HARD P03 — Persistent Settings Panel
============================================
CONCEPT: Store settings in a reactive object, save to localStorage on every
change, reload in onMounted and re-apply (e.g. $q.dark.set). One STORAGE_KEY
keeps it tidy; JSON.stringify/parse handles the object.

PROBLEM: A settings panel with: dark-mode q-toggle applied via $q.dark.set,
a notification-position selector (top/bottom/top-right...), a test-notify
button honoring that position, and a loading-spinner color or language
option. All settings persist to localStorage and apply on load.

TRY THIS: const settings = reactive({ darkMode: false, notifyPosition: 'top-right', ... });
onMounted(() => { loadSettings(); $q.dark.set(settings.darkMode) })

EXPECTED OUTPUT: Toggling/choosing persists across refresh; dark mode and
notification position apply immediately and on reload.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
