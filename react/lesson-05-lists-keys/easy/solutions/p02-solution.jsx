// Lesson 05 — Easy P02: Number List (index as key)
function NumberList() {
  const numbers = Array.from({ length: 10 }, (_, i) => i + 1);
  return <ul>{numbers.map((n, i) => <li key={i}>{n}</li>)}</ul>;
}
export default NumberList;
