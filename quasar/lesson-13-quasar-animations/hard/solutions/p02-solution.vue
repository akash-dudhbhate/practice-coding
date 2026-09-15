<!--
  Lesson 13 - Hard - P02: Staggered Card Entrance
  6 cards fade in one by one with 100ms delay using CSS animation-delay.
  Hover effect scales up the card.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Staggered Card Entrance</div>

    <div class="row q-col-gutter-md">
      <div
        class="col-12 col-sm-6 col-md-4"
        v-for="(card, index) in cards"
        :key="card.id"
      >
        <q-card class="stagger-card" :style="{ animationDelay: `${index * 100}ms` }">
          <q-card-section class="text-center">
            <q-icon :name="card.icon" size="48px" :color="card.color" />
            <div class="text-h6 q-mt-sm">{{ card.title }}</div>
            <div class="text-body2 text-grey-7">{{ card.description }}</div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// 6 cards for the staggered grid
const cards = ref([
  { id: 1, icon: 'flight', color: 'primary', title: 'Travel', description: 'Explore the world' },
  { id: 2, icon: 'restaurant', color: 'secondary', title: 'Food', description: 'Taste new cuisines' },
  { id: 3, icon: 'music_note', color: 'accent', title: 'Music', description: 'Listen and enjoy' },
  { id: 4, icon: 'sports_esports', color: 'warning', title: 'Gaming', description: 'Play and compete' },
  { id: 5, icon: 'book', color: 'info', title: 'Reading', description: 'Learn and grow' },
  { id: 6, icon: 'fitness_center', color: 'positive', title: 'Fitness', description: 'Stay healthy' },
])
</script>

<style scoped>
/* Staggered entrance: each card fades and slides up with a delay */
.stagger-card {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeInUp 0.6s ease forwards;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

/* Hover effect: scale up slightly */
.stagger-card:hover {
  transform: scale(1.03);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

/* Keyframes for the entrance animation */
@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
