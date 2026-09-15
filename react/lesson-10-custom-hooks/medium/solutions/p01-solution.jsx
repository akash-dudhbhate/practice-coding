// Lesson 10 — Medium P01: useFetch
import { useState, useEffect } from "react";
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then((res) => { if (!res.ok) throw new Error("Fetch failed"); return res.json(); })
      .then((data) => { setData(data); setLoading(false); })
      .catch((err) => { setError(err.message); setLoading(false); });
  }, [url]);
  return { data, loading, error };
}
function FetchDemo() {
  const { data, loading, error } = useFetch("https://jsonplaceholder.typicode.com/users/1");
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  return <div><h3>{data.name}</h3><p>{data.email}</p></div>;
}
export default FetchDemo;
