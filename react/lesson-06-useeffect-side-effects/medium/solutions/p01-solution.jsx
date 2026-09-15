// Lesson 06 — Medium P01: Fetch User on Mount
import { useState, useEffect } from "react";
function FetchUser() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users/1")
      .then((res) => res.json())
      .then((data) => { setUser(data); setLoading(false); });
  }, []);
  if (loading) return <p>Loading...</p>;
  return <div><h3>{user.name}</h3><p>{user.email}</p></div>;
}
export default FetchUser;
