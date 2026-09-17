<!--
LESSON 01 — Quasar Basics
HARD P01 — Todo List: Complete & Delete
============================================
CONCEPT: Todos are objects ({ id, text, done }) in a reactive array.
computed() derives values (like a done count) that update
automatically, and v-if can render an empty state when the list is
empty.

PROBLEM: Build a full todo list — a <q-input> with v-model for the
new todo plus an Add <q-btn>. Render todos as a <q-list> with one
<q-item> per todo, each row holding a <q-checkbox v-model="todo.done">,
the todo text (strikethrough class when done), and a delete <q-btn>
that filters the todo out by id. Add a computed() for the completed
count and a v-if empty-state message ("No todos yet").

TRY THIS: add todos, check one off — its text strikes through and
the "N of M completed" line updates. Delete removes the row.

EXPECTED OUTPUT: a working todo list — add, check off (strikethrough),
delete, an empty-state message, and a live completed counter.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
