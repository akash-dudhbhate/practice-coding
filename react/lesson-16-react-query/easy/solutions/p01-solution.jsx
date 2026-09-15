// Lesson 16 — Easy P01: QueryClientProvider + useQuery
import { QueryClient, QueryClientProvider, useQuery } from "@tanstack/react-query";
const queryClient = new QueryClient();
function UserList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["users"],
    queryFn: () => fetch("https://jsonplaceholder.typicode.com/users").then((r) => r.json()),
  });
  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  return <ul>{data.map((u) => <li key={u.id}>{u.name}</li>)}</ul>;
}
function App() {
  return <QueryClientProvider client={queryClient}><UserList /></QueryClientProvider>;
}
export default App;
