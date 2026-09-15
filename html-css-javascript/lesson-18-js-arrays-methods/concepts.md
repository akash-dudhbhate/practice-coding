# Lesson 18 — Concepts Explained (JS Arrays & Methods)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Array Basics

**What:** Arrays store ordered collections of values.

```javascript
const fruits = ["apple", "banana", "cherry"];
fruits[0]              // "apple" (zero-indexed)
fruits.length          // 3
fruits[fruits.length - 1]  // "cherry" (last item)
fruits[3] = "date";    // add item at index 3

// Mixed types (possible but avoid)
const mixed = [1, "hello", true, null, {name: "Akash"}];
```

**Why it exists:** Without arrays, you'd use separate variables: `fruit1`, `fruit2`, `fruit3` → can't loop, can't count, can't sort. Arrays group related values → iterable, manageable.

**Where it's used:** Lists of data — users, products, messages, tasks, search results.

**What goes wrong without it:**
- Accessing out of bounds: `fruits[10]` → `undefined` (not an error). Check `index < array.length` first.
- Arrays are objects: `typeof []` → `"object"`. Use `Array.isArray()` to check.
- Deleting with `delete arr[0]` → leaves a hole (`[undefined, "banana", "cherry"]`). Use `splice()` or `filter()` instead.

---

## push, pop, shift, unshift

**What:** Add and remove items from array ends.

```javascript
const arr = [2, 3, 4];

arr.push(5);       // [2, 3, 4, 5] — add to end
arr.pop();         // [2, 3, 4] — remove from end, returns 5
arr.unshift(1);    // [1, 2, 3, 4] — add to start
arr.shift();       // [2, 3, 4] — remove from start, returns 1
```

**Why it exists:** Without these, you'd manually shift elements with loops → verbose. These methods handle the common add/remove operations efficiently.

**Where it's used:** Stacks (push/pop), queues (push/shift), adding items to lists.

**What goes wrong without it:**
- `shift()` and `unshift()` are O(n) — they reindex all elements. For large arrays, use push/pop (O(1)) instead.
- These methods MUTATE the original array. If you need immutability (React state), use spread: `[...arr, newItem]`.
- `push()` returns the new length, not the array. `const result = arr.push(5)` → `result` is `4` (length), not the array.

---

## splice vs slice

**What:**
- `splice(start, deleteCount, ...items)` — MUTATES the array, removes/inserts items.
- `slice(start, end)` — returns a NEW array, doesn't modify original.

```javascript
const arr = [1, 2, 3, 4, 5];

// splice — modifies original
arr.splice(1, 2);          // removes 2 items at index 1 → [1, 4, 5]
arr.splice(1, 0, "a", "b"); // inserts at index 1 → [1, "a", "b", 4, 5]
arr.splice(2, 1, "c");      // replaces 1 item at index 2 → [1, "a", "c", 4, 5]

// slice — doesn't modify
const copy = arr.slice();      // shallow copy
const part = arr.slice(1, 3);  // items at index 1 and 2
const tail = arr.slice(-2);    // last 2 items
```

**Why it exists:** `splice` for in-place modification (insert, remove, replace). `slice` for extracting a copy without changing the original. Different use cases.

**Where it's used:** `splice` — removing items from a list, inserting at a position. `slice` — copying arrays, pagination, extracting subsets.

**What goes wrong without it:**
- `splice` MUTATES → if you're in React, mutating state doesn't trigger re-render. Use `filter` or spread instead.
- `slice(start, end)` — `end` is EXCLUSIVE. `slice(0, 3)` gets indices 0, 1, 2 (not 3).
- `splice` returns the REMOVED items, not the modified array. `const result = arr.splice(0, 2)` → `result` is the removed items.

---

## map, filter, reduce

**What:** The three most important array methods for data transformation.

```javascript
const numbers = [1, 2, 3, 4, 5];

// map — transform each element (returns new array)
const doubled = numbers.map(n => n * 2);  // [2, 4, 6, 8, 10]
const users = people.map(p => p.name);     // extract names

// filter — keep elements that pass a test (returns new array)
const evens = numbers.filter(n => n % 2 === 0);  // [2, 4]
const adults = people.filter(p => p.age >= 18);   // only adults

// reduce — accumulate into a single value
const sum = numbers.reduce((acc, n) => acc + n, 0);  // 15
const max = numbers.reduce((a, b) => Math.max(a, b)); // 5
const grouped = people.reduce((acc, p) => {
    acc[p.city] = (acc[p.city] || 0) + 1;
    return acc;
}, {});  // { Mumbai: 2, London: 1 }
```

**Why it exists:** Without these, you'd write `for` loops with temporary arrays → verbose, error-prone. `map`/`filter`/`reduce` are declarative — say WHAT you want, not HOW.

**Where it's used:** Every data processing task — transforming API responses, filtering lists, calculating totals, grouping data. The backbone of React/Redux.

**What goes wrong without it:**
- `map` must return a value. `[1,2,3].map(n => { n * 2 })` → `[undefined, undefined, undefined]` (no return). Use `n => n * 2` or `n => { return n * 2 }`.
- `reduce` without initial value: `[].reduce((a,b) => a + b)` → `TypeError` (empty array, no initial value). Always provide initial value: `reduce(fn, 0)`.
- Chaining: `arr.filter(...).map(...).reduce(...)` → each creates a new array → 3 iterations. For performance, combine into one reduce.

---

## forEach vs map

**What:**
- `forEach` — executes a function for each element. Returns `undefined`. Side effects.
- `map` — transforms each element. Returns a new array. Pure.

```javascript
// forEach — side effects (logging, DOM updates)
numbers.forEach(n => console.log(n));
numbers.forEach(n => document.body.innerHTML += `<p>${n}</p>`);

// map — transformation (returns new array)
const doubled = numbers.map(n => n * 2);
```

**Why it exists:** `forEach` is for doing something (side effects). `map` is for creating something (new array). Using the wrong one → bugs.

**Where it's used:** `forEach` — logging, DOM manipulation, saving to database. `map` — transforming data, React rendering.

**What goes wrong without it:**
- `const result = arr.forEach(n => n * 2)` → `result` is `undefined`. `forEach` doesn't return an array. Use `map`.
- `break` doesn't work in `forEach` → can't exit early. Use `for...of` or `some()` if you need to break.
- `return` in `forEach` → skips to next iteration (like `continue`), doesn't return a value.

---

## find, findIndex, some, every, includes

**What:** Search and test array elements.

```javascript
const users = [
    {id: 1, name: "Akash", active: true},
    {id: 2, name: "Bob", active: false},
    {id: 3, name: "Carol", active: true}
];

// find — first matching element (or undefined)
users.find(u => u.active);          // {id: 1, name: "Akash", active: true}
users.find(u => u.id === 5);        // undefined

// findIndex — index of first match (or -1)
users.findIndex(u => u.active);     // 0
users.findIndex(u => u.id === 5);   // -1

// some — true if ANY element passes test
users.some(u => u.active);          // true (at least one active)
users.some(u => u.id === 5);        // false

// every — true if ALL elements pass test
users.every(u => u.active);         // false (Bob is inactive)
users.every(u => u.id > 0);         // true

// includes — simple value check
[1, 2, 3].includes(2);              // true
[1, 2, 3].includes(5);              // false
"hello world".includes("world");    // true (works on strings too)
```

**Why it exists:** Without these, you'd write loops with flags and breaks → verbose. These methods express the intent clearly: "find", "does any", "do all", "includes".

**Where it's used:** Validation (every field is filled), search (find user by ID), checks (any item in stock?), membership tests (includes).

**What goes wrong without it:**
- `find` returns the ELEMENT, `findIndex` returns the INDEX. Mixing them up → wrong value.
- `includes` uses strict equality → `[1, 2, NaN].includes(NaN)` → `true` (unlike `indexOf` which can't find NaN).
- `some([])` → `false` (no elements pass). `every([])` → `true` (vacuously true — all zero elements pass). This is mathematically correct but surprising.

---

## sort

**What:** Sort array elements. MUTATES the original array.

```javascript
// Default sort — converts to strings, sorts alphabetically!
[10, 2, 1, 5].sort();  // [1, 10, 2, 5] — WRONG! (string sort)

// Numeric sort — provide a compare function
[10, 2, 1, 5].sort((a, b) => a - b);  // [1, 2, 5, 10] — ascending
[10, 2, 1, 5].sort((a, b) => b - a);  // [10, 5, 2, 1] — descending

// Sort objects
users.sort((a, b) => a.age - b.age);  // by age ascending
users.sort((a, b) => a.name.localeCompare(b.name));  // by name alphabetical
```

**Why it exists:** Without sort, you'd implement bubble sort or quicksort manually → error-prone. Built-in sort is optimized.

**Where it's used:** Sorting tables, ranking, ordering by date/name/price.

**What goes wrong without it:**
- Default sort converts to STRINGS → `[10, 2].sort()` → `[10, 2]` (because "10" < "2" alphabetically). ALWAYS provide a compare function for numbers.
- `sort()` MUTATES the original array. If you need a sorted copy: `[...arr].sort()` or `arr.toSorted()` (ES2023).
- Compare function: return negative → a before b. Return positive → b before a. Return 0 → equal. `a - b` = ascending. `b - a` = descending.

---

## concat, join, flat

**What:** Combine and flatten arrays.

```javascript
// concat — merge arrays (returns new array)
const merged = [1, 2].concat([3, 4]);  // [1, 2, 3, 4]
// or use spread: [...[1, 2], ...[3, 4]]

// join — array to string
[1, 2, 3].join(", ");    // "1, 2, 3"
["Hello", "World"].join(" ");  // "Hello World"

// flat — flatten nested arrays
[1, [2, 3]].flat();           // [1, 2, 3] (one level)
[1, [2, [3, [4]]]].flat(2);   // [1, 2, 3, [4]] (two levels)
[1, [2, [3, [4]]]].flat(Infinity);  // [1, 2, 3, 4] (all levels)

// flatMap — map then flat (one level)
[1, 2, 3].flatMap(n => [n, n * 2]);  // [1, 2, 2, 4, 3, 6]
```

**Why it exists:** Without these, you'd use loops and push to merge/flatten → verbose. These methods handle common array combination patterns.

**Where it's used:** Merging lists, creating CSV strings, flattening nested data structures, data transformation pipelines.

**What goes wrong without it:**
- `concat` doesn't mutate → original arrays are unchanged. But it's a shallow copy → nested arrays are shared.
- `join(undefined)` → joins with `","` (default). `join("")` → no separator.
- `flat()` without argument → only flattens 1 level. Use `flat(Infinity)` for deep flatten.

---

## Array Destructuring & Spread

**What:** Extract and expand array elements.

```javascript
// Destructuring
const [first, second] = [1, 2];        // first=1, second=2
const [a, , c] = [1, 2, 3];           // a=1, c=3 (skip)
const [first, ...rest] = [1, 2, 3, 4]; // first=1, rest=[2,3,4]
const [a = 10, b = 20] = [1];          // a=1, b=20 (defaults)

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];  // a=2, b=1

// Spread
const copy = [...original];
const extended = [...original, newItem];
const merged = [...arr1, ...arr2];
```

**Why it exists:** Without destructuring, you'd write `const first = arr[0]; const second = arr[1];` → verbose. Without spread, you'd use `.concat()` → less readable.

**Where it's used:** React state updates (`[...items, newItem]`), function arguments, swapping values, extracting values from arrays.

**What goes wrong without it:**
- Spread is shallow: `[...nestedArr]` → top-level copy, nested arrays are references → mutating nested affects original.
- Destructuring fewer variables than elements → extra elements are ignored. More variables → extras are `undefined`.
- Default values only apply for `undefined`, not `null`: `const [a = 1] = [null]` → `a = null` (not 1).
