<!--
  Lesson 12 - Hard - P01: Complete Themed Dashboard
  Custom brand colors, responsive grid, typography hierarchy, icons in
  navigation and cards, dark mode support, spacing utilities. 6+ components.
-->
<template>
  <q-page class="q-pa-md">
    <!-- Navigation bar with icons -->
    <q-bar class="bg-primary text-white q-mb-md rounded-borders">
      <q-icon name="dashboard" />
      <div class="text-h6">Dashboard</div>
      <q-space />
      <q-btn flat round dense icon="dark_mode" @click="$q.dark.toggle" />
      <q-btn flat round dense icon="notifications" />
      <q-btn flat round dense icon="account_circle" />
    </q-bar>

    <!-- Typography hierarchy -->
    <div class="q-mb-lg">
      <div class="text-h4">Analytics Overview</div>
      <div class="text-subtitle1 text-grey-7">Real-time metrics and performance indicators</div>
    </div>

    <!-- Stats cards: responsive grid with icons -->
    <div class="row q-col-gutter-md q-mb-lg">
      <div class="col-12 col-sm-6 col-md-3" v-for="stat in stats" :key="stat.label">
        <q-card flat bordered class="stat-card">
          <q-card-section class="row items-center q-gutter-md">
            <q-icon :name="stat.icon" :color="stat.color" size="40px" />
            <div>
              <div class="text-h5">{{ stat.value }}</div>
              <div class="text-caption text-grey-7">{{ stat.label }}</div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>

    <!-- Content section with cards -->
    <div class="row q-col-gutter-md">
      <div class="col-12 col-md-8">
        <q-card flat bordered>
          <q-card-section class="bg-primary text-white">
            <div class="text-h6">
              <q-icon name="chart_bar" class="q-mr-sm" />
              Recent Activity
            </div>
          </q-card-section>
          <q-card-section>
            <q-list>
              <q-item v-for="activity in activities" :key="activity.id">
                <q-item-section avatar>
                  <q-icon :name="activity.icon" :color="activity.color" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>{{ activity.title }}</q-item-label>
                  <q-item-label caption>{{ activity.time }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>
        </q-card>
      </div>

      <div class="col-12 col-md-4">
        <q-card flat bordered>
          <q-card-section class="bg-secondary text-white">
            <div class="text-h6">
              <q-icon name="task_alt" class="q-mr-sm" />
              Quick Actions
            </div>
          </q-card-section>
          <q-card-section class="q-gutter-sm">
            <q-btn color="primary" icon="add" label="New Project" no-caps class="full-width" />
            <q-btn color="secondary" icon="upload" label="Upload File" no-caps class="full-width" />
            <q-btn color="accent" icon="share" label="Share" no-caps class="full-width" />
          </q-card-section>
        </q-card>
      </div>
    </div>

    <!-- Footer with spacing utilities -->
    <div class="q-mt-xl q-pa-md text-center text-caption text-grey-6">
      Dashboard v1.0 — Powered by Quasar Framework
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Stats data for the 4 metric cards
const stats = ref([
  { label: 'Total Users', value: '12,543', icon: 'group', color: 'primary' },
  { label: 'Revenue', value: '$48.2k', icon: 'attach_money', color: 'positive' },
  { label: 'Orders', value: '1,205', icon: 'shopping_cart', color: 'secondary' },
  { label: 'Conversion', value: '3.2%', icon: 'trending_up', color: 'accent' },
])

// Recent activity list
const activities = ref([
  { id: 1, icon: 'person_add', color: 'primary', title: 'New user registered', time: '2 min ago' },
  { id: 2, icon: 'shopping_cart', color: 'secondary', title: 'New order placed', time: '15 min ago' },
  { id: 3, icon: 'payment', color: 'positive', title: 'Payment received', time: '1 hour ago' },
  { id: 4, icon: 'warning', color: 'warning', title: 'Low stock alert', time: '3 hours ago' },
])
</script>

<style scoped>
.stat-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
