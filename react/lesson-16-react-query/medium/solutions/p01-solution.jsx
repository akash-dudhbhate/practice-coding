// Lesson 16 — Medium P01: Product list with useMutation
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
function ProductList() {
  const queryClient = useQueryClient();
  const [name, setName] = useState("");
  const { data: products, isLoading } = useQuery({
    queryKey: ["products"],
    queryFn: () => fetch("https://jsonplaceholder.typicode.com/posts?_limit=5").then((r) => r.json()),
  });
  const mutation = useMutation({
    mutationFn: (newProduct) => fetch("https://jsonplaceholder.typicode.com/posts", { method: "POST", body: JSON.stringify(newProduct), headers: { "Content-Type": "application/json" } }).then((r) => r.json()),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["products"] }),
  });
  if (isLoading) return <p>Loading...</p>;
  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Product name" />
      <button onClick={() => mutation.mutate({ title: name })} disabled={mutation.isPending}>{mutation.isPending ? "Adding..." : "Add"}</button>
      {mutation.isError && <p style={{ color: "red" }}>Error!</p>}
      <ul>{products.map((p) => <li key={p.id}>{p.title}</li>)}</ul>
    </div>
  );
}
export default ProductList;
