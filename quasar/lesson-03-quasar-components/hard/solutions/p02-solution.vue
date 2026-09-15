<!--
  Lesson 03 - Quasar Components - Hard - Problem 02
  User profile card using q-card, q-avatar, q-chip (skills),
  q-separator, q-list (contact info).
  Avatar, name, bio, 3 skill chips, 3 contact items.
-->
<template>
  <q-page class="flex flex-center">
    <q-card class="profile-card" flat bordered>
      <!-- Avatar section -->
      <q-card-section class="text-center">
        <q-avatar size="100px" class="q-mb-sm">
          <img src="https://cdn.quasar.dev/img/avatar.png" alt="avatar" />
        </q-avatar>
        <div class="text-h6">{{ user.name }}</div>
        <div class="text-subtitle2 text-grey-7">{{ user.role }}</div>
      </q-card-section>

      <q-separator />

      <!-- Bio section -->
      <q-card-section>
        <div class="text-subtitle2 q-mb-xs">About</div>
        <p class="text-body2 text-grey-8">{{ user.bio }}</p>
      </q-card-section>

      <q-separator />

      <!-- Skills as q-chips -->
      <q-card-section>
        <div class="text-subtitle2 q-mb-sm">Skills</div>
        <q-chip
          v-for="skill in user.skills"
          :key="skill"
          color="primary"
          text-color="white"
          icon="star"
        >
          {{ skill }}
        </q-chip>
      </q-card-section>

      <q-separator />

      <!-- Contact info as q-list -->
      <q-card-section>
        <div class="text-subtitle2 q-mb-sm">Contact</div>
        <q-list dense>
          <q-item v-for="contact in user.contacts" :key="contact.label">
            <q-item-section avatar>
              <q-icon :name="contact.icon" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label caption>{{ contact.label }}</q-item-label>
              <q-item-label>{{ contact.value }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// User profile data
const user = ref({
  name: 'Jane Doe',
  role: 'Frontend Developer',
  bio: 'Passionate developer with 5 years of experience building web apps with Vue and Quasar.',
  skills: ['JavaScript', 'Vue.js', 'Quasar'],
  contacts: [
    { label: 'Email', value: 'jane.doe@example.com', icon: 'email' },
    { label: 'Phone', value: '+1 (555) 123-4567', icon: 'phone' },
    { label: 'Location', value: 'San Francisco, CA', icon: 'location_on' },
  ],
})
</script>

<style scoped>
.profile-card {
  width: 100%;
  max-width: 380px;
}
</style>
