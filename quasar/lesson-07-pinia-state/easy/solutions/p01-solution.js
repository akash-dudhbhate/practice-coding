/**
 * Pinia store: useCounterStore
 * - count (ref state)
 * - double (computed getter)
 * - increment / decrement (actions)
 */
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // State
  const count = ref(0)

  // Getter: double the count
  const double = computed(() => count.value * 2)

  // Action: increment count
  function increment() {
    count.value++
  }

  // Action: decrement count
  function decrement() {
    count.value--
  }

  return {
    count,
    double,
    increment,
    decrement,
  }
})

/*
 * Example component usage:
 *
 * <template>
 *   <div>
 *     <p>Count: {{ count }}</p>
 *     <p>Double: {{ double }}</p>
 *     <q-btn label="-" @click="decrement" />
 *     <q-btn label="+" @click="increment" />
 *   </div>
 * </template>
 *
 * <script setup>
 * import { useCounterStore } from './p01-solution'
 * import { storeToRefs } from 'pinia'
 *
 * const store = useCounterStore()
 * const { count, double } = storeToRefs(store)
 * const { increment, decrement } = store
 * </script>
 */
