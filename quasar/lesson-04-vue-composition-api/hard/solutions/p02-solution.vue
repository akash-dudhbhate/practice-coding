<!--
  Lesson 04 - Vue Composition API - Hard - Problem 02
  Form with reactive state ({name, email, age, agree}).
  Computed isValid (name non-empty, email has @, age>0, agree true).
  Disable submit when invalid. Watch isValid, log changes.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md" style="max-width: 400px; margin: 0 auto;">
    <h2 class="text-h6">Registration Form</h2>

    <!-- Form fields bound to reactive state -->
    <q-input v-model="form.name" label="Name" outlined />
    <q-input v-model="form.email" label="Email" outlined type="email" />
    <q-input v-model.number="form.age" label="Age" outlined type="number" />
    <q-toggle v-model="form.agree" label="I agree to the terms" color="primary" />

    <!-- Submit disabled when form is invalid -->
    <q-btn
      color="primary"
      label="Submit"
      :disable="!isValid"
      class="full-width"
      @click="onSubmit"
    />

    <!-- Validation status indicator -->
    <p :class="isValid ? 'text-positive' : 'text-negative'">
      {{ isValid ? 'Form is valid!' : 'Please fill all fields correctly.' }}
    </p>
  </q-page>
</template>

<script setup>
import { reactive, computed, watch } from 'vue'

// Reactive form state
const form = reactive({
  name: '',
  email: '',
  age: 0,
  agree: false,
})

// Computed validation: all conditions must be true
const isValid = computed(() => {
  return (
    form.name.trim() !== '' &&
    form.email.includes('@') &&
    form.age > 0 &&
    form.agree === true
  )
})

// Watch isValid and log whenever it changes
watch(isValid, (newVal, oldVal) => {
  console.log(`Form validity changed from ${oldVal} to ${newVal}`)
})

// Submit handler
function onSubmit() {
  console.log('Form submitted:', { ...form })
  alert('Form submitted successfully!')
}
</script>

<style scoped>
</style>
