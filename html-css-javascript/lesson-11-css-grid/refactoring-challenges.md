# Lesson 11 — Refactoring Challenges

## Refactor 01 (Easy): .then Chains
### Before
```javascript
fetch(url).then(r => r.json()).then(data => console.log(data));
```
### After
```javascript
const data = await (await fetch(url)).json();
console.log(data);
```

## Refactor 02 (Medium): No try/catch
### Before
```javascript
async function getData() {
  const res = await fetch(url);
  return res.json();
}
```
### After
```javascript
async function getData() {
  try {
    const res = await fetch(url);
    return await res.json();
  } catch (e) { return null; }
}
```

## Refactor 03 (Hard): Sequential Independent Awaits
### Before
```javascript
const user = await getUser();
const posts = await getPosts();
const comments = await getComments();
```
### After
```javascript
const [user, posts, comments] = await Promise.all([
  getUser(), getPosts(), getComments()
]);
```
