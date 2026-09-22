/*
LESSON 12 — useReducer
HARD P02 — Data Fetching Reducer (Race-Safe)
============================================
CONCEPT: Async fetching has exactly three states — loading, success, error — which map perfectly to FETCH_START / FETCH_SUCCESS / FETCH_ERROR actions. A request-id ref makes sure a slow stale response can't overwrite a newer one.
PROBLEM: Write a reducer handling `"FETCH_START"` (loading: true), `"FETCH_SUCCESS"` (store `action.data`), `"FETCH_ERROR"` (store `action.error`), and `"RESET"`. Build a `useFetchReducer(url)` hook: `useReducer` for `{data, loading, error}`, a `useRef` counter for request ids, and a `useEffect` that dispatches FETCH_START, calls `fetch(url).then(r => r.json())`, and dispatches SUCCESS/ERROR only when `reqId === reqIdRef.current`. Build `FetchDemo` that uses the hook against a JSON URL and renders Loading / Error / `data.name`.
TRY THIS: Render `<FetchDemo />` pointing at "https://jsonplaceholder.typicode.com/users/1".
EXPECTED OUTPUT: "Loading..." then the fetched user's name; a clean error message on failure.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
