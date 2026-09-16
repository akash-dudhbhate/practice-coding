<!--
LESSON 14 — Quasar Notifications & Dialogs
MEDIUM P01 — Persistent Loading Notification
============================================
CONCEPT: $q.notify returns a dismiss function. With timeout: 0 and
spinner: true the toast stays put until you call it — the manual way to do
"operation in progress" feedback.

PROBLEM: A "Start Operation" button (disabled while running) that shows a
persistent spinner notification, simulates a 3s setTimeout operation, then
calls dismiss() and fires a success toast.

TRY THIS: const dismiss = $q.notify({ message: 'Loading...', spinner: true,
  timeout: 0, position: 'center' });
setTimeout(() => { dismiss(); $q.notify({ type: 'positive', ... }) }, 3000)

EXPECTED OUTPUT: A centered spinner toast for 3s, replaced by a success
notification; the button is disabled during the run.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
