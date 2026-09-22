/*
LESSON 13 — React Router
HARD P01 — Blog App with Dynamic & Filtered Routes
============================================
CONCEPT: Real apps combine several route patterns: a static list page, a `/:slug` detail page that looks data up by param, a `/:category` filtered list, and a `*` catch-all.
PROBLEM: Define a `posts` array (slug, title, category). Build `Home` mapping posts to `Link`s at `/post/${slug}`; `Post` reading `slug` via `useParams` and finding the post ("Post not found" fallback); `Category` reading `category` and filtering posts; `Admin` and `NotFound` pages. `App` renders a nav plus `Routes`: `/`, `/post/:slug`, `/category/:category`, `/admin`, and `*`.
TRY THIS: Render `<App />`, click a post, then visit /category/tech, then /bogus.
EXPECTED OUTPUT: Post detail by slug, filtered list by category, "404" on unknown paths.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
