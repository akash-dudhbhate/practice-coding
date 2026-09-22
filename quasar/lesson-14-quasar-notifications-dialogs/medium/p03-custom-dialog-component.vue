<!--
LESSON 14 — Quasar Notifications & Dialogs
MEDIUM P03 — Custom Dialog Component
============================================
CONCEPT: $q.dialog({ component: MyDialog }) mounts your own component as a
dialog. Inside, emit('ok', payload) resolves it — the caller receives the
payload in .onOk(data).

PROBLEM: A `CustomFormDialog` (defineComponent with a name+email form, OK
emitting the form object) opened via $q.dialog; onOk shows a notification
with the submitted data.

TRY THIS: const CustomFormDialog = defineComponent({ emits: ['ok'],
  setup(props, { emit }) { ... template with @click="emit('ok', {...form})" });
$q.dialog({ component: CustomFormDialog }).onOk(data => $q.notify(...))

EXPECTED OUTPUT: The custom dialog collects name + email; OK toasts the
entered values.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
