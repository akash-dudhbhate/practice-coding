// Lesson 05 — Easy P01: Fruit List
const fruits = [
  { id: 1, name: "Apple" }, { id: 2, name: "Banana" }, { id: 3, name: "Cherry" },
];
function FruitList() {
  return <ul>{fruits.map((f) => <li key={f.id}>{f.name}</li>)}</ul>;
}
export default FruitList;
