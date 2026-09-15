<template>
  <!-- Registration form with sections: 2-column desktop, 1-column mobile -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Registration Form</div>
      </q-card-section>
      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <!-- Personal Info Section -->
          <div class="text-h6">Personal Info</div>
          <div class="row q-col-gutter-md">
            <div class="col-12 col-md-6">
              <q-input
                v-model="form.name"
                label="Full Name"
                :rules="[val => !!val || 'Name is required']"
              />
            </div>
            <div class="col-12 col-md-6">
              <q-input
                v-model="form.email"
                label="Email"
                type="email"
                :rules="[
                  val => !!val || 'Email is required',
                  val => /.+@.+\..+/.test(val) || 'Invalid email'
                ]"
              />
            </div>
          </div>

          <q-separator class="q-my-md" />

          <!-- Address Section -->
          <div class="text-h6">Address</div>
          <div class="row q-col-gutter-md">
            <div class="col-12 col-md-6">
              <q-input
                v-model="form.street"
                label="Street"
                :rules="[val => !!val || 'Street is required']"
              />
            </div>
            <div class="col-12 col-md-6">
              <q-input
                v-model="form.city"
                label="City"
                :rules="[val => !!val || 'City is required']"
              />
            </div>
            <div class="col-12 col-md-6">
              <q-input
                v-model="form.zip"
                label="ZIP Code"
                :rules="[val => !!val || 'ZIP is required']"
              />
            </div>
          </div>

          <q-separator class="q-my-md" />

          <!-- Preferences Section -->
          <div class="text-h6">Preferences</div>
          <div class="row q-col-gutter-md">
            <div class="col-12 col-md-6">
              <q-toggle v-model="form.newsletter" label="Subscribe to Newsletter" />
            </div>
            <div class="col-12 col-md-6">
              <q-select
                v-model="form.theme"
                :options="themes"
                label="Theme Preference"
              />
            </div>
          </div>

          <q-btn type="submit" label="Register" color="primary" class="q-mt-md" />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const themes = ['Light', 'Dark', 'Auto']

const form = ref({
  name: '',
  email: '',
  street: '',
  city: '',
  zip: '',
  newsletter: false,
  theme: 'Light',
})

function onSubmit() {
  $q.notify({ type: 'positive', message: 'Registration successful!' })
}
</script>

<style scoped>
.q-card {
  max-width: 700px;
  margin: 0 auto;
}
</style>
