# Lesson 10 — Refactoring Challenges

## Refactor 01 (Easy): Logic in Component
### Before
```jsx
function Component() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false)); }, []);
}
```
### After
```jsx
function Component() {
  const { data, loading } = useFetch(url);
}
```

## Refactor 02 (Medium): Hook Returns Too Much
### Before
```jsx
const { data, loading, error, refetch, setData, setError, lastUpdated } = useApi();
```
### After
```jsx
const { data, loading, error, refetch } = useApi();
// internal state stays internal
```

## Refactor 03 (Hard): No Hook Reuse
### Before
```jsx
function UserProfile() {
  const [user, setUser] = useState(null);
  useEffect(() => { fetchUser(id).then(setUser); }, [id]);
}
function PostAuthor({ postId }) {
  const [post, setPost] = useState(null);
  const [author, setAuthor] = useState(null);
  useEffect(() => { fetchPost(postId).then(p => { setPost(p); fetchUser(p.authorId).then(setAuthor); }); }, [postId]);
}
```
### After
```jsx
const useFetch = (url) => { /* generic fetch hook */ };
function UserProfile() { const { data: user } = useFetch(`/users/${id}`); }
```
