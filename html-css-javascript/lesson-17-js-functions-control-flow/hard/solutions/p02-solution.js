// Lesson 17 — Hard P02: Analyze data with destructuring
function analyzeData(data) {
  let totalAge = 0;
  const cityCount = {};
  let oldest = data[0];
  for (const { name, age, city } of data) {
    totalAge += age;
    cityCount[city] = (cityCount[city] || 0) + 1;
    if (age > oldest.age) oldest = { name, age, city };
  }
  return { averageAge: totalAge / data.length, usersPerCity: cityCount, oldestUser: oldest };
}
console.log(analyzeData([
  { name: "Alice", age: 30, city: "Mumbai" },
  { name: "Bob", age: 25, city: "Delhi" },
  { name: "Charlie", age: 35, city: "Mumbai" },
]));
