<!--
LESSON 08 — Quasar Plugins
HARD P01 — useNotifications Composable
============================================
CONCEPT: Wrap $q.notify in a composable with a presets map — each type gets
default color/icon/timeout. Presets + spread overrides keep call sites
one-liners. The `actions` array adds buttons like Undo.

PROBLEM: An inline `useNotifications()` composable returning success,
error, warning, info methods (each with its own icon/timeout preset), used
by four buttons — plus a "Delete with Undo" button whose notification has
an actions array with an Undo handler.

TRY THIS: const presets = { success: { type: 'positive', icon: 'check_circle', timeout: 3000 }, ... };
$q.notify({ ...preset, message, actions: [{ label: 'Undo', handler: () => ... }] })

EXPECTED OUTPUT: Five buttons; each fires a typed toast, and the delete one
offers a working Undo action.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
