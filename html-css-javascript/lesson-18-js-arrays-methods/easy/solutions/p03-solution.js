// Lesson 18 — Easy P03: find user by ID
function findUser(users, id) {
  const user = users.find(u => u.id === id);
  return user || "Not found";
}
const users = [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }];
console.log(findUser(users, 2));      // { id: 2, name: "Bob" }
console.log(findUser(users, 99));     // "Not found"
