<template>
  <div class="q-pa-md">
    <p>Full Name (1): {{ fullName }}</p>
    <p>Full Name (2): {{ fullName }}</p>
    <q-input v-model="firstName" label="First Name" />
    <q-input v-model="lastName" label="Last Name" />
    <q-btn label="Change First Name" color="primary" @click="firstName = 'Bob'" class="q-mt-sm" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const firstName = ref('Alice')
const lastName = ref('Smith')

// Computed is cached — console.log proves it only runs when dependencies change
const fullName = computed(() => {
  console.log('computed fullName called')
  return `${firstName.value} ${lastName.value}`
})
</script>
