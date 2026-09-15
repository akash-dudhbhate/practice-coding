<!--
  Lesson 03 - Quasar Components - Hard - Problem 03
  Settings page with q-expansion-item sections (Profile, Privacy, Notifications).
  Each expands to show q-toggle switches.
  q-separator between sections.
-->
<template>
  <q-page class="q-pa-md" style="max-width: 500px; margin: 0 auto;">
    <h2 class="text-h5 q-mb-md">Settings</h2>

    <!-- Profile section -->
    <q-expansion-item
      icon="person"
      label="Profile"
      default-opened
      header-class="text-primary"
    >
      <q-list dense class="q-pl-md">
        <q-item>
          <q-item-section>Show profile publicly</q-item-section>
          <q-item-section side>
            <q-toggle v-model="settings.profilePublic" color="primary" />
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>Display real name</q-item-section>
          <q-item-section side>
            <q-toggle v-model="settings.showRealName" color="primary" />
          </q-item-section>
        </q-item>
      </q-list>
    </q-expansion-item>

    <q-separator spaced />

    <!-- Privacy section -->
    <q-expansion-item
      icon="lock"
      label="Privacy"
      header-class="text-primary"
    >
      <q-list dense class="q-pl-md">
        <q-item>
          <q-item-section>Private account</q-item-section>
          <q-item-section side>
            <q-toggle v-model="settings.privateAccount" color="primary" />
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>Allow search by email</q-item-section>
          <q-item-section side>
            <q-toggle v-model="settings.searchByEmail" color="primary" />
          </q-item-section>
        </q-item>
      </q-list>
    </q-expansion-item>

    <q-separator spaced />

    <!-- Notifications section -->
    <q-expansion-item
      icon="notifications"
      label="Notifications"
      header-class="text-primary"
    >
      <q-list dense class="q-pl-md">
        <q-item>
          <q-item-section>Email notifications</q-item-section>
          <q-item-section side>
            <q-toggle v-model="settings.emailNotifications" color="primary" />
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>Push notifications</q-item-section>
          <q-item-section side>
            <q-toggle v-model="settings.pushNotifications" color="primary" />
          </q-item-section>
        </q-item>
      </q-list>
    </q-expansion-item>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// All settings toggles in one reactive object
const settings = ref({
  profilePublic: true,
  showRealName: false,
  privateAccount: false,
  searchByEmail: true,
  emailNotifications: true,
  pushNotifications: false,
})
</script>

<style scoped>
</style>
