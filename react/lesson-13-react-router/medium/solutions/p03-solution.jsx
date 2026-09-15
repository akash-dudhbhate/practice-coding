// Lesson 13 — Medium P03: useSearchParams for pagination & sorting
import { BrowserRouter, Routes, Route, useSearchParams } from "react-router-dom";
function ProductList() {
  const [params, setParams] = useSearchParams();
  const page = parseInt(params.get("page") || "1");
  const sort = params.get("sort") || "name";
  const setPage = (p) => setParams({ page: String(p), sort });
  const setSort = (s) => setParams({ page: String(page), sort: s });
  return (
    <div>
      <p>Page: {page}, Sort: {sort}</p>
      <button onClick={() => setPage(page + 1)}>Next Page</button>
      <button onClick={() => setPage(Math.max(1, page - 1))}>Prev Page</button>
      <button onClick={() => setSort("price")}>Sort by Price</button>
      <button onClick={() => setSort("name")}>Sort by Name</button>
    </div>
  );
}
function App() {
  return (
    <BrowserRouter>
      <Routes><Route path="/" element={<ProductList />} /></Routes>
    </BrowserRouter>
  );
}
export default App;
