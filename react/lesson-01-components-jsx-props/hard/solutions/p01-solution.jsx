// Lesson 01 — Hard P01: Reusable Table Component
function Table({ columns, rows }) {
  return (
    <table style={{ borderCollapse: "collapse", width: "100%" }}>
      <thead>
        <tr>{columns.map((col) => <th key={col.key} style={{ border: "1px solid #ddd", padding: "8px", textAlign: "left" }}>{col.label}</th>)}</tr>
      </thead>
      <tbody>
        {rows.map((row, i) => (
          <tr key={i}>
            {columns.map((col) => <td key={col.key} style={{ border: "1px solid #ddd", padding: "8px" }}>{row[col.key]}</td>)}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
export default Table;
