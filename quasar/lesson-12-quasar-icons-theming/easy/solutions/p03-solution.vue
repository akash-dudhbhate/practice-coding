<!--
  Lesson 12 - Easy - P03: Responsive Grid
  3 cards using col-12 col-md-6 col-lg-4 breakpoint classes.
  Each card has an icon, title, and description.
  Stacks on mobile (1 column), 2 columns on tablet, 3 on desktop.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Responsive Card Grid</div>

    <div class="row q-col-gutter-md">
      <!-- col-12: full width on mobile (stacks vertically)
           col-md-6: half width on tablet (2 columns)
           col-lg-4: third width on desktop (3 columns) -->
      <div class="col-12 col-md-6 col-lg-4" v-for="card in cards" :key="card.id">
        <q-card class="my-card full-height">
          <q-card-section class="text-center">
            <q-icon :name="card.icon" size="48px" :color="card.color" />
            <div class="text-h6 q-mt-sm">{{ card.title }}</div>
            <div class="text-body2 text-grey-7 q-mt-xs">{{ card.description }}</div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const cards = ref([
  {
    id: 1,
    icon: 'speed',
    color: 'primary',
    title: 'Fast Performance',
    description: 'Optimized for speed and efficiency in every interaction.',
  },
  {
    id: 2,
    icon: 'security',
    color: 'secondary',
    title: 'Secure by Design',
    description: 'Built-in security features to protect your data.',
  },
  {
    id: 3,
    icon: 'palette',
    color: 'accent',
    title: 'Beautiful UI',
    description: 'Material Design components with customizable themes.',
  },
])
</script>

<style scoped>
.my-card {
  transition: transform 0.2s ease;
}
.my-card:hover {
  transform: translateY(-4px);
}
</style>
