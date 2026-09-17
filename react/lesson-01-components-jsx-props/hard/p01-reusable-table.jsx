/*
LESSON 01 — Components, JSX & Props
HARD P01 — Reusable Table
============================================
CONCEPT: Generic components take data plus a config describing how to display it. Nested `.map()` calls let one component render any two-dimensional data.
PROBLEM: Build a `Table` component taking `columns` (array of `{ key, label }`) and `rows` (array of objects) props. Render a `<table>` whose `<thead>` maps `columns` to `<th key={col.key}>` labels, and whose `<tbody>` maps `rows` to `<tr>`s — each containing one `<td key={col.key}>` per column showing `row[col.key]`.
TRY THIS: Render `<Table columns={[{ key: "name", label: "Name" }, { key: "age", label: "Age" }]} rows={[{ name: "Amy", age: 30 }, { name: "Ben", age: 25 }]} />`.
EXPECTED OUTPUT: A table with a "Name"/"Age" header row and two data rows showing "Amy"/"30" and "Ben"/"25".
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
