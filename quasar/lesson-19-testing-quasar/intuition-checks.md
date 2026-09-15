# Lesson 19 — Intuition Checks

## Check 01: Quasar testing setup
<details><summary>Answer</summary>
Install testing extension: `quasar ext add @quasar/testing-unit-vitest`. Provides `installQuasarPlugin()`, test utilities, config. Works with Vitest or Jest.
</details>

## Check 02: installQuasarPlugin
```javascript
installQuasarPlugin();
test("test", () => {
  const wrapper = mount(MyComponent);
  // q-btn, q-input etc. work
});
```
<details><summary>Answer</summary>
Registers Quasar components globally for tests. Call once at top of test file. Without it, Quasar components don't render.
</details>

## Check 03: Mocking $q
```javascript
const notify = vi.fn();
config.global.mocks = { $q: { notify, dark: { isActive: false } } };
```
<details><summary>Answer</summary>
Mock Quasar plugins. `$q.notify`, `$q.dialog` etc. Replace with vi.fn() to assert calls. Dark mode, screen size also mockable.
</details>

## Check 04: flushPromises
```javascript
import { flushPromises } from "@vue/test-utils";
await flushPromises(); // resolve pending promises
```
<details><summary>Answer</summary>
Waits for all pending promises to resolve. Needed after async operations in component. Without it, DOM not updated.
</details>

## Check 05: Testing q-btn click
```javascript
const wrapper = mount(MyComp);
await wrapper.findComponent({ name: "QBtn" }).trigger("click");
expect(emitted).toHaveBeenCalled();
```
<details><summary>Answer</summary>
Find Quasar component by name. Trigger events. Assert handlers called. Quasar components have specific names (QBtn, QInput).
</details>
