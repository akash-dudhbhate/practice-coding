# Lesson 05 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01 — ref and reactive side by side
- [ ] `title` declared with `ref('...')`.
- [ ] `book` declared with `reactive({ author: '...', year: ... })`.
- [ ] `ref` and `reactive` imported from 'vue'.
- [ ] Template displays `title`, `book.author`, and `book.year`.
- [ ] Button updates all three: `title.value = ...`, `book.author = ...`, `book.year = ...`.
- [ ] UI updates for all three values when button clicked.

### p02 — Deep nested reactive
- [ ] Reactive object has 3 levels: `user.profile.settings.theme`.
- [ ] Initial `theme` value displayed in template.
- [ ] Button changes `user.profile.settings.theme` to a new value.
- [ ] UI updates when the deepest property changes.
- [ ] No `.value` used (it's reactive, not ref).

### p03 — Computed caching proof
- [ ] `firstName` and `lastName` declared with `ref()`.
- [ ] `fullName` is `computed(() => { console.log('computing...'); return firstName.value + ' ' + lastName.value })`.
- [ ] `{{ fullName }}` appears in TWO places in the template.
- [ ] Button changes `firstName.value`.
- [ ] Console shows "computing..." only ONCE per change (not twice) — proving caching.
- [ ] Both template locations show the updated value.

## Medium

### p01 — watchEffect auto-tracking
- [ ] `firstName` and `lastName` declared with `ref()`.
- [ ] `watchEffect` sets `document.title = firstName.value + ' ' + lastName.value`.
- [ ] Two `<q-input>` components bound to `firstName` and `lastName`.
- [ ] Changing either input updates `document.title` (check browser tab).
- [ ] Effect runs immediately on mount (document.title set before any input).
- [ ] No explicit dependency list (auto-tracked).

### p02 — Watch with getter and multiple sources
- [ ] `state` declared with `reactive({ count: 0, name: 'Alice' })`.
- [ ] `watch(() => state.count, (newVal, oldVal) => ...)` logs both values.
- [ ] `watch([() => state.count, () => state.name], ([newCount, newName], [oldCount, oldName]) => ...)` watches both.
- [ ] Buttons to change `state.count` and `state.name`.
- [ ] Console shows old and new values when either changes.
- [ ] Watcher does NOT fire on mount (watch is lazy by default).

### p03 — toRefs destructuring
- [ ] `state` declared with `reactive({ count: 0, name: 'Alice' })`.
- [ ] `const { count, name } = toRefs(state)` — destructured with `toRefs`.
- [ ] `toRefs` imported from 'vue'.
- [ ] `watch(count, (newVal) => ...)` watches the destructured ref.
- [ ] Button changes `state.count` directly (not the ref).
- [ ] Watcher fires — proving the destructured ref is still connected to `state`.
- [ ] Template displays `count` and `name` (auto-unwrapped refs).

## Hard

### p01 — Computed vs function call count
- [ ] `items` ref with at least 5 objects `{ name, category }`.
- [ ] `filterCategory` ref (string).
- [ ] `computedCallCount` ref starting at 0.
- [ ] `functionCallCount` ref starting at 0.
- [ ] `filteredComputed` is `computed(() => { computedCallCount.value++; return items.value.filter(...) })`.
- [ ] `function getFiltered() { functionCallCount.value++; return items.value.filter(...) }`.
- [ ] Both displayed in template (computed used twice, function called twice).
- [ ] Display both call counts in template.
- [ ] Changing filter: computed count increments by 1, function count increments by 2 (per render).
- [ ] Proves computed caches (called once per change) vs function (called per use).

### p02 — nextTick focus input
- [ ] `showInput` declared with `ref(false)`.
- [ ] `inputRef` declared with `ref(null)`.
- [ ] Button toggles `showInput` to true.
- [ ] `async function showAndFocus()` sets `showInput.value = true`.
- [ ] `await nextTick()` called after setting `showInput`.
- [ ] `inputRef.value.focus()` called after `nextTick`.
- [ ] `nextTick` imported from 'vue'.
- [ ] `ref="inputRef"` on the `<q-input>` that has `v-if="showInput"`.
- [ ] No error thrown — input is focused after it appears.
- [ ] Button can toggle back (hide input) without errors.

### p03 — shallowRef behavior
- [ ] `items` declared with `shallowRef([...])` containing at least 5 generated items.
- [ ] `shallowRef` imported from 'vue'.
- [ ] Items displayed with `v-for` and `:key`.
- [ ] Button 1: mutates nested property — `items.value[0].name = 'Changed'` — UI does NOT update.
- [ ] Button 2: reassigns `.value` — `items.value = [...items.value]` — UI DOES update.
- [ ] Button 3: mutates nested then calls `triggerRef(items)` — UI DOES update.
- [ ] `triggerRef` imported from 'vue'.
- [ ] Clear visual difference between the three buttons' effects.

## How to verify

Use the Docker container (see quasar/README.md):
```bash
docker build -t quasar-dev .
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
# Inside container:
quasar create test-app
cp easy/p01-solve.vue test-app/src/pages/Index.vue
cd test-app && quasar dev
```
Open http://localhost:8080 and verify:
- Reactive nested changes update the UI immediately.
- Console shows computed caching (one log per change, not per template use).
- `document.title` (browser tab) updates when inputs change (watchEffect).
- Watch logs show old → new values in console.
- Input is focused automatically after appearing (nextTick).
- shallowRef nested mutation doesn't update UI until triggerRef or reassignment.
