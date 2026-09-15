# Lesson 19 — Common Mistakes

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
