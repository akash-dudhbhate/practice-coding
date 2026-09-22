<!--
PROBLEM: Editable Table — Inline Cell Editing (Hard)
=====================================================

CONCEPT: Inline editing inside body-cell slots — edit mode state,
keyboard handling (Enter/Escape), notifications, add/delete rows.

TASK: Build an editable table: double-click a cell to edit it inline.
Use QInput in edit mode. Save on Enter, cancel on Escape. Show a
notification on save. Include add row and delete row buttons.

TRY THIS:
- Track which cell is being edited (row id + field name) plus the edit value
- Double-click on a cell swaps the text for an autofocused input
- Enter or blur saves; Escape cancels — notify on save
- "Add Row" appends a new row with a computed next id
- A delete action column removes the row

EXPECTED OUTPUT: Double-clicking name/email/age turns it into an input.
Enter saves with a toast; Escape discards. Add/Delete buttons work.

CHECK: python3 check.py hard/p03

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: add-row button + table with editable cells -->
  </q-page>
</template>

<script setup>
// TODO: editing state {rowId, field}, editValue, start/save/cancel edit
</script>
