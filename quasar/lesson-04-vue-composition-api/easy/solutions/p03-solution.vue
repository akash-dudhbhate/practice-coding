<!--
  Lesson 04 - Vue Composition API - Easy - Problem 03
  Computed fullName from firstName and lastName refs.
  Display it. Inputs to change both names.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md" style="max-width: 400px; margin: 0 auto;">
    <!-- Display the computed full name -->
    <div class="text-h5 text-primary">{{ fullName }}</div>

    <!-- Inputs to change first and last name -->
    <q-input v-model="firstName" label="First Name" outlined />
    <q-input v-model="lastName" label="Last Name" outlined />
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'

// Two independent refs for first and last name
const firstName = ref('John')
const lastName = ref('Doe')

// computed() creates a cached derived value that updates only when
// firstName or lastName changes
const fullName = computed(() => `${firstName.value} ${lastName.value}`)
</script>

<style scoped>
</style>
