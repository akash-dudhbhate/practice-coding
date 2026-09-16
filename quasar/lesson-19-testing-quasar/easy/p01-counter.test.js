/**
 * LESSON 19 — Testing Quasar Apps
 * EASY P01 — Counter Component Test
 * ============================================
 * CONCEPT: @vue/test-utils' mount() renders a component in jsdom;
 * wrapper.find('[data-test=...]') selects elements, .trigger('click')
 * fires events (await it — DOM updates are async), .text()/.classes()
 * make assertions.
 *
 * PROBLEM: Write a Vitest suite for an inline Counter component
 * (data-test="count" paragraph, "increment"/"decrement" buttons).
 * Assert the initial count is 0, increment → 1, decrement → -1.
 *
 * TRY THIS: const wrapper = mount(Counter)
 * await wrapper.find('[data-test="increment"]').trigger('click')
 * expect(wrapper.find('[data-test="count"]').text()).toBe('1')
 *
 * EXPECTED OUTPUT: Three passing its covering initial/increment/decrement.
 *
 * CHECK: python3 check.py easy/p01
 */
// TODO: write your counter tests here
