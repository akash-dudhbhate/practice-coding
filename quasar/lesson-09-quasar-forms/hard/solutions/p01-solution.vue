<template>
  <!-- Multi-step form wizard: 3 steps (personal, contact, review) -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Registration Wizard</div>
      </q-card-section>

      <!-- Progress indicator -->
      <q-stepper
        v-model="step"
        ref="stepperRef"
        color="primary"
        animated
        contracted
      >
        <!-- Step 1: Personal Info -->
        <q-step :name="1" title="Personal" :done="step > 1">
          <q-form ref="step1Form" class="q-gutter-md">
            <q-input
              v-model="form.name"
              label="Full Name"
              :rules="[val => !!val || 'Name is required']"
            />
            <q-input
              v-model="form.email"
              label="Email"
              type="email"
              :rules="[
                val => !!val || 'Email is required',
                val => /.+@.+\..+/.test(val) || 'Invalid email'
              ]"
            />
          </q-form>
        </q-step>

        <!-- Step 2: Contact Info -->
        <q-step :name="2" title="Contact" :done="step > 2">
          <q-form ref="step2Form" class="q-gutter-md">
            <q-input
              v-model="form.phone"
              label="Phone Number"
              :rules="[val => !!val || 'Phone is required']"
            />
            <q-input
              v-model="form.address"
              label="Address"
              :rules="[val => !!val || 'Address is required']"
            />
          </q-form>
        </q-step>

        <!-- Step 3: Review -->
        <q-step :name="3" title="Review">
          <div class="text-h6">Review Your Information</div>
          <q-list bordered separator class="q-mt-md">
            <q-item><q-item-section><strong>Name:</strong> {{ form.name }}</q-item-section></q-item>
            <q-item><q-item-section><strong>Email:</strong> {{ form.email }}</q-item-section></q-item>
            <q-item><q-item-section><strong>Phone:</strong> {{ form.phone }}</q-item-section></q-item>
            <q-item><q-item-section><strong>Address:</strong> {{ form.address }}</q-item-section></q-item>
          </q-list>
        </q-step>

        <!-- Navigation buttons -->
        <template #navigation>
          <q-stepper-navigation>
            <q-btn
              v-if="step < 3"
              label="Next"
              color="primary"
              @click="validateAndNext"
            />
            <q-btn
              v-if="step === 3"
              label="Submit"
              color="positive"
              @click="onSubmit"
            />
            <q-btn
              v-if="step > 1"
              label="Back"
              color="grey"
              flat
              class="q-ml-sm"
              @click="stepperRef.previous()"
            />
          </q-stepper-navigation>
        </template>
      </q-stepper>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const step = ref(1)
const stepperRef = ref(null)
const step1Form = ref(null)
const step2Form = ref(null)

const form = ref({
  name: '',
  email: '',
  phone: '',
  address: '',
})

// Validate current step before moving to next
async function validateAndNext() {
  const currentForm = step.value === 1 ? step1Form.value : step2Form.value
  if (currentForm) {
    const valid = await currentForm.validate()
    if (valid) {
      stepperRef.value.next()
    }
  } else {
    stepperRef.value.next()
  }
}

function onSubmit() {
  $q.notify({ type: 'positive', message: 'Registration complete!' })
}
</script>

<style scoped>
.q-card {
  max-width: 600px;
  margin: 0 auto;
}
</style>
