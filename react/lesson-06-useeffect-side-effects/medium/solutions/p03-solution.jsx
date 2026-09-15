// Lesson 06 — Medium P03: Re-fetch on Prop Change
import { useState, useEffect } from "react";
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    setLoading(true);
    fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
      .then((res) => res.json())
      .then((data) => { setUser(data); setLoading(false); });
  }, [userId]);
  if (loading) return <p>Loading...</p>;
  return <div><h3>{user.name}</h3><p>{user.email}</p></div>;
}
export default UserProfile;
