<!--
LESSON 10 — API Integration in Quasar
HARD P02 — Full CRUD Users App
============================================
CONCEPT: CRUD UIs reuse one dialog for create and edit — `editing` (null =
create, object = edit) drives the title, the HTTP method (POST vs PUT), and
whether you unshift a new row or patch an existing one. Deletes go through
$q.dialog confirm.

PROBLEM: A q-table of users with an actions column (edit/delete buttons),
an "Add User" button, a q-dialog form (name/email/phone) that creates or
updates via fetch POST/PUT, delete via $q.dialog confirm + DELETE, with
loading/saving states and notify on every outcome.

TRY THIS: async saveUser() { editing.value
  ? await fetch(`${API}/${editing.value.id}`, { method: 'PUT', ... })
  : await fetch(API, { method: 'POST', ... }) }

EXPECTED OUTPUT: A user table where you can add, edit, and delete rows —
each with spinner feedback and success/error toasts.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
