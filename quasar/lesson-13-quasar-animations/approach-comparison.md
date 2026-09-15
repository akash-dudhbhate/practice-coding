# Lesson 13 — Approach Comparison

## Problem: Animate Show/Hide

### Approach 1: CSS animation
```css
@keyframes fadeIn { from { opacity: 0; } }
.show { animation: fadeIn 0.3s; }
```

### Approach 2: Vue transition
```vue
<transition name="fade"><div v-if="show" /></transition>
```

**Winner:** Approach 2 — handles enter/leave automatically.

---

## Problem: List Animation

### Approach 1: transition
```vue
<transition><ul v-if="items.length" /></transition>
```

### Approach 2: transition-group
```vue
<transition-group name="list" tag="ul"><li v-for="..." :key="..." /></transition-group>
```

**Winner:** Approach 2 — animates individual items.
