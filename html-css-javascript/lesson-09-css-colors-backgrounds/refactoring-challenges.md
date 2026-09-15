# Lesson 09 — Refactoring Challenges

## Refactor 01 (Easy): for Loop to forEach
### Before
```javascript
for (let i = 0; i < arr.length; i++) { console.log(arr[i]); }
```
### After
```javascript
arr.forEach(item => console.log(item));
```

## Refactor 02 (Medium): Manual Object Creation
### Before
```javascript
const user = {};
user.name = "John";
user.age = 30;
user.email = "john@example.com";
```
### After
```javascript
const user = { name: "John", age: 30, email: "john@example.com" };
```

## Refactor 03 (Hard): Nested Loops to Map/Filter
### Before
```javascript
const result = [];
for (const user of users) {
  for (const post of user.posts) {
    if (post.published) result.push(post);
  }
}
```
### After
```javascript
const result = users.flatMap(u => u.posts).filter(p => p.published);
```
