/*
LESSON 16 — React Query
MEDIUM P01 — useMutation + Query Invalidation
============================================
CONCEPT: `useMutation` handles writes (POST/PUT/DELETE). Its `onSuccess` callback calling `queryClient.invalidateQueries({queryKey})` tells React Query the cached list is stale → automatic refetch.
PROBLEM: Build `ProductList`: `useQuery` for `["products"]` (fetch 5 posts); a `useMutation` whose `mutationFn` POSTs a new product and whose `onSuccess` invalidates `["products"]` via `useQueryClient()`. Render a controlled name input, an Add button calling `mutation.mutate({title: name})` that disables while `mutation.isPending` ("Adding..."), a red "Error!" when `mutation.isError`, and the product `<ul>`.
TRY THIS: Render `<ProductList />`, type a name, click Add — the list refetches and shows the new item.
EXPECTED OUTPUT: Button reads "Adding..." during the POST; list refreshes on success; errors surface.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
