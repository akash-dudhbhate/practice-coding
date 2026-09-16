<!--
LESSON 14 — Quasar Notifications & Dialogs
EASY P02 — Delete Confirm + Undo Notification
============================================
CONCEPT: Chain $q.dialog().onOk()/.onCancel() for confirm flows. The
notification's `actions` array embeds buttons — an Undo handler that fires
another notify to "restore" the item.

PROBLEM: A Delete q-btn opening a $q.dialog (title, message, cancel: true,
persistent). On OK: a 5-second "deleted" notification with an Undo action
that notifies "restored". On cancel: a "cancelled" info toast.

TRY THIS: $q.dialog({...}).onOk(() => $q.notify({ ..., timeout: 5000,
  actions: [{ label: 'Undo', handler: () => $q.notify({...}) }] }))
  .onCancel(() => $q.notify({ type: 'info', message: 'Cancelled' }))

EXPECTED OUTPUT: Delete → confirm modal → toast with an Undo button that
works; dismissing shows "cancelled".

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
