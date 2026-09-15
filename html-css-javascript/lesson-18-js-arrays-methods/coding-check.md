# Lesson 18 — Coding Check

## Easy

### p01-solve.js — map/filter/reduce basics
- [ ] `map` doubles each number correctly
- [ ] `filter` keeps only even numbers
- [ ] `reduce` sums all numbers correctly
- [ ] All three results are printed

### p02-solve.js — push/pop/shift/unshift
- [ ] `push` adds item to end
- [ ] `pop` removes from end
- [ ] `unshift` adds to start
- [ ] `shift` removes from start
- [ ] Array state printed after each operation

### p03-solve.js — findUser
- [ ] `findUser(users, 1)` returns the user with id=1
- [ ] `findUser(users, 999)` returns "Not found"
- [ ] Uses `find()` method
- [ ] Works with array of user objects

## Medium

### p01-solve.js — processNumbers chain
- [ ] `map` doubles each number
- [ ] `filter` keeps numbers > 10
- [ ] `sort` sorts ascending
- [ ] Methods are chained: `arr.map().filter().sort()`
- [ ] Returns the final array

### p02-solve.js — groupBy
- [ ] Groups objects by the specified key
- [ ] Uses `reduce` method
- [ ] Example: groupBy([{city:"Mumbai"},{city:"London"},{city:"Mumbai"}], "city")
- [ ] Returns {Mumbai: [...], London: [...]}
- [ ] Works with any key

### p03-solve.js — removeDuplicates
- [ ] Removes duplicate values
- [ ] Returns a NEW array (doesn't mutate original)
- [ ] [1, 2, 2, 3, 3, 3] → [1, 2, 3]
- [ ] Uses filter+indexOf OR Set+spread

## Hard

### p01-solve.js — analyzeGrades
- [ ] Calculates average for each student (using reduce)
- [ ] Determines letter grade (A/B/C/D/F)
- [ ] Filters passing students (average >= 60)
- [ ] Sorts by average descending
- [ ] Returns top 3 students
- [ ] Handles ties in sorting

### p02-solve.js — flattenAndUnique
- [ ] Flattens nested array of any depth
- [ ] Uses `flat(Infinity)` or recursive approach
- [ ] Removes duplicates
- [ ] Sorts numerically (ascending)
- [ ] [[1,2],[3,[4,2]],[1,5]] → [1,2,3,4,5]
- [ ] Handles empty arrays

### p03-solve.js — createPagination
- [ ] Uses `slice` to extract page items
- [ ] Returns object with: items, currentPage, totalPages, hasNext, hasPrev
- [ ] totalPages calculated correctly (Math.ceil)
- [ ] hasNext and hasPrev are correct booleans
- [ ] Edge cases: page beyond range returns empty items
- [ ] pageSize of 0 or negative handled gracefully
