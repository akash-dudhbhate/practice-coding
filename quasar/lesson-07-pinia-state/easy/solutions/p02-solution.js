/**
 * Component using useCounterStore with storeToRefs.
 * The store is imported from p01-solution.js.
 *
 * This file exports a Vue component object that uses the counter store.
 */
import { useCounterStore } from './p01-solution.js'
import { storeToRefs } from 'pinia'

// Vue component definition (options-style for .js compatibility)
export default {
  name: 'CounterComponent',
  setup() {
    // Initialize the store
    const store = useCounterStore()

    // Use storeToRefs for reactive state and getters
    const { count, double } = storeToRefs(store)

    // Actions can be destructured directly (they are not reactive refs)
    const { increment, decrement } = store

    return {
      count,
      double,
      increment,
      decrement,
    }
  },
  template: `
    <div class="counter-component">
      <p>Count: {{ count }}</p>
      <p>Double: {{ double }}</p>
      <q-btn label="Decrement" color="negative" @click="decrement" class="q-mr-sm" />
      <q-btn label="Increment" color="positive" @click="increment" />
    </div>
  `,
}

/*
 * Equivalent <script setup> version if using .vue:
 *
 * <template>
 *   <div>
 *     <p>Count: {{ count }}</p>
 *     <p>Double: {{ double }}</p>
 *     <q-btn label="-" color="negative" @click="decrement" />
 *     <q-btn label="+" color="positive" @click="increment" />
 *   </div>
 * </template>
 *
 * <script setup>
 * import { useCounterStore } from './p01-solution.js'
 * import { storeToRefs } from 'pinia'
 *
 * const store = useCounterStore()
 * const { count, double } = storeToRefs(store)
 * const { increment, decrement } = store
 * </script>
 */
