<template>
  <!-- Dynamic form: add/remove phone number fields -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Phone Numbers</div>
      </q-card-section>
      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <!-- Dynamic phone number fields -->
          <div
            v-for="(phone, index) in form.phones"
            :key="index"
            class="row items-center q-col-gutter-sm"
          >
            <div class="col">
              <q-input
                v-model="phone.value"
                :label="`Phone Number ${index + 1}`"
                :rules="[
                  val => !!val || 'Phone number is required',
                  val => val.length >= 10 || 'Must be at least 10 digits'
                ]"
              />
            </div>
            <div class="col-auto">
              <!-- Remove button (only show if more than 1 field) -->
              <q-btn
                v-if="form.phones.length > 1"
                round
                dense
                flat
                color="negative"
                icon="remove"
                @click="removePhone(index)"
              />
            </div>
          </div>

          <!-- Add another phone number -->
          <q-btn
            label="Add Another Phone"
            color="secondary"
            icon="add"
            outline
            @click="addPhone"
          />

          <q-btn type="submit" label="Submit" color="primary" class="q-ml-sm" />
        </q-form>
      </q-card-section>

      <!-- Display collected data -->
      <q-separator />
      <q-card-section>
        <div class="text-h6">Submitted Data</div>
        <pre>{{ submittedData }}</pre>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Form with dynamic phone array
const form = ref({
  phones: [{ value: '' }],
})

const submittedData = ref('')

// Add a new phone number field
function addPhone() {
  form.value.phones.push({ value: '' })
}

// Remove a phone number field by index
function removePhone(index) {
  form.value.phones.splice(index, 1)
}

// Submit: collect all phone numbers
function onSubmit() {
  const phones = form.value.phones.map((p) => p.value).filter(Boolean)
  submittedData.value = JSON.stringify(phones, null, 2)
  $q.notify({ type: 'positive', message: `${phones.length} phone number(s) submitted!` })
}
</script>

<style scoped>
.q-card {
  max-width: 600px;
  margin: 0 auto;
}
pre {
  white-space: pre-wrap;
  word-break: break-word;
}
</style>
