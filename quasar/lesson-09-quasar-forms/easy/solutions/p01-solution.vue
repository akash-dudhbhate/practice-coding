<template>
  <!-- Login form with email/password validation -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Login</div>
      </q-card-section>
      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <!-- Email: required + format validation -->
          <q-input
            v-model="form.email"
            label="Email"
            type="email"
            :rules="[
              val => !!val || 'Email is required',
              val => /.+@.+\..+/.test(val) || 'Please enter a valid email'
            ]"
          />
          <!-- Password: required + min 6 characters -->
          <q-input
            v-model="form.password"
            label="Password"
            type="password"
            :rules="[
              val => !!val || 'Password is required',
              val => val.length >= 6 || 'Password must be at least 6 characters'
            ]"
          />
          <q-btn type="submit" label="Login" color="primary" />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const form = ref({ email: '', password: '' })

// On submit, show notification with form values
function onSubmit() {
  $q.notify({
    type: 'positive',
    message: `Logged in with email: ${form.value.email}`,
  })
}
</script>

<style scoped>
.q-card {
  max-width: 400px;
  margin: 0 auto;
}
</style>
