<template>
  <div class="q-pa-md">
    <div class="row q-mb-md items-center">
      <q-space />
      <q-btn label="Add User" color="primary" @click="openCreateDialog" />
    </div>

    <q-table :rows="users" :columns="columns" row-key="id" :loading="loading">
      <template #body-cell-actions="props">
        <q-td :props="props">
          <q-btn flat icon="edit" @click="openEditDialog(props.row)" />
          <q-btn flat icon="delete" color="negative" @click="confirmDelete(props.row)" />
        </q-td>
      </template>
    </q-table>

    <!-- Create/Edit Dialog -->
    <q-dialog v-model="dialogOpen">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">{{ editing ? 'Edit User' : 'Create User' }}</div>
        </q-card-section>
        <q-card-section>
          <q-input v-model="form.name" label="Name" />
          <q-input v-model="form.email" label="Email" type="email" />
          <q-input v-model="form.phone" label="Phone" />
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" @click="dialogOpen = false" />
          <q-btn flat label="Save" color="primary" :loading="saving" @click="saveUser" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const API = 'https://jsonplaceholder.typicode.com/users'

const users = ref([])
const loading = ref(false)
const saving = ref(false)
const dialogOpen = ref(false)
const editing = ref(null)
const form = ref({ name: '', email: '', phone: '' })

const columns = [
  { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
  { name: 'email', label: 'Email', field: 'email', align: 'left' },
  { name: 'phone', label: 'Phone', field: 'phone', align: 'left' },
  { name: 'actions', label: 'Actions', field: 'actions', align: 'center' },
]

async function fetchUsers() {
  loading.value = true
  try {
    const res = await fetch(API)
    users.value = await res.json()
  } catch (e) {
    $q.notify({ type: 'negative', message: 'Failed to load users' })
  } finally {
    loading.value = false
  }
}

function openCreateDialog() {
  editing.value = null
  form.value = { name: '', email: '', phone: '' }
  dialogOpen.value = true
}

function openEditDialog(user) {
  editing.value = user
  form.value = { ...user }
  dialogOpen.value = true
}

async function saveUser() {
  saving.value = true
  try {
    if (editing.value) {
      await fetch(`${API}/${editing.value.id}`, {
        method: 'PUT', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form.value),
      })
      const idx = users.value.findIndex(u => u.id === editing.value.id)
      if (idx !== -1) users.value[idx] = { ...form.value, id: editing.value.id }
      $q.notify({ type: 'positive', message: 'User updated' })
    } else {
      const res = await fetch(API, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form.value),
      })
      const newUser = await res.json()
      users.value.unshift(newUser)
      $q.notify({ type: 'positive', message: 'User created' })
    }
    dialogOpen.value = false
  } catch (e) {
    $q.notify({ type: 'negative', message: 'Save failed' })
  } finally {
    saving.value = false
  }
}

function confirmDelete(user) {
  $q.dialog({
    title: 'Delete User',
    message: `Delete ${user.name}?`,
    cancel: true,
  }).onOk(async () => {
    try {
      await fetch(`${API}/${user.id}`, { method: 'DELETE' })
      users.value = users.value.filter(u => u.id !== user.id)
      $q.notify({ type: 'positive', message: 'User deleted' })
    } catch (e) {
      $q.notify({ type: 'negative', message: 'Delete failed' })
    }
  })
}

onMounted(fetchUsers)
</script>
