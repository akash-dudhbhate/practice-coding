# Lesson 05 — Debug Exercises

## Debug 01 (Easy: Adding New Property
```javascript
const state = reactive({ user: { name: "A" } });
state.user.age = 25; // reactive?
```
<details><summary>Answer</summary>
In Vue 3, this IS reactive (Proxy-based). In Vue 2, it wasn't (needed `Vue.set`). Vue 3 fixed this.
</details>

## Debug 02 (Medium: Array Index Assignment
```javascript
const list = reactive([1, 2, 3]);
list[0] = 99; // reactive?
```
<details><summary>Answer</summary>
In Vue 3, yes (Proxy). In Vue 2, no (needed `Vue.set(list, 0, 99)`). Vue 3 handles this correctly.
</details>

## Debug 03 (Hard: Computed Not Updating
```javascript
const data = ref({ count: 0 });
const double = computed(() => data.value.count * 2);
data.value.count = 5; // does double update?
```
<details><summary>Answer</summary>
Yes — `data.value` is a reactive object. Changing `.count` triggers reactivity. `double` updates to 10.
</details>
