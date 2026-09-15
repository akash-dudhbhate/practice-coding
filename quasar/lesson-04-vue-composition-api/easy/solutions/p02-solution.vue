<!--
  Lesson 04 - Vue Composition API - Easy - Problem 02
  Reactive user object (reactive({name, email, role})).
  Display all three. Button changes name.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <q-card flat bordered class="q-pa-md" style="min-width: 300px;">
      <q-card-section>
        <div class="text-h6">{{ user.name }}</div>
        <div class="text-subtitle2 text-grey-7">{{ user.email }}</div>
        <div class="text-body2 q-mt-sm">
          <q-badge color="primary" :label="user.role" />
        </div>
      </q-card-section>
    </q-card>

    <!-- Button changes the name property of the reactive object -->
    <q-btn color="primary" label="Change Name" @click="user.name = 'Jane Doe'" />
  </q-page>
</template>

<script setup>
import { reactive } from 'vue'

// reactive() makes the entire object deeply reactive
const user = reactive({
  name: 'John Doe',
  email: 'john@example.com',
  role: 'Developer',
})
</script>

<style scoped>
</style>
