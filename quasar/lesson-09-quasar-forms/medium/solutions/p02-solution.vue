<template>
  <!-- Form with async validation: username availability check -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Username Check</div>
      </q-card-section>
      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <q-input
            v-model="username"
            label="Username"
            debounce="500"
            :loading="checking"
            :rules="[
              val => !!val || 'Username is required',
              val => val.length >= 3 || 'At least 3 characters'
            ]"
          >
            <!-- Show availability status as hint/append -->
            <template #append>
              <q-icon v-if="status === 'available'" name="check_circle" color="positive" />
              <q-icon v-if="status === 'taken'" name="cancel" color="negative" />
              <q-spinner v-if="status === 'checking'" color="primary" />
            </template>
          </q-input>

          <!-- Status message -->
          <div v-if="status === 'checking'" class="text-info">
            <q-spinner size="16px" /> Checking availability...
          </div>
          <div v-else-if="status === 'available'" class="text-positive">
            Username is available!
          </div>
          <div v-else-if="status === 'taken'" class="text-negative">
            Username is already taken.
          </div>

          <q-btn type="submit" label="Submit" color="primary" :disable="status !== 'available'" />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const username = ref('')
const checking = ref(false)
const status = ref('idle') // 'idle', 'checking', 'available', 'taken'

// Mock taken usernames
const takenUsernames = ['admin', 'user', 'test', 'guest', 'root']

// Watch username changes and check availability (debounced via q-input debounce)
watch(username, async (newVal) => {
  if (!newVal || newVal.length < 3) {
    status.value = 'idle'
    return
  }

  checking.value = true
  status.value = 'checking'

  // Simulate async API call with setTimeout
  await new Promise((resolve) => setTimeout(resolve, 800))

  checking.value = false
  status.value = takenUsernames.includes(newVal.toLowerCase()) ? 'taken' : 'available'
})

function onSubmit() {
  $q.notify({ type: 'positive', message: `Username "${username.value}" registered!` })
}
</script>

<style scoped>
.q-card {
  max-width: 450px;
  margin: 0 auto;
}
</style>
