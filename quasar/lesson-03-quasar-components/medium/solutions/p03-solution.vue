<!--
  Lesson 03 - Quasar Components - Medium - Problem 03
  Filter bar with 4 removable q-chips (JavaScript, Vue, Quasar, CSS).
  Clicking X removes the chip.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <h2 class="text-h6">Filter Tags</h2>

    <!-- q-chip with removable prop shows an X button -->
    <div class="row q-gutter-sm">
      <q-chip
        v-for="chip in chips"
        :key="chip"
        removable
        color="primary"
        text-color="white"
        icon="tag"
        @remove="removeChip(chip)"
      >
        {{ chip }}
      </q-chip>
    </div>

    <!-- Message when all chips are removed -->
    <p v-if="chips.length === 0" class="text-grey-7">
      All filters removed. Refresh to restore.
    </p>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Initial list of filter chips
const chips = ref(['JavaScript', 'Vue', 'Quasar', 'CSS'])

// Remove a chip by filtering it out of the array
function removeChip(chip) {
  chips.value = chips.value.filter(c => c !== chip)
}
</script>

<style scoped>
</style>
