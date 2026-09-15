<!--
  Lesson 04 - Vue Composition API - Medium - Problem 03
  Timer using onMounted (setInterval) and onUnmounted (clearInterval).
  Display elapsed seconds. Start/stop buttons.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <h2 class="text-h6">Timer</h2>

    <!-- Display elapsed seconds -->
    <div class="text-h2 text-primary">{{ elapsed }}s</div>

    <!-- Start and stop buttons -->
    <div class="row q-gutter-md">
      <q-btn color="positive" label="Start" :disable="running" @click="start" />
      <q-btn color="negative" label="Stop" :disable="!running" @click="stop" />
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Elapsed time in seconds
const elapsed = ref(0)
// Whether the timer is currently running
const running = ref(false)
// Holds the interval ID so we can clear it later
let intervalId = null

// Start the timer
function start() {
  if (running.value) return
  running.value = true
  intervalId = setInterval(() => {
    elapsed.value++
  }, 1000)
}

// Stop the timer
function stop() {
  running.value = false
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = null
  }
}

// onMounted: auto-start the timer when the component mounts
onMounted(() => {
  start()
})

// onUnmounted: clean up the interval to prevent memory leaks
onUnmounted(() => {
  stop()
})
</script>

<style scoped>
</style>
