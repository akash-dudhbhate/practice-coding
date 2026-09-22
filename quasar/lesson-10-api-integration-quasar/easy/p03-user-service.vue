<!--
LESSON 10 — API Integration in Quasar
EASY P03 — userService + List Component
============================================
CONCEPT: The service pattern wraps raw fetch/axios calls in a named object —
userService.getAll(), .getById(id), .create(data), .update(id, data),
.remove(id) — so components never build URLs themselves.

PROBLEM: A `userService` object with all five CRUD methods against
jsonplaceholder /users (fetch + method/headers/JSON body), and a component
that calls getAll() on mount with loading + error states and a q-list of
users.

TRY THIS: async getAll() { const res = await fetch(this.baseURL); if (!res.ok) throw ...; return res.json() }
create: fetch(url, { method: 'POST', headers: {...}, body: JSON.stringify(data) })

EXPECTED OUTPUT: Users render in a list after a loading bar; service methods
are ready for create/update/delete.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
