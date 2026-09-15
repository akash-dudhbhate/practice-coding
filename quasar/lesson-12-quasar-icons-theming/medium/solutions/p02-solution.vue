<!--
  Lesson 12 - Medium - P02: Custom Dark Mode Styles
  Uses .body--dark class (applied by Quasar when dark mode is active)
  to change card background and text color. Toggle dark mode to verify.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Dark Mode Custom Styles</div>

    <!-- Toggle dark mode -->
    <q-toggle
      v-model="darkMode"
      label="Dark Mode"
      @update:model-value="toggleDark"
      class="q-mb-md"
    />

    <!-- Cards that adapt to dark mode via .body--dark scoped styles -->
    <div class="row q-col-gutter-md">
      <div class="col-12 col-md-6">
        <q-card class="custom-card">
          <q-card-section>
            <div class="text-h6">Card 1</div>
            <p class="text-body2">
              This card's background and text color change automatically
              when dark mode is toggled. The .body--dark selector targets
              the body element when Quasar applies dark mode.
            </p>
          </q-card-section>
        </q-card>
      </div>

      <div class="col-12 col-md-6">
        <q-card class="custom-card">
          <q-card-section>
            <div class="text-h6">Card 2</div>
            <p class="text-body2">
              Toggle the switch above to see the custom dark mode styles
              apply to these cards. The transition is smooth.
            </p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const darkMode = ref($q.dark.isActive)

// Toggle Quasar's dark mode
function toggleDark(val) {
  $q.dark.set(val)
}
</script>

<style scoped>
/* Light mode: default card styling */
.custom-card {
  background-color: #f5f5f5;
  color: #333;
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* Dark mode: .body--dark is applied to <body> when dark mode is active */
/* Use :deep() to reach outside scoped boundary, or use global styles */
:global(.body--dark) .custom-card {
  background-color: #1e1e1e !important;
  color: #e0e0e0 !important;
}
</style>
