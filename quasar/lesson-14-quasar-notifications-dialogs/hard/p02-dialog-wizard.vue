<!--
LESSON 14 — Quasar Notifications & Dialogs
HARD P02 — Multi-Step Dialog Wizard
============================================
CONCEPT: A custom dialog component can hold its own step state. Track
`step` (1-3), validate per step, and emit('ok', data) on finish — the
caller gets the collected form in onOk.

PROBLEM: A `WizardDialog` defineComponent with 3 steps (form: name+email;
review/plan select; confirm summary), Back/Next/Confirm/Cancel buttons,
per-step validation with error display, opened via $q.dialog — onOk
notifies the result, onCancel notifies cancellation.

TRY THIS: function next() { if (validateStep()) step.value++ }
step 3 → emit('ok', { ...form.value }) with v-close-popup;
<q-linear-progress :value="step / 3" />

EXPECTED OUTPUT: A dialog that walks form → plan → confirm, blocking Next
on invalid input, and toasts the collected data.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
