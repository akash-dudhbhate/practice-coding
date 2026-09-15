<!--
  Touch Gestures Demo
  --------------------
  Uses Quasar touch directives:
    v-touch-swipe  — swipe left/right to change a counter
    v-touch-hold   — long-press to reset the counter to zero
  The current value and brief instructions are displayed so the user
  knows which gestures are available.
-->
<template>
  <q-page class="column flex-center q-pa-md">
    <!-- Instruction panel -->
    <q-card flat bordered class="q-pa-md q-mb-lg text-center">
      <div class="text-subtitle1">Touch Gesture Counter</div>
      <p class="text-grey-7 q-mb-none">
        Swipe <b>left</b> to decrement · Swipe <b>right</b> to increment ·
        <b>Long-press</b> to reset
      </p>
    </q-card>

    <!-- Touch area — directives listen on this element -->
    <div
      v-touch-swipe.left="decrement"
      v-touch-swipe.right="increment"
      v-touch-hold="reset"
      class="touch-area column flex-center"
    >
      <div class="text-h1 text-primary">{{ count }}</div>
      <div class="text-caption text-grey-6">Swipe or hold here</div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Reactive counter value
const count = ref(0)

// Swipe right → increase
function increment() {
  count.value++
}

// Swipe left → decrease (never go below zero)
function decrement() {
  count.value = Math.max(0, count.value - 1)
}

// Long-press → reset to zero
function reset() {
  count.value = 0
}
</script>

<style scoped>
.touch-area {
  width: 300px;
  height: 300px;
  border: 2px dashed var(--q-primary);
  border-radius: 16px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: none; /* let Quasar handle the gestures */
}
</style>
