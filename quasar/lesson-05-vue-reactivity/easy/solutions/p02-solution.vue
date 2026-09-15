<template>
  <div class="q-pa-md">
    <p>Theme: {{ user.profile.settings.theme }}</p>
    <q-btn label="Change Theme" color="primary" @click="changeTheme" />
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const user = reactive({
  profile: {
    settings: {
      theme: 'light'
    }
  }
})

function changeTheme() {
  user.profile.settings.theme = user.profile.settings.theme === 'light' ? 'dark' : 'light'
}
</script>
