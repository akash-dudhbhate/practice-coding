// Lesson 16 — Easy P03: Fetch user by ID with caching
import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
function UserById({ userId }) {
  const { data, isLoading } = useQuery({
    queryKey: ["user", userId],
    queryFn: () => fetch(`https://jsonplaceholder.typicode.com/users/${userId}`).then((r) => r.json()),
  });
  if (isLoading) return <p>Loading...</p>;
  return <div><h3>{data.name}</h3><p>{data.email}</p></div>;
}
function App() {
  const [userId, setUserId] = useState(1);
  return (
    <div>
      <button onClick={() => setUserId(1)}>User 1</button>
      <button onClick={() => setUserId(2)}>User 2</button>
      <button onClick={() => setUserId(3)}>User 3</button>
      <UserById userId={userId} />
    </div>
  );
}
export default App;
