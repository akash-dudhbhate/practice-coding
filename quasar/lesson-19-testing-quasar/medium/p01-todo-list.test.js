/**
 * LESSON 19 — Testing Quasar Apps
 * MEDIUM P01 — TodoList Component Test
 * ============================================
 * CONCEPT: setValue() types into inputs, findAll() counts repeated
 * elements, .classes() checks toggled classes. Mount once per test in
 * beforeEach so state doesn't leak.
 *
 * PROBLEM: Test an inline TodoList (input[data-test="new-todo"], add
 * button, todo-item li's with toggleable text + delete buttons): initial
 * todos render, typing + add appends one, clicking the text toggles
 * 'done', delete removes it.
 *
 * TRY THIS: await wrapper.find('[data-test="new-todo"]').setValue('X')
 * await wrapper.find('[data-test="add"]').trigger('click')
 * expect(wrapper.findAll('[data-test="todo-item"]')).toHaveLength(2)
 *
 * EXPECTED OUTPUT: Four its covering render/add/toggle/delete.
 *
 * CHECK: python3 check.py medium/p01
 */
// TODO: write your TodoList tests here
