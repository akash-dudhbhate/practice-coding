// Lesson 05 — Hard P01: Nested Category List
const categories = [
  { id: 1, name: "Fruits", items: [{ id: 11, name: "Apple" }, { id: 12, name: "Banana" }] },
  { id: 2, name: "Vegetables", items: [{ id: 21, name: "Carrot" }, { id: 22, name: "Spinach" }] },
];
function NestedList() {
  return (
    <div>
      {categories.map((cat) => (
        <div key={cat.id}>
          <h3>{cat.name}</h3>
          <ul>{cat.items.map((item) => <li key={item.id}>{item.name}</li>)}</ul>
        </div>
      ))}
    </div>
  );
}
export default NestedList;
