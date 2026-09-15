# Lesson 05 — Approach Comparison

## Problem: Track Changes

### Approach 1: watch
```javascript
watch(count, (newVal) => { saveToLocalStorage(newVal); });
```

### Approach 2: watchEffect
```javascript
watchEffect(() => { saveToLocalStorage(count.value); });
```

**Winner:** Approach 1 — explicit, gets old value. Approach 2 for simple side effects.

---

## Problem: Derived State

### Approach 1: Method
```javascript
function fullName() { return first.value + " " + last.value; }
```
**Cons:** Recomputes every call.

### Approach 2: Computed
```javascript
const fullName = computed(() => first.value + " " + last.value);
```

**Winner:** Approach 2 — cached, reactive.
