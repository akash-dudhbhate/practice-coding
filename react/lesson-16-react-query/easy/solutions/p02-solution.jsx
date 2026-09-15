// Lesson 16 — Easy P02: useQuery with error handling
import { useQuery } from "@tanstack/react-query";
const fetchWithError = async () => {
  if (Math.random() > 0.5) throw new Error("Random API failure");
  return fetch("https://jsonplaceholder.typicode.com/users/1").then((r) => r.json());
};
function UserWithErrors() {
  const { data, isLoading, error, refetch } = useQuery({ queryKey: ["user-random"], queryFn: fetchWithError });
  if (isLoading) return <p>Loading...</p>;
  if (error) return <div><p style={{ color: "red" }}>Error: {error.message}</p><button onClick={() => refetch()}>Retry</button></div>;
  return <div><p>{data.name}</p><button onClick={() => refetch()}>Refetch</button></div>;
}
export default UserWithErrors;
