# Lesson 16 — Coding Check

## Easy

### p01-solve.jsx — QueryClient setup + user list
- [ ] `QueryClient` created outside component
- [ ] `QueryClientProvider` wraps the app
- [ ] `useQuery` fetches from JSONPlaceholder
- [ ] Users displayed in a list
- [ ] Loading state handled

### p02-solve.jsx — Error handling
- [ ] `useQuery` with a flaky queryFn (50% error)
- [ ] Loading state displayed
- [ ] Error state displayed with message
- [ ] Success state displays data
- [ ] Retry works (refetch on error)

### p03-solve.jsx — Query key with parameter
- [ ] Query key is `['user', userId]`
- [ ] Buttons switch between user IDs
- [ ] Data updates when switching users
- [ ] Switching back to a previous user → instant (cached)
- [ ] No unnecessary refetches for cached data

## Medium

### p01-solve.jsx — Product list + add mutation
- [ ] `useQuery` fetches products
- [ ] `useMutation` for adding product
- [ ] `onSuccess` invalidates products query
- [ ] Mutation pending state shown on button
- [ ] Mutation error displayed
- [ ] Mutation success message shown
- [ ] List updates after successful add

### p02-solve.jsx — Todo app with mutations
- [ ] Fetch todos with `useQuery`
- [ ] Add todo mutation
- [ ] Toggle todo mutation
- [ ] Delete todo mutation
- [ ] All mutations invalidate todos query
- [ ] Loading states per action
- [ ] Error handling for each mutation

### p03-solve.jsx — Paginated list
- [ ] Page parameter in query key: `['products', page]`
- [ ] Prev/Next buttons
- [ ] `placeholderData: keepPreviousData` used
- [ ] No loading flash between pages
- [ ] Current page displayed
- [ ] Prev disabled on page 1

## Hard

### p01-solve.jsx — Debounced search
- [ ] Search input with debounce (500ms)
- [ ] Query key includes search term
- [ ] Empty search → no query (enabled: false)
- [ ] Loading state during search
- [ ] No results state
- [ ] Results update as user types (debounced)
- [ ] Previous results kept while fetching new

### p02-solve.jsx — Optimistic updates
- [ ] `onMutate` updates cache immediately
- [ ] `cancelQueries` before optimistic update
- [ ] Previous data saved for rollback
- [ ] `onError` rolls back to previous data
- [ ] `onSettled` invalidates query
- [ ] "Simulate Error" toggle works
- [ ] Rollback visible on error
- [ ] Instant UI feedback on success

### p03-solve.jsx — Infinite scroll
- [ ] `useInfiniteQuery` used
- [ ] 10 posts per page
- [ ] `getNextPageParam` returns undefined when no more
- [ ] "Load More" button fetches next page
- [ ] Button disabled when no more pages
- [ ] Loading indicator for next page
- [ ] Error retry for failed page load
- [ ] All pages accumulate in the list
