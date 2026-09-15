// Lesson 16 — Medium P03: Paginated list with keepPreviousData
import { useState } from "react";
import { useQuery, keepPreviousData } from "@tanstack/react-query";
function PaginatedList() {
  const [page, setPage] = useState(1);
  const { data, isLoading, isFetching } = useQuery({
    queryKey: ["posts", page],
    queryFn: () => fetch(`https://jsonplaceholder.typicode.com/posts?_page=${page}&_limit=5`).then((r) => r.json()),
    placeholderData: keepPreviousData,
  });
  return (
    <div>
      <p>{isFetching ? "Fetching..." : "Ready"}</p>
      {isLoading ? <p>Loading...</p> : <ul>{data.map((p) => <li key={p.id}>{p.title}</li>)}</ul>}
      <button onClick={() => setPage((p) => Math.max(1, p - 1))}>Prev</button>
      <span> Page {page} </span>
      <button onClick={() => setPage((p) => p + 1)}>Next</button>
    </div>
  );
}
export default PaginatedList;
