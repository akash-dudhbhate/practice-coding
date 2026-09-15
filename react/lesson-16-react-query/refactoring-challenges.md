# Lesson 16 — Refactoring Challenges

## Refactor 01 (Easy): Manual Fetch State
### Before
```jsx
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);
useEffect(() => {
  fetch(url).then(r => r.json()).then(setData).catch(setError).finally(() => setLoading(false));
}, [url]);
```
### After
```jsx
const { data, loading, error } = useQuery(["key", url], () => fetch(url).then(r => r.json()));
```

## Refactor 02 (Medium): No Cache Key
### Before
```jsx
useQuery(["users"], fetchUsers);
useQuery(["users"], fetchUsers); // duplicate
```
### After
```jsx
// Same key = shared cache
useQuery(["users"], fetchUsers); // both components share
```

## Refactor 03 (Hard): Manual Mutation
### Before
```jsx
async function addUser(user) {
  await api.post("/users", user);
  const users = await api.get("/users");
  setUsers(users);
}
```
### After
```jsx
const mutation = useMutation((user) => api.post("/users", user), {
  onSuccess: () => queryClient.invalidateQueries(["users"]),
});
```
