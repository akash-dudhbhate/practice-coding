// Lesson 12 — Hard P02: Data fetching reducer
import { useReducer, useEffect, useRef } from "react";
const reducer = (state, action) => {
  switch (action.type) {
    case "FETCH_START": return { ...state, loading: true, error: null };
    case "FETCH_SUCCESS": return { data: action.data, loading: false, error: null };
    case "FETCH_ERROR": return { ...state, loading: false, error: action.error };
    case "RESET": return { data: null, loading: false, error: null };
    default: return state;
  }
};
function useFetchReducer(url) {
  const [state, dispatch] = useReducer(reducer, { data: null, loading: false, error: null });
  const reqIdRef = useRef(0);
  useEffect(() => {
    if (!url) return;
    const reqId = ++reqIdRef.current;
    dispatch({ type: "FETCH_START" });
    fetch(url).then((r) => r.json()).then((data) => {
      if (reqId === reqIdRef.current) dispatch({ type: "FETCH_SUCCESS", data });
    }).catch((err) => {
      if (reqId === reqIdRef.current) dispatch({ type: "FETCH_ERROR", error: err.message });
    });
  }, [url]);
  return [state, dispatch];
}
function FetchDemo() {
  const [{ data, loading, error }] = useFetchReducer("https://jsonplaceholder.typicode.com/users/1");
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  return data ? <p>{data.name}</p> : null;
}
export default FetchDemo;
