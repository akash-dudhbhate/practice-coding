<!--
  Lesson 13 - Easy - P01: Fade Transition
  Toggle button showing/hiding a div with a fade transition.
  Uses Vue's <Transition> component with CSS classes.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Fade Transition</div>

    <q-btn color="primary" :label="visible ? 'Hide' : 'Show'" no-caps @click="visible = !visible" class="q-mb-md" />

    <!-- Vue <Transition> component wraps the toggled element -->
    <Transition>
      <div v-if="visible" class="fade-box">
        This content fades in and out smoothly!
      </div>
    </Transition>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const visible = ref(true)
</script>

<style scoped>
.fade-box {
  padding: 24px;
  background: #e8eaf6;
  border-radius: 8px;
  font-size: 16px;
}

/* Vue Transition CSS classes for fade effect */
/* .v-enter-active and .v-leave-active apply during the transition */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.4s ease;
}

/* .v-enter-from and .v-leave-to define start/end states */
.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
