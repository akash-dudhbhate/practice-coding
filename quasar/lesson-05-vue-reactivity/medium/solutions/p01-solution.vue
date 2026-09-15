<template>
  <div class="q-pa-md">
    <q-input v-model="firstName" label="First Name" />
    <q-input v-model="lastName" label="Last Name" />
    <p>Document title is now: "{{ firstName }} {{ lastName }}"</p>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'

const firstName = ref('John')
const lastName = ref('Doe')

// watchEffect auto-tracks both firstName and lastName as dependencies
watchEffect(() => {
  document.title = `${firstName.value} ${lastName.value}`
})
</script>
