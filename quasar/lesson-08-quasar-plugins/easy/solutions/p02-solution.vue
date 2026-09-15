<template>
  <!-- Dark mode toggle button using $q.dark.toggle() -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Dark Mode Toggle</div>
    <q-card class="q-pa-lg">
      <q-card-section>
        <p>Current state: <strong>{{ darkActive ? 'Dark' : 'Light' }}</strong></p>
        <q-btn
          :label="darkActive ? 'Switch to Light' : 'Switch to Dark'"
          :icon="darkActive ? 'light_mode' : 'dark_mode'"
          :color="darkActive ? 'orange' : 'indigo'"
          @click="toggleDark"
        />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Reactive computed for current dark mode state
const darkActive = computed(() => $q.dark.isActive)

// Toggle dark mode using $q.dark.toggle()
function toggleDark() {
  $q.dark.toggle()
}
</script>

<style scoped>
.q-card {
  max-width: 400px;
  margin: 0 auto;
}
</style>
