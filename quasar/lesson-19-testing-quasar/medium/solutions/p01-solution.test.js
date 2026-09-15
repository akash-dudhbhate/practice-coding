// Tests for TodoList component
// Run: vitest run medium/p01-solution.test.js
import { describe, it, expect, beforeEach } from 'vitest'
import { mount } from '@vue/test-utils'

// --- TodoList component (inline for self-contained test) ---
const TodoList = {
  data() {
    return { todos: [{ id: 1, text: 'Learn Vue', done: false }], newTodo: '' }
  },
  template: `
    <div data-test="todo-list">
      <input data-test="new-todo" v-model="newTodo" @keyup.enter="addTodo" />
      <button data-test="add" @click="addTodo">Add</button>
      <ul>
        <li v-for="todo in todos" :key="todo.id" data-test="todo-item">
          <span data-test="todo-text" :class="{ done: todo.done }" @click="toggle(todo.id)">{{ todo.text }}</span>
          <button data-test="delete" @click="remove(todo.id)">x</button>
        </li>
      </ul>
    </div>
  `,
  methods: {
    addTodo() {
      if (!this.newTodo.trim()) return
      this.todos.push({ id: Date.now(), text: this.newTodo, done: false })
      this.newTodo = ''
    },
    toggle(id) {
      const todo = this.todos.find(t => t.id === id)
      if (todo) todo.done = !todo.done
    },
    remove(id) {
      this.todos = this.todos.filter(t => t.id !== id)
    },
  },
}

// --- Tests ---
describe('TodoList', () => {
  let wrapper
  beforeEach(() => { wrapper = mount(TodoList) })

  it('renders initial todos', () => {
    expect(wrapper.findAll('[data-test="todo-item"]')).toHaveLength(1)
    expect(wrapper.find('[data-test="todo-text"]').text()).toBe('Learn Vue')
  })

  it('adds a todo on button click', async () => {
    await wrapper.find('[data-test="new-todo"]').setValue('New task')
    await wrapper.find('[data-test="add"]').trigger('click')
    expect(wrapper.findAll('[data-test="todo-item"]')).toHaveLength(2)
    expect(wrapper.findAll('[data-test="todo-text"]')[1].text()).toBe('New task')
  })

  it('toggles todo done state on click', async () => {
    await wrapper.find('[data-test="todo-text"]').trigger('click')
    expect(wrapper.find('[data-test="todo-text"]').classes()).toContain('done')
  })

  it('deletes a todo', async () => {
    await wrapper.find('[data-test="delete"]').trigger('click')
    expect(wrapper.findAll('[data-test="todo-item"]')).toHaveLength(0)
  })
})
