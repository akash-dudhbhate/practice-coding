/**
 * LESSON 19 — Testing Quasar Apps
 * EASY P02 — UserCard Props & Events Test
 * ============================================
 * CONCEPT: Pass props at mount time ({ props: { user } }); assert emitted
 * events via wrapper.emitted('delete') — an array of call-arg arrays.
 *
 * PROBLEM: Test an inline UserCard (props: user {id,name,email}; emits
 * 'delete'): it renders name + email in data-test elements, and clicking
 * the delete button emits 'delete' with the user's id as payload.
 *
 * TRY THIS: mount(UserCard, { props: { user: mockUser } })
 * expect(wrapper.emitted('delete')[0]).toEqual([1])
 *
 * EXPECTED OUTPUT: Two passing its — prop rendering and the delete event
 * payload.
 *
 * CHECK: python3 check.py easy/p02
 */
// TODO: write your UserCard tests here
