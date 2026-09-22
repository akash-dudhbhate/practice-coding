# Lesson 16 — React Query (TanStack Query)

## What you'll learn
- React Query basics (data fetching with caching)
- QueryClient and Provider setup
- useQuery (loading, error, data states)
- Query keys (cache identification)
- useMutation (create, update, delete)
- Cache invalidation (refetching stale data)
- Optimistic updates (instant UI feedback)
- Pagination and infinite queries

## Lesson

### Setup
```jsx
const queryClient = new QueryClient();
<QueryClientProvider client={queryClient}><App /></QueryClientProvider>
```

### useQuery
```jsx
const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json()),
});
```

### useMutation + invalidate
```jsx
const mutation = useMutation({
    mutationFn: (newUser) => fetch('/api/users', { method: 'POST', body: JSON.stringify(newUser) }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['users'] }),
});
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Set up `QueryClientProvider` at the app root. Create a component that uses `useQuery` to fetch and display a list of users from JSONPlaceholder API.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Loading...   ->   * Leanne Graham
                     * Ervin Howell
                     * Clementine Bauch   <- <ul> of user names
                     ...
   ```
2. `easy/p02-solve.jsx` — Create a component with `useQuery` that displays loading, error, and success states. Use a fake API that sometimes fails (random 50% error) to test error handling.

   WHAT IT SHOULD LOOK LIKE:
   ```
   SUCCESS:                 ERROR (~50%):
   Leanne Graham            Error: Random API failure  <- red
   [ Refetch ]              [ Retry ]
   ```
3. `easy/p03-solve.jsx` — Create a component that fetches a user by ID using a query key `['user', userId]`. Add buttons to switch between user IDs 1, 2, 3. Verify caching (no refetch when switching back).

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ User 1 ] [ User 2 ] [ User 3 ]
   Leanne Graham                  <- name + email
   Sincere@april.biz
   (revisiting an id shows cached data — no Loading flash)
   ```

### Medium
4. `medium/p01-solve.jsx` — Create a product list with `useQuery` and an "Add Product" form with `useMutation`. On successful add, invalidate the products query to refetch. Show mutation states (pending, error, success).

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------+ +-----------+
   | New product    | | Adding... |   <- button disabled+pends
   +----------------+ +-----------+
   * Post title one
   * Post title two                 <- <ul> refreshes on success
   ...
   ```
5. `medium/p02-solve.jsx` — Create a todo app with React Query: fetch todos, add todo (mutation), toggle todo (mutation), delete todo (mutation). All mutations invalidate the todos query. Show loading states per action.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +--------------+ [ Add ]
   | new task     |
   +--------------+
   * Buy milk        [Toggle] [Delete]
   * Walk the dog ✓  [Toggle] [Delete]   <- check shows completed
   ```
6. `medium/p03-solve.jsx` — Create a paginated list using `useQuery` with page parameter in the query key. Prev/Next buttons change the page. Use `placeholderData: keepPreviousData` to avoid loading flash between pages.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Fetching...          <- small indicator on background refetch
   * Post 6
   * Post 7
   * Post 8             <- previous data stays while page 2 loads
   Page 2   [ Prev ] [ Next ]
   ```

### Hard
7. `hard/p01-solve.jsx` — Build a search component with debounced query: user types, query is debounced 500ms, `useQuery` fetches results. Query key includes the search term. Handle empty search, loading, and no results states.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   | lean             |          <- debounced input
   +------------------+
   Searching...   ->    * Leanne Graham
   (empty input shows "Type to search";
    no matches shows "No results")
   ```
8. `hard/p02-solve.jsx` — Build a todo app with optimistic updates: adding a todo shows it instantly (onMutate), rolls back on error (onError), and refetches on settle (onSettled). Include a "Simulate Error" toggle to test rollback.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [x] Simulate Error    [ Add Todo ]
   * Todo 1
   * Todo 2
   * NEW todo   <- appears INSTANTLY, vanishes again if the
                  mutation fails (rollback)
   ```
9. `hard/p03-solve.jsx` — Build an infinite scroll feed using `useInfiniteQuery`: load 10 posts per page, "Load More" button fetches next page, disable button when no more pages. Include loading indicator for next page and error retry.

   WHAT IT SHOULD LOOK LIKE:
   ```
   * Post 1  ...  * Post 10        <- page 1
   * Post 11 ...  * Post 20        <- appended page 2
   [ Load More ]  -> [ Loading more... ] -> [ No more posts ]
   ```

### How to work
- Write your complete React solution.
- Remove the TODO comment when done.
- Test by importing into a React app with @tanstack/react-query installed.
