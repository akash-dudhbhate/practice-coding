# lesson-19-testing-quasar — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not installing Quasar plugin
```javascript
// WRONG — components don't render
mount(MyComp);
// CORRECT
installQuasarPlugin();
mount(MyComp);
```

## Mistake 02: Not mocking $q
```javascript
// WRONG — $q undefined
// CORRECT
config.global.mocks = { $q: { notify: vi.fn() } };
```

## Mistake 03: Not awaiting async
```javascript
// WRONG
test("x", () => { mount(C); expect(...); });
// CORRECT
test("x", async () => { mount(C); await flushPromises(); expect(...); });
```

## Mistake 04: Testing implementation details
```javascript
// WRONG — tests internals
expect(wrapper.vm.internalState).toBe(true);
// CORRECT — test behavior
expect(wrapper.text()).toContain("Saved");
```

## Mistake 05: Not using testing extension
```bash
# Use official extension, not manual setup
quasar ext add @quasar/testing-unit-vitest
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No installQuasarPlugin
### Before
```javascript
mount(MyComp); // Quasar components don't render
```
### After
```javascript
installQuasarPlugin();
mount(MyComp);
```

## Refactor 02 (Medium): Not Mocking $q
### Before
```javascript
await wrapper.vm.$q.notify("test"); // undefined
```
### After
```javascript
config.global.mocks = { $q: { notify: vi.fn() } };
```

## Refactor 03 (Hard: Testing Implementation
### Before
```javascript
expect(wrapper.vm.internalState).toBe(true);
```
### After
```javascript
expect(wrapper.text()).toContain("Saved");
```

---

## Approach Comparison — different ways to solve it

## Problem: Test Setup

### Approach 1: Manual
```javascript
// Configure Quasar, plugins, mocks manually
```

### Approach 2: Testing extension
```bash
quasar ext add @quasar/testing-unit-vitest
```

**Winner:** Approach 2 — handles everything, official.

---

## Problem: Mock Plugins

### Approach 1: Global mock
```javascript
config.global.mocks = { $q: { notify: vi.fn() } };
```

### Approach 2: Per-test mock
```javascript
const notify = vi.fn();
mount(C, { global: { mocks: { $q: { notify } } } });
```

**Winner:** Approach 2 — isolated, reset per test.
