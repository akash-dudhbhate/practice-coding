<template>
  <!-- Component with onBeforeRouteLeave guard -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Edit Form</div>
        <q-input
          v-model="formData"
          label="Enter some text"
          class="q-mt-md"
          @update:model-value="hasUnsavedChanges = true"
        />
        <q-btn
          label="Save"
          color="positive"
          class="q-mt-md"
          @click="save"
        />
        <q-btn
          label="Go to About"
          color="primary"
          class="q-mt-md q-ml-sm"
          to="/about"
        />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { onBeforeRouteLeave } from 'vue-router'

const formData = ref('')
const hasUnsavedChanges = ref(false)

// Save the form and clear the unsaved flag
function save() {
  hasUnsavedChanges.value = false
}

// Navigation guard: confirm before leaving with unsaved changes
onBeforeRouteLeave((to, from, next) => {
  if (hasUnsavedChanges.value) {
    const confirmLeave = window.confirm(
      'You have unsaved changes. Are you sure you want to leave?'
    )
    if (!confirmLeave) {
      next(false) // Cancel navigation
      return
    }
  }
  next() // Allow navigation
})
</script>

<style scoped>
.q-card {
  max-width: 500px;
  margin: 0 auto;
}
</style>
