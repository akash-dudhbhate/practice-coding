// Lesson 01 — Medium P02: Price List from array prop
function PriceList({ items }) {
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{item.name}: ${item.price}</li>
      ))}
    </ul>
  );
}
export default PriceList;
