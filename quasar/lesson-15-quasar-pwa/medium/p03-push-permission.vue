<!--
LESSON 15 — Quasar PWA
MEDIUM P03 — Push Permission Requester
============================================
CONCEPT: Notification.permission is 'default'/'granted'/'denied';
Notification.requestPermission() asks the user. On iOS push only works in
an installed PWA — detect it and show a warning banner.

PROBLEM: An "Enable Push Notifications" button (disabled once granted), a
status line showing the permission, a "Send Test Notification" button when
granted firing `new Notification(...)`, and an iOS-limitation banner when
the userAgent is iOS but not standalone.

TRY THIS: const result = await Notification.requestPermission();
new Notification('Test', { body: '...', icon: '/icons/icon-128.png' });
const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent)

EXPECTED OUTPUT: Clicking asks for permission, shows its status, and — once
granted — sends a test notification. iOS users see the install-first note.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
