<!--
LESSON 17 — Quasar Electron
MEDIUM P02 — File Editor Component
============================================
CONCEPT: The renderer never touches fs — it calls the preload bridge
window.electronAPI.readFile()/saveFile(). A null result means the user
cancelled; an {error} field or a rejected promise means failure.

PROBLEM: A simple editor: Open button → electronAPI.readFile() fills
fileName + content (handle cancel + error); a q-input textarea bound to
content that marks a `dirty` ref on change; Save button →
electronAPI.saveFile(fileName, content) with a success/cancel notify;
an "unsaved" badge shows when dirty.

TRY THIS: const result = await window.electronAPI.readFile();
if (result === null) return; if (result.error) { $q.notify(...) }

EXPECTED OUTPUT: Open loads a file into the textarea, edits flag dirty,
Save writes it back and clears the flag.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
