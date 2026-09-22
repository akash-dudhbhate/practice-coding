<!--
LESSON 17 — Quasar Electron
HARD P03 — Desktop Settings App
============================================
CONCEPT: Desktop settings persist via Electron Store (bridged as
window.electronAPI.settings.get/set) with a localStorage fallback on web.
Sections: window geometry, theme applied via $q.dark.set, startup
behavior, auto-update toggle, and a static shortcuts reference.

PROBLEM: A settings page with cards: Appearance (dark-mode toggle →
saveAndApply), Window (width/height/x/y number inputs → save on change),
Startup (minimize-to-tray + auto-update toggles), and Keyboard Shortcuts
(q-list of action/keys badges). loadSettings() merges stored JSON over
defaults on mount.

TRY THIS: if (window.electronAPI?.settings?.get) {
  const s = await window.electronAPI.settings.get('app-settings'); ... }
$q.dark.set(settings.value.darkMode)

EXPECTED OUTPUT: Every toggle/input persists and dark mode applies
immediately; shortcuts list renders.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
