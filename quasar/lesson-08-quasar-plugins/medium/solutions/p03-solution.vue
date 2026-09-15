<template>
  <!-- Form submission flow with $q.loading spinner -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Form Submission</div>
    <q-card class="q-pa-lg">
      <q-card-section>
        <q-form @submit="handleSubmit">
          <q-input v-model="formData.name" label="Name" :rules="[v => !!v || 'Name is required']" />
          <q-input v-model="formData.email" label="Email" type="email"
            :rules="[v => !!v || 'Email is required']" />
          <q-btn type="submit" label="Save" color="primary" class="q-mt-md" />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const formData = ref({ name: '', email: '' })

// Form submission: show loading, simulate async save, then notify
async function handleSubmit() {
  $q.loading.show({
    message: 'Saving your data...',
    spinnerColor: 'primary',
  })

  try {
    // Simulate async save operation (2 seconds)
    await new Promise((resolve) => setTimeout(resolve, 2000))

    // Success notification
    $q.notify({
      type: 'positive',
      message: 'Data saved successfully!',
    })
  } catch (error) {
    // Error notification
    $q.notify({
      type: 'negative',
      message: 'Failed to save: ' + error.message,
    })
  } finally {
    // Always hide loading, even on error
    $q.loading.hide()
  }
}
</script>

<style scoped>
.q-card {
  max-width: 500px;
  margin: 0 auto;
}
</style>
