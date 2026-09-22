/*
LESSON 16 — React Query
MEDIUM P03 — Pagination with keepPreviousData
============================================
CONCEPT: Changing the `page` in the `queryKey` normally flashes a Loading state each click. `placeholderData: keepPreviousData` keeps showing the OLD page's data while the new page fetches — smooth pagination.
PROBLEM: Build `PaginatedList`: `page` in `useState(1)`; `useQuery` with `queryKey: ["posts", page]`, `queryFn` fetching `?_page=${page}&_limit=5`, and `placeholderData: keepPreviousData`. Render an "Fetching.../Ready" indicator from `isFetching`, the post list (full Loading only when there's no data), "Page N", and Prev/Next buttons updating `page`.
TRY THIS: Render `<PaginatedList />` and click Next — old posts stay visible while page 2 loads, no flash.
EXPECTED OUTPUT: Seamless page changes; isFetching indicator shows background refetches.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
