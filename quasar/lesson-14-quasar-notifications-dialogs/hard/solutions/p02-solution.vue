<template>
  <div class="q-pa-md">
    <q-btn label="Open Wizard" color="primary" @click="openWizard" />
  </div>
</template>

<script setup>
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue'

// Multi-step dialog wizard component
const WizardDialog = defineComponent({
  name: 'WizardDialog',
  emits: ['ok'],
  setup(props, { emit }) {
    const step = ref(1)
    const form = ref({ name: '', email: '', plan: 'basic' })
    const errors = ref({})

    function validateStep() {
      errors.value = {}
      if (step.value === 1) {
        if (!form.value.name.trim()) errors.value.name = 'Name is required'
        if (!form.value.email.trim()) errors.value.email = 'Email is required'
      }
      return Object.keys(errors.value).length === 0
    }

    function next() {
      if (validateStep()) step.value++
    }
    function prev() {
      if (step.value > 1) step.value--
    }
    function finish() {
      emit('ok', { ...form.value })
    }

    return { step, form, errors, next, prev, finish }
  },
  template: `
    <q-card class="q-pa-md" style="min-width: 400px">
      <q-card-section>
        <div class="text-h6">Wizard — Step {{ step }} of 3</div>
        <q-linear-progress :value="step / 3" class="q-mt-sm" color="primary" />
      </q-card-section>

      <q-card-section v-if="step === 1">
        <q-input v-model="form.name" label="Name" :error="!!errors.name" :error-message="errors.name" />
        <q-input v-model="form.email" label="Email" type="email" :error="!!errors.email" :error-message="errors.email" />
      </q-card-section>

      <q-card-section v-if="step === 2">
        <p><strong>Name:</strong> {{ form.name }}</p>
        <p><strong>Email:</strong> {{ form.email }}</p>
        <q-select v-model="form.plan" :options="['basic', 'pro', 'enterprise']" label="Plan" />
      </q-card-section>

      <q-card-section v-if="step === 3">
        <p>Confirm your details:</p>
        <p><strong>Name:</strong> {{ form.name }}</p>
        <p><strong>Email:</strong> {{ form.email }}</p>
        <p><strong>Plan:</strong> {{ form.plan }}</p>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Cancel" color="grey" v-close-popup />
        <q-btn v-if="step > 1" flat label="Back" @click="prev" />
        <q-btn v-if="step < 3" flat label="Next" color="primary" @click="next" />
        <q-btn v-if="step === 3" flat label="Confirm" color="positive" @click="finish" v-close-popup />
      </q-card-actions>
    </q-card>
  `,
})

const $q = useQuasar()

function openWizard() {
  $q.dialog({
    component: WizardDialog,
  }).onOk((data) => {
    $q.notify({
      type: 'positive',
      message: `Wizard complete: ${data.name} (${data.plan})`,
      position: 'top',
      timeout: 5000,
    })
  }).onCancel(() => {
    $q.notify({ type: 'info', message: 'Wizard cancelled' })
  })
}
</script>
