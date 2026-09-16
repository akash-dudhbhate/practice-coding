<!--
PROBLEM: Custom Cells with Badges & Actions (Easy)
===================================================

CONCEPT: QTable body-cell slots — custom rendering per column.

TASK: Add a custom cell for the "status" column. Show a green badge for
"active" and red for "inactive". Add an "actions" column with edit and
delete buttons.

TRY THIS:
- Add a status column and an actions column to the columns array
- Use a body-cell slot for status that renders a colored badge
- Use a body-cell slot for actions with two small round buttons
- On delete, remove the row; on edit, show a notification

EXPECTED OUTPUT: Status cells show green/red badges. Each row has edit and
delete icon buttons; delete removes the row.

CHECK: python3 check.py easy/p03

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: table with body-cell slots for status and actions -->
  </q-page>
</template>

<script setup>
// TODO: import ref from 'vue' and useQuasar from 'quasar'
</script>
