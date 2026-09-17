# lesson-18-js-arrays-methods — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: map vs filter vs reduce
```javascript
[1, 2, 3].map(x => x * 2);      // [2, 4, 6]
[1, 2, 3].filter(x => x > 1);   // [2, 3]
[1, 2, 3].reduce((a, b) => a + b, 0); // 6
```
<details><summary>Answer</summary>
- map — transform each element
- filter — keep elements matching condition
- reduce — combine all into one value
</details>

## Check 02: spread operator
```javascript
const a = [1, 2];
const b = [...a, 3];
console.log(b);
```
<details><summary>Answer</summary>
`[1, 2, 3]` — spread unpacks the array. Creates a new array (shallow copy).
</details>

## Check 03: find vs filter
```javascript
const users = [{ id: 1 }, { id: 2 }];
users.find(u => u.id === 1);    // { id: 1 }
users.filter(u => u.id === 1);  // [{ id: 1 }]
```
<details><summary>Answer</summary>
`find` returns the first matching element. `filter` returns ALL matching elements as an array.
</details>

## Check 04: some vs every
```javascript
[1, 2, 3].some(x => x > 2);   // true
[1, 2, 3].every(x => x > 0);  // true
```
<details><summary>Answer</summary>
`some` — at least one matches. `every` — all must match. Both short-circuit.
</details>

## Check 05: sort mutation
```javascript
const arr = [3, 1, 2];
arr.sort();
console.log(arr);
```
<details><summary>Answer</summary>
`[1, 2, 3]` — `sort` mutates the original array. To avoid: `[...arr].sort()`.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: forEach when you need map
```javascript
// WRONG — returns undefined
const doubled = arr.forEach(x => x * 2);
// CORRECT
const doubled = arr.map(x => x * 2);
```

## Mistake 02: Mutating with map
```javascript
// WRONG — mutates original
arr.map(obj => { obj.x = 1; return obj; });
// CORRECT
arr.map(obj => ({ ...obj, x: 1 }));
```

## Mistake 03: sort without compare function
```javascript
// WRONG — sorts as strings
[10, 2, 1].sort(); // [1, 10, 2]
// CORRECT
[10, 2, 1].sort((a, b) => a - b); // [1, 2, 10]
```

## Mistake 04: Not spreading
```javascript
// WRONG — nested array
const combined = [arr1, arr2];
// CORRECT
const combined = [...arr1, ...arr2];
```

## Mistake 05: Chaining after forEach
```javascript
// WRONG — forEach returns undefined
arr.forEach(x => x * 2).filter(...);
// CORRECT — use map
arr.map(x => x * 2).filter(...);
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Error Handling
### Before
```javascript
const data = JSON.parse(str);
```
### After
```javascript
try { const data = JSON.parse(str); }
catch (e) { console.error("Invalid JSON"); }
```

## Refactor 02 (Medium): Generic Catch
### Before
```javascript
try { ... } catch (e) { console.log("Error"); }
```
### After
```javascript
try { ... } catch (e) {
  if (e instanceof SyntaxError) console.error("Parse error");
  else throw e;
}
```

## Refactor 03 (Hard): Repeated Try/Catch
### Before
```javascript
function safeA() { try { return a(); } catch { return null; } }
function safeB() { try { return b(); } catch { return null; } }
```
### After
```javascript
function safe(fn, fallback = null) {
  try { return fn(); } catch { return fallback; }
}
const safeA = () => safe(a);
```

---

## Approach Comparison — different ways to solve it

## Problem: Transform Array

### Approach 1: for loop
```javascript
const result = [];
for (let i = 0; i < arr.length; i++) {
  result.push(arr[i] * 2);
}
```

### Approach 2: map
```javascript
const result = arr.map(x => x * 2);
```

**Winner:** Approach 2 — declarative, immutable, chainable.

---

## Problem: Unique Values

### Approach 1: filter + indexOf
```javascript
arr.filter((x, i) => arr.indexOf(x) === i);
```

### Approach 2: Set
```javascript
[...new Set(arr)];
```

**Winner:** Approach 2 — cleaner, faster.
