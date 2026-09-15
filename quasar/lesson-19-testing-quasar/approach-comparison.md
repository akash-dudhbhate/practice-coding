# Lesson 19 — Approach Comparison

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
