<!--
LESSON 14 — Quasar Notifications & Dialogs
EASY P03 — Prompt Dialog with Validation
============================================
CONCEPT: $q.dialog's `prompt` option embeds a text input; isValid(val)
gates the OK button. The entered string arrives as onOk's argument.

PROBLEM: A button opening a prompt dialog for a name (prompt.model '',
type 'text', isValid non-empty). onOk notifies "You entered: X"; onCancel
notifies the cancel.

TRY THIS: $q.dialog({ title: '...', prompt: { model: '', type: 'text',
  isValid: val => val.trim().length > 0 }, cancel: true, persistent: true })
  .onOk(name => $q.notify({ message: `You entered: ${name}` }))

EXPECTED OUTPUT: The dialog blocks empty input; OK toasts the entered text.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
