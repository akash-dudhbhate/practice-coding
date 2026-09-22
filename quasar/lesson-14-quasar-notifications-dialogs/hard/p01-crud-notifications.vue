<!--
LESSON 14 — Quasar Notifications & Dialogs
HARD P01 — useCrudNotifications Composable
============================================
CONCEPT: Wrap CRUD operations in a composable so every create/update/delete
gets identical UX: a dismissable loading toast, a success toast, an error
toast on failure, and an Undo action on delete.

PROBLEM: An inline `useCrudNotifications()` returning create/update/remove
async functions. Each shows a spinner toast (timeout: 0), awaits a mock
delay, dismisses, then notifies success — delete's toast carries an Undo
action that "restores". Wire three buttons to it.

TRY THIS: const dismiss = notifyLoading('Creating...');
try { await delay; dismiss(); notifySuccess(...) }
catch (e) { dismiss(); notifyError(...) }
actions: [{ label: 'Undo', handler: onUndo }]

EXPECTED OUTPUT: Each button shows a loading toast then a success toast;
delete offers a working Undo.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
