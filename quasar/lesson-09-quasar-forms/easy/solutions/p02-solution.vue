<template>
  <!-- Form with QSelect, QToggle, QCheckbox, QRadio - display form state -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Profile Form</div>
      </q-card-section>
      <q-card-section>
        <q-form class="q-gutter-md">
          <!-- QSelect: country -->
          <q-select
            v-model="form.country"
            :options="countries"
            label="Country"
          />
          <!-- QToggle: notifications -->
          <q-toggle
            v-model="form.notifications"
            label="Enable Notifications"
          />
          <!-- QCheckbox: terms -->
          <q-checkbox
            v-model="form.terms"
            label="I accept the terms and conditions"
          />
          <!-- QRadio: gender -->
          <div>
            <div class="text-subtitle1 q-mb-sm">Gender</div>
            <q-radio v-model="form.gender" val="male" label="Male" />
            <q-radio v-model="form.gender" val="female" label="Female" />
            <q-radio v-model="form.gender" val="other" label="Other" />
          </div>
        </q-form>
      </q-card-section>

      <!-- Display form state below -->
      <q-separator />
      <q-card-section>
        <div class="text-h6">Form State</div>
        <pre>{{ JSON.stringify(form, null, 2) }}</pre>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const countries = ['USA', 'Canada', 'UK', 'Australia', 'Germany']

// Form state
const form = ref({
  country: null,
  notifications: false,
  terms: false,
  gender: null,
})
</script>

<style scoped>
.q-card {
  max-width: 500px;
  margin: 0 auto;
}
pre {
  white-space: pre-wrap;
  word-break: break-word;
}
</style>
