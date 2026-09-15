# Lesson 18 — Intuition Checks

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
