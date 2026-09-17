/*
LESSON 01 — Components, JSX & Props
HARD P03 — Layout Composition
============================================
CONCEPT: The `children` prop is whatever JSX sits between a component's open and close tags — it lets wrapper components frame any content without knowing what it is.
PROBLEM: Build a `Header` component and a `Footer` component, each taking `children` and rendering them inside a styled `<header>`/`<footer>`. Then build a `Layout` component taking `children` that renders a `<div>` containing a `<Header>` (with an `<h1>` title), a `<main>` wrapping `children`, and a `<Footer>` (with copyright text). `Layout` is the component this file provides by default.
TRY THIS: Render `<Layout><p>Welcome to my page</p></Layout>`.
EXPECTED OUTPUT: A dark header bar with the title, the paragraph in the main area, and a footer bar — the classic page shell.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
