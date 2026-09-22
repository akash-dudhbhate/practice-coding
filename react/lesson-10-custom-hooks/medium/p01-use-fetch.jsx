/*
LESSON 10 — Custom Hooks
MEDIUM P01 — useFetch Hook
============================================
CONCEPT: useFetch(url) hides the whole loading/error/data dance behind one call — the dep array on `url` makes it re-fetch when the URL changes.
PROBLEM: Build `useFetch(url)` with `data`/`loading`/`error` state: in a `[url]` effect, fetch, throw on `!res.ok`, set data or error, always clear loading. Then `FetchDemo` renders Loading / Error / name+email for `.../users/1`. Export `FetchDemo` default.
TRY THIS: Render `<FetchDemo />`.
EXPECTED OUTPUT: "Loading..." then the fetched user's name and email.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
