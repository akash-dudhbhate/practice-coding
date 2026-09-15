# Lesson 19 — Debug Exercises

## Debug 01: Not Mounting with Quasar
```javascript
import { mount } from "@vue/test-utils";
mount(MyComponent); // Quasar components not registered
```
<details><summary>Answer</summary>
**Bug:** Quasar components not registered — q-btn etc. don't render.
**Fix:** Use `installQuasarPlugin()` from `@quasar/quasar-app-extension-testing-unit-vitest`.
</details>

## Debug 02: No Plugin Mock
```javascript
await wrapper.vm.$q.notify("test");
// Notify not registered in test
```
<details><summary>Answer</summary>
**Bug:** Notify plugin not available in test.
**Fix:** Mock: `config.global.mocks.$q = { notify: vi.fn() }`.
</details>

## Debug 03: Async Not Awaited
```javascript
test("loads", () => {
  mount(Component);
  expect(screen.getByText("Data")).toBeInTheDocument(); // not loaded yet
});
```
<details><summary>Answer</summary>
**Bug:** Async data not awaited.
**Fix:** `test("loads", async () => { ... await flushPromises(); ... })`.
</details>
