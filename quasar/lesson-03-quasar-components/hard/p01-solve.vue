<!--
LESSON 03 — Quasar Components
HARD P01 — Table with Custom Status Cell
============================================
CONCEPT: q-table slots let you override cell rendering — the slot
name is body-cell-<column-name>, and it receives props (incl.
props.value) for the current cell.

PROBLEM: Build a q-table with columns ID, Name, Status and 5 rows
with mixed 'Active'/'Inactive' statuses. Use a
#body-cell-status slot to render a q-badge — green when the value is
'Active', red when 'Inactive'.

TRY THIS: inside the slot use <q-td :props="props"> to keep table
cell styling.

EXPECTED OUTPUT: a table where the Status column shows colored
badges instead of plain text.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
