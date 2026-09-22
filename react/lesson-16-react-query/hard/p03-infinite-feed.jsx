/*
LESSON 16 — React Query
HARD P03 — Infinite Scroll with useInfiniteQuery
============================================
CONCEPT: `useInfiniteQuery` accumulates `data.pages` (an array of page results). `getNextPageParam` inspects the last page to compute the next param — returning `undefined` means "no more", which drives `hasNextPage`.
PROBLEM: Build `InfiniteFeed` with `useInfiniteQuery`: `queryKey: ["posts-infinite"]`, `queryFn({pageParam = 1})` fetching `?_page=${pageParam}&_limit=10`, `initialPageParam: 1`, and `getNextPageParam` returning `allPages.length + 1` when the last page has 10 items else `undefined`. Render Loading, an error state with Retry (`fetchNextPage`), each page's posts (nested `map` with `key`s), and a "Load More" button disabled when `!hasNextPage || isFetchingNextPage` with three label states.
TRY THIS: Render `<InfiniteFeed />` and click Load More — 10 more posts append each time.
EXPECTED OUTPUT: Pages accumulate; button shows "Loading more..." while fetching, "No more posts" at the end.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
