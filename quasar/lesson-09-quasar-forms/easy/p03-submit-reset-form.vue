<!--
LESSON 09 — Quasar Forms
EASY P03 — Submit + Reset with resetValidation
============================================
CONCEPT: Give q-form a template ref (ref="formRef") to call its methods.
Resetting means two steps: clear the bound values AND call
formRef.value.resetValidation() to wipe the red error messages.

PROBLEM: A contact q-form (name, email with format rule, message textarea —
all required) with Submit and Reset buttons. Reset clears the form object
and calls resetValidation(); both buttons notify.

TRY THIS: <q-form ref="formRef" @submit="onSubmit">
function onReset() { form.value = { name:'', email:'', message:'' }; formRef.value.resetValidation() }

EXPECTED OUTPUT: Invalid submit shows errors; Reset clears fields and
removes all error styling.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
