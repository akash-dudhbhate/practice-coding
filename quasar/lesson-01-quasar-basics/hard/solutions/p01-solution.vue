<!--
  Lesson 01 - Quasar Basics - Hard - Problem 01
  Full todo list with toggle done (q-checkbox), delete button,
  and empty state message.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md" style="max-width: 500px; margin: 0 auto;">
    <h2 class="text-h5">Todo List</h2>

    <!-- Input row to add a new todo -->
    <div class="row q-gutter-sm full-width">
      <q-input
        v-model="newTodo"
        label="What needs to be done?"
        outlined
        class="col"
        @keyup.enter="addTodo"
      />
      <q-btn color="primary" label="Add" @click="addTodo" />
    </div>

    <!-- Empty state when there are no todos -->
    <q-banner v-if="todos.length === 0" class="bg-grey-2 full-width">
      No todos yet. Add one to get started!
    </q-banner>

    <!-- Todo list -->
    <q-list bordered separator class="full-width">
      <q-item v-for="todo in todos" :key="todo.id">
        <!-- Checkbox toggles the done state -->
        <q-item-section avatar>
          <q-checkbox v-model="todo.done" />
        </q-item-section>

        <!-- Label with strikethrough when done -->
        <q-item-section>
          <q-item-label :class="{ 'text-strike': todo.done }">
            {{ todo.text }}
          </q-item-label>
        </q-item-section>

        <!-- Delete button -->
        <q-item-section side>
          <q-btn flat dense color="negative" icon="delete" @click="deleteTodo(todo.id)" />
        </q-item-section>
      </q-item>
    </q-list>

    <!-- Summary -->
    <p class="text-grey-7">
      {{ doneCount }} of {{ todos.length }} completed
    </p>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'

// Each todo is an object with id, text, and done flag
const todos = ref([
  { id: 1, text: 'Learn Vue 3 Composition API', done: true },
  { id: 2, text: 'Master Quasar components', done: false },
])

// Auto-incrementing id for new todos
let nextId = 3

const newTodo = ref('')

// Computed count of completed todos
const doneCount = computed(() => todos.value.filter(t => t.done).length)

// Add a new todo if the input is non-empty
function addTodo() {
  const trimmed = newTodo.value.trim()
  if (trimmed) {
    todos.value.push({ id: nextId++, text: trimmed, done: false })
    newTodo.value = ''
  }
}

// Delete a todo by id
function deleteTodo(id) {
  todos.value = todos.value.filter(t => t.id !== id)
}
</script>

<style scoped>
/* text-strike utility adds a line-through for completed items */
</style>
