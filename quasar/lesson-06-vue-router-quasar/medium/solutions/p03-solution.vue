<template>
  <!-- User list page with links to user detail pages using named routes -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">User List</div>
    <q-list bordered separator>
      <q-item v-for="user in users" :key="user.id">
        <q-item-section>
          <q-item-label>{{ user.name }}</q-item-label>
          <q-item-label caption>{{ user.email }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <!-- q-btn with :to using named route and params -->
          <q-btn
            label="View Details"
            color="primary"
            size="sm"
            :to="{ name: 'UserDetail', params: { id: user.id } }"
          />
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script setup>
// Mock user data - 5 users
const users = [
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com' },
  { id: 3, name: 'Carol Williams', email: 'carol@example.com' },
  { id: 4, name: 'Dave Brown', email: 'dave@example.com' },
  { id: 5, name: 'Eve Davis', email: 'eve@example.com' },
]
</script>

<style scoped>
.q-page {
  max-width: 600px;
  margin: 0 auto;
}
</style>
