<!--
  Lesson 03 - Quasar Components - Medium - Problem 02
  q-dialog opening from button. Inside: q-card with form
  (name input, email input) and Cancel/Save buttons with v-close-popup.
-->
<template>
  <q-page class="flex flex-center">
    <!-- Button to open the dialog -->
    <q-btn color="primary" label="Open Form Dialog" @click="dialog = true" />

    <!-- q-dialog controlled by v-model -->
    <q-dialog v-model="dialog">
      <q-card style="min-width: 350px;">
        <q-card-section>
          <div class="text-h6">User Form</div>
        </q-card-section>

        <!-- Form inputs -->
        <q-card-section class="q-gutter-md">
          <q-input v-model="form.name" label="Name" outlined />
          <q-input v-model="form.email" label="Email" outlined type="email" />
        </q-card-section>

        <!-- Action buttons: v-close-popup closes the dialog -->
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="grey-7" v-close-popup />
          <q-btn flat label="Save" color="primary" v-close-popup @click="onSave" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Dialog visibility
const dialog = ref(false)

// Form data
const form = ref({
  name: '',
  email: '',
})

// Called when Save is clicked (before v-close-popup closes the dialog)
function onSave() {
  console.log('Saved form data:', form.value)
}
</script>

<style scoped>
</style>
