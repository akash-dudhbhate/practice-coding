<!--
LESSON 17 — Quasar Electron
HARD P01 — Complete Text Editor
============================================
CONCEPT: A real desktop editor layers: dirty tracking (• in title),
beforeunload guard on close, a $q.dialog confirm before discarding, a
persisted recent-files list (localStorage or electronAPI.settings), and
onMenuAction wiring so File → Open/Save in the native menu work.

PROBLEM: Editor + sidebar: Open/Save via window.electronAPI; textarea
edits set dirty and show a dot; opening with unsaved changes asks to
confirm; beforeunload warns; a Recent Files card lists up to 10 entries
with remove buttons; menu actions 'open'/'save' trigger the same paths.

TRY THIS: window.addEventListener('beforeunload', e => { if (dirty.value) { e.preventDefault(); e.returnValue = '' } })
window.electronAPI.onMenuAction(a => { if (a === 'open') openFile() })

EXPECTED OUTPUT: Full open→edit→save loop with unsaved-changes guards and
a working recent list.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
