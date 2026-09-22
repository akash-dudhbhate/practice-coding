/*
LESSON 06 — useEffect & Side Effects
MEDIUM P01 — Fetch User on Mount
============================================
CONCEPT: fetch inside a `[]`-deps effect is the classic load-once pattern: set state in .then, flip a loading flag when done.
PROBLEM: Build a `FetchUser` component with `user` and `loading` state. On mount, fetch `https://jsonplaceholder.typicode.com/users/1`, store the JSON, set loading false. Early-return "Loading..." while loading, then show name + email.
TRY THIS: Render `<FetchUser />`.
EXPECTED OUTPUT: "Loading..." appears briefly, then Leanne Graham's name and email.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
