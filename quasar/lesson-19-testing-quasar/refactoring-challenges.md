# Lesson 19 — Refactoring Challenges

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
