<!--
PROBLEM: Row Selection with Bulk Delete (Medium)
=================================================

CONCEPT: QTable row selection — multiple selection via v-model:selected,
confirm dialog, clearing selection.

TASK: Create a table with multiple row selection. Add a "Delete Selected"
button that shows how many rows are selected. On click, confirm with a
dialog and clear selection after.

TRY THIS:
- Enable multiple selection on the table and track selected rows
- Button label includes the selected count; disable it when none selected
- Ask for confirmation via a dialog before deleting
- After deleting, reset the selection to an empty list

EXPECTED OUTPUT: Checkboxes appear on rows. The button reads e.g.
"Delete Selected (3)". Confirming removes those rows and unchecks all.

CHECK: python3 check.py medium/p02

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: delete button + selectable table -->
  </q-page>
</template>

<script setup>
// TODO: import ref + useQuasar; track selected rows
</script>
