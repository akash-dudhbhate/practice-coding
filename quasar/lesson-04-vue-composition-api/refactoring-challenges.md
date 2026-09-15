# Lesson 04 — Refactoring Challenges

## Refactor 01 (Easy): Options API for Simple Component
### Before
```javascript
export default { data() { return { count: 0 }; }, methods: { inc() { this.count++; } } }
```
### After
```javascript
const count = ref(0);
const inc = () => count.value++;
```

## Refactor 02 (Medium): setup() Function
### Before
```javascript
export default {
  setup() {
    const count = ref(0);
    return { count };
  }
}
```
### After
```vue
<script setup>
const count = ref(0);
</script>
```

## Refactor 03 (Hard: Destructured Reactive
### Before
```javascript
const state = reactive({ count: 0 });
const { count } = state; // loses reactivity
```
### After
```javascript
const state = reactive({ count: 0 });
const { count } = toRefs(state);
```
