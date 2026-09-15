<!--
  Lesson 01 - Quasar Basics - Hard - Problem 03
  3-step form wizard with conditional rendering,
  next/back buttons, and a progress indicator.
-->
<template>
  <q-page class="flex flex-center column q-gutter-lg" style="max-width: 500px; margin: 0 auto;">
    <h2 class="text-h5">Form Wizard</h2>

    <!-- Progress indicator: shows current step out of 3 -->
    <q-linear-progress :value="step / 3" color="primary" class="full-width" />
    <p class="text-grey-7">Step {{ step }} of 3</p>

    <!-- Step 1: Personal Info -->
    <div v-if="step === 1" class="full-width q-gutter-md">
      <h3 class="text-h6">Personal Info</h3>
      <q-input v-model="form.name" label="Full Name" outlined />
      <q-input v-model="form.email" label="Email" outlined type="email" />
    </div>

    <!-- Step 2: Address -->
    <div v-if="step === 2" class="full-width q-gutter-md">
      <h3 class="text-h6">Address</h3>
      <q-input v-model="form.address" label="Street Address" outlined />
      <q-input v-model="form.city" label="City" outlined />
    </div>

    <!-- Step 3: Review & Submit -->
    <div v-if="step === 3" class="full-width q-gutter-md">
      <h3 class="text-h6">Review</h3>
      <q-list bordered separator>
        <q-item><q-item-section><strong>Name:</strong> {{ form.name }}</q-item-section></q-item>
        <q-item><q-item-section><strong>Email:</strong> {{ form.email }}</q-item-section></q-item>
        <q-item><q-item-section><strong>Address:</strong> {{ form.address }}</q-item-section></q-item>
        <q-item><q-item-section><strong>City:</strong> {{ form.city }}</q-item-section></q-item>
      </q-list>
    </div>

    <!-- Navigation buttons -->
    <div class="row q-gutter-md full-width justify-between">
      <q-btn
        color="grey-7"
        label="Back"
        outline
        :disable="step === 1"
        @click="step--"
      />
      <q-btn
        v-if="step < 3"
        color="primary"
        label="Next"
        @click="step++"
      />
      <q-btn
        v-else
        color="positive"
        label="Submit"
        @click="onSubmit"
      />
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Current step (1-3)
const step = ref(1)

// Form data collected across all steps
const form = ref({
  name: '',
  email: '',
  address: '',
  city: '',
})

// Called when the user clicks Submit on the final step
function onSubmit() {
  alert('Form submitted!\n' + JSON.stringify(form.value, null, 2))
}
</script>

<style scoped>
</style>
