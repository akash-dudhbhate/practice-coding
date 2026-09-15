<template>
  <!-- Form with submit and reset buttons - resetValidation() -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Contact Form</div>
      </q-card-section>
      <q-card-section>
        <q-form ref="formRef" @submit="onSubmit" class="q-gutter-md">
          <q-input
            v-model="form.name"
            label="Name"
            :rules="[val => !!val || 'Name is required']"
          />
          <q-input
            v-model="form.email"
            label="Email"
            type="email"
            :rules="[
              val => !!val || 'Email is required',
              val => /.+@.+\..+/.test(val) || 'Invalid email format'
            ]"
          />
          <q-input
            v-model="form.message"
            label="Message"
            type="textarea"
            :rules="[val => !!val || 'Message is required']"
          />
          <div class="row q-gutter-md">
            <q-btn type="submit" label="Submit" color="primary" />
            <q-btn label="Reset" color="grey" @click="onReset" />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Form ref to access resetValidation()
const formRef = ref(null)

const form = ref({ name: '', email: '', message: '' })

// Submit handler
function onSubmit() {
  $q.notify({ type: 'positive', message: 'Form submitted successfully!' })
}

// Reset: clear all fields and validation errors
function onReset() {
  form.value = { name: '', email: '', message: '' }
  formRef.value.resetValidation()
  $q.notify({ type: 'info', message: 'Form reset' })
}
</script>

<style scoped>
.q-card {
  max-width: 500px;
  margin: 0 auto;
}
</style>
