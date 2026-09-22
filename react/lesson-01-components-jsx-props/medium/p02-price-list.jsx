/*
LESSON 01 — Components, JSX & Props
MEDIUM P02 — Price List
============================================
CONCEPT: To render a list, call `.map()` on an array prop and return JSX per item. React needs a stable `key` on each element to track items between renders.
PROBLEM: Build a `PriceList` component taking an `items` prop — an array of `{ id, name, price }` objects. Render a `<ul>` where `items.map(...)` produces one `<li key={item.id}>` per item showing "name: $price".
TRY THIS: Render `<PriceList items={[{ id: 1, name: "Apple", price: 1.5 }, { id: 2, name: "Bread", price: 2.25 }]} />`.
EXPECTED OUTPUT: A bullet list with lines like "Apple: $1.5" and "Bread: $2.25".
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
