<!--
LESSON 08 — Quasar Plugins
MEDIUM P01 — Delete Confirm Dialog
============================================
CONCEPT: $q.dialog() opens a modal that returns chainable handlers:
.onOk() fires on confirm, .onCancel() on cancel. Add cancel: true and
persistent: true for a real confirmation.

PROBLEM: A "Delete Item" q-btn opening a $q.dialog with title, message,
cancel: true. On OK show a positive "deleted" $q.notify; on cancel show an
info "cancelled" notification.

TRY THIS: $q.dialog({ title: 'Confirm Delete', message: '...', cancel: true })
  .onOk(() => $q.notify({ type: 'positive', message: 'Item deleted!' }))
  .onCancel(() => $q.notify({ type: 'info', message: 'Cancelled' }))

EXPECTED OUTPUT: Clicking delete pops a modal; confirming toasts "deleted",
dismissing toasts "cancelled".

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
