# Lesson 05 — Intuition Checks

## Check 01: How Vue reactivity works
<details><summary>Answer</summary>
Vue 3 uses Proxy. When you access reactive data, Vue tracks it as a dependency. When data changes, Vue triggers updates. Automatic — no manual subscribe.
</details>

## Check 02: Reactive limitations
```javascript
const state = reactive({ date: new Date() });
state.date.setDate(15); // triggers update?
```
<details><summary>Answer</summary>
No — mutating Date object doesn't trigger reactivity (Proxy doesn't intercept Date methods). Need to reassign: `state.date = new Date(state.date)`.
</details>

## Check 03: watch vs watchEffect
```javascript
watch(count, (newVal) => { ... });      // explicit dependency
watchEffect(() => { console.log(count.value); }); // auto-tracks
```
<details><summary>Answer</summary>
watch — specify what to watch, callback gets old/new values. watchEffect — runs immediately, auto-tracks dependencies used inside. Use watch for specific values, watchEffect for side effects.
</details>

## Check 04: Computed caching
```javascript
const expensive = computed(() => heavyCalc(data.value));
console.log(expensive.value); // computes
console.log(expensive.value); // cached
data.value = "new";
console.log(expensive.value); // recomputes
```
<details><summary>Answer</summary>
Computed caches result. Only recomputes when dependencies change. Multiple accesses use cache. More efficient than methods.
</details>

## Check 05: Shallow reactivity
```javascript
const state = shallowReactive({ a: { b: 1 } });
state.a.b = 2; // not reactive
```
<details><summary>Answer</summary>
`shallowReactive` — only top-level properties are reactive. Nested changes don't trigger updates. Use for performance with deep objects you don't need to track.
</details>
