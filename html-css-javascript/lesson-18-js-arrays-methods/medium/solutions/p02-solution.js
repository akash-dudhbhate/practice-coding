// Lesson 18 — Medium P02: Group by with reduce
function groupBy(arr, key) {
  return arr.reduce((groups, item) => {
    const val = item[key];
    (groups[val] = groups[val] || []).push(item);
    return groups;
  }, {});
}
const users = [
  { name: "Alice", city: "Mumbai" },
  { name: "Bob", city: "London" },
  { name: "Charlie", city: "Mumbai" },
];
console.log(groupBy(users, "city"));
// { Mumbai: [...], London: [...] }
