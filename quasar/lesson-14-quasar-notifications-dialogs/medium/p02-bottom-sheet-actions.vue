<!--
LESSON 14 — Quasar Notifications & Dialogs
MEDIUM P02 — Bottom Sheet Action Menu
============================================
CONCEPT: $q.bottomSheet slides a mobile-friendly action list up from the
bottom. `actions` entries take label/icon/id/color; onOk receives the
chosen action.

PROBLEM: A button opening $q.bottomSheet with 4 actions (Share, Copy, Edit,
Delete — each with icon and color). Selecting one notifies "Selected: X";
cancelling notifies dismissal.

TRY THIS: $q.bottomSheet({ title: 'Choose an action', actions: [
  { label: 'Share', icon: 'share', id: 'share' }, ...] })
  .onOk(action => $q.notify({ message: `Selected: ${action.label}` }))

EXPECTED OUTPUT: A bottom sheet with four icon rows; tapping one toasts the
choice.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
