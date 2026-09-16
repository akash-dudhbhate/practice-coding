/*
LESSON 06 — useEffect & Side Effects
MEDIUM P03 — Re-fetch on Prop Change
============================================
CONCEPT: Put a prop in the dep array and the effect re-runs whenever that prop changes — the data follows the prop.
PROBLEM: Build a `UserProfile({ userId })` component with `user`/`loading` state. In a `[userId]`-deps effect: set loading true, fetch `.../users/${userId}`, store data. Render Loading... then name/email.
TRY THIS: Render `<UserProfile userId={1} />` then re-render with `userId={2}`.
EXPECTED OUTPUT: User 1's data shows first; changing the prop loads and shows user 2.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
