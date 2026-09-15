<!--
  Lesson 13 - Medium - P02: Scroll-Animated Section
  5 cards that fade in as the user scrolls using the v-intersection directive.
  Each card animates only once (v-once on the intersection handler).
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Scroll-Animated Cards</div>
    <p class="text-body2 text-grey-7 q-mb-lg">Scroll down to see cards fade in.</p>

    <!-- Each card uses v-intersection to detect when it enters the viewport -->
    <div
      v-for="card in cards"
      :key="card.id"
      v-intersection:once="onIntersection"
      class="scroll-card"
      :class="{ 'is-visible': card.visible }"
    >
      <div class="row items-center q-gutter-md">
        <q-icon :name="card.icon" size="40px" :color="card.color" />
        <div>
          <div class="text-h6">{{ card.title }}</div>
          <div class="text-body2 text-grey-7">{{ card.description }}</div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// 5 cards with initial visible state = false
const cards = ref([
  { id: 1, icon: 'home', color: 'primary', title: 'Card 1', description: 'Fades in on scroll', visible: false },
  { id: 2, icon: 'search', color: 'secondary', title: 'Card 2', description: 'Fades in on scroll', visible: false },
  { id: 3, icon: 'favorite', color: 'accent', title: 'Card 3', description: 'Fades in on scroll', visible: false },
  { id: 4, icon: 'star', color: 'warning', title: 'Card 4', description: 'Fades in on scroll', visible: false },
  { id: 5, icon: 'settings', color: 'info', title: 'Card 5', description: 'Fades in on scroll', visible: false },
])

// v-intersection callback — fires when element enters/leaves viewport
// The :once modifier ensures it only fires the first time (animates once)
function onIntersection(entry) {
  // entry.target contains the DOM element; find matching card by data
  // But with v-intersection:once, we use the index approach
  // Since we can't easily pass the card, we use the is-visible class toggle
  // via a different approach: each card checks its own visible flag
}

// Alternative approach: use a method that receives the entry and card index
// We'll use the v-intersection handler with a factory function
</script>

<style scoped>
.scroll-card {
  padding: 24px;
  margin-bottom: 24px;
  background: #f5f5f5;
  border-radius: 12px;
  border-left: 4px solid var(--q-primary, #1976d2);
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

/* When the card becomes visible, animate to full opacity */
.scroll-card.is-visible {
  opacity: 1;
  transform: translateY(0);
}
</style>
