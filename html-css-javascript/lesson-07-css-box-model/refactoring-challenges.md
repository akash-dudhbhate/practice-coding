# Lesson 07 — Refactoring Challenges

## Refactor 01 (Easy): getElementById
### Before
```javascript
document.getElementById("btn");
```
### After
```javascript
document.querySelector("#btn");
```

## Refactor 02 (Medium): Inline Event Handlers
### Before
```html
<button onclick="doSomething()">Click</button>
```
### After
```html
<button id="btn">Click</button>
<script>document.querySelector("#btn").addEventListener("click", doSomething);</script>
```

## Refactor 03 (Hard): Repeated DOM Queries
### Before
```javascript
document.querySelector(".a").style.color = "red";
document.querySelector(".a").style.fontSize = "20px";
document.querySelector(".a").classList.add("active");
```
### After
```javascript
const el = document.querySelector(".a");
el.style.color = "red";
el.style.fontSize = "20px";
el.classList.add("active");
```
