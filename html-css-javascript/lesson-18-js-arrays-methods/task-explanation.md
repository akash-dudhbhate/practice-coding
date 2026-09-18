# Lesson 18 — JS Arrays & Methods

## What you'll learn
- Array basics (indexing, length)
- push, pop, shift, unshift
- splice vs slice
- map, filter, reduce (the big three)
- forEach vs map
- find, findIndex, some, every, includes
- sort (with compare function)
- concat, join, flat
- Array destructuring and spread

## Lesson

### map / filter / reduce
```javascript
const doubled = nums.map(n => n * 2);
const evens = nums.filter(n => n % 2 === 0);
const sum = nums.reduce((acc, n) => acc + n, 0);
```

### Search methods
```javascript
const user = users.find(u => u.id === 5);
const hasActive = users.some(u => u.active);
const allActive = users.every(u => u.active);
```

### Sort
```javascript
nums.sort((a, b) => a - b);  // ascending
users.sort((a, b) => a.name.localeCompare(b.name));
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Create an array of 5 numbers. Use `map` to double each, `filter` to keep evens, and `reduce` to sum them. Print all results.

   ```
   EXPECTED CONSOLE OUTPUT:
   doubled: [2, 4, 6, 8, 10]
   evens:   [2, 4, 6, 8, 10]
   sum:     30
   ```
2. `easy/p02-solve.js` — Create an array of fruits. Use `push`, `pop`, `shift`, `unshift` to add and remove items. Print the array after each operation.

   ```
   EXPECTED CONSOLE OUTPUT:
   ["apple", "banana", "cherry"]
   ["apple", "banana", "cherry", "date"]     <- push
   ["apple", "banana", "cherry"]             <- pop
   ["avocado", "apple", "banana", "cherry"]  <- unshift
   ["apple", "banana", "cherry"]             <- shift
   ```
3. `easy/p03-solve.js` — Write a function `findUser(users, id)` that uses `find` to return a user by ID. Return "Not found" if not found.

   ```
   EXPECTED CONSOLE OUTPUT:
   findUser(users, 2)  -> { id: 2, name: "Bob" }
   findUser(users, 99) -> "Not found"
   ```

### Medium
4. `medium/p01-solve.js` — Write a function `processNumbers(nums)` that chains map (double), filter (>10), and sort (ascending). Returns the resulting array.

   ```
   EXPECTED CONSOLE OUTPUT:
   processNumbers([3, 7, 1, 8, 5, 12]) -> [14, 16, 24]
   (double each, keep > 10, sort ascending)
   ```
5. `medium/p02-solve.js` — Write a function `groupBy(arr, key)` that uses `reduce` to group objects by a key. Example: group users by city → `{Mumbai: [...], London: [...]}`.

   ```
   EXPECTED CONSOLE OUTPUT:
   groupBy(users, "city") ->
   { Mumbai: [ {Alice}, {Charlie} ], London: [ {Bob} ] }
   ```
6. `medium/p03-solve.js` — Write a function `removeDuplicates(arr)` that removes duplicate values from an array. Use `filter` + `indexOf`, or `Set` + spread. Return a new array.

   ```
   EXPECTED CONSOLE OUTPUT:
   removeDuplicates([1, 2, 2, 3, 4, 4, 5]) -> [1, 2, 3, 4, 5]
   ```

### Hard
7. `hard/p01-solve.js` — Write a function `analyzeGrades(students)` where students is `[{name, scores: [90, 85, 92]}]`. For each student: calculate average (reduce), determine grade (map), filter passing students (>= 60), sort by average descending. Return top 3 students.

   ```
   EXPECTED CONSOLE OUTPUT:
   analyzeGrades(students) -> top 3 passing students,
   best average first, each with avg + grade added, e.g.
   [ { name: "Sara", avg: 92, grade: "A" }, ... ]
   ```
8. `hard/p02-solve.js` — Write a function `flattenAndUnique(nestedArr)` that flattens a nested array of any depth (flat(Infinity)), removes duplicates, and sorts numerically. Example: `[[1,2],[3,[4,2]],[1,5]]` → `[1,2,3,4,5]`.

   ```
   EXPECTED CONSOLE OUTPUT:
   flattenAndUnique([[1,2],[3,[4,2]],[1,5]]) -> [1, 2, 3, 4, 5]
   ```
9. `hard/p03-solve.js` — Write a function `createPagination(items, page, pageSize)` that uses `slice` to return items for a given page. Also return total pages, current page, and whether there's a next/prev page. Return an object with all pagination info.

   ```
   EXPECTED CONSOLE OUTPUT:
   createPagination(items, 2, 10) ->
   { items: [11..20], currentPage: 2, totalPages: 3,
     hasNext: true, hasPrev: true }
   ```

### How to work
- Write your complete JavaScript solution.
- Remove the TODO comment when done.
- Test with `node <filename>` or in browser console.
