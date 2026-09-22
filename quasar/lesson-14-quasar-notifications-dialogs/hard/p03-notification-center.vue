<!--
LESSON 14 — Quasar Notifications & Dialogs
HARD P03 — Notification Center
============================================
CONCEPT: A bell + floating badge showing unread count, a q-menu dropdown
listing notifications with per-type icon/color, click-to-mark-read, and a
"Mark all read" — with read state persisted to localStorage via a deep
watch.

PROBLEM: A notification center: notifications ref (~4 items with
type/message/time/read), `unreadCount` computed, q-btn bell with q-badge,
q-menu with a scrollable q-list, markAsRead/markAllRead, iconForType/
colorForType maps, and localStorage save+load of read state.

TRY THIS: const unreadCount = computed(() => notifications.value.filter(n => !n.read).length);
watch(notifications, v => localStorage.setItem('notif_read_state', JSON.stringify(...)), { deep: true })

EXPECTED OUTPUT: The badge counts unread items; clicking a notification
greys it out and drops the count; reload preserves read state.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
