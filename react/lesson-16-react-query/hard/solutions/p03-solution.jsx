// Lesson 16 — Hard P03: Infinite scroll with useInfiniteQuery
import { useInfiniteQuery } from "@tanstack/react-query";
function InfiniteFeed() {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage, isLoading, error } = useInfiniteQuery({
    queryKey: ["posts-infinite"],
    queryFn: ({ pageParam = 1 }) => fetch(`https://jsonplaceholder.typicode.com/posts?_page=${pageParam}&_limit=10`).then((r) => r.json()),
    initialPageParam: 1,
    getNextPageParam: (lastPage, allPages) => lastPage.length === 10 ? allPages.length + 1 : undefined,
  });
  if (isLoading) return <p>Loading...</p>;
  if (error) return <div><p>Error: {error.message}</p><button onClick={() => fetchNextPage()}>Retry</button></div>;
  return (
    <div>
      {data.pages.map((page, i) => (
        <div key={i}>{page.map((post) => <p key={post.id}>{post.title}</p>)}</div>
      ))}
      <button onClick={() => fetchNextPage()} disabled={!hasNextPage || isFetchingNextPage}>
        {isFetchingNextPage ? "Loading more..." : hasNextPage ? "Load More" : "No more posts"}
      </button>
    </div>
  );
}
export default InfiniteFeed;
