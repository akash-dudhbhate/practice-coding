# Lesson 06 — Refactoring Challenges

## Refactor 01 (Easy): var Instead of const/let
### Before
```javascript
var x = 5;
var name = "John";
```
### After
```javascript
const x = 5;
const name = "John";
// let only if reassigned
```

## Refactor 02 (Medium): Function Instead of Arrow
### Before
```javascript
const nums = [1, 2, 3];
const doubled = nums.map(function(n) { return n * 2; });
```
### After
```javascript
const doubled = nums.map(n => n * 2);
```

## Refactor 03 (Hard): Manual Loop vs Array Methods
### Before
```javascript
const result = [];
for (let i = 0; i < arr.length; i++) {
  if (arr[i] > 0) result.push(arr[i] * 2);
}
```
### After
```javascript
const result = arr.filter(n => n > 0).map(n => n * 2);
