# Lesson 14 — Refactoring Challenges

## Refactor 01 (Easy): var
### Before
```javascript
var x = 1; var y = 2;
```
### After
```javascript
const x = 1; const y = 2;
```

## Refactor 02 (Medium): String Concatenation
### Before
```javascript
const msg = "Hello " + name + ", you are " + age + " years old";
```
### After
```javascript
const msg = `Hello ${name}, you are ${age} years old`;
```

## Refactor 03 (Hard): Manual Object Property
### Before
```javascript
const obj = {};
obj.name = name;
obj.age = age;
obj[x] = value;
```
### After
```javascript
const obj = { name, age, [x]: value };
```
