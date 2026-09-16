<!--
LESSON 08 — Quasar Plugins
HARD P02 — Platform-Aware Menu
============================================
CONCEPT: Combine $q.platform.is.mobile with $q.screen.xs to decide UI: a
q-menu dropdown suits desktop; a $q.bottomSheet modal suits thumbs on
mobile. Same menu items, different container.

PROBLEM: A component with 4+ menu items. On desktop render a q-btn with an
embedded q-menu dropdown; on mobile a q-btn that opens $q.bottomSheet with
the items as actions. Show the detected platform + screen badge.

TRY THIS: const isMobile = computed(() => $q.platform.is.mobile || $q.screen.xs);
$q.bottomSheet({ title: 'Menu', actions: menuItems.map(i => ({ label: i.label, icon: i.icon })) })

EXPECTED OUTPUT: Desktop shows a dropdown; mobile shows a bottom sheet;
both notify the selected item.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
