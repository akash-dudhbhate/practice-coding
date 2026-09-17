/*
LESSON 01 — Components, JSX & Props
HARD P02 — Nested Comment Tree
============================================
CONCEPT: Components can render themselves. Recursion handles data of unknown depth — like a comment thread where every reply can have its own replies.
PROBLEM: Build a `Comment` component taking a `comment` prop shaped like `{ id, author, text, replies }`. Render an indented `<div>` (margin-left + left border) showing the author and text in a `<p>`. If `comment.replies` exists, `.map()` over it and render a nested `<Comment key={reply.id} comment={reply} />` for each reply.
TRY THIS: Render `<Comment comment={{ id: 1, author: "Amy", text: "Great post!", replies: [{ id: 2, author: "Bob", text: "Thanks!", replies: [] }] }} />`.
EXPECTED OUTPUT: Amy's comment with Bob's reply nested underneath, indented with a left border.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
