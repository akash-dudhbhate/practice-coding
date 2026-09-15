# Lesson 16 — Refactoring Challenges

## Refactor 01 (Easy): Constructor Function
### Before
```javascript
function User(name) { this.name = name; }
User.prototype.greet = function() { return "Hi " + this.name; };
```
### After
```javascript
class User {
  constructor(name) { this.name = name; }
  greet() { return `Hi ${this.name}`; }
}
```

## Refactor 02 (Medium): Prototype Methods
### Before
```javascript
function Animal(type) { this.type = type; }
Animal.prototype.sound = function() { return "..."; };
```
### After
```javascript
class Animal {
  constructor(type) { this.type = type; }
  sound() { return "..."; }
}
```

## Refactor 03 (Hard): Deep Inheritance
### Before
```javascript
class A {} class B extends A {} class C extends B {} class D extends C {}
```
### After
```javascript
class D { constructor() { this.a = new A(); this.b = new B(); } }
```
