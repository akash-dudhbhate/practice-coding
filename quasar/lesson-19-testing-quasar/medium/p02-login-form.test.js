/**
 * LESSON 19 — Testing Quasar Apps
 * MEDIUM P02 — LoginForm with Quasar Test
 * ============================================
 * CONCEPT: Quasar components need the plugin registered in tests:
 * mount(Comp, { global: { plugins: [[Quasar, {}]] } }). Then test
 * disabled states via attributes('disable') and emitted payloads.
 *
 * PROBLEM: Test an inline LoginForm (q-form with q-inputs + submit
 * q-btn, emits 'submit', shows error text): submit is disabled when
 * fields are empty, valid input emits 'submit' with {email, password},
 * an invalid email shows an error element.
 *
 * TRY THIS: function mountWithQuasar(c) {
 *   return mount(c, { global: { plugins: [[Quasar, {}]] } }) }
 * expect(wrapper.emitted('submit')[0][0]).toEqual({email, password})
 *
 * EXPECTED OUTPUT: Three its — disabled submit, emit payload, error shown.
 *
 * CHECK: python3 check.py medium/p02
 */
// TODO: write your LoginForm tests here
