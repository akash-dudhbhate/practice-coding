# Lesson 04 — Approach Comparison

## Problem: Component Logic

### Approach 1: Options API
```javascript
export default {
  data() { return { count: 0 }; },
  methods: { increment() { this.count++; } },
  computed: { double() { return this.count * 2; } }
}
```

### Approach 2: Composition API
```javascript
const count = ref(0);
const increment = () => count.value++;
const double = computed(() => count.value * 2);
```

**Winner:** Approach 2 — better organization, TypeScript, reusability.

---

## Problem: Reactive State

### Approach 1: ref
```javascript
const count = ref(0);
const name = ref("");
```

### Approach 2: reactive
```javascript
const state = reactive({ count: 0, name: "" });
```

**Winner:** ref for independent values. reactive for grouped state.
