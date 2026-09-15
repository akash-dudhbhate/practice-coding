// Lesson 18 — Easy P01: map, filter, reduce
const nums = [1, 2, 3, 4, 5];
const doubled = nums.map(n => n * 2);
const evens = doubled.filter(n => n % 2 === 0);
const sum = evens.reduce((acc, n) => acc + n, 0);
console.log({ doubled, evens, sum });
// { doubled: [2,4,6,8,10], evens: [2,4,6,8,10], sum: 30 }
