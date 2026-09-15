# Lesson 18 — Debug Exercises

## Debug 01 (Easy): map Returns undefined
```javascript
const result = [1, 2, 3].map(x => { x * 2 });
```
<details><summary>Answer</summary>
**Bug:** Curly braces make it a function body, not implicit return. Returns `[undefined, undefined, undefined]`.
**Fix:** Remove braces: `x => x * 2` or add `return`.
</details>

## Debug 02 (Medium): forEach vs map
```javascript
const result = [1, 2, 3].forEach(x => x * 2);
```
<details><summary>Answer</summary>
**Bug:** `forEach` returns `undefined`, not a new array. Use `map` for transformation.
**Fix:** `const result = [1, 2, 3].map(x => x * 2);`.
</details>

## Debug 03 (Hard): Mutating with map
```javascript
const users = [{ name: "A" }, { name: "B" }];
const updated = users.map(u => { u.name = u.name.toUpperCase(); return u; });
```
<details><summary>Answer</summary>
**Bug:** Mutates original objects. `users` is also changed.
**Fix:** `users.map(u => ({ ...u, name: u.name.toUpperCase() }))`.
</details>
