<template>
  <div class="q-pa-md">
    <q-btn label="Open Custom Dialog" color="primary" @click="openCustomDialog" />
  </div>
</template>

<script setup>
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue'

// Custom dialog component with form
const CustomFormDialog = defineComponent({
  name: 'CustomFormDialog',
  props: ['name', 'email'],
  emits: ['ok'],
  setup(props, { emit }) {
    const form = ref({ name: props.name || '', email: props.email || '' })
    return { form, emit }
  },
  template: `
    <q-card class="q-pa-md" style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">Enter Your Details</div>
      </q-card-section>
      <q-card-section>
        <q-input v-model="form.name" label="Name" />
        <q-input v-model="form.email" label="Email" type="email" />
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="Cancel" color="grey" v-close-popup />
        <q-btn flat label="OK" color="primary" @click="emit('ok', { ...form })" v-close-popup />
      </q-card-actions>
    </q-card>
  `,
})

const $q = useQuasar()

function openCustomDialog() {
  $q.dialog({
    component: CustomFormDialog,
  }).onOk((data) => {
    $q.notify({
      type: 'positive',
      message: `Form data: ${data.name} (${data.email})`,
      position: 'top',
      timeout: 5000,
    })
  })
}
</script>
